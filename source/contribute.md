Contribute
==========

-   Before reporting a bug
-   Where to report a bug
-   How to report a bug
-   How to contribute code to Geppetto
-   Geppetto contribution guidelines
-   Geppetto code of conduct

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

Geppetto Code of conduct
------------------------
					
All contributors of Geppetto are required to agree with the following code of conduct. Project leads will enforce this code at all times. 		
			
## The Deed (aka the short version)
					
The Geppetto is dedicated to providing a harassment- free experience for everyone regardless of gender, gender identity and expression, sexual orientation, disability, physical appearance, body size, race, age or religion. We do not tolerate harassment of contributors in any form. Advertisement is not appropriate for any Geppetto channel, including Slack. Sexual language and imagery is not appropriate for any Geppetto channel, including Slack. Conference participants violating these rules may be sanctioned or expelled from the Geppetto at the discretion of the Community Organizers. Additionally, Geppetto reserves the right to deny access to community spaces such as forums, channels or any other Geppetto related venue for conversation at any time and for any reason in its sole discretion.
					
## More Detail - Full Policy*
					
Harassment includes verbal comments that reinforce social structures of domination related to gender, gender identity and expression, sexual orientation, disability, physical appearance, body size, race, age, religion; sexual images in public spaces; deliberate intimidation; stalking; following; harassing photography or recording; sustained disruption of meetings or other events; inappropriate physical contact; and unwelcome sexual attention. Contributors asked to stop any harassing behavior are expected to comply immediately.
					
### Expected Behavior
					
The following behaviors are expected and requested of all community members:
					
-   Participate in an authentic and active way. In doing so, you contribute to the health and longevity of this community.				
-   Exercise consideration and respect in your speech and actions.
-   Attempt collaboration before conflict.
-   Refrain from demeaning, discriminatory, or harassing behavior and speech.
-   Be mindful of your surroundings and of your fellow participants. Alert community leaders if you notice a dangerous situation, someone in distress, or violations of this Code of Conduct, even if they seem inconsequential.					
-   Remember that community spaces (Slack, mailing lists, etc.) are shared with members of the public; please be respectful and inclusive at all times
					
### Unacceptable Behavior
					
The following behaviors are considered harassment and are unacceptable within our community:
					
-   Violence, threats of violence or violent language directed against another person.
-   Sexist, racist, homophobic, transphobic, ableist or otherwise discriminatory jokes and language.				
-   Posting advertising material or soliciting business opportunities.
-   Posting or displaying sexually explicit or violent material.
-   Posting or threatening to post other people’s personally identifying information ("doxing").
-   Personal insults, particularly those related to gender, sexual orientation, race, religion, or disability.
-   Inappropriate photography or recording.
-   Inappropriate physical contact. You should have someone’s consent before touching them.
-   Unwelcome sexual attention. This includes, sexualized comments or jokes; inappropriate touching, groping, and unwelcomed sexual advances.
-   Deliberate intimidation, stalking or following (online or in person).
-   Advocating for, or encouraging, any of the above behavior.
-   Sustained disruption of community events, including talks and presentations. 

#### Consequences of Unacceptable Behavior
Anyone asked to stop unacceptable behavior is expected to comply immediately.
We expect participants to follow this code of conduct at all conference venues and conference- related social events.
					
### Reporting
					
If someone makes you or anyone else feel unsafe or unwelcome, please report it as soon as possible. Harassment and other code of conduct violations reduce the value of our event for everyone. We want you to be safe and happy at our event. People like you make our event a better place.
					
Unacceptable behavior from any community member, including sponsors and those with decision-making authority, will not be tolerated.
					
If a community member engages in unacceptable behavior, the community organizers may take any action they deem appropriate, up to and including a temporary ban or permanent expulsion from the community without warning and without refund.
					
You can make a report either personally or anonymously.
Reporting personally can be done directly to conference staff and volunteers.
					
They can be identified by special badges throughout the conference venue.
									
Conference staff will help participants contact hotel/venue security or local law enforcement, provide escorts, or otherwise assist those experiencing harassment to feel safe for the duration of the conference. We value your attendance.
					
### Sponsors and exhibitors
					
Sponsors and exhibitors are also subject to the anti-harassment policy. In particular, exhibitors are asked to not use sexualized images, activities, or other material, and their staff (including volunteers) should not use sexualized clothing/uniforms/costumes, or otherwise create a sexualized environment.
					
This document draws on:
							
http://geekfeminism.wikia.com/wiki/Conference_anti-harassment OW-0 http://confcodeofconduct.com/, OW-BY-SA http://citizencodeofconduct.org/ OW-BY-SA
				




