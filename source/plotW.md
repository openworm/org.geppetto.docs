Plot Widget
===========

This widget allows Geppetto plotting of simulation variables and data

A new Plot widget can be created from the console using the command

``` {.sourceCode .javascript}
G.addWidget(Widgets.PLOT)
```

Alternatively *Shortcut Key: Ctl+Alt+P* - Toggles existing plotting
widgets, if none exist it creates a new one.

Plotting widgets can plot variables straight from the simulation, given
you are watching the variables at the time you start plotting it. Each
variable will have its own line plot, and it's accompanied by a label to
distinguish it from other variables being drawn.

In order to plot a Simulation variable, you can use the command

``` {.sourceCode .javascript}
Plot1.plotData(variable);
```

Where "Plot1" is the name of the plotting widget that was returned after
creation.

![image](http://i.imgur.com/PigAtLo.png)

Other variables can also be plotted, as a two dimensional array plotted
against x and y coordinates. You can customize your line plot and change
the dimensions of the axis in your plot, use the "Commands" section as a
reference to see what options you have to modify your plot.

![image](http://i.imgur.com/Sf9byfH.png)

Setting Legend for Variables ----------User can modify the legend that
is displayed for a variable being plotted using the following command:

``` {.sourceCode .javascript}
Plot1.setLegend(variable, legend);
```

Where variable represents the object being plotted, and legend is a
string with the new legend to be displayed for corresponding variable.

If user fails to specify a legend, the instance path of the variable
being plotted will be used. However, it will only be partially displayed
to save space inside the widget. To view the full name of the variable
user can hover over the legend and a tool-tip with full name will
appear.

Setting Options ----------User can modify a Plot Widget settings,
including: x and y axis, line plot's visibility of points and lines.
Create a javascript object in the console specifying the options, and
use setOptions() with the created object to set the options for the Plot
Widget.

The following values can be used to modify a Plot settings.

-   yaxis - Object that sets a minimimum and maximum value for the Y
    axis of the graph. Use {yaxis : { min : 'value', max : 'value'}} to
    set yaxis.
-   xaxis - Object that sets a minimimum and maximum value for the X
    axis of the graph. Use {xaxis : { min : 'value', max : 'value'}} to
    set xaxis.
-   series - Object that turns on/off lines and points in the graph.

**Example:**

``` {.sourceCode .javascript}
var linePlotOptions ={
        yaxis: { min : 0,max : 15},
        xaxis: {min : 0, max : 15},
        series: {
                lines: { show: true },
                points: { show: true }
        },
}

//set the options for the plot
plot1.setPlotOptions(plotOptions);
```
