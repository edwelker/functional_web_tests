from sst.actions import * 

go_to('http://www.pubmed.gov')
assert_title_contains('PubMed')
