functional_web_tests
====================

Functional web tests

install sst
download chrome drivers, and add location to path (PATH=$PATH:/path/to/drivers; export PATH)
Chrome drivers: http://code.google.com/p/chromedriver/downloads/list (as given by http://code.google.com/p/selenium/wiki/ChromeDriver)
do the same thing for PhantomJS, but add the bin directory to the path
PhantomJS drivers: http://phantomjs.org/download.html (for installing, don't forget "uname -m" for 32 or 64 bit)


sst-run -b Chrome #calls the chrome binary

from sst import config
config.browser_test = 'Chrome'

from sst.actions import *

nosetests --verbose test*.py
(see https://github.com/nose-devs/nose/issues/2 , nosetests --with-xunit --processes=2 won't work)

Todo:
High
DCLT-279, 201, 196
* document inherited assertions
* test csv imports
* need to be able to pass in the domain to set as the base_url
* determine if project install should be multi-user local, single-user local, or global
* create_testcase command or whatever to create class-based test
* start editing the documentation
* are docstrings passed through on failure?
* remote name should be the test directory

Low
* need package-level test suites not to be run for each checkin (snapshot commit)
* declaration of dependencies (account snapshot, for instance)
* could piggyback off of portal's unit test syntax for simple (not CI related) manual runs
* queue to run tests on snapshot commit
* screenshots and checkins of them/visual diffs

Very Low
* Look at https://developer.mozilla.org/en-US/docs/Marionette
