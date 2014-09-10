EntityNode
======
An EntityNode is the client side representation of an entity. It can contain any amount of entities, and aspects.

AspectNode
=====
The node that contains the simulator and model interpreter references. It contains three subtrees for visualization, the model 
and simulation variables. 

AspectSubTreeNode
==========
Subtrees of AspectNode. Each aspect has three of these; one for the ModelTree, VisualizationTree and the SimulationTree.

CompositeNode
=========
A node that can have many children. Used to store tree hierarchies in AspectNode subtrees

VariableNode
======
A node used to represent a Simulation state variable. It stores a value, unit and scaling factor. 

Node
======
The parent class of all nodes. This is the class that all nodes extend, has the properties that all nodes have in common; name, id, instancepath. 
