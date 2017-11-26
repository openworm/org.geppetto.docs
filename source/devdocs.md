Developers documentation
========================

This guide will show you how to build a Geppetto based application and how to contribute to Geppetto.

## Why should I use Geppetto?
Web applications to visualize neuroscience data and/or simulate computational models come with an intrinsic complexity. Neuroscience data is available in a wide range of formats, whether it represents an MRI, a set of large electromicroscopy images, reconstructed neuron morphologies, a set of electrophysiology traces or a time-varying computational model. Usually applications require to load these different type of data from different repositories. Organizing the data before it can be accessed from a frontend is a challenge. Sometimes the data can be accessed from a database and the application that you are building might require to perform queries to fetch and lazy load what the user is interested in. If you are working with multimodal data that you need to integrate then you need to organize the data in a structured, often hierarchical way. You might need to search and query the data from your web application. If you are dealing with computational models then you might want to be able to perform operations like instantiate mulitple population of cells and visualize and simulate them. As you do this you don't want to have to redefine each cell that you want to visualize and you might want to be able to programmatically access each one of them from the web browser with a dedicated API. To simulate your models you might want to have a way of setting different parameters for your models and also parameters specific to your simulator, like the timestep and the duration of your simulation. To transfer all of the data from the backend to the frontend you will have to solve data compression and streaming for it to be efficient. Once the data is available on your frontend you would have to pick and test different libraries to visualize it, making them compatible with your data writing ad-hoc code to interface with each specific API. You would have to do this for each type of data and model. As you are building your frontend application you might want to build a control to search your data, a control panel to manage every entity that was loaded and multiple viewers. You might want to have a way to write tests that can automatically test the backend and the UI of your application and have them running with every commit.

All of the above comes for free in Geppetto, it's a lot of code, it took us years to engineer, implement and test and ultimately is agnostic from the specific application you have to build. Instead, you can focus on building the workflows that are specific to your application and rest upon a robust infrastructure that can contain your code. You can fully customise the UI to make it look like you need. You can reuse all the components we have already built and combine them in any way you want. And you can leverage the Geppetto Model to structure your data so that it becomes automatically indexed and you have programmatic access to it from Javascript.

If you need a persistence layer and user authentication in your application Geppetto offers a persistence bundle that can regulate user authentication and persist user projects using a MySQL database (for more see: [How to configure the Persistence bundle](./persistence.html))

**To put it in one sentence you should use Geppetto to save yourself up to five years of development and skip to building only the code specific to your neuroscience application.**

## What formats does Geppetto support?
 - [BigTIFF](https://www.awaresystems.be/imaging/tiff/bigtiff.html)
 - [COLLADA](https://www.khronos.org/collada/)
 - [DICOM](https://www.dicomlibrary.com/dicom/)
 - [DZI](https://openseadragon.github.io/examples/tilesource-dzi/)
 - [HTML](https://www.w3.org/html/)
 - [LEMS](http://lems.github.io/LEMS/)
 - [NeuroML](https://www.neuroml.org/)
 - [NIfTI](https://brainder.org/2012/09/23/the-nifti-file-format/)
 - [NWB](http://www.nwb.org/)
 - [OBJ](https://en.wikipedia.org/wiki/Wavefront_.obj_file)
 - [SVS](http://openslide.org/formats/aperio/)
 - [SWC](http://www.neuronland.org/NLMorphologyConverter/MorphologyFormats/SWC/Spec.html)
 - *Add more*

## How do I build my own application using Geppetto?
You will need first of all to decide what type deployment you want to use. Our Java backend allows you to build a client server application that can be deployed on your own server or on the cloud (e.g. Amazon EC2, Cloud Docker, etc.). Alternatively client server Python based backends are also available (see this template for Django and this for Flask). [pygeppetto](https://github.com/openworm/pygeppetto) lets you create a Geppetto Model from Python. If you work with Jupyter notebook you also can build Geppetto applications that can run locally on your own Jupyter server. If you use a different stack you will still be able to reuse the Geppetto frontend but you will have to write more integration code.
To customise the frontend of Geppetto you can write your own extension. An extension will let you create your own pages, organise the pre-existing components or add new ones. Although most of the extensions at present use React you will also be able to write an extension using a different Javascript framework. For more info see [here](./build.html).

## What are widgets? What are components?
The user interface of a Geppetto applications can be easily customized. As a developer you will be able to choose among a number of pre-existing components or create new ones specific for your own application. The majority of the components in Geppetto are defined using React although you can use any Javascript technology you are familiar with. Components can be layed out with any CSS layout you will choose. Geppetto offers out of the box the ability to wrap any component with a floating dialog if you desire to create a windows based type of user interface. Historically all components were wrapped in dialog and called widgets while nowadays the floating layout is optional and we call widget any component that has been wrapped in a dialog. All components are designed to expose a Javascript API to control the operation specifics to each. Interactions with the UI result in API calls to each component making it possible to script the whole user interface and to write automated tests against it.

## What components can I reuse?
 - 3D Canvas
 - Big image viewer (suitable for tiled EM, virtual slices)
 - Configurable controls (buttons, menu buttons, popups, etc.)
 - Configurable control panel
 - Configurable search
 - Gallery with thumbnails
 - HTML (to visualize custom HTML)
 - Network connectivity
 - MRI viewer
 - Plot
 - Stack viewer (suitable for Z stacks, connects to an IIP3D server)
 - Tutorial component
 - Tree viewer (suitable to visualize hierarchies)
 - *Add yours*

## What neuronal simulators does Geppetto support?
 - [NEURON](https://www.neuron.yale.edu/neuron/)
 - [NetPyNE](http://www.neurosimlab.org/netpyne/index.html)
 - [jNeuroML](https://github.com/NeuroML/jNeuroML)
 - *Add yours*

## What backends does Geppetto support?
 - JAVA
  - [Source Setup on OSX and Linux](./osxlinuxsetup.html)
  - [Source Setup on Windows](./windowssetup.html)
 - Python
  - [Django template](https://github.com/MetaCell/geppetto-django-template)
  - [Tornado Flask template](https://github.com/MetaCell/geppetto-tornado-flask-template)
 - Jupyter Notebook
  - [NEURON-UI Example](https://github.com/MetaCell/NEURON-UI)
 - [Node.js](https://github.com/openworm/org.geppetto.frontend.nodejs)
 - *Add yours*

## What concepts are covered by the Geppetto Model?
 - 3D primitives
 - Compound types (containers of other types)
 - Experiments
 - Input Parameters
 - Primitive types
 - Queries
 - Simulation
 - Time Series
 - State variables

For a in-depth explanation of the Geppetto Model see [Explain me the Geppetto Model](./geppettomodel.html)

## IDEs
You can develop a Geppetto application using any IDE of your choosing. Eclipse has plugins that make it easier to integrate with the Virgo server were you to choose a Java based deployment, for instructions see [Configuring Geppetto on Eclipse](./eclipsesetup.html) and [Having troubles with Eclipse? Tips and tricks](./devtips.html). To speed up development we use the Webpack development server which let us hot-deploy any change made to the frontend, including the extensions, in seconds. To start the Webpack development server simply type `npm start` from the [webapp](https://github.com/openworm/org.geppetto.frontend/tree/master/src/main/webapp) folder and then access the frontend at the port 8081.

## I don't understand how * works!
Although we put our best effort to document Geppetto there might be things that we haven't yet fully explained in writing. If you have a specific question you can either [join one of our public bi-weekly development meetings](https://calendar.google.com/event?action=TEMPLATE&tmeid=cjAyc2h0cjEwaGFnbjJvYjYxbmRlbzVjcTBfMjAxNzEyMDVUMTYwMDAwWiBicXZscm02NDJtM2lyamVoYmV0aG9ra2NkZ0Bn&tmsrc=bqvlrm642m3irjehbethokkcdg%40group.calendar.google.com&scp=ALL), [ask a question on GitHub](https://github.com/openworm/org.geppetto/issues) or email info@geppetto.org.

## Standing on the shoulders of giants

Geppetto uses the following third party libraries:
- Backend
 - [Eclipse Virgo](http://www.eclipse.org/virgo/)
 - [EMF](https://www.eclipse.org/modeling/emf/)
 - [EMF2JSON](http://emfjson.org/)
 - [maven](https://maven.apache.org/)
 - [OSGi](https://www.osgi.org/)
 - [pyecore](https://github.com/pyecore/pyecore)
 - [Shiro](https://shiro.apache.org/)
 - [Spring](https://spring.io/)

  For a full list of our Java dependencies see [core pom.xml](https://github.com/openworm/org.geppetto.core/blob/master/pom.xml) and [frontend pom.xml](https://github.com/openworm/org.geppetto.frontend/blob/master/src/main/webapp/package.json).

- Frontend
 - [AMI](https://github.com/FNNDSC/ami)
 - [d3.js](https://d3js.org/)
 - [jQuery](https://jquery.com/)
 - [jQuery UI](https://jqueryui.com/)
 - [lightgallery](http://sachinchoolur.github.io/lightGallery/)
 - [npm](https://www.npmjs.com/)
 - [OpenSeadragon](https://openseadragon.github.io/)
 - [pako.js](https://github.com/nodeca/pako)
 - [pixi](http://www.pixijs.com/)
 - [plot.ly.js](https://plot.ly/plotly-js-scientific-d3-charting-library/)
 - [React](https://reactjs.org/)
 - [THREE.js](https://threejs.org/)
 - [webpack](https://webpack.js.org/)

 For a full list see our [package.json](https://github.com/openworm/org.geppetto.frontend/blob/master/src/main/webapp/package.json).

## Index of pages

  - [Contribution guidelines](./contribute.html)
  - [Explain me the Geppetto Model](./geppettomodel.html)
  - [Source Setup on OSX and Linux](./osxlinuxsetup.html)
  - [Source Setup on Windows](./windowssetup.html)
  - [Configuring Geppetto on Eclipse](./eclipsesetup.html)
  - [Having troubles with Eclipse? Tips and tricks](./devtips.html)
  - [Configure and build a custom Geppetto deployment](./build.html)
  - [How to add a new widget](./widgets.html) (slightly obsolete)
  - [How to customise the Search component](./spotlightcustom.html)
  - [How to customise the Control Panel](./controlpanelcustom.html)
  - [How to configure the Persistence bundle](./persistence.html)
  - [How to create a Geppetto Recording with Python](./recordingandreplaying.html)
