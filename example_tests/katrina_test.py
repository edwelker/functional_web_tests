from sst.actions import *
from urlparse import urlparse, urljoin

go_to('http://qa.ncbi.nlm.nih.gov/pmc')
write_textfield('term', 'cat')
click_button('search')
record = get_element_by_xpath("//div[@class='rprt'][1]//div[@class='title']//a[@class='view']")
click_link(record)
assert_url('http://qa.ncbi.nlm.nih.gov/pmc/articles/PMC2848379/')
click_link( get_elements_by_css("a.jig-ncbiinpagenav-goto-heading")[0] )
popup = assert_displayed( get_element_by_css('.ui-ncbilinksmenu') )
link_to_click = popup.find_element_by_link_text('Footnotes')
click_link( link_to_click )

footnote_header = (x for x in get_elements(tag='h2') if x.text=='Footnotes').next()
print footnote_header.location
print get_current_url()

new_footnote_header = (x for x in get_elements(tag='h2') if x.text=='Footnotes').next()

print new_footnote_header.location
print get_current_url()
