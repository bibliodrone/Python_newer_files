# Actually uses Classic much more easily. Gets record info from ISBN query.
# extracts holdings record link and queries that record as well, returning status
# Holdings: /rest/v2/classic/holdings/....
# hplus = "http://webservices.lib.harvard.edu/rest/v2/hollisplus/search/dc/?query=isbn,contains,9783944258034&limit=20&facets=creator"

import requests, bs4, time

def getISBNs():
    ibnlist = []
    with open ('safariNotAvail.txt', 'r') as s:
        for line in s:
            ibnlist.append(line[1:len(line)-2])
    return(ibnlist)

#Runs from within runQueries
def getResponse(urlsubmit):
    response = requests.get(urlsubmit)
    response.raise_for_status()

    record = bs4.BeautifulSoup(response.text, "lxml")

    title= record.title.getText()
    tag = record.select("physicallocation")
    id = record.item.attrs['id']
    identifier = record.select("identifier")
    hlk = record.select('holdingslink')
    holdings = hlk[0].getText()

    responseDataString = str(id + " ; " + title + " ; " + tag[0].getText())
    return responseDataString


def runQueries(ibnlist):
    hclassic = "http://webservices.lib.harvard.edu/rest/classic/search/cite/ibn="
    responses = []
    for item in ibnlist:
        try:
            qisbn = item
            print("Searching", str(qisbn))
            urlsubmit = hclassic + qisbn
            responses.append(getResponse(urlsubmit)) #sub-routine         
        except:
            responses.append("!" + qisbn)
            print("  " + qisbn + " not found")

        time.sleep(1)

    return(responses)

    
def main():
    print("Retrieving ISBN's")

    ibnlist = getISBNs()
    responses = runQueries(ibnlist)

    with open('HOLLIS_output.txt', 'w') as out:
        for item in responses:
            print(item)
            out.write(item + "\n")
"""

    print("Title:", title)
    print("Location:", tag[0].getText(), end="  Record#: ")
    print(id)
    print()
    print("Identifiers: ")
    for i in identifier:
        print(i['type']+ ": " + i.getText())

    print()

    holdURL=baseURL + holdings
    holdLinks.append holdURL
    
#---- Messy, should make a function
urlsubmit2 = holdURL

#print(holdURL)

response2 = requests.get(urlsubmit2)
response2.raise_for_status()

record2 = bs4.BeautifulSoup(response2.text, "lxml")

status = record2.select('stat')
checkedout = status[0].getText()

print("Item Status: ", checkedout)

"""
main()

