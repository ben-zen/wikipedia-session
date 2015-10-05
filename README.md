Wikipedia CDSW Session README
=============================

&copy; 2015 Ben Lewis.
Documents are publised under the CC-BY-SA 4.0 license, source code is published
under the MIT license (see the LICENSE file.)

This project is an introduction to using the
[Requests library](http://docs.python-requests.org/en/latest/) with the
Wikipedia API to build data sets and explore them, as a part of the Community
Data Science Workshops at the University of Washington.

The initial work was done by Mako, however I chose to take the development of
the session in a different direction, to try and de-duplicate as much as
possible. Instead of writing out one long query URL, we build it piecemeal and
then immediately move to using the handy `params` named variable for the get
function in Requests; this way, students see what a query string looks like and
can build one by hand if they ever need to, but they're also immediately using
the tools they'll be using in the future.
