***********************
Source Setup on Windows
***********************

This will tell you how to get the Geppetto source code and build it on a Windows machine. 

You might also want to have a look at the install instructions for the `release version <http://docs.geppetto.org/en/latest/install.html>`_ of Geppetto or at the instructions for `OSX and Linux <http://docs.geppetto.org/en/latest/osxlinuxsetup.html>`_.

Still here? Cool, let's get started!

Psst: If you get stuck at any point, drop us a line at the `OpenWorm-discuss mailing list <https://groups.google.com/forum/#!forum/openworm-discuss>`_ or the contact formular on the `Geppetto website <http://www.geppetto.org/>`_.

Prerequisite software
=====================

You need a bunch of other software to run Geppetto. The good news: You probably have some of this on your machine already!

* *Java SE Development Kit 7*: `Installer <http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html>`_

* *Python 2.7*: `Installer <https://www.python.org/download/>`_

* *setuptools* for Python 2.7: `Installer <http://www.lfd.uci.edu/~gohlke/pythonlibs/#setuptools>`_

* *pip* for Python 2.7: `Installer <http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip>`_

* *OpenCL*: You can use `GPU Caps viewer <http://www.softpedia.com/get/Tweak/Video-Tweak/GPU-Caps-Viewer.shtml>`_ to check whether OpenCL (version 1.2) is already installed (tip: you can run some nice demos at the bottom of the OpenCL tab). If it is not there, update the driver of your graphics card to the newest version (`Intel <http://www.intel.com/p/en_US/support/detect/graphics>`_ and `Nvidia <http://www.nvidia.com/Download/index.aspx?lang=en-us>`_). Then, install the Intel SDK for OpenCL Applications (`Installer <https://software.intel.com/en-us/vcsource/tools/opencl-sdk>`_). Use GPU Caps viewer again to check that everything works. 

* *Maven*: `ZIP file <http://maven.apache.org/download.cgi>`_, follow these `instructions <http://maven.apache.org/download.cgi#Installation>`_ and set the environment variables accordingly (more information on environment variables below)

* *git*: `Installer <http://git-scm.com/download/win>`_

* *Apache Tomcat*: `All Downloads <http://tomcat.apache.org/index.html>`_, use the 32-bit/64-bit Windows Service Installer

* *Virgo Server for Apache Tomcat*: `ZIP file <http://www.eclipse.org/virgo/download/>`_, unpack it to your desired location

Environment Variables
=====================

Environment variables tell your operating system and other programs where you installed certain software. To modify them, go to the *Control Panel* (start menu or search for it), select *System*, then *Advanced System Settings* and click on *Environment variables*. 

Once there, you can specify user variables (only for your account) and system variables (for everybody). Both will work for us, only JAVA_HOME should generally be a system variable. 

Create variables with the following names and values, or look if they already exist:

* JAVA_HOME: path to Java SE Development Kit 7

* PYTHON_HOME: path to Python 2.7

* SERVER_HOME: path to Virgo Server for Apache Tomcat

* MVN_HOME: path to Maven

Maven needs to build with Java 7. If you want to point your JAVA_HOME variable to a different version, create a file *mavenrc_pre.bat* in your home directory that contains: 

	``JAVA_HOME=<path to Java 7>``

Next, you have to modify the PATH variable. This will allow you and Geppetto to run several programs from the command prompt. You may see that the PATH variable exist twice: Once as a user variable, once as a system variable. Use the one where the variables above belong to. Select it and click on edit. Append the following strings to the value field, seperated by semicolons:

* %JAVA_HOME%

* %JAVA_HOME%\\bin

* %PYTHON_HOME%

* %PYTHON_HOME%\\Scripts

OK, that was everything you need, let's get the source code now.

Setup Geppetto Repositories
===========================

First, create a directory where you want the Geppetto source code to live (<source directory> from now on). Open up the command prompt (cmd.exe) and navigate to it by typing:

	``cd <source directory>``

Once there, clone the org.geppetto repository from GitHub by entering:

	``git clone https://github.com/openworm/org.geppetto.git``

In Windows Explorer, navigate to <source directory>\\org.geppetto\\utilities\\all_os_utils. Open the *config.json* file in a text editor and change the value of the *sourcesdir* field to the path of your source directory (use \\\\ as separators).

Go back to your command prompt and enter:

	``cd org.geppetto\utilities\all_os_utils``

You are now in the all_os_utils folder, which contains some handy scripts. First, run the setup.py script:

	``python setup.py``

This will copy all of the required repositories to your source directory. Make sure that you have writing permissions for it. If a repository is missing, check that it is entered correctly in *config.json*.

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

To deploy Geppetto to the Virgo server, navigate your command prompt again to the all_os_utils directory by typing:

	``cd utilities\all_os_utils``

Then run:

	``python update_server.py``

This will copy all of the built jars and wars over to %SERVER_HOME%\\repository\\usr and the *geppetto.plan* file in org.geppetto to %SERVER_HOME%\\pickup.

Starting and Stopping Virgo
===========================

The Virgo server is started and stopped via batch scripts. Simply go to %SERVER_HOME%\\bin (in Windows Explorer or through the command line) and run the *startup.bat* or *shutdown.bat* file.

For more info on Virgo's control scripts, see `here <http://eclipse.org/virgo/documentation/virgo-documentation-2.1.1.RELEASE/docs/virgo-user-guide/htmlsingle/virgo-user-guide.html>`_.

With that you are basically done! So, fire up the *startup.bat* file, wait until its output stops, cross your fingers and point your browser to:

	``http://localhost:8080/org.geppetto.frontend``

You should now see Geppetto starting up. Good job! 

Not quite there yet? Get in touch with us, we are there to help you! You can use the `OpenWorm-discuss mailing list <https://groups.google.com/forum/#!forum/openworm-discuss>`_ or the contact formular on the `Geppetto website <http://www.geppetto.org/>`_.

Using gitall.py
===============

The gitall.py script allows you to perform git commands on all repositories at once. This makes it easier to maintain the state of the many repos required by Geppetto.

To use it, navigate your command prompt to the all_os_utils folder and type:

	``python gitall.py branches``:
		print the current branch of each repo
	``python gitall.py checkout <branch>``:
		Checkout <branch> on each repo. Note the branch must exist on each repo.
	``python gitall.py fetch [remote] [branch]``:
		Perform git fetch on each repo
	``python gitall.py pull [remote] [branch]``:
		Perform git pull on each repo