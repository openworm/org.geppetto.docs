**************
Using Geppetto
**************

* Getting Started
* Using the Graphic Interface Controls
  - Loading the Simulation
  - Running the Simulation
  - Navigation
* Console
  - G object commands
  - Simulation control commands
  - Clipboard
  - Watching Variables
* Reference
  - Keyboard Shortcuts

Getting Started
===============
Once Geppetto is loaded in your browser, you can load a simulation. There are two ways to interact with Geppetto:
* Use the GUI buttons to load, control and interact with the simulations.
* Use the API through the Javascript console and enter commands to load, control and interact with the simulations.

Using the Graphic Interface Controls
====================================
Loading the Simulation
----------------------
.. image:: http://i.imgur.com/1kI749N.png

Select the "Load Simulation" button at the top to open a console to either select a pre-loaded simulation or upload your own simulation file.

.. image:: http://i.imgur.com/DRaae8U.png

Alternatively you can customize the simulation before loading.

.. image:: http://i.imgur.com/zxOJ2KG.png

Running the Simulation
----------------------
Once the simulation has been loaded, you can start, pause and stop the simulation at any point.

.. image:: http://i.imgur.com/pXEsYDn.png

Navigation
----------
The navigation buttons along the left side of Geppetto allow you to change your view of the simulation within Geppetto.  You can reposition, rotate it and zoom in and out.  To reset, just hit the "home" icon to undo rotation or repositioning.  The buttons can be accessed once the simulation has been loaded as well as before, during and after the simulation run.

.. image:: http://i.imgur.com/A2BngUx.png

In addition to the navigation buttons, you can use a mouse to rotate, drag or zoom the simulation.

Selection
----------
3D objects in GEPPETTO consist of Entities or Aspects, and can be selected/unselected by clicking on them or
using the select command of the entity as such:

.. code-block:: javascript

	-- Entity.select()

	-- Entity.Aspect.select()

	-- Entity.unselect()

	-- Entity.Aspect.unselect()

	-- Simulation.selectEntity()

To retrieve those entities that are selected, you can use the command:

.. code-block:: javascript

	Simulation.getSelection()

Console
=======
Additionally, you can open a console at the bottom while the simulation is running to make adjustments.
*Shortcut Key: Ctl+Alt+J*

.. image:: http://i.imgur.com/d5CLO9F.png
   View of the open console.

.. image:: http://i.imgur.com/ts859ap.png

A complete list of the simulation commands will display by typing help() into the console. The following commands are available in the Geppetto console.

AutoCompletion
--------------
Within the console, the Tab button assists with entering commands.
Tab once, to autocomplete the current word of the command.
Tab twice, to show all the options available.
If autocompletion detected a command with parameters, it will autocomplete the command and place the cursor in between the parentheses where the variables are located.

G object commands
-----------------
.. code-block:: javascript

	-- G.addWidget(type)

      -- G.availableWidgets()
         Gets list of available widgets
         @returns {List} - List of available widget types

      -- G.clear()
         Clears the console history

      -- G.copyHistoryToClipboard()
         Copies console history to OS clipboard

      -- G.debug(toggle)
         Toggles debug statement on/off
         @param toggle - toggles debug statements

      -- G.getCurrentSimulation()
         Gets the object for the current Simulation, if any.
         @returns Returns current Simulation object if it exists

      -- G.help()
         Get all commands and descriptions available for object G.
         @returns {String} - All commands and descriptions for G.

      -- G.runScript(scriptURL)
         Takes the URL corresponding to a script, executes
         commands inside the script. (see example)
         @param scriptURL - URL of script to execute

      -- G.wait(commands,ms)
         Waits some amount of time before executing a set of commands
         @param commands - commands to execute
         @param ms - milliseconds to wait before executing commands

Simulation control commands
---------------------------
.. code-block:: javascript

      -- Simulation.start()
         Start the simulation.
         @returns {String} - Simulation status after starting it.

      -- Simulation.pause()
         Pauses the simulation
         @returns {String} - Status of Simulation after pausing it.

      -- Simulation.stop()
         Stops the simulation.
         @returns {String} - Status of simulation after stopping it.

      -- Simulation.load(simulationURL)
         Loads a simulation from a URL.
         @param simulationURL - URL of simulation file to be loaded.
         @returns {String} - Status of attempt to load simulation using url.

      -- Simulation.loadFromContent(content)
         Loads a simulation using the content's from the simulation file editor.
         @param content - Content of simulation to be loaded.
         @returns {String} - Status of attempt to load simulation from content window.

      -- Simulation.isLoaded()
         Checks status of the simulation, whether it has been loaded or not.
         @returns {Boolean} - True if simulation has been loaded, false if not.

      -- Simulation.setWatchedVariables(watchLists)
         Add watchlists to the simulation.
         @param {Array} watchLists - Array listing variables to be watched.

      -- Simulation.clearWatchLists()
         Clears all watch lists for the given simulation
         @returns {String} - status after request.

      -- Simulation.help()
         Outputs list of commands with descriptions associated with the Simulation object.
         @returns  Returns list of all commands for the Simulation object"

.. _Console Commands section:

Plot Commands
--------
*Plot1 represents one plot widget instance. Each new plot widget (Plot2, Plot3, Plot4, etc ...) instance has these commands.

.. code-block:: javascript

      -- Plot1.plotData(newData,options)
         Takes data series and plots them.
         To plot array(s) , use it as plotData([[1,2],[2,3]])
         To plot an object , use it as plotData(objectName)
         Multiples arrays can be specified at once in this method, but only one object
         at a time.
         @param newData - series to plot, can be array or an object
         @param options - options for the plotting widget, if null uses default

      -- Plot1.removeDataSet(set)
         Removes the data set from the plot.
         EX: removeDataSet(dummyDouble)
         @param set - Data set to be removed from the plot

      -- Plot1.resetPlot()
         Resets the plot widget, deletes all the data series but does not
         destroy the widget window.

      -- Plot1.setOptions(options)
         Set the options for the plotting widget
         @param options

      -- Plot1.destroy()
         Resets the plot widget, deletes all the data series but does not
         destroy the widget window.

      -- Plot1.setLegend(variable, legend)
         Sets the legend for a variable

Check our JS documentation for more plot commands_

 .. _commands: http://54.200.254.75:8080/org.geppetto.frontend/jsdocs/global.html#Plot

Entity Commands
--------
*EntityNode represents a general case, to use commands on own entity replace "EntityNode" by the name
of the entity, you will be able to access commands this way.

.. code-block:: javascript

      -- EntityNode.hide()
         Hides the entity

      -- EntityNode.show()
         Shows the entity

      -- EntityNode.unselect()
         Unselects the entity

      -- EntityNode.select()
         Selects the entity

      -- EntityNode.zoomTo()
         Zooms to entity

      -- EntityNode.getId()
         Get the id associated with entity
         @returns {String} - ID of entity

      -- EntityNode.getAspects()
         Get this entity's aspects
         @returns {List<Aspect>} - List of aspects

      -- EntityNode.getEntities()
         Get this entity's children entities
         @returns {List<Aspect>} - List of aspects

Aspect Commands
--------
*AspectNode represents a general case, to use commands on own aspect replace "AspectNode" by the name
of the aspect, you will be able to access commands this way.

.. code-block:: javascript

      -- AspectNode.hide()
         Hides the aspect

      -- AspectNode.show()
         Shows the aspect

      -- AspectNode.unselect()
         Unselects the aspect

      -- AspectNode.select()
         Selects the aspect

      -- AspectNode.getModelTreee()
         Get the Model Tree for the aspect
         @returns {Object} - ID of aspect

      -- AspectNode.getSimulationTree()
         Get formatted simulation watch tree for this aspect.
         @returns {Object} - ID of aspect

      -- AspectNode.getVisualizationTree()
         Get the Visualization Tree for the Aspect
         @returns {Object} - ID of aspect

      -- AspectNode.getId()
         Get the id associated with aspect
         @returns {String} - ID of aspect

Simulation Variables Commands
---------
*VariableNode should be replaced by the full path of the variable to use the commands below.

.. code-block:: javascript

      -- VariableNode.getId()
         Get the id associated with the VariableNode
         @returns {String} - ID of variableNode

      -- VariableNode.getName()
         Get the name associated with the VariableNode
         @returns {String} - Name of variableNode

      -- VariableNode.getInstancePath()
         Get the instance path of the variable
         @returns {String} - InstancePath of variableNode

      -- VariableNode.getValue()
         Get value of quantity
         @returns {String} - Value of quantity

      -- VariableNode.getUnit()
         Get unit of quantity
         @returns {String} - Unit of quantity

      -- VariableNode.getScalingFactor()
         Get scaling factor
         @returns {String} - Scaling Factor for value and unit

The Print Command
---------
The print() command can be called on objects for printing it out nicely formatted.

For example, to print out the simulation variables that an entity has you can do:

.. code-block:: javascript

      -- AspectNode.SimulationTree.print()

You can do the same for the VisualizationTree and the ModelTree.

Clipboard
---------
From the console, use the following command to open a clipboard and copy the console history.

.. code-block:: javascript

      -- G.copyHistoryToClipboard()
         Copies console history to OS clipboard

.. image:: http://i.imgur.com/f0MLjt6.png

Watching State Variables
------------------------------
Simulation states can be watched as the simulation is running. It brings the user the possibility to access the value of the variable client side, i.e. drawing their results as part of a Plot, through our Plotting widget interface, showing the information in a tree visualiser widget, etc.
Once the model has been loaded and before starting the simulation we can set the variables to be watched. In order to do this, firstly we need to populate the simulation tree. Assuming our entity is hhcell and the aspect is electrical we will have to execute the following command:

.. code-block:: javascript

   hhcell.electrical.getSimulationTree();
   
This command will populate the simulation tree (hhcell.electrical.SimulationTree) with all the watchable variables. By default the variables are not being watched. To start watching a/some variable/s there are two commands:

.. code-block:: javascript

   hhcell.electrical.SimulationTree.hhpop[0].v.setWatched(true);
   
   Simulation.setWatchedVariables([hhcell.electrical.SimulationTree.hhpop[0].v, hhcell.electrical.SimulationTree.hhpop[0].spiking]);
   
These commands can be executed before we start running the simulation. However if it is an interactive simulation (e.g. JLems Simulator), not an asynchronous one, we can also modified the variables we are watching on run time using the commands aforementioned.

G.runScript(scriptURL) Example
------------------------------
Within Geppetto, it's possible to execute a script consisting of Geppetto commands and
javascript commands.

Reference a public URL which contains a series of commands, as in the link in this example and
run the command with that URL_.
 .. _URL: http://raw.github.com/openworm/org.geppetto.testbackend/development/src/main/resources/TestSimulationScript.js

To save a series of executed commands from console:
* Copy history to clipboard *
* Copy content of the clipboard to a file and put the file in a public folder *
* Get the URL of that file *
* Feed that link to this command. The set of operations specified in the URL will be executed in Geppetto. *


Connecting with Geppetto
========================
There are two ways to connect with Geppetto.  In the lower right hand screen are two expandable areas. Click on the first will open
an interface to share via Facebook or Twitter. The second opens a contact form to reach the Geppetto team with questions or comments.

.. image:: http://i.imgur.com/mQAcCxf.png

.. image:: http://i.imgur.com/Y3SbmmQ.png



Reference
=========

Keyboard Short Cuts
-------------------
=================  ================================================================
   Key Strokes      Action
=================  ================================================================
  Ctl - Alt - J     Opens console
  Ctl - Alt - P     Toggles Plot widget(s). If none exist at time, it creates one.
=================  ================================================================
