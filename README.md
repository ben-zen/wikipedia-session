Wikipedia CDSW Session README
=============================

&copy; 2015 Ben Lewis.

Documents are published under the [CC-BY-SA 4.0 license][cc], source code is
published under the MIT license (see the LICENSE file.)

This project is an introduction to using the [Requests library][requests] with
the [Wikipedia API][wiki-api] to build data sets and explore them, as a part of
the [Community Data Science Workshops][cdsw] at the
[University of Washington][uw].

The initial work was done by [Mako][mako], however I chose to take the
development of the session in a different direction, to try and de-duplicate as
much as possible. Instead of writing out one long query URL, we build it
piecemeal and then immediately move to using the handy `params` named variable
for the get function in Requests; this way, students see what a query string
looks like and can build one by hand if they ever need to, but they're also
immediately using the tools they'll be using in the future.

[cc]: http://creativecommons.org/licenses/by-sa/4.0/ "Attribution - Share Alike"
[requests]: http://docs.python-requests.org/en/latest/ "HTTP for Humans!"
[wiki-api]: https://www.mediawiki.org/wiki/API:Main_page "MediaWiki API docs."
[cdsw]: http://wiki.communitydata.cc/ "An organization I'm involved with."
[uw]: https://www.washington.edu/ "A fine, upstanding university."
[mako]: https://mako.cc/ "Mako's personal site."
