*****************************
Source Setup on OSX and Linux
*****************************

This will tell you how to get the Geppetto source code and build it on a OSX and Linux machine (`OSX? Linux? I'm on Windows! <http://docs.geppetto.org/en/latest/osxlinuxsetup.html>`_). 

It might be a good idea to test the `release version <http://docs.geppetto.org/en/latest/install.html>`_ of Geppetto on your system before you move on.

Already did that? Cool, let's get started!

Psst: If you get stuck at any point, drop us a line at the `OpenWorm-discuss mailing list <https://groups.google.com/forum/#!forum/openworm-discuss>`_ or the contact formular on the `Geppetto website <http://www.geppetto.org/>`_. You can also send us screenshots and log files!

Prerequisite software
=====================

You need a bunch of other software to run Geppetto. The good news: You probably have some of this on your machine already!

OSX and Linux
-------------

* Java SE Development Kit 7

* Python 2.7

* OpenCL (version 1.2)

* Virgo Server for Apache Tomcat: `ZIP file <http://www.eclipse.org/virgo/download/>`_, unpack it to your desired location by:

	``gunzip -a virgo.zip -d <desired directory>``

OSX
---

* *homebrew* (see `here <http://brew.sh/>`_): ``bash ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"``

* *Maven*: ``brew install maven``

* *git*: ``brew install git``

* *pip*: `Instructions <https://pip.pypa.io/en/latest/installing.html>`_

* *Apache Tomcat*: ``brew install tomcat``

Linux: Debian and variants (e.g. Ubuntu)
----------------------------------------

This should also work for alternative distributions, by substituting *apt-get* with the appropriate package manager, e.g. *pacman* for Arch, *yum* for Fedora.

* *Maven*: ``sudo apt-get install maven``

* *git*: ``sudo apt-get install git``

* *pip*: ``sudo apt-get install python-pip``

* *Apache Tomcat*: ``sudo apt-get install tomcat7``

Environment Variables
=====================

Environment variables tell your operating system and other programs where you installed certain software. 

Create variables with the following names and values, or look if they already exist:

* JAVA_HOME: path to Java SE Development Kit 7

* SERVER_HOME: path to Virgo Server for Apache Tomcat

* MVN_HOME: path to Maven

You can do this for example in .bashrc with:

	``export MVN_HOME="$(brew --prefix maven)/libexec"``

	``export JAVA_HOME="$(/usr/libexec/java_home)"``

	``export SERVER_HOME="$(/usr/local/Cellar/virgo/virgo-tomcat-server-3.6.2.RELEASE)"``

Maven needs to build with Java 7. If you want to point your JAVA_HOME variable to a different version, create a file *.mavenrc* in your home directory that contains: 

	``export JAVA_HOME="$(/path/to/java7)"``

OK, that was everything you need, let's get the source code now.

Setup Geppetto Repositories
===========================

First, create a directory where you want the Geppetto source code to live (geppetto-sources from now on). Open up the shell and navigate to it by typing:

	``cd geppetto-sources``

Once there, clone the org.geppetto repository from GitHub by entering:

	``git clone https://github.com/openworm/org.geppetto.git``

Navigate your shell to the source_setup directory by typing:

	``cd org.geppetto/utilities/source_setup``

Alternatively, copy the contents of source_setup to a convenient directory of your choice:

	``cp -r org.geppetto/utilities/source_setup/* <some other location>``

Open the *config.json* file in a text editor and change the value of the *sourcesdir* field to the path of your source directory.

The source_setup folder contains some handy scripts. First, run the setup.py script:

	``./setup``

This will copy all of the required repositories to geppetto-sources. Make sure that you have writing permissions for it. If a repository is missing, check that it is entered correctly in *config.json*.

Building Geppetto
=================
	
To build Geppetto, navigate your command prompt back to the org.geppetto directory. You can do this simply by entering twice:

	``cd ..``

Once there, run:

	``mvn install``

This will build all of the Geppetto modules at once. As you do development, you probably don't want to re-build all modules if you only worked on a few ones. In this case, you can build the modules individually and then re-deploy. To prevent problems caused by old build files, you may want to clean before reinstalling by:

	``mvn clean install``

Deploying Geppetto
==================

To deploy Geppetto to the Virgo server, navigate your shell again to the source_setup directory by typing:

	``cd utilities/source_setup``

Then run:

	``./update_server``

This will copy all of the built jars, wars and dependencies over to %SERVER_HOME%/repository/usr and the *geppetto.plan* file in org.geppetto to %SERVER_HOME%/pickup.

If you plan to start the server from the eclipse environment run the update_server script with the "eclipse" flag:

	``./update_server eclipse``

This will copy only dependencies over to %SERVER_HOME%/repository/usr. Geppetto JARs and WARs will be copied by Eclipse in the Virgo stage folder upon deployment.

Starting and Stopping Virgo
===========================

The Virgo server is started and stopped via shell scripts in $SERVER_HOME/bin. To run these in the terminal, it is easiest to create a function in *.bashrc* that proxies commands to the scripts::

	function virgo() {
    		bash $SERVER_HOME/bin/$1
	}

Then Virgo can be started using the command:
	
	``virgo startup.sh``

Or shutdown using the command:
	
	``virgo shutdown.sh``

For more info on Virgo's control scripts, see `here <http://eclipse.org/virgo/documentation/virgo-documentation-2.1.1.RELEASE/docs/virgo-user-guide/htmlsingle/virgo-user-guide.html>`_.

With that you are basically done! So, fire up the *startup.bat* file, wait until its output stops, cross your fingers and point your browser to:

	``http://localhost:8080/org.geppetto.frontend``

You should now see Geppetto starting up. Good job! 

Not quite there yet? Get in touch with us, we are there to help you! You can use the `OpenWorm-discuss mailing list <https://groups.google.com/forum/#!forum/openworm-discuss>`_ or the contact formular on the `Geppetto website <http://www.geppetto.org/>`_.

Using gitall.py
===============

The gitall.py script allows you to perform git commands on all repositories at once. This makes it easier to maintain the state of the many repos required by Geppetto.

To use it, navigate your shell to the source_setup folder and type:

	``./gitall branches``:
		print the current branch of each repo
	``./gitall checkout <branch>``:
		Checkout <branch> on each repo. Note the branch must exist on each repo.
	``./gitall fetch [remote] [branch]``:
		Perform git fetch on each repo
	``./gitall pull [remote] [branch]``:
		Perform git pull on each repo
