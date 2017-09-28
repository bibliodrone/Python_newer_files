import requests, bs4, time, csv

# soup.find_all({"ix:nonfraction"}) 

urls = []
holdings = []

qStrings = ["http://webservices.lib.harvard.edu/rest/classic/search/marc/wip=adam%20matthew%20digital",
"http://webservices.lib.harvard.edu/rest/classic/results/marc/608134/86/26/50?wip=adam%20matthew%20digital",
"http://webservices.lib.harvard.edu/rest/classic/results/marc/608134/86/51/75?wip=adam%20matthew%20digital",
 "http://webservices.lib.harvard.edu/rest/classic/results/marc/608134/86/75/86?wip=adam%20matthew%20digital"]

qTest = "http://webservices.lib.harvard.edu/rest/classic/search/dc/wip=adam%20matthew%20digital"

csv_f = open('AdamMatt_results-dc-test.csv', 'w', newline = '')
f = csv.writer(csv_f)

f.writerow(['ID', 'Title', 'Creation Date', 'Holdings Record'])

query = qTest
 
response = requests.get(query)
response.raise_for_status()

soup = bs4.BeautifulSoup(response.text, "xml")

elements = soup.select('item')

for e in elements:
    
    _recid = str(e.identifier.getText())
    _title = str(e.title.getText())
    _crDate = str(e.date.getText())
    _url = str(e.identifier.url.getText())
    _holdings = str(e.holdingslink.getText())

    f.writerow([_recid, _title, _holdings, _url, _crDate])


"""

for r in range(0, 4):
    query = qStrings[r]
 
    response = requests.get(query)
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, "lxml")

    elements = soup.select('item')

    for e in elements:
        
        _recid = str(e.{dc:identifier}.getText())
        _title = str(e.{dc:title}.getText())
        _crDate = str(e.{dc:date}.getText())
        _url = str(e.{dc:identifier}.url.getText())
        _holdings = str(e.holdingslink.getText())

        f.writerow([_recid, _title, _holdings, _url, _crDate])
"""
csv_f.close()
