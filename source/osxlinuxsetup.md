Source Setup on OSX and Linux
=============================

This will tell you how to get the Geppetto source code and build it on a
OSX and Linux machine ([OSX? Linux? I'm on
Windows!](http://docs.geppetto.org/en/latest/windowssetup.html)).

Note: if you just want to play with a sample Geppetto deployment you
don't need to install anything, just visit <https://live.geppetto.org>.
If you want to install the latest released sample deployment just
download it from
[here](https://github.com/openworm/org.geppetto/releases) and run
`./bin/startup.sh`. The following instructions are if you want to setup
Geppetto from sources.

Psst: If you get stuck at any point, you can join our Slack channel and we
will assist you. Send an email to [info@geppetto.org](mailto:info@geppetto.org)
for an invite or if you just have a quick question.
You can also send us screenshots and log files!

Prerequisite software
---------------------

You need a bunch of other software to install Geppetto from sources. The
good news: You probably have some of this on your machine already!

### OSX and Linux

-   Java SE Development Kit 7
-   Python 2.7
-   Virgo Server for Apache Tomcat: [ZIP
    file](http://www.eclipse.org/downloads/download.php?file=/virgo/release/VP/3.6.4.RELEASE/virgo-tomcat-server-3.6.4.RELEASE.zip)
    unpack it to your desired location by:

    gunzip -a virgo-tomcat-server-3.6.4.RELEASE.zip -d <desired directory>

Note that Geppetto currently uses virgo tomcat sever 3.6.4, although the
development team is currently moving towards virgo-tomcat-server 3.6.5
and beyond. If you are trying to install 3.6.5, please contact the dev
team.

### OSX

-   *homebrew* (see [here](http://brew.sh/)):
    `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
-   *Maven*: `brew install maven`
-   *git*: `brew install git`
-   *pip*: [Instructions](https://pip.pypa.io/en/latest/installing.html)
-   *Apache Tomcat*: `brew install tomcat`

### Linux: Debian and variants (e.g. Ubuntu)

This should also work for alternative distributions, by substituting
*apt-get* with the appropriate package manager, e.g. *pacman* for Arch,
*yum* for Fedora and so forth.

-   *homebrew* (see
    [here](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-linuxbrew-on-a-linux-vps))
-   *Maven*: `sudo apt-get install maven`
-   *git*: `sudo apt-get install git`
-   *pip*: `sudo apt-get install python-pip`
-   *Apache Tomcat*: `sudo apt-get install tomcat7`

Environment Variables
---------------------

Environment variables tell your operating system and other programs
where you installed certain software.

Linux Variables
---------------

Create variables with the following names and values, or look if they
already exist:

-   JAVA\_HOME: path to Java SE Development Kit 7
-   SERVER\_HOME: path to Virgo Server for Apache Tomcat
-   MVN\_HOME: path to Maven

You can do this for example in .bashrc with:

    export MVN_HOME="$(brew --prefix maven)/libexec"
    export JAVA_HOME="$(/usr/libexec/java_home)"
    export SERVER_HOME="/usr/local/Cellar/virgo/virgo-tomcat-server-3.6.xx.RELEASE"

Maven needs to build with Java 7. If you want to point your JAVA\_HOME
variable to a different version, create a file *.mavenrc* in your home
directory that contains:

    export JAVA_HOME="/path/to/java7"

Note that if you are using Java 8, you may want to install both Java 7
and Java 8 and have a conditional statement to switch between the two.

    export JAVA_HOME="$(/usr/libexec/java_home -v 1.7)"
    setjdk() 
        {export JAVA_HOME="$(/usr/libexec/java_home -v $1)"}
    export SERVER_HOME="/usr/local/Cellar/virgo/virgo-tomcat-server.3.6.xx.RELEASE"

When you close your terminal, it is possible that bashrc may reset
SERVER\_HOME. In order to reset SERVER\_HOME, issue the following
command from the terminal.

    SERVER_HOME="/usr/local/Cellar/virgo/virgo-tomcat-server.3.6.xx.RELEASE"

Mac OS X Variables
------------------

    export MVN_HOME="$(brew --prefix maven)/libexec"
    export JAVA_HOME="/usr/lib/jvm/java-1.7.0-openjdk"
    export SERVER_HOME="/opt/virgo-tomcat-server-3.6.4.RELEASE"

The SERVER\_HOME directory may be one of the directories that you are
prompted to install to. Once you find where virgo tomcat is installed
to, use that as your directory.

Also, following the guide above to installing homebrew on Linux, you
made need to add extra details to your bashrc file.

OK, that was everything you need, let's get the source code now.

Setup Geppetto Repositories
---------------------------

First, create a directory for the Geppetto source code (geppetto-sources
from now on):

    mkdir geppetto-sources
    cd geppetto-sources

Once there, clone the org.geppetto repository from GitHub:

    git clone https://github.com/openworm/org.geppetto.git

Navigate your shell to the source\_setup directory:

    cd org.geppetto/utilities/source_setup

Alternatively, copy the contents of source\_setup to a convenient
directory of your choice:

    cp -r org.geppetto/utilities/source_setup/* <some other location>

Open the *config.json* file in a text editor and change the value of the
*sourcesdir* field to the path of your source directory.

The source\_setup folder contains some handy scripts. First, run the
setup.py script:

    ./setup

or

    python setup.py

Running this script will prompt you to enter the repositories you want
copied to geppetto sources. At present, the repositories are:

    org.geppetto
    org.geppetto.core
    org.geppetto.frontend
    org.geppetto.model
    org.geppetto.model.neuroml
    org.geppetto.simulation

However, you will have the option to select other repositories from this
list when you run the install script.

Make sure that your account has permission to write into
geppetto-sources. If a repository is missing, check that the url for
that repository is entered correctly in *config.json* and *pom.xml*.

Building Geppetto
-----------------

Navigate back to the org.geppetto directory from
utilities/source\_setup:

    cd ../..

Once there, run:

    mvn -Dhttps.protocols=TLSv1.2 install

This will build all of the Geppetto modules at once. As you do
development, you probably don't want to re-build all modules if you only
worked on a few. In this case, you can build the modules individually
and then re-deploy. To build an individual module, just run the install
command from its directory. To prevent problems caused by old build files, you
may want to clean before reinstalling by:

    mvn -Dhttps.protocols=TLSv1.2 clean install

Deploying Geppetto
------------------

To deploy Geppetto to the Virgo server, navigate your shell to the
source\_setup directory again by typing:

    cd utilities/source_setup

Then run:

    ./update_server

or

    python update_server.py

This will copy all of the built jars, wars and dependencies over to
%SERVER\_HOME%/repository/usr and the *geppetto.plan* file in
org.geppetto to %SERVER\_HOME%/pickup.

If you plan to start the server from the eclipse environment run the
update\_server script with the "eclipse" flag:

    ./update_server eclipse

This will copy only dependencies over to %SERVER\_HOME%/repository/usr.
Geppetto JARs and WARs will be copied by Eclipse in the Virgo stage
folder upon deployment.

Starting and Stopping Virgo
---------------------------

The Virgo server is started and stopped via shell scripts in
\$SERVER\_HOME/bin. To run these in the terminal, create a function in
*.bashrc* that proxies commands to the scripts:

    function virgo() {
            bash $SERVER_HOME/bin/$1
    }

Then Virgo can be started using the command:

    virgo startup.sh

Or shutdown using the command:

    virgo shutdown.sh

For more info on Virgo's control scripts, see
[here](https://www.eclipse.org/virgo/documentation/virgo-documentation-3.6.4.RELEASE/docs/virgo-user-guide/htmlsingle/virgo-user-guide.html).

Note that when you are running on Linux, there may be other services
that are using Port 8080.

Use:

    netstat -plten | grep 8080

to find the process number on port 8080.

Then identify the process number and issue the following command to kill
it:

    sudo kill -9 <process number>

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

To use it, navigate your shell to the source\_setup folder and type:

    ./gitall branches

to print the current branch of each repo
    
    ./gitall checkout <branch>

to checkout <branch> for each repo. Note the branch must exist on each repo.

    ./gitall fetch [remote] [branch]

to git fetch on each repo
    
    ./gitall pull [remote] [branch]

to git pull on each repo


