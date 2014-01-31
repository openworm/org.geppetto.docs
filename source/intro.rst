**************
Using Geppetto
**************

* Getting Started 
* Using the Graphic Interface Controls
  - Loading the Simulation
  - Running the Simulation
  - Navigation
  - Plotting
* Console
  - G object commands
  - Simulation control commands
  - Clipboard
  - Watching State Variables
* Reference
  - Keyboard Short Cuts

Getting Started
===============
Once the Geppetto dev instances has been opened, you can begin to load a simulation.  There are two ways to interact with the Geppetto platform:
* Use the GUI buttons to load, control and interact with the simulations.
* Use the console and enter commands to load, control and interact with the simulations.

Using the Graphic Interface Controls
====================================
Loading the Simulation
----------------------
.. image:: http://i.imgur.com/1kI749N.png

Select the "Load Simulation" button at the top to open a console to either select a pre-loaded simulation or upload your own simulation file. 

.. image:: http://i.imgur.com/nMT2vAP.png

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


Plotting
--------
Geppetto allows plotting of simulation variables and data using our built in Plot functionality. 

A new Plot widget can be created from the console using the command "G.addWidget(Widgets.PLOT)".

Alternatively *Shortcut Key: Ctl+Alt+P* - Toggles existing plotting widgets, if none exist it creates a new one. 

Plotting widgets can plot variables straight from the simulation, given you are watching the variables at the time
you start plotting it. Each variable will have its own line plot, and it's accompanied by a label to distinguish it
from other variables being drawn. 

.. image:: http://i.imgur.com/PigAtLo.png

Other variables can also be plotted, as a two dimensional array  plotted against x and y coordinates. 
You can customize your line plot and change the dimensions of the axis in your plot, use the "Commands" section
as a reference to see what options you have to modify your plot. 

.. image:: http://i.imgur.com/Sf9byfH.png


Console
=======
Additionally, you can open a console at the bottom while the simulation is running to make adjustments. 
*Shortcut Key: Ctl+Alt+J*

.. image:: http://i.imgur.com/d5CLO9F.png
   View of the open console. 
   
.. image:: http://i.imgur.com/ts859ap.png

A complete list of the simulation commands by typing help() into the console. The following commands are available in the Geppetto console.

Autocompletion
--------------
Within the console, the Tab button assists with entering commands.
Tab once, to autocomplete the current word of the command.
Tab twice, to show all the options available.

G object commands 
-----------------
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
         
      -- Simulation.listWatchableVariables()
         List watchable variables for the simulation.
         @returns {String} - status after requesting list of watchable variables.

      -- Simulation.listForceableVariables()
         List forceable variables for the simulation.
         @returns {String} - status after requesting list of forceable variables.

      -- Simulation.addWatchLists(watchLists)

      -- Simulation.getWatchLists()
         Retrieve watchlists available the simulation.
         @returns {String} - status after request.

      -- Simulation.startWatch()
         Start watching variables for the simulation.
         @returns {String} - status after request.

      -- Simulation.stopWatch()
         Stop watching variables for the simulation.
         @returns {String} - status after request.

      -- Simulation.clearWatchLists()
         Clears all watch lists for the given simulation
         @returns {String} - status after request.

      -- Simulation.getWatchTree()
         Gets tree for variables being watched if any.
         @returns {String} - status after request.

      -- Simulation.help()
         Outputs list of commands with descriptions associated with the Simulation object.
         @returns  Returns list of all commands for the Simulation object"

Plot Commands
--------
*Plot1 represents one plot widget instance. Each new plot widget (Plot2, Plot3, Plot4, etc ...) instance has these commands.

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

      -- Plot1.updateDataSet(label,newValue)

      -- Plot1.plotDataFunction(func,data,options)

      -- Plot1.resetPlot()
         Resets the plot widget, deletes all the data series but does not
         destroy the widget window.

      -- Plot1.setOptions(options)
         Set the options for the plotting widget
         @param options

      -- Plot1.getDataSets()

      -- Plot1.help()

      -- Plot1.destroy()
         Resets the plot widget, deletes all the data series but does not
         destroy the widget window.

      -- Plot1.hide()

      -- Plot1.show()

      -- Plot1.getName()

      -- Plot1.setName(name)

      -- Plot1.setPosition(left,top)

      -- Plot1.setSize(h,w)

      -- Plot1.getPosition()

      -- Plot1.getSize()

      -- Plot1.getId()

      -- Plot1.isVisible()"

Clipboard
---------
From the console, use the following command to open a clipboard and copy the console history.

      -- G.copyHistoryToClipboard()
         Copies console history to OS clipboard

.. image:: http://i.imgur.com/f0MLjt6.png

Watching State Variables
------------------------------
Simulation states can be watched as the simulation is running, give the user the possibility of drawing their results 
as part of a Plot, through our Plotting widget interface.  A simulation must be loaded in order to watch variables
from it. 

Watching State Variables Example
-----------------------------
*Load Lems Simulation, first one from drop-down samples menu. 
*Watch two simulation states by using Simulation.addWatchLists(lists) command
 *Simulation.addWatchLists([{name:"hhvars",variablePaths:["example1.hhpop[0].v", "example1.hhpop[0].spiking"]}]);*
 In this case the two states being watched are "hhpop[0].v" and "hhpop[0].spiking". 
*Once variables have been added to watch list, use command *Simulation.startWatch()* to start  
 watching these simulation states.
* When you have started watching these simulation states you can plot them in a widget to see 
  the different values. Refer to the "Plotting" section for more information on how to do this, and use 
  "Simulation.help()" for more commands to use with variable watch. 

G.runScript(scriptURL) Example
------------------------------
Within Geppetto, it's possible to execute a script consisting of Geppetto commands and 
javascript commands. 

Reference a public URL which contains a series of commands, as in this exaple and 
run the command with that URL. https://raw.github.com/openworm/org.geppetto.testbackend/development/src/main/resources/TestSimulationScript.js

To save a series of executed commands from console:
* Copy history to clipboard
* Copy content of the clipboard to a file and put the file in a public folder
* Get the URL of that file
* Feed that link to this command. The set of operations specified in the URL will be executed in Geppetto.


Reference
=========
Keyboard Short Cuts
-------------------

==========		==========
Keystrokes		  Action 
==========		==========
Ctl + Alt + J	Opens console
Ctl + Alt + P	Toggles Plot widget(s). If none exist at time, it creates one. 
==========		===========






