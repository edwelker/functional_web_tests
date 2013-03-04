from sst import config
config.browser_type = 'Chrome'
from sst.actions import *
go_to('http://www.ncbi.nlm.nih.gov/m/pubmed')
assert_url('http://www.ncbi.nlm.nih.gov/m/pubmed/')
assert_title('PubMed Mobile')
exists_element(id='srch')
assert_element(id='srch')
write_textfield('srch', 'Red Sox')
assert_button('but')
click_button('but')

#moved to new search page
assert_url_contains('?term=Red+Sox')
assert_title_contains('Red Sox')
assert_textfield('srch')
assert_attribute('srch', 'value', 'Red Sox')
results = get_elements_by_xpath("//ul[@class='r']/li/a")
