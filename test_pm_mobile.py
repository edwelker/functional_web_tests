from sst.actions import *
from sst import runtests

class PMMobile_HomePage(runtests.SSTTestCase):
    "Test the PubMed Mobile homepage"
    browser_type = 'PhantomJS'

    def test_redirect(self):
        go_to('http://www.ncbi.nlm.nih.gov/m/pubmed')
        assert_url('http://www.ncbi.nlm.nih.gov/m/pubmed/')

    def test_page_elements(self):
        go_to('http://www.ncbi.nlm.nih.gov/m/pubmed')
        assert_title('PubMed Mobile')
        exists_element(id='srch')
        assert_element(id='srch')
        assert_button('but')

    def test_homepage_search(self):
        go_to('http://www.ncbi.nlm.nih.gov/m/pubmed')
        write_textfield('srch', 'Red Sox')
        click_button('but')
        #moved to new search page
        assert_url_contains('?term=Red+Sox')
        assert_title_contains('Red Sox')

class PMMobile_SearchResults(runtests.SSTTestCase):
    "Test the PubMed Mobile search results page"
    browser_type = 'PhantomJS'

    def test_page_elements(self):
        go_to('http://www.ncbi.nlm.nih.gov/m/pubmed?term=Red+Sox')
        assert_textfield('srch')
        assert_attribute('srch', 'value', 'Red Sox')
        results = get_elements_by_xpath("//ul[@class='r']/li/a")
        
        assert( len(results), 10)

class PMMobile_AbstractPage(runtests.SSTTestCase):
    "Test the PubMed Mobile Abstract Page"
    browser_type = 'PhantomJS'

    def test_page_elements(self):
        go_to('http://www.ncbi.nlm.nih.gov/m/pubmed/17328369')
        assert_url_contains('m/pubmed/17328369/')
        assert_title_contains('When the Red Sox shocked the Yankees: c - PubMed Mobile')

        assert_css_property( get_element_by_css('h2'), 'font-size', '16px')

def test():
    assert False
