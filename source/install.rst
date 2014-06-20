**********************************
Geppetto Installation Instructions
**********************************

These steps presume you have Java installed and have set your JAVA_HOME correctly to point at it. To set JAVA_HOME, you can use the following instructions: .. _Windows: https://confluence.atlassian.com/display/DOC/Setting+the+JAVA_HOME+Variable+in+Windows / .. _Linux: http://www.cyberciti.biz/faq/linux-unix-set-java_home-path-variable/

*Java 7* is required to run the latest version of Geppetto.

Install OpenCL drivers:
* On 'Linux <https://github.com/openworm/org.geppetto.solver.sph/blob/master/INSTALL>'_
  - On Mac OS X (Should already be installed)
  - On .. _Windows: https://software.intel.com/en-us/vcsource/tools/opencl-sdk (Should already be installed)
  - Download .. _Geppetto release: https://github.com/openworm/org.geppetto/releases/ and unpack the downloaded archive to a directory (${GEPPETTO_HOME} from here on)
* Start Geppetto ./${GEPPETTO_HOME}/bin/startup.sh (or .bat on Windows)
* Wait. After starting the Kernel there are a lot of things that have to happen to get the server started up. It could take few minutes. Watch the console output until it stops. Geppetto is now running on your machine.
* Point your browser to .. _http://localhost:8080/org.geppetto.frontend/: http://localhost:8080/org.geppetto.frontend/

.. image:: https://dl.dropboxusercontent.com/u/7538688/Screen%20Shot%202014-02-19%20at%2017.36.36.png

You can try loading any of the sample simulations, for instance:
* Small Fluid Hydrodynamics simulation consisting of 780 particles of liquid matter
* Single Hodgkin-Huxley neuron model described in NeuroML and simulated through jLEMS (plotting of two variables is automatically displayed, more can be plotted interacting with the console)

Common Issues
=============
The most common reason your set up will not load is because your OpenCL drivers are not installed properly.
Sometimes this will manifest itself in console errors that look like segmentation faults. Double check that you have properly installed OpenCL. If you still cannot load this, please drop a line to .. _openworm-discuss@googlegroups.com: openworm-discuss@googlegroups.com. In the worst case scenario, you can disable the OpenCL support by removing references to sph in geppetto.plan.

Questions
=========
.. _openworm-discuss@googlegroups.com: openworm-discuss@googlegroups.com
