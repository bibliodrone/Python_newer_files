
# CCL Search for 'Adam Matthew Digital' titles

import requests, bs4

# 86 records will return 4 separate pages of XML; 
# qString = http://webservices.lib.harvard.edu/rest/classic/search/mods/wip=adam%20matthew%20digital"

qStrings = ["http://webservices.lib.harvard.edu/rest/classic/search/mods/wip=adam%20matthew%20digital",
"http://webservices.lib.harvard.edu/rest/classic/results/mods/421719/86/26/50?wip=adam%20matthew%20digital",
"http://webservices.lib.harvard.edu/rest/classic/results/mods/421719/86/51/75?wip=adam%20matthew%20digital",
 "http://webservices.lib.harvard.edu/rest/classic/results/mods/421719/86/26/50?wip=adam%20matthew%20digital"]
 

#Made loop to get results 1-86 and append (skipping qStrings 0)

for q in range (0, 4):
    filename = "AmatthewQuery"+str(q)+".txt"

    with open (filename, "w", encoding = "utf-8") as am:
    
        response = requests.get(qStrings[q])
        response.raise_for_status()

        result = bs4.BeautifulSoup(response.text, "lxml")
        full = result.select("*")

        am.write(response.text)
        print("Wrote file ", filename)
        print()


        


