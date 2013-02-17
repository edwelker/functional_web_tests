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

Todo:
* try using nose to run class based (and procedural) tests, look at multiprocessing
* see if browser_type can be passed, rather than hardcoded into class tests
* determine if project install should be multi-user local, single-user local, or global
* Look at https://developer.mozilla.org/en-US/docs/Marionette
