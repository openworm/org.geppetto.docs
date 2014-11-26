**********************************
Geppetto Build
**********************************

* Maven Profiles
* Development Build
* Production Build

Maven Profiles
============

Geppetto is build with Maven, using the command. Maven allows for different build steps to be specified for different environments. These optional lists of build steps are called profiles. When building for a production environment, certain steps are followed that are not desired in a development environment. These changes are made via Grunt tasks:

+------------------------------------+------------------------------------+------------------------------------+
| Environment                        | Development                        | Production                         |
+====================================+====================================+====================================+
| Web context path                   | /org.geppetto.frontend             | /                                  |   
+------------------------------------+------------------------------------+------------------------------------+
| SSL Enabled?                       | false                              | true                               |   
+------------------------------------+------------------------------------+------------------------------------+
| Javascript Optimization?           | false                              | true                               |   
+------------------------------------+------------------------------------+------------------------------------+
| Less compiled to CSS?              | false                              | true                               |   
+------------------------------------+------------------------------------+------------------------------------+

Building for development
=============

::
    mvn install

When the command "mvn install" is run, none of the optimization tasks are not run. When developing Geppetto, it is not neccessary to run these build profiles unless you wish to simulate a production environment.

 
Building for production
=========

::
    mvn install -P master

Grunt tasks are run via maven when the "master" profile is specified. The grunt tasks run by this profile will run the javascript optimizer, compile less to css, and compile the velocity templates. The compiled templates are places in the directory "templates/dist", and these are used by the application. These compiled templates will load the optimized JS file, as well as the compiled CSS. 

::
    mvn install -P development

The "development" profile undoes the changes introduced by the "master" profile. The grunt tasks run by this profile will compile the velocity templates, overwriting the comiled templates produced by the "master" profile. These compiled templates will load the non-optimized javascript, and will load the LESS files directly into the browser.