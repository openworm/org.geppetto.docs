Instructions for setting up Geppetto on Eclipse Neon
====================================================

Last Update: June 29th 2017

If you have any problems following this documentation please write on
the [Gitter chat](https://gitter.im/openworm/org.geppetto)

-   Install Eclipse Neon for J2EE
    -   [Download and install Eclipse
        Neon](http://www.eclipse.org/downloads/packages/eclipse-ide-java-ee-developers/neon3).
-   Install Virgo Server and Geppetto Sources
    -   Now we need to install Virgo and clone the geppetto sources
        locally unless you have done those steps already. If not follow
        the instructions for either [OSX or
        Linux](http://docs.geppetto.org/en/latest/osxlinuxsetup.html) or
        [Windows](http://docs.geppetto.org/en/latest/windowssetup.html).
        Follow the steps until Deploying Geppetto section and make sure
        to use the eclipse flag when you use the update\_server script.
`./update_server eclipse`
    -   Now we need to import all the bundles that were cloned into
        Eclipse, to do so click on File->Import-> “Import Existing
        project into workspace” and follow the instructions.
    -   You now have all the Geppetto bundles in your workspace, let's
        add a link to the Virgo Server inside Eclipse. To do this we
        first need to install the Eclipse Virgo plugin.

-   Install Virgo IDE Tooling
    -   Help -> Install New Software
    -   Work With -> <http://download.eclipse.org/virgo/release/tooling>
    -   Select "Eclipse Virgo Tools" and install it, you will be asked
        to restart Eclipse at the end.
    -   Click on Window -> Show View -> Others -> Servers
    -   From the new view create a new Virgo Runtime server (New Servers
        Wizard -> EclipseRT -> Virgo runtime)
    -   Name it anything you like
    -   For installation directory put the folder where you unzipped the
        virgo server above e.g. /opt/virgo-tomcat-serve-VERSION-NUMBER
    -   Once the server is created right click on it and choose add,
        select all the bundles you wish to deploy and that’s it, at the
        end of this step you should have no errors on the bundles. If
        the bundles don't show you need to add the Virgo Nature to them,
        you can do so by right clicking on them on the Package Explorer
        and selecting Virgo -> Add OSGi Bundle Project Nature. Once
        you added the bundles to Virgo it should look like this:
![image](http://i.imgur.com/mucT88s.png?1)
    -   Before starting the server we need to make sure that the different bundles are deployed in the right order. Double click on the Virg server in the Server view, an editor will open. Look for the Artefacts Deployment Order pane and move the bundles up and down to reflect the following order. Save the content of the editor once you are done.
```
org.geppetto.model
org.geppetto.core
org.geppetto.simulation
*anything else in any order*
org.geppetto.frontend
```
You now have Geppetto configured in your Eclipse, right click on the server and choose debug or start, in the console you will see all the bundles loading up and you should see no errors. At the end of the process your server will be up and running, so just point your browser
to:

[127.0.0.1:8080/org.geppetto.frontend/](http://127.0.0.1:8080/org.geppetto.frontend/)

If you want to use the Webpack dev server for hot deployment using your
terminal go to the /org.geppetto.frontend/src/main/webapp/ folder and
run

    npm start

Once the webpack devserver is running you can connect to it using the
port 8081 instead of 8080. Every change made to the web resources will
refresh automatically the server and update your browser.
