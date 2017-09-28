# Searches for datasets matching a query string, returns a list of results with some information.
# Harvard Dataverse documentation #http://guides.dataverse.org/en/4.7.1/api/search.html

import requests
import json
import pprint
import time

query = input("Enter a search term ---> ")


url = 'https://www.datarefuge.org/api/3/action/package_search?q=' + query
url2 = 'https://dataverse.harvard.edu/api/search?q=trees' #Harvard's Dataverse query; tested in Firefox. Returns JSON.
url3 = 'https://dataverse.harvard.edu/api/search?q=trees&show_relevance=true&show_facets=true&fq=publicationDate:2016' #More Advanced; 
url4 = 'https://dataverse.harvard.edu/api/search?q=services&type=dataverse&fq=hhs' #hhs is the 'identifier'
url5 = 'https://dataverse.harvard.edu/api/search?q=justice&type=dataverse&fq=spelling_alternatives' #interesting; returns mangled spelling variations
#also can use &subtree='xxx'

#1)package_search
#2)tag_search (returns different document structure: results; numbered; each has 'vocabulary_id', 'id', 'name' keys)

search_log = str("q_" + query + ".txt")

# Request a package search by query string.
response = requests.get(url)
response.raise_for_status

manifest = json.loads(response.text)
res = " results "

#pprint.pprint(response)
ml = manifest['result']['results']
if len(ml) == 0:
    print("Search results are null")
    exit
if len(ml) == 1:
    res = " result "

print(str(len(ml)) + res +  "for << "+ query + " >>")

with open(search_log, 'w', encoding = 'utf-8') as outfile:
    outfile.write(url+"\n\n")
    
    for i in range(0, len(ml)):
        try:
            title = ml[i]['title']
            typ = ml[i]['type']
            notes = ml[i]['notes']
            tags = ml [i]['tags']
            outfile.write("\n")
            outfile.write("-" + str(i+1) + "-\n\n" + "Title: " + title +  " (" + typ + ")\n")
            outfile.write("\n")
            notes_section = "{0:<40}".format(notes)
            outfile.write("Notes:\n\n")
            outfile.write("    "+ notes_section + "\n\n")
            outfile.write("-------------------------------\n")
            outfile.write("Tags:\n")
            for k in tags[0].items():
                k0 = str(k[0])
                k1 = str(k[1])
                tgs = " {0:<15}: {1:<15}\n".format(k0, k1)
                #tgs = " " + str(k[0]) + ": " + str(k[1])+"\n"
                outfile.write(tgs)
            outfile.write("-------------------------------\n\n")  
        except:
            print("Error reading data...")
            continue
    outfile.write("{0:^25}".format("--- End of Results ---"))

print("Results file: " + search_log)
"""

with open(search_log, 'w', encoding = 'utf-8') as outfile:
    outfile.write('Search Results\n\n')
    for i in ml:
        i = pprint.pformat(i)
        outfile.write(i)
"""
