*************************
Geppetto Widgets Tutorial
*************************

 * Creating a Widget
 * Adding Widget to Geppetto
 * Using a Widget Inside Geppetto

Creating a Widget
=================

This tutorial will describe the steps needed start creating your own Geppetto Widget. To begin, you will want to set up a specific file and folder structure. Letâ€™s say you are interested in creating a Geppetto Widget that can plot one or multiple Simulation Variables values in a chart. For example, letâ€™s call it a â€œChartâ€� Widget. The first step would be to create the folder structure, which consists of a parent folder named after the Widget and multiple folders inside it for the controllers and vendor libraries. Â Your folder structure should look something like this. ::

 /chart                  
    /controllers        
    /vendor             
	
The widget will use a combination of Javascript and CSS files, consisting of a main class, configuration script, controller class and a styling CSS file. Below is a brief explanation of the purpose of each of these files. 

Files Needed
------------
Recommended files needed for creating a widget:

+--------------------------------------+----------------------------+--------------------------------------------------------------------------------------------------------------------------+
| File Format                          | Example                    | File Function                                                                                                            |
+======================================+============================+==========================================================================================================================+
| [NameofWidget].js                    | Chart.js                   | Main class of widget: instructions for how the code should behave goes in here.                                          |   
+--------------------------------------+----------------------------+--------------------------------------------------------------------------------------------------------------------------+
| config.js                            | config.js                  | Configuration class for the widget: use to specify the libraries for the widget and export the scripts using requireJS   |   
+--------------------------------------+----------------------------+--------------------------------------------------------------------------------------------------------------------------+
| [NameofWidget].css                   | Chart.css                  | Use to customize your widget.                                                                                            |  
+--------------------------------------+----------------------------+--------------------------------------------------------------------------------------------------------------------------+
| [NameofWidget]Controller.js          | ChartController.js         | Use to bind Geppetto with your widgets: tells your widget what to do when Geppetto tells it to do it.                    |  
+--------------------------------------+----------------------------+--------------------------------------------------------------------------------------------------------------------------+

External libraries and existing plugins can be used as part of your widget. Your newly-created widget class should be the one communicating and using the external libraries/plugins. For example, if wanted to create a widget to chart things in Geppetto, and you know of a javascript library that does charting, you can use that library as a dependency for your widget and build on top of it rather than having to write charting from scratch.

Creating the Main Widget Class
------------------------------
A superclass called `Widget.js <https://github.com/openworm/org.geppetto.frontend/blob/development/src/main/webapp/js/widgets/Widget.js#L43>`_ exists and this contains getters, setters and other global methods for properties that all widgets have, including name, position, id, size, and visibility. The widget class you will be creating extends this superclass. ::

.. code-block:: javascript

   var Chart = Widget.View.extend({
   })
  
Next you will need to populate the class with methods corresponding to the functionality of the widget, such as plotting and updating the chart data. It is within the main widget class that you can use external libraries and plugins to build the widget. Look at the `Plot.js <https://github.com/openworm/org.geppetto.frontend/blob/development/src/main/webapp/js/widgets/plot/Plot.js#L38>`_ widget as an example of a widget built on top of an external library. 

Creating the Controller Class
-----------------------------
The Controller class regulates the handling of events received from Geppetto and how they interact with your widget. The WidgetsListener class, located in the “Widgets” folder, will already handle many of the event types shared among all widgets (e.g., those implemented in Widget.js superclass) including notifying all widgets about new updates. However, you should add an update method to your controller class to handle how updates are sent to the widgets. Other methods that can be added to the controller class are “addWidget()” and “removeWidget()”, which control the creation of your widgets. Take a look at the PlotsController for an example of how to do this. 

.. code-block:: javascript

	define(function(require) {
	return function(GEPPETTO) {
	
		//Rest of Controller code
		}	
	}
	
Creating the config.js Class
----------------------------
The purpose of having a config.js class inside your widget folder is to specify the libraries for the widget and be able to export them via this script. To export the libraries, use `requireJS library <http://requirejs.org/>`_, which allows scripts to load dynamically. If you want to add the files for the widget you just created, include the following lines in the config.js file. ::

.. code-block:: javascript

   var chartModule = [];
	chartModule("widgets/chart/vendor/chartsplugin-1.0");
	chartModule("widgets/chart/Chart");


Where the array chartModule holds the path of all the JS libraries needed for the widget, the “.js” extension can be omitted when adding the scripts to the array, however, the omission is not required.  Notice that the controller class has been omitted for now, we will be adding that class as an AMD Module which is explained in the next section. 

When you have finished populating your chartModule array with your scripts, add them to Geppetto using requireJS as in the example below. The function($) will be called once the scripts have been loaded successfully, at which time you will be able to load the CSS files for the widget. 

.. code-block:: javascript

   require(chartModule, function($) {
      loadCss("js/widgets/chart/Chart.css");
      }); 
  
Folder Structure
----------------
As an example, you have finished creating that widget named â€œChartâ€� for which you used an external library named â€œchartsplugin-1.0â€�. The folder structure of the widget should look like this. ::

    /chart
       -Chart.js
       -Chart.css
       -config.js 
       /controllers
         -ChartController.js
       /vendor
         -chartsplugin-1.0.j
  
The folder named “chart” holds the main widget file “Chart.js” and the related CSS file. The “controllers” folder contains the class binding Geppetto with the widgets. Tthe “vendor” folder contains the external libraries used to create this widget.

Adding Widget to Geppetto
=========================
If you have structured your folder using the recommended structure from the `previous section <https://docs.google.com/a/metacell.us/document/d/160pXT0CProgY2xs5Y8zdHnVGZuV_X-A6ZWvYWnAIYDQ/edit#heading=h.5ncyvsoawo2>`_, you can then drop them inside the “widgets” folder located in the frontend bundle under “src/main/webapp/js”. 

Locate the file “src/main/webapp/js/main.js” and import your widget by adding the location of the script using requireJS. Using our widget example above, we would add the following line to the config.js file.

.. code-block:: javascript

	require(“widgets/chart/config.js”, function($) {});

Using a Widget Inside Geppetto
==============================
If you would like to use your widget from the console within Geppetto, there are a few additional steps. First, you will need to expand the â€œWidgetFactory.jsâ€� class inside the frontend bundle to handle adding and removing your new widget via the console. 

To do this, first add the type of your new widget to the global â€œWidgetsâ€� variable. Simply add the name of your widget followed by the next number from the sequence of previously added widget types. The example â€œCHART,â€� would look like this, ::

.. code-block:: javascript

   var Widgets = {
  		 PLOT : 0,
  		 CHART : 1
       };

Inside the WidgetFactory.addWidget(widgetType) method, add a case inside the switch statement that connects it to your controllerâ€™s new widget method. For example: ::

.. code-block:: javascript

  case Widgets.CHART:
       widget = ChartController.addChartWidget();
       break;

Follow the same logic for WidgetFactory.removeWidget(widgetType): ::

.. code-block:: javascript

  case Widgets.CHART:
       widget = ChartController.removeChartWidget();
       break;

Doing this will allow you to create new widgets from the console using the following commands: ::

.. code-block:: javascript

  G.addWidget(Widgets.CHART);
  G.removeWidget(Widgets.CHART);
