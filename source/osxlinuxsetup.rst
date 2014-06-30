*****************
OSX / Linux Setup
*****************

* Install prerequisite software
* Setup environment variables
* Setup geppetto repositories
* Using gitall.py
* Building geppetto
* Deploying geppetto
* Starting / stopping Virgo

Install prerequisite software
=============================

OSX
---

# Install `homebrew <http://brew.sh/>`__ :
    ```bash
    ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
    ```

# Install *Maven*: ``brew install maven``

# Install *git*: ``brew install git``

# Install *pip*: See: https://pip.pypa.io/en/latest/installing.html

# Install *Apache Tomcat*: ``brew install tomcat``

Linux - Debian and variants (e.g. Ubuntu)
-----------------------------------------

*[notice: should work for alternative distributions, by substituting _apt-get_ with the appropriate package manager, e.g. _pacman_ for Arch, _yum_ for Fedora)]*

# Install *Maven*: ``sudo apt-get install maven``

# Install *git*: ``sudo apt-get install git``

# Install *pip*: ``sudo apt-get install python-pip``

# Install *Apache Tomcat*: ``sudo apt-get install tomcat7``


Setup Virgo
===========

Download Virgo web server for apache tomcat `http://www.eclipse.org/virgo/download/ <http://www.eclipse.org/virgo/download/>`__

Unpack to your desired directory location:

	gunzip -a virgo.zip -d [PATH_TO_VIRGO]

Setup Environmental Variables
=============================

Set $SERVER_HOME to point to your Virgo installation

Set $JAVA_HOME to point to java 7

Set $MVN_HOME to point to your maven installation

Example in .bashrc:

	export MVN_HOME="$(brew --prefix maven)/libexec"

	export JAVA_HOME="$(/usr/libexec/java_home)"

	export SERVER_HOME="$(/usr/local/Cellar/virgo/virgo-tomcat-server-3.6.2.RELEASE)"


Ensure maven is building with Java 7. To do this you may need to set up a .mavenrc file that contains: 

	export JAVA_HOME="$(/path/to/java7)"

Setup Geppetto Repositories:
============================

CD into the directory where you want the source code to live and clone repo org.geppetto:

	git clone https://github.com/openworm/org.geppetto.git

cd into org.geppetto/utilities/osx_utils, or copy the contents of osx_utils to a convenient directory of your choice:
	
	cd org.geppetto/utilities/osx_utils
		or
	cp -r org.geppetto/utilities/osx_utils/* <some_other_location>

Change the “sourcesdir” field in config.json to the file path of your sources directory (This is where all the repos will be copied to).

Run setup.py:

	./setup

This should copy all of the required directories to the sources directory that is specified in config.json. Make sure that rw permissions are correctly set on this folder. If a repo is missing, check that it is entered correctly in config.json

Using gitall.py
===============

gitall.py allows you to perform git commands on all the repos at once. This will hopefully make it easier to maintain the state of the many repos required by Geppetto.

Commands:

	./gitall branches:
		print the current branch of each repo
	./gitall checkout <branch>:
		Checkout <branch> on each repo. Note the branch must exist on each repo.
	./gitall fetch [remote] [branch]:
		Perform git fetch on each repo
	./gitall pull [remote] [branch]:
		Perform git pull on each repo

Building Geppetto
=================
	
To build Geppetto, first cd into repo org.geppetto, and run:

	mvn install

This will build all of the modules at once. As you do development, you won't want to re-build all of the modules if you have only made changes in one or two of them. You can build these modules individually and then re-deploy. You probably want to clean before reinstalling, to prevent problems caused by old build files hanging around:

	mvn clean install

Deploying Geppetto
==================

To deploy Geppetto to Virgo, all of the built jars and wars must be copied over to $SERVER_HOME/repository/usr. Also, the .plan file in org.geppetto should be copied to $SERVER_HOME/pickup

To deploy, run the "update_server" script in osx_utils:
	
	./update_server

Starting/Stopping Virgo
=======================

Virgo is started and stopped via shell scripts in $SERVER_HOME/bin. To run these scripts in the terminal, it is easiest to create a function in .bashrc that proxies commands to those scripts:

	function virgo() {
    		bash $SERVER_HOME/bin/$1
	}

Then virgo can be started using the command:
	
	virgo startup.sh

Virgo can be shutdown using the command:
	
	virgo shutdown.sh

For more info on Virgo's control scripts, see this `page <http://eclipse.org/virgo/documentation/virgo-documentation-2.1.1.RELEASE/docs/virgo-user-guide/htmlsingle/virgo-user-guide.html>`__

If the startup is successful, you will be able to access Geppetto in your web browser at:

	http://localhost:8080/org.geppetto.frontend
