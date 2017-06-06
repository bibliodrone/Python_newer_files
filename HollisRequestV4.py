import urllib.request as urllib

with urllib.urlopen("http://webservices.lib.harvard.edu/rest/classic/search/dc/psc=net%20safar")as response:
    html = response.read().decode("utf-8")
    
with open("outHvd.txt", "w") as outh:
    for line in html:
        outh.write(line)
        
        
