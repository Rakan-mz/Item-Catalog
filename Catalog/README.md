# Item Catalog Project

this is Item Catalog Project, part of the Udacity

### Goal of project
 an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

### Required Libraries
this project code requires the following:

* requests
* flask
* sqlalchemy


You can run the project in a Vagrant managed virtual machine (VM) .
(see below for how to run the VM). For this you
will need to downlods first VM [Vagrant](https://www.vagrantup.com/downloads) and
[VirtualBox](https://www.virtualbox.org/wiki/Downloads) software installed on
your system.

### Project contents
This project consists of the following files:

* `static` - folder is contain files for styling the project.
* `templates` - folder is contain the templates HTML file for each page.
* `client_secrets.json` - JSON file for API .
* `database_setup` - file contain the tables .
* `project.py` - file contain the Code for the project .
* `teammenu.py` - file contain the Code for teams .
* `teammenuwithusers` - file contain the Code for teams with users.
* `README.md` - This read me file.



### Bringing the VM up
Bring up the VM with the following run the command:

```bash
vagrant up
```

The first time you run this command, it will take awhile, as Vagrant needs to
download the VM image.

You can then log into the VM with the following command:

```bash
vagrant ssh
```
if you want  More detailed instructions for installing the Vagrant VM can be found
[here](https://www.udacity.com/wiki/ud197/install-vagrant).

### Make sure you're in the right place
Once inside the VM, navigate to the tournament directory with this command:

```bash
cd /vagrant
```


### Running the Team Menu App
Once it is up and running, type vagrant ssh. This will log your terminal into the virtual machine, and you'll get a Linux shell prompt. When you want to log out, type exit at the shell prompt. To turn the virtual machine off (without deleting anything), type vagrant halt. If you do this, you'll need to run vagrant up again before you can log into it.

Now that you have Vagrant up and running type vagrant ssh to log into your VM. change to the /vagrant directory by typing cd /vagrant. This will take you to the shared folder between your virtual machine and host machine.

Type ls to ensure that you are inside the directory that contains project.py, database_setup.py, and other directories named 'templates' and 'static' etc..

Now type python database_setup.py to initialize the database.

Type python teammenu.py to populate the database with teams and menu players.

Type python project.py to run the Flask web server. In your browser visit http://localhost:8000 to view the Team menu app. You should be able to view, add, edit, and delete menu items and restaurants.


### Shutting the VM down
When you are finished with the VM, press `Ctrl-D` to log out of it and shut it
down with this command:

```bash
vagrant halt
```
