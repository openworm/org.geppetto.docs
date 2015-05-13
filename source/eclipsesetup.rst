Instructions for setting up Geppetto on Eclipse Juno
****************************************************

Last Update: Jan 5 2015

If you have any problems following this documentation please email openworm-discuss@googlegroups.com

BLUE PILL
---------

We created `eclipse distributions <http://blog.openworm.org/post/31859097261/openworm-eclipse-distributions-released>`__ for the OpenWorm project with all the plugins already installed. You can download this, skip all the plugin install steps below (except source control plugin EGit) and go straight to `Now you can install Geppetto sources <https://docs.google.com/a/metacell.us/document/d/1UPfS5UbQ9z61EJ4Uf6saivSy8IR4JHoyQO38FY66ifE/edit#bookmark=id.4hjcg1t9izg0>`__.

RED PILL
--------

* Install Eclipse Juno for J2EE

  * `http://www.eclipse.org/downloads/packages/eclipse-ide-java-ee-developers/junor <http://www.eclipse.org/downloads/packages/eclipse-ide-java-ee-developers/junor>`__
  * Taking eclipse from any other repository is discouraged
  
* Install Spring Source Studio

  * Download this file to your local disk `http://dist.springsource.com/snapshot/TOOLS/composite/e4.2/bookmarks.xml <http://dist.springsource.com/snapshot/TOOLS/composite/e4.2/bookmarks.xml>`__
  * Go To Help -> Install New Software -> Available Software Sites -> Import and point to the downloaded file to add the required update sites.
  * Now back to the main dialog select from the dropdown the springsource update site
  * Select the following items and install them:

    * Core/Spring IDE
    * Spring Tool Suite
    * Extensions (Incubation) / Spring IDE
    * Extensions / Spring IDE
    * Integrations / Spring IDE

* Install Maven m2e plugin (now it is part of the Eclipse project) 

  * Select the default Juno update site from Install new Software, search for “m2e” and install it

* Install Virgo Tomcat Server
  * `http://www.eclipse.org/downloads/download.php?file=/virgo/release/VP/3.6.2.RELEASE/virgo-tomcat-server-3.6.2.RELEASE.zip <http://www.eclipse.org/downloads/download.php?file=/virgo/release/VP/3.6.2.RELEASE/virgo-tomcat-server-3.6.2.RELEASE.zip>`__
  * This will depend on your OS, for Ubuntu: download the zip file and do: “sudo unzip virgo-tomcat-server-3.6.2.RELEASE.zip -d /opt/”

* Install EGit

  * Select Install new Software and search for “egit” in the following update site:

    * http://download.eclipse.org/releases/juno

  * Select

    * Eclipse EGit
    * Eclipse EGit Mylin GitHub Feature
    * EGit Import Support

* Install Virgo IDE Tooling 

  * Update Site: http://download.eclipse.org/virgo/milestone/tooling

Now you can install Geppetto Sources


Install Geppetto Sources
************************

BLUE PILL
---------

We created a Python script to download Virgo Tomcat and clone all the repositories from Git automatically, the script is available here. If you use the script you can skip to here once you have created your Eclipse workspace and manually imported all the bundles into it one by one (File->Import-> “Import Existing project into workspace” and follow the instructions).

RED PILL
--------

Install Virgo Tomcat Server (skip if you have taken the red pill to install Eclipse)

* `http://www.eclipse.org/downloads/download.php?file=/virgo/release/VP/3.6.2.RELEASE/virgo-tomcat-server-3.6.2.RELEASE.zip <http://www.eclipse.org/downloads/download.php?file=/virgo/release/VP/3.6.2.RELEASE/virgo-tomcat-server-3.6.2.RELEASE.zip>`__

After all the tools are installed you can import the geppetto bundles you are interested in from GitHub (`https://github.com/openworm <https://github.com/openworm>`__).

To do so go to File -> Import -> Git -> Projects from GitHub repository and type “org.geppetto”, select the bundles and click Finish, this will add all the Geppetto repositories to your workspace.  (Unfortunately it is not possible to select all the bundles at once so they will have to be clones one by one). The bundles needed for Geppetto are:

* Essential

  * org.geppetto.core 
  * org.geppetto.simulation 
  * org.geppetto.frontend 

* Domain Specific

  * Neuronal simulation

    * org.geppetto.model.neuroml 
    * org.geppetto.simulator.jlems 

  * Fluid mechanics simulation

    * org.geppetto.model.sph 
    * org.geppetto.solver.sph 
    * org.geppetto.simulator.sph
    
.. image:: http://i.imgur.com/bYJFHgw.png?1


Now you need to import your projects into Eclipse.

Make sure you have the head repository (org.geppetto) in the 'git' folder that you will find located on your local drive, probably in your home directory. You will also find the other repositories you have imported located there.

Now from Eclipse click, File -> Import -> Mavern -> Existing Mavern Projects, and point it to the 'git' folder. 

Eclipse will now be able to install all the projects in one go with the correct classpaths and structure in place.



We are **almost** there. 

You now have all the Geppetto bundles on your workspace. All the bundles use Maven so we need now to install them so that all dependencies are downloaded and the JAR files created and deployed to the local Maven repository. To do so right click on each one of the project and choose Run As -> Maven install.

.. image:: http://i.imgur.com/WiwWgbB.png?1

Now we need to copy the dependencies JAR required by Geppetto to the Virgo Tomcat Webserver, these JARs have been gathered by Maven during the install step and they can be found in your_git_path/org.geppetto.bundle_you_are interested_in/target/classes/lib. **You need to copy all of them for each one of your bundles into your_virgo_tomcat_path/repository/usr/.** We’ll automate this last step in the future.

Create Virgo Server using Eclipse Virgo tooling
***********************************************

You now need to create an instance of a Virgo Tomcat Webserver. Here’s how:

* Help -> Install New Software
* Work With -> “Virgo Tooling”
* Select all the packages and install them
* Windows -> Show View -> Servers
* From the new view create a new Virgo Runtime server (New Servers Wizard -> EclipseRT ->Virgo runtime)
* Name it anything you like
* For installation directory use the “ virgo-tomcat-server” folder that was downloaded by the python script (if you used the python script to get it). If not, point to your virgo tomcat server install, eg /opt/virgo-tomcat-serve-VERSION-NUMBER
* Once the server is created right click on it and choose add, select all the bundles you wish to deploy and that’s it, at the end of this step you should have no errors on the bundles.

.. image:: http://i.imgur.com/mucT88s.png?1

That’s it folks, right click on the server and choose start, you will see in the console all the bundles getting loaded up and you should see no errors. At the end of the process your server will be up and running, so just point your browser to: 

`127.0.0.1:8080/org.geppetto.frontend/ <http://127.0.0.1:8080/org.geppetto.frontend/>`__ 

Click the load simulation button and copy-pasting one of the following URLs in the text box (or pick one of the available samples from the drop-down) and then hit load (these are sample fluid dynamics simulations):

* `https://www.dropbox.com/s/72efwkb9nm7mo27/sph-sim-config-test.xml?dl=1 <https://www.dropbox.com/s/72efwkb9nm7mo27/sph-sim-config-test.xml?dl=1>`__ (216 particles, they mostly collapse to one point)
* `https://www.dropbox.com/s/2oczzgnheple0mk/sph-sim-config.xml?dl=1 <https://www.dropbox.com/s/2oczzgnheple0mk/sph-sim-config.xml?dl=1>`__ (15 particles that never go to rest)
* Same hosted on Google Drive

  * `https://docs.google.com/uc?export=download&id=0B-GW0T4RUrQ6Umw4MkZwdjVCQzA <https://docs.google.com/uc?export=download&id=0B-GW0T4RUrQ6Umw4MkZwdjVCQzA>`__
  * `https://docs.google.com/uc?export=download&id=0B-GW0T4RUrQ6ck5QMVpRTkU2Tmc <https://docs.google.com/uc?export=download&id=0B-GW0T4RUrQ6ck5QMVpRTkU2Tmc>`__

After loading, hit “start” and enjoy!

