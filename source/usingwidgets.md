Widgets
=======

Geppetto has a modular architecture that allows to visualize and
interact with the data through different widgets. Widgets are an
essential aspect of the user interface of Geppetto. You can imagine them
as "at-a-glance" views of data and functionality that is accessible
right from the browser. Users can move widgets across the screen, resize
them and interact with their functionality through their API or the
provided UI.

## [Plot](./plotW.html)
## [Popup](./popupW.html)
## [Connectivity Widget](./connectivityW.html)
## Movie player (Docs TBD)
## MRI widget (Docs TBD)
## Stack Viewer (Docs TBD)
## Big Images Viewer (Docs TBD)

Widgets are normally created using the user interface, to create one manually from the console the following API can be used

```
G.addWidget("PLOT")
```

or

```
G.addWidget(0)
```

For more information see the documentation related to each individual
widget. If you are interested in contributing a new widget to Geppetto
you can follow [this tutorial](./widgets.html).
