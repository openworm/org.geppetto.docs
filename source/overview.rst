********
Overview
********

 * Background
 * The architecture
 * Technology stack
 * Status
 * Feedback



Background
==========

The decision to build Geppetto came after an analysis of the requirements for a platform to support a full-scale simulation of the C. elegans and potentially even more complex organisms in times to come.  Beside the functional requirements, Geppetto's goal is to move away from the common monolithic approach usually found in academic software projects.  Geppetto is an `open source project <https://github.com/openworm/org.geppetto/blob/master/README.md>`__  and engineers, scientists and developers are welcome to contribute to its development by adding functionalities to existing plugins or writing new ones without having to deal with millions of lines of code with no clearly defined boundaries.

Computational neuroscience has produced software systems, including NEURON and Genesis, that are extremely useful for simulating systems of neurons that include biophysical details (`Brette et al, 2007 <http://arxiv.org/abs/q-bio.NC/0611089>`__).  There also exist a range of other algorithms devised in other areas of computational biology (`Barnes & Chu, 2010 <http://g.ua/MhoV>`__) for which simulators have been produced (`Takahashi, 2004 <http://web.sfc.keio.ac.jp/~shafi/takahashi-thesis.pdf>`__).  Several investigations have pointed to the challenges in building a single system that integrates multiple simulation algorithms together into a single biological model (`Takahashi et al., 2002 <http://g.ua/Mhx1>`__, `Dada and Mendes, 2007 <http://dx.doi.org/10.1007/978-3-642-02879-3>`__ , `Cornelis et al., 2012 <http://g.ua/Mhxa>`__ ).  

Geppetto aims to address these scientific challenges along with some engineering ones. Geppetto's design leverages cutting edge software technologies and its architecture and development follows industry standards. 

The architecture
================

The analysis of the requirements for Geppetto resulted in a clearly identified set of architectural features that have driven its development:

*Modular*
---------

Geppetto allows separation of functionality into independent, interchangeable modules such that each contains everything necessary to execute a given aspect of desired functionality.

*Scalable*
----------

Geppetto can handle a growing amount of work in a robust fashion by being intrinsically distributed, scaling up to accomodate growing load.

*Extensible*
------------

Geppetto allows for future growth by including hooks and mechanisms for expanding/enhancing the system with anticipated capabilities, without having to make ad-hoc changes to the system infrastructure.

*Generic*
---------

Geppetto is not tied to any specific biological simulation, nor to the model being simulated or the simulation aspects (neuronal, mechanical, etc.) being simulated.

*Client-Server*
---------------

Geppetto is based on a client-server model, where the simulation is controlled by a client through a web interface.

*Distributed*
-------------

Geppetto architecture needs to allow separation of the execution of a simulation into multiple processes which can be executed by different server and which communicate with each other by exchanging messages.

*Dynamic deployment*
--------------------

Geppetto components can be deployed, re-deployed, and un-deployed without a system (server) restart.


Technology stack
================

Geppetto is written in JAVA on top of the 'OSGi framework <http://en.wikipedia.org/wiki/OSGi>`__. This enables us to build modules as “OSGi bundles”, independent components that allow for clean separations between functional areas that are simulating different aspects of a bio-physical system. 

On top of OSGi, `Spring <http://www.springsource.org/about>`__ has been chosen as the glue-framework to assemble a complex system from a set of loosely-coupled components (POJOs) in a consistent and transparent fashion.

`Technology stack <http://static.springsource.org/osgi/docs/1.1.0/reference/html/images/spring-osgi-model.png>`__

Geppetto OSGi based bundles are deployed on the `Eclipse Virgo <http://www.eclipse.org/virgo/>`__ WebServer.

`Virgo <http://www.eclipse.org/virgo/images/virgo-logo.png>`__


Status
======

Geppetto is currently in development. A version is `released every month <https://github.com/openworm/org.geppetto/releases/>`__ with new added features.
While the Geppetto platform is engineered with a generic framework capable of encapsulating any algorithm into a module, the `OpenWorm project <http://www.openworm.org>`__ has begun implementing specific modules to meet the particular challenges of its domain. The OpenWorm case study has led to the development of one module to simulate the electrophysiology of neuronal cells and networks, and another to simulate fluid-mechanics based on the smoothed particle hydrodynamics (SPH) algorithm (`Solenthaler 2011 <http://www.zora.uzh.ch/29724/1/Barbara.pdf>`__ ). SPH provides the ability to simulate soft tissues and their interface to liquids of varying viscosities, which in turn allows for the simulation of forces created by muscles pulling on a non-rigid body.

Feedback
========

Geppetto is being developed to combine cutting edge science into an industry grade software platform. The open source nature is essential in this process and so is your feedback. If you have any question please `email us <mailto:info@geppetto.org>`__ . If you wish to raise a bug, request a feature or an enhancement please do so by logging an `issue <https://github.com/openworm/org.geppetto/issues>`__ . If the issues is related to a specific module (e.g. `frontend <https://github.com/openworm/org.geppetto.frontend/issues>`__ , `fluid mechanics simulator <https://github.com/openworm/org.geppetto.simulator.sph/issues>`__ , etc.) you can log it directly on it.




