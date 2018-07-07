Source Setup on Windows
=======================

This will tell you how to get the Geppetto source code and build it on a
Windows machine ([Windows? I'm on
OSX/Linux!](http://docs.geppetto.org/en/latest/osxlinuxsetup.html)).

Note: if you just want to play with a sample Geppetto deployment you
don't need to install anything, just visit <https://live.geppetto.org>.
If you want to install the latest released sample deployment just
download it from
[here](https://github.com/openworm/org.geppetto/releases) and run
`/bin/startup.bat`. The following instructions are if you want to setup
Geppetto from sources.

Psst: If you get stuck at any point, you can join our Slack channel and we
will assist you. Send an email to [info@geppetto.org](mailto:info@geppetto.org)
for an invite or if you just have a quick question.
You can also send us screenshots and log files!

Prerequisite software
---------------------

You need a bunch of other software to setup Geppetto from sources. The
good news: You probably have some of this on your machine already!

-   *Java SE Development Kit 7*:
    [Installer](http://www.oracle.com/technetwork/java/javase/downloads/java-archive-downloads-javase7-521261.html), you will need to make an oracle.com account in order to download
-   *Python 2.7*: [Installer](https://www.python.org/download/)
-   *setuptools* for Python 2.7:
    [Installer](http://www.lfd.uci.edu/~gohlke/pythonlibs/#setuptools)
-   *pip* for Python 2.7:
    [Installer](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip)
-   *Maven*: [ZIP file](http://maven.apache.org/download.cgi), please
    follow [these
    instructions](http://maven.apache.org/download.cgi#Installation) -
    particularly, you have to set the M2 environment variable
    accordingly (What are environment variables? See below)
-   *git*: [Installer](http://git-scm.com/download/win), make sure to
    select "Use Git from the Windows Command Prompt" during the
    installation
-   *Apache Tomcat*: [All
    Downloads](http://tomcat.apache.org/index.html), use the
    32-bit/64-bit Windows Service Installer
-   *Virgo Server for Apache Tomcat*: [ZIP
    file](http://www.eclipse.org/downloads/download.php?file=/virgo/release/VP/3.6.4.RELEASE/virgo-tomcat-server-3.6.4.RELEASE.zip), unpack it to your
    desired location

Environment Variables
---------------------

Environment variables tell your operating system and other programs
where you installed certain software. To modify them, go to the *Control
Panel* (start menu or search for it), select *System*, then *Advanced
System Settings* and click on *Environment variables*.

Once there, you can specify user variables (only for your account) and
system variables (for everybody). Both will work for us, only JAVA\_HOME
should generally be a system variable.

Create variables with the following names and values, or look if they
already exist:

-   JAVA\_HOME: path to Java SE Development Kit 7
-   PYTHON\_HOME: path to Python 2.7
-   SERVER\_HOME: path to Virgo Server for Apache Tomcat
-   MVN\_HOME: path to Maven

Maven needs to build with Java 7. If you want to point your JAVA\_HOME
variable to a different version, create a file *mavenrc\_pre.bat* in
your home directory that contains:

    JAVA_HOME=path\to\Java7

Next, you have to modify the PATH variable. This will allow you and
Geppetto to run several programs from the command prompt. You may see
that the PATH variable exists twice: Once as a user variable, once as a
system variable. Use the one where the variables above belong to (and if
it doesn't exist, create it). Select it and click on edit. Append the
following strings to the value field, separated by semicolons:

-   %JAVA\_HOME%
-   %JAVA\_HOME%\\bin
-   %PYTHON\_HOME%
-   %PYTHON\_HOME%\\Scripts

Make sure that there is no semicolon at the end of the path variable.
OK, that was everything you need, let's get the source code now.

Setup Geppetto Repositories
---------------------------

First, create a directory where you want the Geppetto source code to
live (geppetto-sources from here on). Open up the command prompt
(cmd.exe) and navigate to it by typing:

    cd geppetto-sources

Once there, clone the org.geppetto repository from GitHub by entering:

    git clone https://github.com/openworm/org.geppetto.git

In Windows Explorer, navigate to
geppetto-sources\\org.geppetto\\utilities\\source\_setup. Open the
*config.json* file in a text editor and change the value of the
*sourcesdir* field to the path of your source directory (use \\\\ as
separators).

Go back to your command prompt and enter:

    cd org.geppetto\utilities\source_setup

You are now in the source\_setup folder, which contains some handy
scripts. First, run the setup.py script:

    python setup.py

This will copy all of the required repositories to geppetto-sources.
Make sure that you have writing permissions for it. If a repository is
missing, check that it is entered correctly in *config.json*.

Building Geppetto
-----------------

To build Geppetto, navigate your command prompt back to the org.geppetto
directory. You can do this simply by entering twice:

    cd ..

Once there, run:

    mvn install

This will build all of the Geppetto modules at once. As you do
development, you probably don't want to re-build all modules if you only
worked on a few ones. In this case, you can build the modules
individually and then re-deploy. To prevent problems caused by old build
files, you may want to clean before reinstalling by:

    mvn clean install

Deploying Geppetto
------------------

To deploy Geppetto to the Virgo server, navigate your command prompt
again to the source\_setup directory by typing:

    cd utilities\source_setup

Then run:

    python update_server.py

This will copy all of the built jars and wars over to
%SERVER\_HOME%\\repository\\usr and the *geppetto.plan* file in
org.geppetto to %SERVER\_HOME%\\pickup.

Starting and Stopping Virgo
---------------------------

The Virgo server is started and stopped via batch scripts. Simply go to
%SERVER\_HOME%\\bin (in Windows Explorer or through the command line)
and run the *startup.bat* or *shutdown.bat* file.

For more info on Virgo's control scripts, see
[here](http://eclipse.org/virgo/documentation/virgo-documentation-2.1.1.RELEASE/docs/virgo-user-guide/htmlsingle/virgo-user-guide.html).

With that you are basically done! So, fire up the *startup.bat* file,
wait until its output stops, cross your fingers and point your browser
to:

    http://localhost:8080/org.geppetto.frontend

You should now see Geppetto starting up. Good job!

Not quite there yet? Get in touch with us, we are there to help you!
Send an email to [info@geppetto.org](mailto:info@geppetto.org) for an
invitation to our Slack channel or if you just have a quick question.

Using gitall.py
---------------

The gitall.py script allows you to perform git commands on all
repositories at once. This makes it easier to maintain the state of the
many repos required by Geppetto.

To use it, navigate your command prompt to the source\_setup folder and
type:

    python gitall.py branches

to print the current branch of each repo
    
    python gitall.py checkout <branch>

to checkout <branch> on each repo. Note the branch must exist on each repo.
    
    python gitall.py fetch [remote] [branch]

to perform git fetch on each repo

    python gitall.py pull [remote] [branch]

to perform git pull on each repo

