*************************
Visualizing Groups 
*************************
Visual Groups in Geppetto allow grouping of visual objects. Each Visual Group can contain multiple Visual Group Elements,
which specify a default color and/or parameter to determine color of group. 
   
Getting Started
=================
Visual Groups reside inside the Visualization Tree, which is inside the subtrees of Aspects.
Visualizing these groups within Geppetto requires using the console, typing up to VisualizationTree
path on the console and doing a getChildren() on it returns all visual group elements that it has. Alternatively
doing a double tab after typing up to VisualizationTree shows all element inside. 

.. code-block:: javascript

	Entity.Aspect.VisualizationTree

Once you find the groups, navigate inside one of them and use the "show(visible)" command to visualize 
all visual objects that belong to this group, where "visible" must be true or false.

.. code-block:: javascript

	Entity.Aspect.VisualizationTree.Group1.show(true);

The above command shows all the visual objects that belong to group by coloring using the color specify in the Visual Group Element 
node or by parameter. 
	
.. code-block:: javascript

	Entity.Aspect.VisualizationTree.Group1.show(false);

Above command hides all visual objects that belong to Group 1 if they are being displayed. 

Visual group elements can also be visualized individually with the "show(visible)" command.

.. code-block:: javascript

	Entity.Aspect.VisualizationTree.Group1.Element1.show(true);
	
Console Commands
---------
The whole set of commands for Connection are:

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
