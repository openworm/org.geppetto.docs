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
.. loadsimulation:: http://i.imgur.com/1kI749N.png

Select the "Load Simulation" button at the top to open a console to either select a pre-loaded simulation or upload your own simulation file. 
.. loadsimulation2:: http://i.imgur.com/nMT2vAP.png

Alternatively you can customize the simulation before loading.
.. loadsimulationcustom:: http://i.imgur.com/zxOJ2KG.png

Running the Simulation
----------------------
Once the simulation has been loaded, you can start, pause and stop the simulation at any point. 
.. runsimulation:: http://i.imgur.com/pXEsYDn.png

Navigation
----------
The navigation buttons along the left side of Geppetto allow you to change your view of the simulation within Geppetto.  You can reposition, rotate it and zoom in and out.  To reset, just hit the "home" icon to undo rotation or repositioning.  The buttons can be accessed once the simulation has been loaded as well as before, during and after the simulation run. 
.. navigation:: http://i.imgur.com/A2BngUx.png

In addition to the navigation buttons, you can use a mouse to rotate, drag or zoom the simulation.


Plotting
--------
Proof of concept only. This feature is only available on the LEMS Sample Hodgkin-Huxley Neuron simulation. Full plotting features are currently under development.
*Shortcut Key: Ctl+Alt+P*
.. plotting:: http://i.imgur.com/Q9PDezm.png


Console
=======
Additionally, you can open a console at the bottom while the simulation is running to make adjustments. 
*Shortcut Key: Ctl+Alt+J*

.. console:: http://i.imgur.com/d5CLO9F.png
   View of the open console. 
   
.. consoledetail:: http://i.imgur.com/ts859ap.png

A complete list of the simulation commands by typing help() into the console. The following commands are available in the Geppetto console.

Autocompletion
--------------
Within the console, the Tab button assists with entering commands.
Tab once, to autocomplete the current word of the command.
Tab twice, to show all the options available.

G object commands 
-----------------
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

      -- Simulation.help()
         Outputs list of commands with descriptions associated with the Simulation object.
         @returns  Returns list of all commands for the Simulation object"


Clipboard
---------
From the console, use the following command to open a clipboard and copy the console history.

      -- G.copyHistoryToClipboard()
         Copies console history to OS clipboard

.. clipboard:: http://i.imgur.com/KijJGhb.png


G.runScript(scriptURL) Example
------------------------------
* Type some commands
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
Ctl + Alt + P	Opens plotting feature (currently shows hardcoded variables)
==========		===========






