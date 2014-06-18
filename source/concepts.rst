*****************
Geppetto Concepts
*****************

Entity
======
An Entity is the basic building block of the simulated world. An entity can aggregate other entities and be described by different Models. In the real world an entity could be a cell, a worm, a leaf or a city for instance. Entities are boundary containers which make possible to logically described what needs to be simulated. Geppetto is not strongly typed and an entity is solely described by its models and aggregated entities.

Model
=====
A Model describes a specific aspect of an entity. A Model could describe an entity as a particle system, while another model could describe its biophysical properties. A model is simulated by a specific simulator bundle.

Simulation
==========
A Simulation is the top level controller of Geppetto. A simulation is configured through a file which describes what entities and models are to be simulated.

Simulator
=========
A Simulator is directly responsible to simulate a class of models by employing one or more solvers. A simulator can be seen as a controller which drives the solvers to compute one or more simulation steps on the models it is responsible for.

Solver
======
A Solver is the lowest level component of the simulation stack and is in charge of mathematical computation. Generic solvers (e.g. ODE,PDE,etc.) can be reused across different simulators while specific one can be implemented ad-hoc for a specific algorithm (e.g. SPH).
