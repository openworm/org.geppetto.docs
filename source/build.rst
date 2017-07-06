**********************************
Geppetto Build
**********************************

* Geppetto Configuration
* Maven Profiles
* Development Build
* Production Build

Geppetto Configuration
============

Geppetto allows configuring your instance with a set of parameters that can be found inside org.geppetto.frontend/src/main/webapp/GeppettoConfiguration.json. This file exposes the following parameters:

- contextPath: The context path is the prefix of the URL path to access Geppetto. Typically development contextPath is "org.geppetto.frontend" and "/" for production. Assuming a local development environment with contextPath "org.geppetto.frontend", you will access Geppetto at localhost: localhost:8080/org.geppetto.frontend

- useSsl: Geppetto will be configured to use https calls.

- embedded: Geppetto is configured to work as an embedded instance inside an iframe. This means CORS will be enabled, a postMessage channel will be available for the main frame, some layout and href calls customization, etc.

- embbedderURL: URL of the main frame container. For security reasons Geppetto will only accept calls from this URL

- noTest: If false, tests will be run as part of the build process.

- extensions: Geppetto can be customised using JS and LESS/CSS files creating a folder inside the extensions folder (Documentation still under construction) and enabling the extension with this parameter. By default, Gepppetto provides an extension that configures a ready to use instance.

- themes: Geppetto is configured to use this theme (set of colours). So far we only expose a few parameters. As follow you can find the parameters and its values by default. 

    ``@primary_color: #fc6320;``
    
    ``@secondary_color: #fc401a;``
    
    ``@background_color_body_0: #141a1e;``
    
    ``@background_color_body_50: #5c6268;``
    
    ``@background_color_body_73: #60666d;``
    
    ``@background_color_body_100: #515359;``
    
    ``@background_color_widget: rgb(66, 59, 59);``

In order to implement a new theme, a less file needs to be created defining some or all these parameters and the theme needs to be enabled in the GeppettoConfiguration.json.

This is how the default (and recommended for development environments) GeppettoConfiguration.json looks like:
::
    {
        "contextPath": "org.geppetto.frontend",
        "useSsl": false,
        "embedded": false,
        "embedderURL": ["/"],
        "noTest": false,
        "extensions": {
            "geppetto-default/ComponentsInitialization": true,
            "geppetto-osb/ComponentsInitialization": false,
            "geppetto-vfb/ComponentsInitialization": false,
            "geppetto-neuron/ComponentsInitialization": false,
            "geppetto-hm/ComponentsInitialization": false
        },
        "themes": {
            "geppetto-default/colors": true,
            "geppetto-hm/pages/styles/colors": false
        }
    }

and this is an example of a production environment with a different extension and theme:
::
    {
        "contextPath": "/",
        "useSsl": true,
        "embedded": false,
        "embedderURL": ["/"],
        "noTest": false,
        "extensions": {
            "geppetto-default/ComponentsInitialization": false,
            "geppetto-osb/ComponentsInitialization": false,
            "geppetto-vfb/ComponentsInitialization": false,
            "geppetto-neuron/ComponentsInitialization": false,
            "geppetto-hm/ComponentsInitialization": true
        },
        "themes": {
            "geppetto-default/colors": true,
            "geppetto-hm/hm_theme": true
        }
    }

Maven Profiles
============

Geppetto is build with Maven, using the command. Maven allows for different build steps to be specified for different environments. Geppetto provides a development and a production profile. When building for a production environment, certain steps are followed that are not desired in a development environment.


Building for development
=========

``mvn install``

When the command "mvn install" is run, none of the optimisation tasks is run. When developing Geppetto, it is not necessary to run these build profiles unless you wish to simulate a production environment.


 
Building for production
=========

``mvn install -P master``

Some optimisation tasks are perform to optimise Geppetto performance and security.

Overriding Geppetto Parameters with mvn
=========

Geppetto configuration settings can be overwritten by passing the parameters in the mvn install command. Find as follow an example:

``mvn install "-DcontextPath=theearth" "-DuseSsl=true" "-Dembedded=true" "-DembedderURL=universe,milkyway"``





