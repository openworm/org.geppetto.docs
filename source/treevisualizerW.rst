***************
Tree Visualizer Widget
***************

The following commands will let you load up a tree visualizer, assuming that you have an entity loaded up named 'net':

.. code-block:: javascript

	G.addWidget(GEPPETTO.Widgets.TREEVISUALISERDAT);
	TreeVisualiserDAT1.setData(net);

Note that you can pass any node to a tree visualizer, e.g. assuming that you have a sub entity named 'muscle_0':

.. code-block:: javascript

	TreeVisualiserDAT1.setData(net.muscle_0);

The properties of tree visualizer widget can be easily set as for any other widget:

.. code-block:: javascript

	TreeVisualiserDAT1.setSize(50,200);
	TreeVisualiserDAT1.setPosition(100,200);
	TreeVisualiserDAT1.setName("MyTree");
	
If the Model sub tree for a given aspect is empty, remember that the model tree is not populated by default but can easily be done with the following command (assuming an entity named 'net' containing an aspect named 'electrical'):

.. code-block:: javascript

	net.electrical.getModelTree();
	

