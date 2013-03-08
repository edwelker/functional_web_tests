from sst.actions import *
from urlparse import urlparse, urljoin

#just go to a url
go_to('http://qa.ncbi.nlm.nih.gov/pmc')

#write something in the text box with id="term"
write_textfield('term', 'cat')

#click the button, by default it'll wait until a <body> element is loaded before resuming
click_button('search')

#get the first record link
record = get_element_by_xpath("//div[@class='rprt'][1]//div[@class='title']//a[@class='view']")

#click that link
click_link(record)

#make sure that we got to the page that we expected
assert_url('http://qa.ncbi.nlm.nih.gov/pmc/articles/PMC2848379/')

#click on the Goto: link
click_link( get_elements_by_css("a.jig-ncbiinpagenav-goto-heading")[0] )

#make sure that the popup is visible on the page
popup = assert_displayed( get_element_by_css('.ui-ncbilinksmenu') )

#get the link called "Footnotes"
link_to_click = popup.find_element_by_link_text('Footnotes')

#click on that link
click_link( link_to_click )

#get all the H2 elements, and then give me the only one with text "Footnotes"
footnote_header = (x for x in get_elements(tag='h2') if x.text=='Footnotes').next()

#print this stuff, because the scroll isn't working
print footnote_header.get_attribute('id')
print footnote_header.location
print get_current_url()

new_url = urljoin( get_current_url(), "#" + footnote_header.get_attribute('id') )
go_to( new_url )
new_footnote_header = (x for x in get_elements(tag='h2') if x.text=='Footnotes').next()

print new_footnote_header.location
print get_current_url()
