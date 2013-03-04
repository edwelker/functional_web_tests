from sst.actions import *
from nose.tools import with_setup

def setup():
    browser_type = 'PhantomJS'

@with_setup(setup)
def test_redirect():
    browser_type = 'PhantomJS'
    go_to('http://www.ncbi.nlm.nih.gov/m/pubmed')
    assert_url('http://www.ncbi.nlm.nih.gov/m/pubmed/')
