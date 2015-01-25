Tips for developer to configure/deploy Eclipse + Virgo
********************************************************

Last Update: January 24th 2015

This section provides information on how to style the geppetto frontend using CSS and LESS.
Currently, GEPPETTO uses LESS styling sheets to give the frontend components their current look. 
Each component has a corresponding LESS file, which is also referenced from inside the main.less file.
During development stages, the LESS files will be used, but CSS files will be used during production.
Building the frontend using "mvn clean install -P master" will create a file css file from the LESS components.

The structure of CSS and LESS files looks something like this, and this is how you can expect to 
find the files inside the frontend bundle. 

:
	css

	  main.css

	less

	  components
	    
	     button.less

	  main.less

If you were to make changes to button.less file, the changes would be reflected on the frontend when running it 
using the LESS files, but would not be reflected if pointing to the main.css file. The build using the "-P master" flag 
would be required to compile LESS files into CSS.

The CSS styling sheets for plugin components can be found inside the css directory, these are not part of LESS and are used as provided by their corresponding plugin (font-awesome, codemirror, qunit, jsConsole etc)