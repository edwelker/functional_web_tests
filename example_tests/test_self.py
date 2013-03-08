from sst.actions import *
from sst import runtests
from selenium.webdriver.common.action_chains import ActionChains

class Test_hover_actions(runtests.SSTTestCase):
    """
    Test hover actions, using the internal low-level webdriver component
    """
    browser_type = 'PhantomJS'

    def test_page_elements(self):
        go_to('http://www.ncbi.nlm.nih.gov/m/pubmed')
        assert_title('PubMed Mobile')
        ele = self.browser.find_element_by_id('srch')

        h = ActionChains(self.browser).move_to_element( ele )
        h.perform()
