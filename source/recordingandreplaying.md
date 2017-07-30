Recordings for dev
==================

A recording stores all the raw data of your simulation run. In Geppetto,
a recording is simply a file in the popular binary data format HDF5.

Furthermore, we developed some handy tools to create Geppetto recordings
from NEURON and Brian simulations. Just replay these in Geppetto, and
couple your existing models with any other simulations that runs in
Geppetto.

Looking at a recording
----------------------

A convenient way to look (as well as edit) a recording is
[HDFView](http://www.hdfgroup.org/products/java/hdfview/), a graphical
browser for HDF5 files.

If you want to dig deeper, there are several implementations of HDF5 for
the command line and all major programming languages. We have found
Python and the [h5py](http://www.h5py.org/) package to be a pretty
intuitive solution.

Why don't you go ahead and try that with one of our [sample
recordings](https://github.com/openworm/org.geppetto.recording/tree/master/samples)?

Creating a recording
--------------------

We have developed a Python 2.7 package which makes it extremely simple
to create recordings. The package is called org.geppetto.recording and
available on
[PyPi](https://pypi.python.org/pypi/org.geppetto.recording/0.0.1). For
install instructions and code, see the [Github
repository](https://github.com/openworm/org.geppetto.recording).

As recording files are plain HDF5, they can also be created and
manipulated by many other tools and programming languages
([examples](http://www.hdfgroup.org/HDF5/examples/)).

### Manually

You successfully installed org.geppetto.recording? Cool, then let's go
down to Python and import everything that we need:

    >>> from org.geppetto.recording.creators import RecordingCreator, MetaType

`RecordingCreator` is the base class to create a recording for Geppetto.
It allows you to add variables and values, define a time step vector
(fixed or variable) and add metadata for the recording. Other creators
(for example for NEURON or Brian) inherit from this class, so you can
always manipulate their data manually.

To create a new recording file, run:

    >>> c = RecordingCreator('recording_file.h5')

If you see nothing happen on your file system, don't worry: The actual
file will be written in the end. This just sets up everything and makes
sure the file name is available.

Next, we will populate our recording with some values:

    >>> c.add_values('cell.voltage', [-60.0, -59.9, -59.8], 'mV', MetaType.STATE_VARIABLE)
    >>> c.add_values('cell.voltage', -59.7)
    >>> c.add_values('cell.radius', 20, 'um', MetaType.PARAMETER)

As you can see, the name of the variable can be dot separated to express
a hierarchical relation. This hierarchy will also be represented in the
HDF5 file later (see File Format\_).

The `add_values` method can both take single values or iterables of
values. Its last parameter describes which kind of variable you want to
store (the so called meta type). It can be one of
`MetaType.STATE_VARIABLE`, `MetaType.PARAMETER`, `MetaType.PROPERTY`,
`MetaType.EVENT`. Furthermore, you can call `add_values` multiple times
for the same variable to append further values (you can omit unit and
meta type then).

A simulation is nothing without time! In Geppetto, each value of a state
variables is associated with a point in time (the variable changes its
"state" over time). You can either add a fixed time step (i. e. the
interval between two time points):

    >>> c.set_time_step(0.1, 'ms')

Or you can supply the individual time points as you like:

    >>> c.add_time_points([0.1, 0.15, 0.3], 'ms')

Just as with values, you can add single or multiple time points and call
`add_time_points` again to append. Keep in mind to only use one of these
two methods - we don't want to have multiple timelines ;)

Next to values, the recording file can also store metadata for your
simulation. Simply call:

    >>> c.add_metadata('version', 1.0)

When you have added enough values, tell the creator to flush everything
to file by calling:

    >>> c.create()

There you go! If you want to have a look at your new recording, try
[HDFView](http://www.hdfgroup.org/products/java/hdfview/) (or read
Looking at a recording\_).

Complete documentation for the `RecordingCreator` class coming soon!

### From Brian

### From NEURON

File format
-----------

Geppetto's recordings are plain [HDF5](http://www.hdfgroup.org/HDF5/)
files.

HDF5 is an efficient binary format and very popular amongst the
scientific community. Furthermore, it is hierarchical: Every HDF5 file
is made up of groups (these act like folders in a file system) and
datasets (these act like files in a file system). Both groups and
datasets can have attributes, which makes it fairly easy to store
metadata along with your actual data. See also [the official
tutorial](http://www.hdfgroup.org/HDF5/Tutor/fileorg.html).

A Geppetto recording is a pretty intuitive implementation of HDF5:
Hierarchies of entities and variables are expressed 1:1 as hierarchies
in HDF5. For example, if you have one variable `cell.voltage` and
another one `cell.radius` in your simulation, there will be one group
`cell` with two datasets `voltage` and `radius` in the file. The unit
and meta type of these variables will be stored as attributes to their
respective datasets.

Additionally, there will be one dataset in the root group called `time`.
This is simply an array of all time points during the simulation (these
are associated with the state variables in the recording).

Global metadata for the recording is stored as attributes of the root
group.
