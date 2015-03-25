*************************
Geppetto Events Tutorial
*************************

 * The Events
 * Registering a Widget to an Event

The Events
=================
Geppetto has a class called GEPPETTO.Events.js that declares a set of events that 
widgets can register and listen to. These events are the result of user interaction with
the environment; selection, restarting simulation, loading simulation. 

.. code-block:: javascript

	var Events = {
			Select : "simulation:selection_changed",
			Simulation_restarted : "simulation:restarted",
			Simulation_loaded : 'simulation:modelloaded',
		};

If a widget is registered to listen to an event, it will receive updates once such event takes place in 
Geppetto.   

Registering a Widget to an Event
=================
At the moment TreeVisualizerDAT1 is the only widget with a method that allows it to 
register to listen to the Geppetto Events described above. To use it, call the
register event method and pass it the event to which you want the widget to listen.

.. code-block:: javascript

	TreeVisualizerDAT1.registerEvent(Events.Select);
	
In our example above our widget would be registered to the selection event, and will
receive updates every time the selection changes in Geppetto. 