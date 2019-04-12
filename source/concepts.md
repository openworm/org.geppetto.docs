Geppetto Concepts
=================

Project
-------

The entry point for a Geppetto application is the ***Geppetto Project***. 
Each Geppetto Project holds a reference to a single Geppetto Model and in 
addition stores the current state of the application (e.g. which components 
are open along with their content and position). Every Geppetto application 
can make use of one or multiple Geppetto Projects.

Every Geppetto Project holds:

* A **model**. Every project has a reference model
* A set of **experiments**
* A custom load script (deprecated)

In addition, a project can be:
* **volatile**: a volatile project cannot be stored
* **public**: a public project can be accessed by every user

Experiment
---------

The Geppetto model defines its own structure and initial values.
A computational experiment in Geppetto defines:
* the parameter values for the simulation of the model (aspect configurations).
* the variables to be recorded for the simulation.
* views configuration

In addition, after the simulation has finished, 
the experiment stores the result of the simulation.
The current model values are then a combination of:
* Initial values
* Experiment parameters
* Simulation results

Model
-----

A Geppetto Model is at the core of every Geppetto project.
A model describes a structured entity; one model could describe
an entity as a particle system, while another model could describe its
biophysical properties. 
A model defines its structure using types and variables, allows to represent
complex data at different abstraction levels, and has the capability to load only the required parts
when needed (lazy loading). See more [here](./geppettomodel.html).
The dynamics of the model are defined through experiments/simulation results. 

Application and worflows
-----------
A basic Geppetto workflow starts by loading a project in the frontend.
After the project is loaded
we can inspect the visual parts of
the model through the widgets defined in the project view.
We can define experiments, run simulations and look at simulation results.

A **Geppetto application** (former *extension*) can define a custom 
workflow and components on the frontend.

Another (old) way to define custom behavior is through project scripts, which are custom
Javascript files which are loaded with the project.

Simulation
----------

A Simulation is the top level controller of Geppetto. A simulation is
configured through a file which describes what entities and models are
to be simulated.

Simulator
---------

A Simulator is directly responsible to simulate a class of models by
employing one or more solvers. A simulator can be seen as a controller
which drives the solvers to compute one or more simulation steps on the
models it is responsible for.

Conversion - Model Interpreter
----------

A Conversion is in charge of converting a model from one format to
another. This conversion service takes place between the **Model
Interpreter** (the service which generates a Geppetto Model from a set of
files) and the simulator. This conversion service can be specified by
the user in the simulation file or automatically invoke by Geppetto.
Geppetto will automatically call this service if the output format of
the model interpreter doesn't match any of the input formats in the
simulation.

Solver
------

A Solver is the lowest level component of the simulation stack and is in
charge of mathematical computation. Generic solvers (e.g. ODE,PDE,etc.)
can be reused across different simulators while specific one can be
implemented ad-hoc for a specific algorithm (e.g. SPH).
