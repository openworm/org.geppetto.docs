=================
Button Bar Widget
=================

This widget allows the user to define a custom button bar. Each button has customizable label, icon, tooltip, and can fire any sequence of Geppetto commands when pressed.  Buttons are also grouped in groups.

Button bars can either be read from external *json* files, or explicitly through javascript objects.


Reading a Button Bar defined in an external configuration *json* file
=====================================================================

In order to load an externally defined button bar (i. e. defined in a self-contained file), run the following command:

.. code-block:: javascript

  G.addWidget(Widgets.BUTTONBAR).fromJSON('http://path.to/file')


Configuration file syntax
=========================

Here is an example of a button bar definition in *json*:

.. code-block:: json

  {
   "Sample ButtonBar": {
      "buttonGroupOne": {
        "buttonOne": {
          "actions": [
            "GEPPETTO.Console.log('button1.action1')",
            "GEPPETTO.Console.log('button1.action2')"
          ],
          "icon": "gpt-osb",
          "label": "1",
          "tooltip": "This is a button"
        },
        "buttonTwo": {
          "actions": [
            "GEPPETTO.Console.log('button2.action1')"
          ],
          "icon": "gpt-pyramidal-cell",
          "label": "2",
          "tooltip": "This is another button"
        },
        "buttonThree": {
          "actions": [
            "G.addWidget(1).setMessage('hello from button 3')"
          ],
          "icon": "gpt-ion-channel",
          "label": "3",
          "tooltip": "Yet another"
        }
    	},
	    "buttonGroupTwo": {
	      "buttonFour": {
	        "actions": [
	          "G.addWidget(1).setMessage('hello from button 4')"
	        ],
	        "icon": "gpt-make-group",
	        "label": "four",
	        "tooltip": "And yet another..."
	      },
	      "buttonFive": {
          "actions": [
            "G.addWidget(1).setMessage('hello from The Worm')"
          ],
          "icon": "gpt-worm",
          "label": "five",
          "tooltip": "OK, I'll stop now!"
        }
      }
	   }
  }

This configuration file gives rise to the following button bar:

.. |bubar| figure:: images/bubar/bubar.png


The syntax of the configuration file is meant to be intuitive:

1. rd level : the name of the toolbar (only one)
2. rd level : button group definitions (any number)
3. rd level : definition (any number)


Each button has the following attributes:


* label: text displayes inside the actual button
* icon:  button icon displayed alongside the label. See the `Geppetto Icons <https://github.com/borismarin/org.geppetto.frontend.icons>`_ project for
  custom icons
* action: a list of Geppetto commands to be executed sequentially *exactly as if being typed from the console*.
* tooltip: text displayed when the mouse is hovered over the button.
