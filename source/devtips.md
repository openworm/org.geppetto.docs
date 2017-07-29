Tips for developer to configure/deploy Eclipse + Virgo
======================================================

Last Update: July 29th 2017

This section provides tips to solve some problems regarding Geppetto
deploying in a Virgo Server (with Eclipse). These tips summarizes the
experience of some Geppetto developers. Some may work on your
environment and configuration, some don't. You will have to identify
which one makes sense for you so some software developer skills are
required. Unfortunately, sometimes to configure a Virgo Server with
Geppetto properly requires some knowledge, a lof of common sense and a
little bit of magic. If you have any other tip which can be useful for
someone else, don't hesitate on adding it to the list.

-   Three wise tools.

    -   mvn clean || **Eclipse command**: Run as -> mvn clean
    -   mvn install || **Eclipse command**: Run as -> mvn install
    -   mvn update || **Eclipse command**: Maven -> Update Project

    These three comands are the key tools you will be using during the
    configuration phase. Usually a mvn install from the org.geppetto
    project will be enough but sometimes you have to mvn clean/install
    each project independently. If you don't manage to mvn install all
    the projects from org.geppetto root project, try to mvn
    clean/install the one that is causing the error. Regarding the third
    command, tipically a maven project has a folder structure like this:

        main
            java    
            resources
        test    
            java
            resources

    However, sometimes this folder structure is "corrupted". Therefore,
    some compilation errors, which make no sense (Eclipse is complaining
    about a file although the file is in the right path), are reported.
    Execute a Maven Update to the project and then mvn clean/ install.
    After executing a mvn update, remember to unclick the Maven Project
    Builder (**Eclipse command**: Right click Project ->
    Properties -> Builders -> Unclick Maven Project Builder).
    Otherwise it can slow down and, eventually, crash your Eclipse.

-   In the Virgo server there are four folders to focus on if you are
    having problems:
    -   pickup: if you are not using any IDE you need to have
        a geppetto.map. Otherwise, the file can't be here.
    -   serviceability/log/log.log: If you have any problem have a look
        at the logs file and try to figure out what is failing
    -   stage: If you are using an IDE the geppetto bundles will be
        deployed here. If you are having some problems and you do not
        know what to do, sometimes it is a good option to delete the
        content of this folder. It will be regenerated next time the
        server is started. However, you may need to delete the Virgo
        server from Eclipse and create it again adding all the bundles.
        If you are not using Eclipse, this folder shouldn't have any
        bundles and they have to be placed in the repository/usr as .jar
        and .war files
    -   repository/usr: If using an IDE, this folder contains all the
        .jar dependencies from the different bundles (a script can be
        found in org.geppetto which copies these files into the
        Geppetto server). If any library is added or changed, mvn
        install the geppetto projects and copy the files again.
-   If you have are starting your Virgo Server for the first time and it
    is not working try to have a look at the Geppetto
    folder permissions.
-   When starting the Virgo server, the Eclipse console shows
    information about the process. Every time a new module is deployed
    properly a message like this one is displayed:

        {.sourceCode .none}
        Installed bundle 'org.geppetto.model.neuroml' version '0.3.6'.
        Starting bundle 'org.geppetto.model.neuroml' version '0.3.6'.
        Started bundle 'org.geppetto.model.neuroml' version '0.3.6'.

    However if the module hasn't been deployed properly the version you
    will see is 0.0.0 Double check any compilation or configuration
    error with the project or the dependencies. Execute mvn install to
    the project. This command can be executed while the server running.

-   From time to time, the Eclipse Virgo connector doesn't copy some
    resources properly. Everything seems to run properly but some
    actions are not working fine. You will have to copy the resources
    files into the server (virgo/stage/\[projectname\]). This error
    could be tricky to solve as the symptons can be totally diferent
    depending on the resource that hasn't been copied to the server.
    Note that although the resources are located at /src/main/resources
    in your project folder, in the Virgo Server they can be found in
    virgo/stage/\[projectname\] folder outside any subfolders.

    **Examples**

    -   There is no connection between the client and the server. For
        instance, you can't see the geppetto version in the console when
        the main page is loaded. Also if you try to load a simulation it
        keeps loading forever. -> The spring
        configuration (META-INF/spring) in the org.geppetto.frontend
        resources hasn't been copied in the server.
    -   When executing aspect.getModel() an exception is raised. In the
        log you will see a trace that says "FileNotFound" -> You will
        have to copy the main/resources files of the
        org.geppetto.model.neuroml project.
-   Maven libraries that are downloaded when a mvn install is executed
    for the first time or after a mvn clean, are stored typically in a
    folder called .m2 inside your home folder. If the version of any
    library changes maven automatically download it again. However, if
    the lib content has changed but the lib version remains the same,
    you will have to remove the lib in .m2 manually. Note that this is a
    very uncommon case.
-   You cannot deploy org.geppetto.frontend on your server. This can be
    due to an Eclipse distribution that is missing some components. From
    update site, install the below item:

        {.sourceCode .none}
        Web, XML, Java EE and OSGi Enterprise Development -> Eclipse Java EE Developer Tools
    


