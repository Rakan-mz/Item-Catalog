#!/usr/bin/python
# coding=utf-8
import os, sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Team, Base, MenuPlayer, User

engine = create_engine('sqlite:///teammenuwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="Rakan", email="Rkon24@hotmail.com",picture='')
session.add(User1)
session.commit()


# Team 1 >> Al-Hilal FC
team1 = Team(user_id=1, name = "Al-Hilal FC ")

session.add(team1)
session.commit()


menuPlayer1 = MenuPlayer(user_id=1, name = "Carlos Eduardo", Nationality = "Brazil", number = "3", position = "Midfielder", team = team1)

session.add(menuPlayer1)
session.commit()

menuPlayer2 = MenuPlayer(user_id=1, name = "Abdulmalek Al-Khaibri", Nationality = "Saudi Arabia", number = "6", position = "Midfielder", team = team1)

session.add(menuPlayer2)
session.commit()

menuPlayer3 = MenuPlayer(user_id=1, name = "Salman Al-Faraj", Nationality = "Saudi Arabia", number = "7", position = "Midfielder", team = team1)

session.add(menuPlayer3)
session.commit()

menuPlayer4 = MenuPlayer(user_id=1, name = "Abdullah Otayf", Nationality = "Saudi Arabia", number = "8", position = "Midfielder", team = team1)

session.add(menuPlayer4)
session.commit()

menuPlayer5 = MenuPlayer(user_id=1, name = "Mohammad Al-Shalhoub", Nationality = "Saudi Arabia", number = "10", position = "Midfielder", team = team1)

session.add(menuPlayer5)
session.commit()

menuPlayer6 = MenuPlayer(user_id=1, name = "Andre Carrillo", Nationality = "Peru", number = "19", position = "Midfielder", team = team1)

session.add(menuPlayer6)
session.commit()

menuPlayer7 = MenuPlayer(user_id=1, name = "Ali Al-Habsi", Nationality = "Oman", number = "26", position = "Goalkeeper", team = team1)

session.add(menuPlayer7)
session.commit()

menuPlayer8= MenuPlayer(user_id=1, name = "Abdullah Al-Mayouf", Nationality = "Saudi Arabia", number = "1", position = "Goalkeeper", team = team1)

session.add(menuPlayer8)
session.commit()

menuPlayer9= MenuPlayer(user_id=1, name = "Alberto Botia", Nationality = "Spain", number = "4", position = "Defender", team = team1)

session.add(menuPlayer9)
session.commit()

menuPlayer10= MenuPlayer(user_id=1, name = "Mohammed Jahfali", Nationality = "Saudi Arabia", number = "70", position = "Defender", team = team1)

session.add(menuPlayer10)
session.commit()

# Team 2 >> Al-Nassr FC
team2 = Team(user_id=1, name = "Al-Nassr FC ")

session.add(team2)
session.commit()


menuPlayer1 = MenuPlayer(user_id=1, name = "Brad Jones", Nationality = "Australia", number = "1", position = "Goalkeeper", team = team2)

session.add(menuPlayer1)
session.commit()

menuPlayer2 = MenuPlayer(user_id=1, name = "Yahya Al-Shehri", Nationality = "Saudi Arabia", number = "8", position = "Midfielder", team = team2)

session.add(menuPlayer2)
session.commit()

menuPlayer3 = MenuPlayer(user_id=1, name = "Ibrahim Ghaleb", Nationality = "Saudi Arabia", number = "14", position = "Midfielder", team = team2)

session.add(menuPlayer3)
session.commit()

menuPlayer4 = MenuPlayer(user_id=1, name = "Ahmed Al-Fraidi", Nationality = "Saudi Arabia", number = "15", position = "Midfielder", team = team2)

session.add(menuPlayer4)
session.commit()

menuPlayer5 = MenuPlayer(user_id=1, name = "Awadh Khamis", Nationality = "Saudi Arabia", number = "27", position = "Midfielder", team = team2)

session.add(menuPlayer5)
session.commit()

menuPlayer6 = MenuPlayer(user_id=1, name = "Omar Hawsawi", Nationality = "Saudi Arabia", number = "4", position = "Defender", team = team2)

session.add(menuPlayer6)
session.commit()

menuPlayer7 = MenuPlayer(user_id=1, name = "Abdulaziz Al-Jebreen", Nationality = "Saudi Arabia", number = "16", position = "Midfielder", team = team2)

session.add(menuPlayer7)
session.commit()

menuPlayer8= MenuPlayer(user_id=1, name = "Waleed Abdullah", Nationality = "Saudi Arabia", number = "33", position = "Goalkeeper", team = team2)

session.add(menuPlayer8)
session.commit()

menuPlayer9= MenuPlayer(user_id=1, name = "Khalid Al-Ghamdi", Nationality = "Saudi Arabia", number = "12", position = "Defender", team = team2)

session.add(menuPlayer9)
session.commit()

menuPlayer10= MenuPlayer(user_id=1, name = "Ahmed Musa", Nationality = "Nigeria", number = "7", position = "Midfielder", team = team2)

session.add(menuPlayer10)
session.commit()



# Team 3 >> Real Madrid C.F.
team3 = Team(user_id=1, name = "Real Madrid C.F ")

session.add(team3)
session.commit()


menuPlayer1 = MenuPlayer(user_id=1, name = "Keylor Navas", Nationality = "Costa Rica", number = "1", position = "Goalkeeper", team = team3)

session.add(menuPlayer1)
session.commit()

menuPlayer2 = MenuPlayer(user_id=1, name = "Luka Modric", Nationality = "Croatia", number = "10", position = "Midfielder", team = team3)

session.add(menuPlayer2)
session.commit()

menuPlayer3 = MenuPlayer(user_id=1, name = "Toni Kroos", Nationality = "Germany", number = "8", position = "Midfielder", team = team3)

session.add(menuPlayer3)
session.commit()

menuPlayer4 = MenuPlayer(user_id=1, name = "Marcos Llorente", Nationality = "Spain", number = "18", position = "Midfielder", team = team3)

session.add(menuPlayer4)
session.commit()

menuPlayer5 = MenuPlayer(user_id=1, name = "Marco Asensio", Nationality = "Spain", number = "20", position = "Midfielder", team = team3)

session.add(menuPlayer5)
session.commit()

menuPlayer6 = MenuPlayer(user_id=1, name = "Sergio Ramos", Nationality = "Spain", number = "4", position = "Defender", team = team3)

session.add(menuPlayer6)
session.commit()

menuPlayer7 = MenuPlayer(user_id=1, name = "Isco", Nationality = "Spain", number = "22", position = "Midfielder", team = team3)

session.add(menuPlayer7)
session.commit()

menuPlayer8= MenuPlayer(user_id=1, name = "Thibaut Courtois", Nationality = "Belgium", number = "25", position = "Goalkeeper", team = team3)

session.add(menuPlayer8)
session.commit()

menuPlayer9= MenuPlayer(user_id=1, name = "Marcelo", Nationality = "Brazil", number = "12", position = "Defender", team = team3)

session.add(menuPlayer9)
session.commit()

menuPlayer10= MenuPlayer(user_id=1, name = "Casemiro", Nationality = "Brazil", number = "14", position = "Midfielder", team = team3)

session.add(menuPlayer10)
session.commit()



# Team 4 >> FC Barcelona
team4 = Team(user_id=1, name = "FC Barcelona ")

session.add(team4)
session.commit()


menuPlayer1 = MenuPlayer(user_id=1, name = "Marc-Andre ter Stegen", Nationality = "Germany", number = "1", position = "Goalkeeper", team = team4)

session.add(menuPlayer1)
session.commit()

menuPlayer2 = MenuPlayer(user_id=1, name = "Ivan Rakitic", Nationality = "Croatia", number = "4", position = "Midfielder", team = team4)

session.add(menuPlayer2)
session.commit()

menuPlayer3 = MenuPlayer(user_id=1, name = "Sergio Busquets", Nationality = "Spain", number = "5", position = "Midfielder", team = team4)

session.add(menuPlayer3)
session.commit()

menuPlayer4 = MenuPlayer(user_id=1, name = "Denis Suarez", Nationality = "Spain", number = "6", position = "Midfielder", team = team4)

session.add(menuPlayer4)
session.commit()

menuPlayer5 = MenuPlayer(user_id=1, name = "Rafinha", Nationality = "Brazil", number = "12", position = "Midfielder", team = team4)

session.add(menuPlayer5)
session.commit()

menuPlayer6 = MenuPlayer(user_id=1, name = "Nelson Semedo", Nationality = "Portugal", number = "2", position = "Defender", team = team4)

session.add(menuPlayer6)
session.commit()

menuPlayer7 = MenuPlayer(user_id=1, name = "Sergi Samper", Nationality = "Spain", number = "16", position = "Midfielder", team = team4)

session.add(menuPlayer7)
session.commit()

menuPlayer8= MenuPlayer(user_id=1, name = "Jasper Cillessen", Nationality = "Netherlands", number = "13", position = "Goalkeeper", team = team4)

session.add(menuPlayer8)
session.commit()

menuPlayer9= MenuPlayer(user_id=1, name = "Gerard Pique", Nationality = "Spain", number = "3", position = "Defender", team = team4)

session.add(menuPlayer9)
session.commit()

menuPlayer10= MenuPlayer(user_id=1, name = "Arthur", Nationality = "Brazil", number = "8", position = "Midfielder", team = team4)

session.add(menuPlayer10)
session.commit()




# Team 5 >> Liverpool F.C.
team5 = Team(user_id=1, name = "Liverpool F.C ")

session.add(team5)
session.commit()


menuPlayer1 = MenuPlayer(user_id=1, name = "Alisson", Nationality = "Brazil", number = "13", position = "Goalkeeper", team = team5)

session.add(menuPlayer1)
session.commit()

menuPlayer2 = MenuPlayer(user_id=1, name = "Fabinho", Nationality = "Brazil", number = "3", position = "Midfielder", team = team5)

session.add(menuPlayer2)
session.commit()

menuPlayer3 = MenuPlayer(user_id=1, name = "James Milner", Nationality = "England", number = "7", position = "Midfielder", team = team5)

session.add(menuPlayer3)
session.commit()

menuPlayer4 = MenuPlayer(user_id=1, name = "Jordan Henderson", Nationality = "England", number = "14", position = "Midfielder", team = team5)

session.add(menuPlayer4)
session.commit()

menuPlayer5 = MenuPlayer(user_id=1, name = "Adam Lallana", Nationality = "England", number = "20", position = "Midfielder", team = team5)

session.add(menuPlayer5)
session.commit()

menuPlayer6 = MenuPlayer(user_id=1, name = "Nathaniel Clyne", Nationality = "England", number = "2", position = "Defender", team = team5)

session.add(menuPlayer6)
session.commit()

menuPlayer7 = MenuPlayer(user_id=1, name = "Alex Oxlade-Chamberlain", Nationality = "England", number = "21", position = "Midfielder", team = team5)

session.add(menuPlayer7)
session.commit()

menuPlayer8= MenuPlayer(user_id=1, name = "Simon Mignolet", Nationality = "Belgium", number = "22", position = "Goalkeeper", team = team5)

session.add(menuPlayer8)
session.commit()

menuPlayer9= MenuPlayer(user_id=1, name = "Alberto Moreno", Nationality = "Spain", number = "3", position = "Defender", team = team5)

session.add(menuPlayer9)
session.commit()

menuPlayer10= MenuPlayer(user_id=1, name = "Mohamed Salah", Nationality = "Egypt", number = "11", position = "Midfielder", team = team5)

session.add(menuPlayer10)
session.commit()




## Team 6 >> Manchester City F.C.
team6 = Team(user_id=1, name = "Manchester City F.C ")

session.add(team6)
session.commit()


menuPlayer1 = MenuPlayer(user_id=1, name = "Claudio Bravo", Nationality = "Chile", number = "1", position = "Goalkeeper", team = team6)

session.add(menuPlayer1)
session.commit()

menuPlayer2 = MenuPlayer(user_id=1, name = "Raheem Sterling", Nationality = "England", number = "7", position = "Midfielder", team = team6)

session.add(menuPlayer2)
session.commit()

menuPlayer3 = MenuPlayer(user_id=1, name = "Ilkay Gundogan", Nationality = "Germany", number = "8", position = "Midfielder", team = team6)

session.add(menuPlayer3)
session.commit()

menuPlayer4 = MenuPlayer(user_id=1, name = "Kevin De Bruyne", Nationality = "Belgium", number = "17", position = "Midfielder", team = team6)

session.add(menuPlayer4)
session.commit()

menuPlayer5 = MenuPlayer(user_id=1, name = "Fabian Delph", Nationality = "England", number = "18", position = "Midfielder", team = team6)

session.add(menuPlayer5)
session.commit()

menuPlayer6 = MenuPlayer(user_id=1, name = "John Stones", Nationality = "England", number = "5", position = "Defender", team = team6)

session.add(menuPlayer6)
session.commit()

menuPlayer7 = MenuPlayer(user_id=1, name = "David Silva", Nationality = "Spain", number = "21", position = "Midfielder", team = team6)

session.add(menuPlayer7)
session.commit()

menuPlayer8= MenuPlayer(user_id=1, name = "Ederson", Nationality = "Brazil", number = "31", position = "Goalkeeper", team = team6)

session.add(menuPlayer8)
session.commit()

menuPlayer9= MenuPlayer(user_id=1, name = "Benjamin Mendy", Nationality = "France", number = "22", position = "Defender", team = team6)

session.add(menuPlayer9)
session.commit()

menuPlayer10= MenuPlayer(user_id=1, name = "Riyad Mahrez", Nationality = "Algeria", number = "26", position = "Midfielder", team = team6)

session.add(menuPlayer10)
session.commit()


print "added menu player!"
