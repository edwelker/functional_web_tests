functional_web_tests
====================

Functional web tests

install sst
download chrome drivers, and add location to path (PATH=$PATH:/path/to/drivers; export PATH)
do the same thing for PhantomJS, but add the bin directory to the path

sst-run -b Chrome #calls the chrome binary

from sst import config
config.browser_test = 'Chrome'

from sst.actions import *

