**********************************
Geppetto Build
**********************************

* Geppetto Configuration
* Maven Profiles
* Development Build
* Production Build

Geppetto Configuration
============

Geppetto lets you configure your deployment with a set of parameters that are defined in org.geppetto.frontend/src/main/webapp/GeppettoConfiguration.json. This file exposes the following parameters:

- contextPath: The context path is the prefix of the URL path to access Geppetto. Typically development contextPath is "org.geppetto.frontend" and "/" for production. Assuming a local development environment with contextPath "org.geppetto.frontend", you will access Geppetto at localhost: localhost:8080/org.geppetto.frontend

- useSsl: if true, Geppetto will be configured to use https of http.

- embedded: Geppetto is configured to work as an embedded instance inside an iframe. This means CORS will be enabled, a postMessage channel will be available for the main frame, some layout and href calls customization, etc.

- embbedderURL: if running in embedded mode, this specifies the URL of the main frame container. For security reasons Geppetto will only accept cross-origin calls from this URL.

- noTest: If true, tests are suppressed during the build process. If false, tests will be run as part of the build process.

- extensions: Geppetto can be customised by defining JS and LESS/CSS files dropped in a folder inside the extensions folder. The extension can be enabled using this parameter. By default, Gepppetto provides a default extension (org.geppetto.frontend/src/main/webapp/extensions/geppetto-default) that can be used as an example to build custom extensions.

- themes: defined a geppetto "theme", so far we only expose a few parameters defining colours. Below you can find a list of the parameters exposed that can be overridden by your custom theme file: 

    ``@primary_color: #fc6320;``
    
    ``@secondary_color: #fc401a;``
    
    ``@background_color_body_0: #141a1e;``
    
    ``@background_color_body_50: #5c6268;``
    
    ``@background_color_body_73: #60666d;``
    
    ``@background_color_body_100: #515359;``
    
    ``@background_color_widget: rgb(66, 59, 59);``

In order to implement a new theme, a less file needs to be created defining some or all these parameters and the theme needs to be specified in the themes and set to true.

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

Geppetto is built using Maven, with the "mvn install" command. Maven allows for different build steps to be specified for different environments and Geppetto provides a development and a production profile, see below for how to trigger different builds. Builds can be triggered at the root from the org.geppetto bundle and parameters will be propagated to the children (children bundles are defined in org.geppetto/pom.xml). Maven builds can also be triggered for individual bundles from the specific bundle root that needs to be built. 


Building for development
=========

``mvn install``

When the command "mvn install" is executed, none of the optimisation tasks are run. When doing development, it is not necessary to run the production build unless you wish to simulate a production environment.


 
Building for production
=========

``mvn install -P master``

Some optimisation tasks are applied to the org.geppetto.frontend bundle to optimise performance and security. To see the difference between profiles havea look at org.geppetto.frontend/src/main/webapp/package.json.

Overriding Geppetto Parameters with mvn
=========

Geppetto configuration settings can be overwritten by passing the parameters to the "mvn install" command. An example follows:

``mvn install "-DcontextPath=theearth" "-DuseSsl=true" "-Dembedded=true" "-DembedderURL=universe,milkyway"``





