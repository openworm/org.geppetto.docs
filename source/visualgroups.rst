*************************
Visualizing Groups 
*************************
For users that want to group entities in a simulation and display this grouping in a visual way, 
the concept of "Visual Groups" in Geppetto serves exactly this purpose and enables the user to group of visual objects.
Each Visual Group can contain multiple Visual Group Elements, which specify a default color and/or parameter to determine the color of a group. 
   
Getting Started
=================
In the runtime tree that stores the simulation information, Visual Groups reside in the Visualization Tree, 
which is one of the subtrees contained in the Aspect tree.
To highlight visual groups in the Geppetto UI the Geppetto console must be used. 
To show all visual group elements for that entity, navigate the up to the VisualizationTree for a given entity via console 
commands and run the getChildren() command on it. Alternatively, entering a "double tab" after typing up to VisualizationTree 
shows all elements contained inside the tree: 

.. code-block:: javascript

	Entity.Aspect.VisualizationTree

Once the groups are revealed, the user can navigate to any of them and use the "show(visible)" command to visualize 
all visual objects that belong to this group, where "visible" must be true or false:

.. code-block:: javascript

	Entity.Aspect.VisualizationTree.Group1.show(true);

The above command shows all the visual objects that belong to the group in object by coloring. 
The color is specified in the Visual Group Element node or by parameter. 

The command below hides all visual objects that belong to Group 1 if they are being displayed: 	

.. code-block:: javascript

	Entity.Aspect.VisualizationTree.Group1.show(false);

Visual group elements can also be visualized individually with the "show(visible)" command.

.. code-block:: javascript

	Entity.Aspect.VisualizationTree.Group1.Element1.show(true);
	
Console Commands
---------
The entire set of commands for visual groups are:

.. code-block:: javascript
	
      -- VisualGroup.getType()
         Gets type of visual grup
         
      -- VisualGroup.show(mode)
         Shows the visual group

      -- VisualGroup.getChildren()
         Gets all children of this visual group 
         
      -- VisualGroup.getVisualGroupElements()

      -- VisualGroup.getLowSpectrumColor()

      -- VisualGroup.getHighSpectrumColor()
