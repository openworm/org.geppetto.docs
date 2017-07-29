**********\* Geppetto Source Files Documentation**********\*

Javascript ======== Documentation for the source files can be found in
here

> -   [<http://live.geppetto.org/jsdocs>](http://live.geppetto.org/jsdocs)

Building the docs
=================

The jsdocs are generated using mvn site in the org.geppetto.frontend
bundle. They do not generate automatically during mvn install.

How to Document ======== To make source files appear under the
documentation site, you have to comment your code using jsdocs3 tags.

For example, to document a class you will add at the top comment.

``` {.sourceCode .javascript}
/**
 *
 * Comment of class
 * @module NameOfClass
 * @author  NameofAuthor (author@email.com)
 */
 define(function(require) {
```

To document a method:

``` {.sourceCode .javascript}
/**
 *
 * Method comments
 *
 * @param {Object} options - comments for otions
 * @returns {String} message
 */
method: function(options) {
```

Where the tag @param is used for documenting parameters and @return for
what the method returns

To view more tags for documentation follow the following tutorial.

-   [jsdocs](http://usejsdoc.org/)

