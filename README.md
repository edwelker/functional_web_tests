functional_web_tests
====================

Functional web tests

install sst
download chrome drivers, and add location to path (PATH=$PATH:/path/to/drivers; export PATH)
Chrome drivers: http://code.google.com/p/chromedriver/downloads/list (as given by http://code.google.com/p/selenium/wiki/ChromeDriver)
do the same thing for PhantomJS, but add the bin directory to the path
PhantomJS drivers: http://phantomjs.org/download.html 

sst-run -b Chrome #calls the chrome binary

from sst import config
config.browser_test = 'Chrome'

from sst.actions import *

nosetests test*.py
nodetests --with-xunit test*.py
or
nodetests --processes=2 test*.py

but nodetests --with-xunit --processes=2 test*.py  will not work

Todo:
* need to be able to pass in the domain to set as the base_url
* so node will test imports, and since stt.actions import *, it will fail on run_tests() and end_test(). SST should be refactored to be classes and start/end (utility functions)

* see if browser_type can be passed, rather than hardcoded into class tests
* determine if project install should be multi-user local, single-user local, or global
* Look at https://developer.mozilla.org/en-US/docs/Marionette

* need package-level test suites not to be run for each checkin (snapshot commit)
* declaration of dependencies (account snapshot, for instance)
* could piggyback off of portal's unit test syntax for simple (not CI related) manual runs
* message queue to run tests on snapshot commit
* screenshots and checkins of them/visual diffs
