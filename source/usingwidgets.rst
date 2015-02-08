#########
Widgets
#########

Geppetto has a modular architecture that allows to visualize and interact with the data through different widgets.
Widgets are an essential aspect of the user interface of Geppetto.
You can imagine them as "at-a-glance" views of data and functionality that is accessible right from the browser.
Users can move widgets across the screen, resize them and interact with their functionality through their API or the provided UI.

To see what widgets are available in Geppetto the user can type in the console the command

.. code-block:: javascript

	G.availableWidgets()

which would return a list like this:

.. code-block:: javascript

	{"PLOT":0,"POPUP":1,"SCATTER3D":2,"TREEVISUALISERDAT":3,"TREEVISUALISERD3":4,"VARIABLEVISUALISER":5,"CONNECTIVITY":6}

Specific documentation on different widget types are available below:

* A plot widget shows a line graph of data tied to variables that are changing in a simulation
* A popup widget can display arbitrary text to annotate / document a model
* A Scatter 3D widget shows a scatter plot
* A TreeVisualizer DAT widget shows model properties in a hierarchical tree view.
* A Variable visualizer widget displays the changing values of a variable
* A Connectivity widget displays connections between neurons in a network.


In order to instantiate a widget the user can use the command

.. code-block:: javascript

  G.addWidget(TREEVISUALISERDAT)

or

.. code-block:: javascript

  G.addWidget(3)

For more information see the documentation related to each individual widget.
If you are interested in contributing a new widget to Geppetto you can follow this :ref:`tutorial <contributewidgets>`.

.. toctree::
   :maxdepth: 2

   plotW
   popupW
   scatter3DW
   treevisualizerW
   variablevizW
   connectivityW

