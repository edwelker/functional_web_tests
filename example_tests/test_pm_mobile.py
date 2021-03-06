from sst.actions import *
from sst import runtests


class PMMobile_HomePage(runtests.SSTTestCase):
    """
    Test the PubMed Mobile homepage
    """

    browser_type = 'PhantomJS'

    def test_redirect(self):
        go_to('http://www.ncbi.nlm.nih.gov/m/pubmed')
        assert_url('http://www.ncbi.nlm.nih.gov/m/pubmed/')

    def test_cookies(self):
        set_base_url('http://www.ncbi.nlm.nih.gov/m/')
        go_to('pubmed')
        cookie = (item for item in get_cookies() if item['name'] == "ncbi_mmode").next()
        print cookie
        if cookie:
            assert(cookie['value'] == 'mob')

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
    """
    Test the PubMed Mobile search results page
    """
    browser_type = 'PhantomJS'

    def test_page_elements(self):
        go_to('http://www.ncbi.nlm.nih.gov/m/pubmed?term=Red+Sox')
        assert_textfield('srch')
        assert_attribute('srch', 'value', 'Red Sox')
        results = get_elements_by_xpath("//ul[@class='r']/li/a")

        assert(len(results) == 10)

        for result in results:
            assert_css_property(result, 'font-size', '14px')

        #fails function takes function as first argument
        fails(assert_equal, 1, 2)

        fails(assert_element, css_class='class_doesnt_exist', name='whatever')

        base_url = get_base_url()
        assert_equal(base_url, 'http://www.ncbi.nlm.nih.gov/m/')
        fails(assert_equal, base_url, 'http://www.ncbi.nlm.nih.gov/')


class PMMobile_AbstractPage(runtests.SSTTestCase):
    """
    Test the PubMed Mobile Abstract Page
    """

    browser_type = 'PhantomJS'

    def test_page_elements(self):
        go_to('http://www.ncbi.nlm.nih.gov/m/pubmed/17328369')
        assert_url_contains('m/pubmed/17328369/')
        assert_title_contains('When the Red Sox shocked the Yankees:')

        assert_css_property(get_element_by_css('h2'), 'font-size', '16px')

        go_to('http://pubmed.gov')
        go_back()
        assert_url('http://www.ncbi.nlm.nih.gov/m/pubmed/17328369')


class PMMobile_test_is_header_at_top(runtests.SSTTestCase):
    """
    Test to see if you can determine if something is at the top of the page
    a task that apparently QA doesn't know how to do
    """

    browser_type = 'PhantomJS'

    def test_top_of_page(self):
        go_to('http://www.ncbi.nlm.nih.gov/m/pubmed/23096108/?i=982&from=cat#c')
        assert(get_element(id='c').location['x'] < 20)


class PM_JS_test(runtests.SSTTestCase):
    """
    Test the PubMed page using JavaScript
    """

    browser_type = 'PhantomJS'

    def test_execute_script(self):
        """
        test the execute_script function from SST
        (wrapper around selenium java bindings)
        """
        go_to('http://www.ncbi.nlm.nih.gov/pubmed/')
        execute_script('document.title = "JavaScript Rocks"')
        assert_title('JavaScript Rocks')

        refresh()
        assert_title('Home - PubMed - NCBI')


#you can write class-based tests when the file
#starts with test_* but you can't mix and match
def test():
    assert False
