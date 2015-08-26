***************
Geppetto basics
***************


This section is your key to getting started with Geppetto. It will explain the Geppetto interface, loading projects, opening widgets, and running simulations.
When you are finished reading this section, you will understand how Geppetto works and how to use it to explore a computational model.

* Learning the interface
* Dashboard
* Project explorer

Learning the interface
======================

Geppetto has two main interfaces: the **Dashboard** and the **Project explorer**.
The purpose of the dashboard is to easily view at a glance all the projects that are available to the user.

.. image:: images/sshots/dashboard.png

**Dashboard** - In the demo deployment of Geppetto the dashboard shows some sample projects for a guest user.

Selecting a project in the left pane of the dashboard will reveal its details in the right pane. Double clicking on a project in the left pane will open the selected project in a new browser tab.

.. image:: images/sshots/explorer.png

**Project explorer** - The project explorer shows the morphologies, meta-data and simulation data associated with a given project.


Dashboard
=========

The dashboard is the main entry point to a geppetto based application. The dashboard shows you which projects are available to you. The top right corner indicates which user is logged in for the current session. In the demo deployment of Geppetto this will read "Guest".

Projects
--------

Project
	A Geppetto project is the container of a geppetto model. A project allows you to perform multiple computational experiments on the computational model associated to the project. 

The bar at the top allows you to filter the list of projects, just type in it to search for a specific one.
The right pane shows which experiments are available in the selected project.

Experiments
-----------

Experiment
	A computational experiment in Geppetto lets you specify what value you want to assign to the parameters available in your model and which variables you wish to record when you run a simulation of your model. Recorded variables are called **watched variables** while the parameters are called **model parameters**. An experiment also allows you to specify the **simulation parameters** such as timestep, simulation length and which simulator to use in the given experiment.

An experiment can be in multiple states indicated by a different colour:

Design (Orange)
	The experiment is editable, it is possible to change the variables and parameters associated with it.
Queued (Blue)
	The experiment simulation has been queued and will be executed by the geppetto scheduler soon, from now on the parameters are read only.
Running (Yellow)
	The experiment simulation is currently being executed.
Complete (Green)
	The experiment simulation is completed. It is now possible to replay it and visualize the simulation results.
Error (Red)
	An error occurred while executing the experiment simulation.



Project explorer
================

New experiment
--------------

Simulate experiment
-------------------

