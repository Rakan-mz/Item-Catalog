from flask import Flask, render_template, request,redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Team, Base, MenuPlayer, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Team Players Menu"


# Connect to Database and create database session
engine = create_engine('sqlite:///teammenuwithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create anti-forgery state token
@app.route('/login')
def showLogin():
   state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))
   login_session['state'] = state
   # return "The current session state is %s" % login_session['state']
   return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
   # Validate state token
   if request.args.get('state') != login_session['state']:
       response = make_response(json.dumps('Invalid state parameter.'), 401)
       response.headers['Content-Type'] = 'application/json'
       return response
   # Obtain authorization code
   code = request.data

   try:
       # Upgrade the authorization code into a credentials object
       oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
       oauth_flow.redirect_uri = 'postmessage'
       credentials = oauth_flow.step2_exchange(code)
   except FlowExchangeError:
       response = make_response(
           json.dumps('Failed to upgrade the authorization code.'), 401)
       response.headers['Content-Type'] = 'application/json'
       return response

   # Check that the access token is valid.
   access_token = credentials.access_token
   url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
          % access_token)
   h = httplib2.Http()
   result = json.loads(h.request(url, 'GET')[1])
   # If there was an error in the access token info, abort.
   if result.get('error') is not None:
       response = make_response(json.dumps(result.get('error')), 500)
       response.headers['Content-Type'] = 'application/json'
       return response

   # Verify that the access token is used for the intended user.
   gplus_id = credentials.id_token['sub']
   if result['user_id'] != gplus_id:
       response = make_response(
           json.dumps("Token's user ID doesn't match given user ID."), 401)
       response.headers['Content-Type'] = 'application/json'
       return response

   # Verify that the access token is valid for this app.
   if result['issued_to'] != CLIENT_ID:
       response = make_response(
           json.dumps("Token's client ID does not match app's."), 401)
       print
       "Token's client ID does not match app's."
       response.headers['Content-Type'] = 'application/json'
       return response

   stored_access_token = login_session.get('access_token')
   stored_gplus_id = login_session.get('gplus_id')
   if stored_access_token is not None and gplus_id == stored_gplus_id:
       response = make_response(
           json.dumps('Current user is already connected.'), 200)
       response.headers['Content-Type'] = 'application/json'
       return response

   # Store the access token in the session for later use.
   login_session['access_token'] = credentials.access_token
   login_session['gplus_id'] = gplus_id

   # Get user info
   userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
   params = {'access_token': credentials.access_token, 'alt': 'json'}
   answer = requests.get(userinfo_url, params=params)

   data = answer.json()

   login_session['username'] = data['name']
   login_session['picture'] = data['picture']
   login_session['email'] = data['email']
   # ADD PROVIDER TO LOGIN SESSION
   login_session['provider'] = 'google'

   # See if a user exists, if it doesn't make a new one
   user_id = getUserID(login_session['email'])
   if not user_id:
       user_id = createUser(login_session)
   login_session['user_id'] = user_id

   output = ''
   output += '<h1>Welcome, '
   output += login_session['username']
   output += '!</h1>'
   output += '<img src="'
   output += login_session['picture']
   output += """ ' " style = "width: 300px; height: 300px;
   border-radius: 150px;-webkit-border-radius: 150px;
-moz-border-radius: 150px;"> '"""
   flash("you are now logged in as %s" % login_session['username'])
   print
   "done!"
   return output

    # DISCONNECT - Revoke a current user's token and reset their login_session



@app.route('/gdisconnect')
def gdisconnect():
   access_token = login_session['access_token']
   print
   'In gdisconnect access token is %s', access_token
   print
   'User name is: '
   print
   login_session['username']
   if access_token is None:
       print
       'Access Token is None'
       response = make_response(
           json.dumps('Current user not connected.'), 401)
       response.headers['Content-Type'] = 'application/json'
       return response
   url = ('https://accounts.google.com/o/oauth2/revoke?token=%s'
          % login_session['access_token'])
   h = httplib2.Http()
   result = h.request(url, 'GET')[0]
   print
   'result is '
   print
   result
   if result['status'] == '200':
       response = make_response(json.dumps('Successfully disconnected.'), 200)
       response.headers['Content-Type'] = 'application/json'
       return response
   else:
       print
       "this is the status " + result['status']
       response = make_response(
           json.dumps('Failed to revoke token for given user.', 400))
       response.headers['Content-Type'] = 'application/json'
       return response
# User Helper Functions


def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None



# JSON APIs to view Team Information
@app.route('/team/<int:team_id>/menu/JSON')
def teamMenuJSON(team_id):
    team = session.query(Team).filter_by(id=team_id).one()
    players = session.query(MenuPlayer).filter_by(
        team_id=team_id).all()
    return jsonify(MenuPlayer=[i.serialize for i in players])


@app.route('/team/<int:team_id>/menu/<int:menu_id>/JSON')
def menuPlayerJSON(team_id, menu_id):
    menu_player = session.query(MenuItem).filter_by(id=menu_id).one()
    return jsonify(menu_player=menu_player.serialize)


@app.route('/team/JSON')
def teamsJSON():
    teams = session.query(Team).all()
    return jsonify(teams=[r.serialize for r in teams])


# Show all teams
@app.route('/')
@app.route('/team/')
def showTeams():
    teams = session.query(Team).order_by(asc(Team.name))
    if 'username' not in login_session:
        return render_template('publicteams.html', teams=teams)
    else:
        return render_template('teams.html', teams=teams)


# Create a new team


@app.route('/team/new/', methods=['GET', 'POST'])
def newTeam():
  if 'username' not in login_session:
        return redirect('/login')
  if request.method == 'POST':
        newTeam = Team(name=request.form['name'], user_id=login_session['user_id'])
        session.add(newTeam)
        flash('New Team %s Successfully Created' % newTeam.name)
        session.commit()
        return redirect(url_for('showTeams'))
  else:
        return render_template('newTeam.html')

# Edit a team


@app.route('/team/<int:team_id>/edit/', methods=['GET', 'POST'])
def editTeam(team_id):
    editedTeamm = session.query(
    Team).filter_by(id=team_id).one()
    if 'username' not in login_session:
        return redirect('/login')
        if editTeam.user_id != login_session['user_id']:
            return "<script>function myFunction() {alert('You are not authorized to edit this Team. Please create your own Team in order to edit.');}</script><body onload='myFunction()'>"
    if request.method == 'POST':
        if request.form['name']:
            editedTeamm.name = request.form['name']
            session.add(editedTeamm)
            session.commit()
            flash('Team Successfully Edited %s' % editedTeamm.name)
            return redirect(url_for('showTeams'))
    else:
        return render_template('editTeam.html', team=editedTeamm)


# Delete a Team
@app.route('/team/<int:team_id>/delete/', methods=['GET', 'POST'])
def deleteTeam(team_id):
    TeamToDelete = session.query(Team).filter_by(id=team_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if TeamToDelete.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not authorized to delete this team. Please create your own team in order to delete.');}</script><body onload='myFunction()'>"
    if request.method == 'POST':
        session.delete(TeamToDelete)
        flash('%s Successfully Deleted' % TeamToDelete.name)
        session.commit()
        return redirect(url_for('showTeams', team_id=team_id))
    else:
        return render_template('deleteTeam.html', team=TeamToDelete)

# Show a team menu


@app.route('/team/<int:team_id>/')
@app.route('/team/<int:team_id>/menu/')
def showMenu(team_id):
  team = session.query(Team).filter_by(id=team_id).one()
  players = session.query(MenuPlayer).filter_by(team_id=team_id).all()
  creator = getUserInfo(team.user_id)
  if 'username' not in login_session or creator.id != login_session['user_id']:
        return render_template('publicmenu.html', players=players, team=team, creator=creator)
  else:
        return render_template('menu.html', players=players, team=team, creator=creator)


# Create a new menu player
@app.route('/team/<int:team_id>/menu/new/', methods=['GET', 'POST'])
def newMenuTeam(team_id):
  if 'username' not in login_session:
        return redirect('/login')
  team = session.query(Team).filter_by(id=team_id).one()
  if login_session['user_id'] != team.user_id:
        return "<script>function myFunction() {alert('You are not authorized to add menu items to this team. Please create your own team in order to add players.');}</script><body onload='myFunction()'>"
  if request.method == 'POST':
        newTeam = MenuPlayer(name=request.form['name'], Nationality=request.form[
                           'Nationality'], number=request.form['number'], position=request.form['position'], team_id=team_id, user_id=team.user_id)
        session.add(newTeam)
        session.commit()
        flash('New Menu %s Team Successfully Created' % (newTeam.name))
        return redirect(url_for('showMenu', team_id=team_id))
  else:
      return render_template('newMenuTeam.html', team_id=team_id)

# Edit a menu player


@app.route('/team/<int:team_id>/menu/<int:menu_id>/edit', methods=['GET', 'POST'])
def editMenuTeam(team_id, menu_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedTeam = session.query(MenuPlayer).filter_by(id=menu_id).one()
    team = session.query(Team).filter_by(id=team_id).one()
    if login_session['user_id'] != team.user_id:
        return "<script>function myFunction() {alert('You are not authorized to edit menu players to this team. Please create your own team in order to edit players.');}</script><body onload='myFunction()'>"
    if request.method == 'POST':
        if request.form['name']:
            editedTeam.name = request.form['name']
        if request.form['Nationality']:
            editedTeam.Nationality = request.form['Nationality']
        if request.form['number']:
            editedTeam.number = request.form['number']
        if request.form['position']:
            editedTeam.position = request.form['position']
        session.add(editedTeam)
        session.commit()
        flash('Menu Team Successfully Edited')
        return redirect(url_for('showMenu', team_id=team_id))
    else:
        return render_template('editMenuTeam.html', team_id=team_id, menu_id=menu_id, player=editedTeam)


# Delete a menu player
@app.route('/team/<int:team_id>/menu/<int:menu_id>/delete', methods=['GET', 'POST'])
def deleteMenuTeam(team_id, menu_id):
  if 'username' not in login_session:
        return redirect('/login')
  team = session.query(Team).filter_by(id=team_id).one()
  playerToDelete = session.query(MenuPlayer).filter_by(id=menu_id).one()
  if login_session['user_id'] != team.user_id:
        return "<script>function myFunction() {alert('You are not authorized to delete menu players to this team. Please create your own team in order to delete players.');}</script><body onload='myFunction()'>"
  if request.method == 'POST':
        session.delete(playerToDelete)
        session.commit()
        flash('Menu team Successfully Deleted')
        return redirect(url_for('showMenu', team_id=team_id))
  else:
      return render_template('deleteMenuTeam.html', player=playerToDelete)

# Disconnect based on provider
@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
            del login_session['gplus_id']
            del login_session['access_token']
        if login_session['provider'] == 'facebook':
            fbdisconnect()
            del login_session['facebook_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        del login_session['provider']
        flash("You have successfully been logged out.")
        return redirect(url_for('showTeams'))
    else:
        flash("You were not logged in")
        return redirect(url_for('showTeams'))


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
