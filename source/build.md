What is a Geppetto Extension?
==============

A Geppetto extension is a folder with some custom client code you can write to completely customise the Geppetto UI. A minimal extension consists of an entry point js file (normally named ComponentsInitialization.js, but it can be renamed to anything) and a css file. 

- **ComponentsInitialization.js**: This js file defines which components will be present in the Geppetto UI and where they are placed, but it can also contain any custom js code as needed (simple js functions or importing other files from the extension if any are needed). 
- **CSS**: The css file is meant to provide styles for your Geppetto application. 

The minimal set is the two files described above, but there is no limit to how complex an extension can be. For example, you can develop any number of components and import them with require from any other js file/folder in your extension. 

You can use any of the Geppetto dependencies included in the [package.json](https://github.com/openworm/org.geppetto.frontend/blob/master/src/main/webapp/package.json) in Geppetto, or add your own as static dependencies somewhere in your extensions folder. In the future each extension will have its own package.json file (this feature is on the Geppetto development roadmap). 

How Do I create My Own Geppetto Extension?
==============

Creating your own Geppetto extension is very simple, as simple as creating a folder with a js file and a css file. You might want to create a GitHub repo to contain your files and then clone the repo in the org.geppetto.frontend/scr/main/webapp/extensions folder. You will notice that in the extensions folder there is already a [default Geppetto extension](https://github.com/openworm/org.geppetto.frontend/tree/master/src/main/webapp/extensions/geppetto-default), which defines the default Geppetto UI and provides a first example of what you can do from your custom code to add components to the Geppetto UI. 

In the ComponentInitialization file, for example, you can define your own js functions as needed and interact with the Geppetto API to add components that Geppetto makes available. 

For example, the following code adds the 3D canvas component to the background element with id="sim" (a commonly used component conveniently provided by Geppetto):
```
    //Canvas initialisation
    GEPPETTO.ComponentFactory.addComponent('CANVAS', {}, document.getElementById("sim"), function () {
        this.displayAllInstances();
    });
```

Or as another example, the code below is injecting a logo component to the element with id="geppettologo" (again, conveniently provided by Geppetto; it appears in the top right) and then injecting a Link button component, that links to the source code on GitHub, while also specifying a position for this element:
```
    //Logo initialization
	GEPPETTO.ComponentFactory.addComponent('LOGO', {logo: 'gpt-gpt_logo'}, document.getElementById("geppettologo"));
    //Source code link initialization
	GEPPETTO.ComponentFactory.addComponent('LINKBUTTON', { left: 41, top: 390, icon: 'fa-github', url: 'https://github.com/openworm/org.geppetto'}, document.getElementById("github-logo"));
```
In the examples above we are using DOM elements provided by Geppetto by default for convenience, but nothing stops you from adding your own DOM elements with jQuery (or vanilla js) from your component initialization file and then adding components wherever you want. If a DOM element is not specified, the component will be added in a floating window (also known as a "Geppetto widget").

*NOTE*: Since Geppetto exposes a dependency to [react.js](https://reactjs.org/) (much of its internals use this framework), if you want you can use React to define your custom components or even just to instantiate Geppetto components from a simple React render method. Just require react and react-dom at the top of your ComponentsInitialization.js. 

Once you have created your own extension, you need to tell Geppetto to use it instead of using the default one. This is very simple and achieved by editing the [GeppettoConfiguration.json](https://github.com/openworm/org.geppetto.frontend/blob/master/src/main/webapp/GeppettoConfiguration.json) file located in the same webapp folder. 

Assuming your extension repo/folder is named "geppetto-custom-extension" and your js entry point file is called ComponentsInitialization.js and your css file is called theme.css, the GeppettoConfiguration.json should look like this:

```
{
    "_README" : "http://docs.geppetto.org/en/latest/build.html",
    "contextPath": "org.geppetto.frontend",
    "useSsl": false,
    "embedded": false,
    "embedderURL": ["/"],
    "noTest": false,
    "extensions": {
        "geppetto-default/ComponentsInitialization": false,
        "geppetto-custom-extension/ComponentsInitialization": true
    },
    "themes": {
        "geppetto-default/colors": false,
        "geppetto-custom-extension/theme": true
    }
}
```
All the other parameters in the json will be discussed under the "Geppetto Build" section of this same document. 

Geppetto Extensions Examples
==============

You can achieve virtually any look & feel with a Geppetto extension. We provide below some examples of UIs built as Geppetto extensions (extension code also linked if available as open source software):

[**geppetto-default**](https://github.com/openworm/org.geppetto.frontend/tree/master/src/main/webapp/extensions/geppetto-default): the default Geppetto extension we know and love, available on [live.geppetto.org](https://live.geppetto.org/).
![Geppetto default extension](images/default.png)

[**geppetto-osb**](https://github.com/OpenSourceBrain/geppetto-osb/tree/development): Geppetto extension for [Open Source Brain](http://www.opensourcebrain.org/), a repository of open source computational neuroscience models that features a Geppetto based 3D viewer of morphologies and simulation environment.
![Geppetto OSB extension](images/osb.png)

[**geppetto-vfb**](https://github.com/VirtualFlyBrain/geppetto-vfb/tree/development): Geppetto extension for [Virtual Fly Brain](https://v2a.virtualflybrain.org/), a reference for drosopohila neuroanatomy and ontology. 
![Geppetto VFB extension](images/vfb.png)

**geppetto-hm**: [Patienthm.org](http://patienthm.org/), portal and atlas of all [Patient HM](https://en.wikipedia.org/wiki/Henry_Molaison) imaging data entirely built as a Geppetto extension. 
![Geppetto HM extension - MRI](images/hm1.png)
![Geppetto HM extension - Big image viewer](images/hm2.png)

How to deploy a Geppetto extension in my Eclipse environment
==============

In this section we will show you how to deploy a custom extension, [OpenSourceBrain](http://www.opensourcebrain.org/) (shortened with OSB), to your local Geppetto environment.
The below assumes that you already have your Geppetto and Eclipse environment configured locally. If that is not the case, see the following pages:
-   [Source Setup on OSX and Linux](http://docs.geppetto.org/en/latest/osxlinuxsetup.html) or [Source Setup on Windows](http://docs.geppetto.org/en/latest/windowssetup.html)
-   [Instructions for setting up Geppetto on Eclipse Neon](http://docs.geppetto.org/en/latest/eclipsesetup.html)

First of all, starting from our home folder we begin by cloning the OSB extension repository into the Geppetto Frontend's extension folder, located in the geppetto-sources folder.
```
cd geppetto-sources
cd org.geppetto.frontend/src/main/webapp/extensions/
git clone https://github.com/OpenSourceBrain/geppetto-osb
```

The next step will be to edit, with our favourite editor or Eclipse, the GeppettoConfiguration.json file (path below) in order to disable the default extension and to enable the OSB extension.

`
org.geppetto.frontend/src/main/webapp/GeppettoConfiguration.json
`

Here you have a screenshot of the file pre-change:
![OSB extension pre change](images/osb_extension/osb-ext1.png)

And here it is post-change:
![OSB extension post change](images/osb_extension/osb-ext2.png)

Once done, we can move back to Eclipse. We will need to update our org.geppetto.frontend project to take into account the changes made.
We can start by right clicking on the bundle org.geppetto.frontend->Maven->Update Project.
Then, we right click again on org.geppetto.frontend->Run As->Maven Install. This will re-build our bundle and npm will automatically redeploy the frontend to the Virgo server's folder so that we can use the new extension.
Once the server finishes starting all the bundles, we can open the [Geppetto frontend homepage](http://localhost:8080/org.geppetto.frontend/) with our browser and load, for example, the [CA1 Pyramidal Cell experiment](http://localhost:8080/org.geppetto.frontend/geppetto?load_project_from_id=3) and see our loaded extension working.

Geppetto Build
==============

-   Geppetto Configuration
-   Maven Profiles
-   Development Build
-   Production Build

Geppetto Configuration
======================

Geppetto lets you configure your deployment with a set of parameters
that are defined in
org.geppetto.frontend/src/main/webapp/GeppettoConfiguration.json. This
file exposes the following parameters:

-   `contextPath`: The context path is the prefix of the URL path to
    access Geppetto. Typically contextPath is
    "org.geppetto.frontend" for development and "/" for production. Assuming a local
    development environment with contextPath "org.geppetto.frontend",
    you will access Geppetto at localhost:
    localhost:8080/org.geppetto.frontend
-   `useSsl`: If true, Geppetto will be configured to use https instead of http.
-   `embedded`: Geppetto is configured to work as an embedded instance
    inside an iframe. This means CORS will be enabled, a postMessage
    channel will be available for the main frame, some layout and href
    calls customization, etc.
-   `embbedderURL`: If running in embedded mode, this specifies the URL of
    the main frame container. For security reasons Geppetto will only
    accept cross-origin calls from this URL.
-   `noTest`: If true, tests are suppressed during the build process. If
    false, tests will be run as part of the build process.
-   `extensions`: Geppetto can be customised by defining JS and LESS/CSS
    files placed in a folder inside the extensions folder. The
    extension can be enabled using this parameter. By default, Geppetto
    provides a default
    extension (org.geppetto.frontend/src/main/webapp/extensions/geppetto-default)
    that can be used as an example to build custom extensions.
-   `themes`: Defines a Geppetto "theme". So far, we only expose a few
    parameters defining colours. Below you can find a list of the
    parameters exposed that can be overridden by your custom theme file:

        @primary_color: #fc6320;
        @secondary_color: #fc401a;
        @background_color_body_0: #141a1e;
        @background_color_body_50: #5c6268;
        @background_color_body_73: #60666d;
        @background_color_body_100: #515359;
        @background_color_widget: rgb(66, 59, 59);

In order to implement a new theme, a less file needs to be created
defining some or all these parameters and the theme needs to be
specified in the themes and set to true.

This is how the default (and recommended for development environments)
GeppettoConfiguration.json looks:

        { "contextPath":
        "org.geppetto.frontend", "useSsl": false, "embedded": false,
        "embedderURL": \["/"\], "noTest": false, "extensions": {
        "geppetto-default/ComponentsInitialization": true,
        "geppetto-osb/ComponentsInitialization": false,
        "geppetto-vfb/ComponentsInitialization": false,
        "geppetto-neuron/ComponentsInitialization": false,
        "geppetto-hm/ComponentsInitialization": false }, "themes": {
        "geppetto-default/colors": true, "geppetto-hm/pages/styles/colors":
        false } 
        }

And this is an example of a production environment with a different
extension and theme: 

        { "contextPath": "/", "useSsl": true,
        "embedded": false, "embedderURL": \["/"\], "noTest": false,
        "extensions": { "geppetto-default/ComponentsInitialization": false,
        "geppetto-osb/ComponentsInitialization": false,
        "geppetto-vfb/ComponentsInitialization": false,
        "geppetto-neuron/ComponentsInitialization": false,
        "geppetto-hm/ComponentsInitialization": true }, "themes": {
        "geppetto-default/colors": true, "geppetto-hm/hm\_theme": true } }

Maven Profiles
==============

Geppetto is built using Maven, with the "mvn -Dhttps.protocols=TLSv1.2 install" command. Maven
allows for different build steps to be specified for different
environments, and Geppetto provides a development and a production
profile (see below for how to trigger different builds). Builds can be
triggered at the root from the org.geppetto bundle and parameters will
be propagated to the children (child bundles are defined in
org.geppetto/pom.xml). Maven builds can also be triggered for individual
bundles from the specific bundle root that needs to be built.

Building for development
========================

`mvn -Dhttps.protocols=TLSv1.2 install`

When the command "mvn -Dhttps.protocols=TLSv1.2 install" is executed, none of the optimisation
tasks are run. When doing development, it is not necessary to run the
production build unless you wish to simulate a production environment.

Building for production
=======================

`mvn -Dhttps.protocols=TLSv1.2 install -P master`

Some optimisation tasks are applied to the org.geppetto.frontend bundle
to optimise performance and security. To see the difference between
profiles have a look at
org.geppetto.frontend/src/main/webapp/package.json.

Overriding Geppetto Parameters with mvn 
=======================================

Geppetto configuration settings can be overwritten by passing the
parameters to the "mvn -Dhttps.protocols=TLSv1.2 install" command. An example follows:

`mvn -Dhttps.protocols=TLSv1.2 install "-DcontextPath=theearth" "-DuseSsl=true" "-Dembedded=true" "-DembedderURL=universe,milkyway"`
