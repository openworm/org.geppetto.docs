*****************************
Geppetto Front End Components
*****************************

 * Overview
 * Developing Components


Overview
=================
Geppetto is designed as a platform that provides flexibility for developers to implement their own UI. A components model is intended to decouple UI elements from the core Geppetto application, allowing heavy customization of the front end user experience on a per instance basis.

A componentized model allows Geppetto to load components from a remote repository during the build phase, allowing customization without forking the project. Components are written as `Bower <http://bower.io>`_ packages, and loaded as `require.js <http://http://requirejs.org>`_ modules. Familiarity with Bower and Require.js is recommended for developing components.

Components live in the /js/components directory. The default contents of this directory are:

| /**js**
|   /**components**
|       /**dev**
|       /**dist**
|       components.js
|       install_components.py
|       publish_components.py
|       bower.json



dev/
------------
The dev/ directory contains components under active development. These components exist in the main Geppetto frontend repository, and are loaded by default.

dist/
------------
The dist/ directory is the location for components installed by bower in a production environment.


bower.json
------------
*bower.json* :
::

    {
        "name": "org.geppetto.frontend.components",
        "version": "1.0.0",
        "ignore": [
            ".jshintrc",
            "**/*.txt"
        ],
        "dependencies": {
            "simulationcontrols": "https://github.com/mlolson/geppetto-components/raw/master/simulationcontrols.zip",
            "cameracontrols": "https://github.com/mlolson/geppetto-components/raw/master/cameracontrols.zip",
            "help": "https://github.com/mlolson/geppetto-components/raw/master/help.zip",
            "tutorial": "https://github.com/mlolson/geppetto-components/raw/master/tutorial.zip",
            "bootstrap": "https://github.com/mlolson/geppetto-components/raw/master/bootstrap.zip"
        }
    }

The **dependencies** field specifies the components to be installed from remote repositories. When the command **bower install** is run, the specified packages will be downloaded and installed into the **/dist** directory. If Bower sees the components already in the dist folder, it will not attempt to overwrite them.

components.js
-------------
The components.js file specifies which components to load at runtime via require.js. For example, here we load three components from the **dev** directory, in this case using the JSX parser:
::

    define(function(require) {
        require('jsx!./dev/simulationcontrols/SimulationControls');
        require('jsx!./dev/cameracontrols/CameraControls');
        require('jsx!./dev/tutorial/IntroModal');
    });

install_components.py
---------------------

The install_components script runs the command *bower install*, then generates the **components.js** file to load components from the **dist/** directory. The install_components script is meant to be run on the server, not in a development environment.

publish_components.py
---------------------

Usage: ./publish_components -v <version>

The publish components script attempts to publish the contents of the **dev** directory to a local git repository called org.geppetto.bower. This folder is created at the source root (parrellel to org.geppetto.frontend). Each component directory is zipped and copied to org.geppetto.bower/<version>/<component>.zip. The origin of this repository on github is at https://github.com/openworm/org.geppetto.bower.

Developing Components
=====================

A component is simply a Bower package. It contains a Bower configuration file (bower.json), which tells bower how it should be installed. Information on creating Bower packages can be found `here <http://bower.io/docs/creating-packages/>`_. A component directory might look something like this:

|   /**cameracontrols**
|       CameraControls.js
|       bower.json

*bower.json:*
::

   {
      "name": "cameracontrols",
      "main": "CameraControls",
      "version": "0.0.1",
      "authors": [
        "Matt Olson <mattlolson@gmail.com>"
      ],
      "description": "camera controls for geppetto",
      "moduleType": [
        "amd"
      ],
      "license": "MIT",
      "private": true,
      "ignore": [
        "**/.*",
        "node_modules",
        "bower_components",
        ".",
        "test",
        "tests"
      ]
    }

In order to install Geppetto components correctly, we add one additional field, **main**. It is not part of the Bower spec. **main** tells Geppetto which file is the entry point to the package. In this case the line:

::

        require('jsx!./dev/cameracontrols/CameraControls');

will be added to **components.js** when the install script is run. The file **CameraControls.js** will then be loaded when the app is started.

The components can be hosted on any public server. Github is convenient. Zip the directory and upload it to a location of your choice. When you are ready to use it, add the entry to the dependencies field of bower.json and run the install_components script.
