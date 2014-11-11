**************
Visualizing Connections
**************
An entity can specify multiple connections, input or output, to other entities and sub-entities. 
Being able to connect entities with a specific orientation allows for any orientend graph to be represented in Geppetto.
Extra custom properties can be found inside the Connections and can be used to store domain specific data. 
Along with these custom properties, a connection may also contain a list of visual references, which are used 
to store references to specific parts of entities that could for instance visually represent a connection. 

Getting Started
=================
First step to visualize connections is to load a Simulation that has connected entities, from our current 
samples list the "C302 Experimental Network of integrate and fire neurons" model is a good model to see
connections in action. 

Once you have a model loaded, you can click on the entities in the scene (3D picking) 
to see any connections associated to the selected entity. 
Clicking on an entity will select it - upon selection any connections to/from other entities will be shown via entity color coding. 
The selected entity color will change to yellow, entities that have output connections to selected entity
will change to orange while entities that have input connections to selected entity will change to a light pink color, 
and those entities that have both input and output connections will become green.

The picture below shows the color coding for the different kinds of connection:

.. image:: images/connections/connection_colors.png

Referencing the picture above, let's say we load a simulation with three entities; One, Two and Three where entity One
has input connection to entity Two and output connection to entity Three. If entity One was selected its color will change 
to yellow, entity Two will change color to light pink and entity Three will be represented as orange colored. 

Entity selection and connections visualization can also be accomplished via console.
To visualize connections select the entity by using the "select()" command on it. To return entity to normal look use 
the "unselect()" command. Refer to :ref:`Console Commands` for the rest of available commands for connections.

By default, input and output connections are shown, but this can be modified as explained in :ref:`Changing Selection Options`.

Console Commands
---------
The whole set of commands for Connection are:

.. code-block:: javascript
	
   -- Connection.getEntityInstancePath()

      -- Connection.getType()
         Gets type of connection
         
      -- Connection.highlight(mode)
         Highlights the connection

      -- Connection.getChildren()
         Gets all children of this connection 

      -- Connection.getCustomNodes()
         Gets all custom nodes for connection

      -- Connection.getVisualObjectReferenceNodes()
         Returns array of visual object reference nodes for this connection

Changing Selection Options
---------
By default, selecting an entity shows the connections it has to other entities. This can be changed
by using the command "Simulation.setOnSelectionOptions(options)", where the options is an object 
that specifies different flags. 

The options flags that can be given to the "Simulation.setOnSelectionOptions()" command are:

*show_inputs - Display input connections of selected entity
*show_outputs - Display output connections of selected entity
*hide_not_selected - Hides entities not selected

.. code-block:: javascript

	Simulation.setOnSelectionOptions({show_inputs: true, show_outputs: false, hide_not_selected : true});
 
Highlighting Visual References
=================
Connections can specify visual references. Visual References are a way to associate a connection to to 3D objects in the scene, 
usually used to provide a visual representation of a connection in the 3D scene, but this decision is left to the developer.

Visual references can be explored via console. Once the user navigates to an entity connection, 
visual references can be found inside and can be highlighted individually.

Let's say the user wanted to highlight a single visual reference associated to a given connection, this can be achieved
by typing the following in the Geppetto console:

.. code-block:: javascript

	Entity.Connection.VisualReference.highlight(true);
 
This will highlight, by changing color to red, the specific part of the entity that is noted in the visual reference. 
To undo highlight of a visual reference the user can use same function passing the false flag instead:

.. code-block:: javascript

	Entity.Connection.VisualReference.highlight(false);
 
If the user wants to highlight all visual references for a connection, the following command will be entered in the Geppetto console:

.. code-block:: javascript

	Entity.Connection.highlight(true);
 
Console Commands
---------
The whole set of commands for visual references are:

.. code-block:: javascript
	
      -- VisualObjectReferenceNode.getAspectInstancePath()

      -- VisualObjectReferenceNode.getVisualObjectID()
         
      -- VisualObjectReferenceNode.highlight(mode)
