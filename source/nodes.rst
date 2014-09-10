*****************
Geppetto Nodes
*****************

EntityNode
======
An EntityNode is the client side representation of an entity. It can contain any amount of entities, and aspects.

To retrieve the entities and aspects use the following commands respectively:

.. code-block:: javascript

	-- EntityNode.getEntities()
	
	-- EntityNode.getAspects()
	

AspectNode
=====
The node that contains the simulator and model interpreter references. It contains three subtrees for visualization, the model 
and simulation variables. 

To retrieve each of the subtrees objects used the following commands: 

.. code-block:: javascript

    -- AspectNode.getModelTree()
	
    -- AspectNode.getVisualizationTree()

    -- AspectNode.getSimulationTree()
    
AspectSubTreeNode
==========
Subtrees of AspectNode. Each aspect has three of these; one for the ModelTree, VisualizationTree and the SimulationTree.

One can access this node's children by using the following command.

.. code-block:: javascript

	AspectSubTreeNode.getChildren()
	
For example, to get the children of Simulation tree:

.. code-block:: javascript

	SimulationTree.getChildren()

CompositeNode
=========
A node that can have many children. Used to store tree hierarchies in AspectNode subtrees. 

One can access this node's children by using the following command.

.. code-block:: javascript

	CompositeNode.getChildren()

VariableNode
======
A node used to represent a Simulation state variable. It stores a value, unit and scaling factor. 

Node
======
The parent class of all nodes. This is the class that all nodes extend, has the properties that all nodes have in common; name, id, instancepath. 

Printing a Node's content
======
The content's of each node can be printed by using the following command: 

.. code-block:: javascript

	Node.print()
	
For instance, let's say you an Entity named "hhcell" and within an aspect called "electrical". To print out the contents
of the SimulationTree of the this aspect you will type in the console:

.. code-block:: javascript

	hhcell.electrical.SimulationTree.print()