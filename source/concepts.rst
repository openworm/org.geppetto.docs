*****************
Geppetto Concepts
*****************

Model
=====
A Model describes a specific aspect of an entity. A Model could describe an entity as a particle system, while another model could describe its biophysical properties. A model is simulated by a specific simulator bundle.

Simulation
==========
A Simulation is the top level controller of Geppetto. A simulation is configured through a file which describes what entities and models are to be simulated.

Simulator
=========
A Simulator is directly responsible to simulate a class of models by employing one or more solvers. A simulator can be seen as a controller which drives the solvers to compute one or more simulation steps on the models it is responsible for.

Conversion
==========
A Conversion is in charge of converting a model from one format to another. This conversion service takes place between the model interpreter (the service which generates a Geppetto Model from a set of files) and the simulator. This conversion service can be specified by the user in the simulation file or automatically invoke by Geppetto. Geppetto will automatically call this service if the output format of the model interpreter doesn't match any of the input formats in the simulation.

Solver
======
A Solver is the lowest level component of the simulation stack and is in charge of mathematical computation. Generic solvers (e.g. ODE,PDE,etc.) can be reused across different simulators while specific one can be implemented ad-hoc for a specific algorithm (e.g. SPH).
