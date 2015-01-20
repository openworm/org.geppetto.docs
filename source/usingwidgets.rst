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

In order to instantiate a widget the user can use the command

.. code-block:: javascript

	G.addWidget(TREEVISUALISERDAT)
  or
  G.addWidget(3)

For more information see the documentation related to each individual widget.
If you are interested in contributing a new widget to Geppetto you can follow this :ref:`tutorial <contributewidgets>`.

.. toctree::
   :maxdepth: 2

   plotW
   scatter3DW
   treevisualizerW
   connectivityW
   variablevizW
   popupW
