Instructions for setting up Geppetto on Eclipse Juno
****************************************************

Last Update: July 26th 2013

If you have any problems following this documentation please email openworm-discuss@googlegroups.com

BLUE PILL
---------

We created `eclipse distributions <http://blog.openworm.org/post/31859097261/openworm-eclipse-distributions-released>`__ for the OpenWorm project with all the plugins already installed. You can download this, skip all the plugin install steps below (except source control plugin EGit) and go straight to `Now you can install Geppetto sources <https://docs.google.com/a/metacell.us/document/d/1UPfS5UbQ9z61EJ4Uf6saivSy8IR4JHoyQO38FY66ifE/edit#bookmark=id.4hjcg1t9izg0>`__.

RED PILL
--------

* Install Eclipse Juno for J2EE

  * `http://www.eclipse.org/downloads/packages/eclipse-ide-java-ee-developers/junor <http://www.eclipse.org/downloads/packages/eclipse-ide-java-ee-developers/junor>`__
  * Taking eclipse from any other repository is discouraged
  
* Install Spring Source Studio	**(Optional)**

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

  * Select the default Juno update site from Install new Software
search for “m2e” and install it

* Install Virgo Tomcat Server
  * `http://www.eclipse.org/downloads/download.php?file=/virgo/release/VP/3.6.2.RELEASE/virgo-tomcat-server-3.6.2.RELEASE.czip <http://www.eclipse.org/downloads/download.php?file=/virgo/release/VP/3.6.2.RELEASE/virgo-tomcat-server-3.6.2.RELEASE.czip>`__
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




