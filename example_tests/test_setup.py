from sst.actions import *
from sst import runtests

class PMMobile_HomePage(runtests.SSTTestCase):
    """
    Test the PubMed Mobile homepage
    """
    def test_redirect(self):
        go_to('http://www.ncbi.nlm.nih.gov/m/pubmed')
        assert_url('http://www.ncbi.nlm.nih.gov/m/pubmed/')

    def setUp(self):
        super(PMMobile_HomePage, self).setUp()
        print "setting up myself"
        print dir(self)
        print
        #import pdb; pdb.set_trace()
        print self.__class__.__mro__

        import inspect 
        #print inspect.getmembers(self)
