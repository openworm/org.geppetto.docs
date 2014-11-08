**************
Visualizing Connections
**************
An entity can specify multiple connections, input or output, to other entities and sub-entities. Extra properties 
that tell more about the kind of connection it is can be found inside the Connections. Along with these extra properties, 
a connection may also contain a list of visual references, which are used to store references to specific 
parts of entities. 

Getting Started
=================
First step to visualize connections is to load a Simulation that contains some, from our current 
samples list the "C302 Experimental Network of integrate and fire neurons" model is a good model to run 
to seem them in action. 

Once you have a model loaded, you can click on the entities in the scene to see any connections
that it has. Clicking on an entity will select it, which will then display any connections to other entities
it has. The selected entity color will change to yellow, entities that have output connections to selected entity
will change to orange, entities that have input connections to selected entity will change to a light pink color, 
and those entities that have both input and output connections will become green.The picture below shows the 
different colors of connections.

.. image:: images/connections/connection_colors.png

Using the picture above, let's say we have a simulation with three entities; One, Two and Three where entity One
has input connection to entity Two and output connection to entity Three. If entity One was selected it will change
color to yellow, entity Two will change color to light pink and entity Three will become orange. 

The above can also be accomplished by selecting the entity via console.
To visualize connections select the entity by using the "select()" command on it. To return entity to normal look use 
the "unselect()" command. Refer to :ref:`Console Commands` for the rest of available commands for connections.

By default, input and output connections are shown, but this can be modified as explained in
our :ref:`Changing Selection Options`.

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
Connections can specify visual references, which are references to 3D objects in the scene. 

Visual references can be used by interacting with the console. Navigate inside an entity, then connection and you'll find 
the visual references inside. You can highlight each one of them individually.

For example, let's say you wanted to highlight a single visual reference. You will type in the 
console.

.. code-block:: javascript

	Entity.Connection.VisualReference.highlight(true);
 
This will highlight, by changing color to red, the specific part of the entity that is noted in the visual reference. 
To undo highlight of visual reference you'll use same command, but passing the false flag inside.

.. code-block:: javascript

	Entity.Connection.VisualReference.highlight(false);
 
If you wish to see all the visual references highlight for a connection, you'll use:

.. code-block:: javascript

	Entity.Connection.highlight(true);
 
Console Commands
---------
.. code-block:: javascript
	
	-- VisualObjectReferenceNode.getAspectInstancePath()

      -- VisualObjectReferenceNode.getVisualObjectID()
         
      -- VisualObjectReferenceNode.highlight(mode)