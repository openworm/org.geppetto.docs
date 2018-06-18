Contribute
==========

-   Before reporting a bug
-   Where to report a bug
-   How to report a bug
-   How to contribute code to Geppetto
-   Geppetto contribution guidelines

Before reporting a bug
----------------------

1.  Search issue tracker for similar issues.
2.  If you are running a local install check against [deployed
    version](live.geppetto.org) to know if it's a local problem.

Where to report a bug
---------------------

-   A Geppetto bug should be reported on
    [org.geppetto](https://github.com/openworm/org.geppetto/) if the
    root cause is unknown.
-   If the root cause is known the issue can be reported on the specific
    Geppetto repository, i.e.
    [org.geppetto.frontend](https://github.com/openworm/org.geppetto.frontend).
-   A list of all the sub repositories can be found
    [here](https://github.com/openworm/org.geppetto/blob/master/README.md).

How to report a bug
-------------------

1.  Specify the version number of Geppetto where the bug occurred (the
    version number is written at the top of the console)
2.  Specify your browser version, operating system, and graphics card.
    (for example, Chrome 23.0.1271.95, Windows 7, Nvidia Quadro 2000M)
3.  Describe the problem in detail. Explain what happened, and what you
    expected would happen.
4.  If applicable provide a small test-case in the form of console
    commands that lead to the issue. To get the list of the commands
    that have been issued to Geppetto type in the console at any
    time G.copyHistoryToClipboard()
5.  If helpful, include a screenshot. Annotate the screenshot
    for clarity.

How to contribute code to Geppetto
----------------------------------

1.  Make sure you have a GitHub account.
2.  Fork the repository you want to contribute to on GitHub.
3.  Make changes to your clone of the repository.
4.  Ensure Geppetto contribution guidelines below are respected.
5.  Submit a pull request.

Geppetto contribution guidelines
--------------------------------

-   Always make your contributions for the latest development branch,
    not master.
-   Create separate branches per patch or feature.
-   Once done with a patch / feature do not add more commits to a
    feature branch (pull requests are not repository state snapshots,
    any change you do in that branch will be included in the
    pull request).
-   Before opening a pull request:
    -   If you are adding functionality to the backend of Geppetto add
        JUnit tests to cover the functionality.
    -   If you are adding functionality to the frontend of Geppetto add
        Casper test coverage.
    -   If you are adding functionality for which integration testing is
        relevant add QUnit tests to cover the whole stack.
    -   Run CoreTests.js and UITests.js Casper Tests, make sure they all
        pass, attach screenshot to pull request
    -   Make sure all pre-exisitng JUnit tests and QUnit tests (you can
        run them at /GeppettoTests.html, e.g.
        [live.geppetto.org/GeppettoTests.html](http://live.geppetto.org/GeppettoTests.html))
        are still passing after your changes.
    -   Perform a UI smoke test checking that the samples in the
        frontend still work.
-   If you add a new feature it's good to add also an example (both for
    showing how it's used and for testing it still works after
    eventual refactorings).
-   If you modify existing code (refactoring / optimization / bug fix),
    run relevant examples to check they didn't break or that there
    wasn't some performance regress.
-   If some [GitHub
    issue](https://github.com/openworm/org.geppetto/issues) is relevant
    to patch / feature, it's good to mention issue number with
    hash (e.g. \#41) in a commit message to get cross-reference in
    GitHub web interface.
-   Format whitespace consistently with the rest of code base (For
    Eclipse users you can use
    [this](https://github.com/openworm/org.geppetto/blob/master/eclipse/GeppettoFormatter.xml)
    format template).
-   If you create new files add
    [License](https://github.com/openworm/org.geppetto/blob/master/LICENSE)
    at the top.

*Special thanks to @mrdoob for being of inspiration for this process.*
