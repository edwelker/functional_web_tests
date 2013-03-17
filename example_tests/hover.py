from sst.actions import *
from selenium.webdriver.common.action_chains import ActionChains

browser = start()[0]  #start returns a tuple... browser is first item, what is the second?
go_to('http://www.ncbi.nlm.nih.gov/pubmed?term=cat')
x = get_elements_by_css(.brieflinkpopperctrl)[0] #get the first one

hover = ActionChains(browser).move_to_element(x)
hover.perform()
