
# CCL Search for 'Adam Matthew Digital' titles

import requests, bs4, time, csv, pprint

# 86 records will return 4 separate pages of XML; 
# qString = "http://webservices.lib.harvard.edu/rest/v2/hollisplus/search/dc/?query=lsr04,contains,adam+matthew+digital&limit=100"
# qString = "http://webservices.lib.harvard.edu/rest/mods/hollis/"
# recordList = ['014426426', '011449370', '011818898', '012141641', '012205386', '012655849', '012796511', '013191626', '013192750', '014013731', '014019038', '014066216', '014065928', '014065900', '014065873', '014066180', '014066176', '014151193', '014151192', '014151183', '014151187', '014155020', '014155108', '014155027', '014155021', '014426397', '014426378', '014426425', '014426431', '014426435', '014426430', '014426433', '012123517', '014916678', '014989442', '014576894', '014065867', '014426404', '011472885', '011472987', '011472942', '011816065', '012165271', '012205355', '013001288', '013001286', '013192752', '013192369', '014065911', '014065871', '014065868', '014066174', '014066175', '014151191', '014155265', '014154904', '014426424', '014426423', '014151185', '014151182', '014426434', '014151184', '014426429', '014426427', '014426401', '014426422', '014151186', '014151190', '014426428', '014426432', '014151188', '014151189', '012141621', '011999517', '013194284', '010468896', '013158630', '013158634', '013158632', '013158579', '013158606', '013158617', '013158635', '013158593', '013158581', '011410020']

#urls = []
#holdings = []

qStrings = ["http://webservices.lib.harvard.edu/rest/classic/search/marc/wip=adam%20matthew%20digital",
"http://webservices.lib.harvard.edu/rest/classic/results/marc/608134/86/26/50?wip=adam%20matthew%20digital",
"http://webservices.lib.harvard.edu/rest/classic/results/marc/608134/86/51/75?wip=adam%20matthew%20digital",
 "http://webservices.lib.harvard.edu/rest/classic/results/marc/608134/86/75/86?wip=adam%20matthew%20digital"]

# soup.item.attrs...
# Made loop to get results 1-86 and append (skipping qStrings 0)
# x.name to get the html tag name as string; str(x.getText()) to get the value as string
# recid = e.item['id'].getText()
# posit = e.item['postion'].getText()

with open ('AdamMatt_results3.txt', 'w', encoding = 'utf-8') as f:
    for r in range(0, 4):
        query = qStrings[r]
     
        response = requests.get(query)
        response.raise_for_status()

        soup = bs4.BeautifulSoup(response.text, "lxml")

        elements = soup.select('*')
        f.write(str(elements))
""""
        for e in elements:
                _recid = str(e.recordidentifier.getText())
            _title = str(e.title.getText())
            _crDate = str(e.recordcreationdate.getText())
            _url = str(e.url.getText())
            _holdings = str(e.holdingslink.getText())
            
            f.writerow([_recid, _title, _holdings, _url, _crDate])
        
        

        #f.write(_title + "-- " +  _url + "-- " + _holdings)
        #f.write("--- " + str(r_count) + " ---\n")           
        #f.write(_recid + ";\n")
        #f.write(_title + ";\n")
        #f.write(_url + ";\n")
        #f.write(_holdings + "\n")
        #f.write("****************")
        #f.write("\n")

     
        for e in elements:
            line = (e.title, "; ", e.url, "; ",e.holdingslink)
            f.write (str(line)+"\n")
        
            f.write(str(e.getText()).replace("\n", " ;", 1))
            f.write('\n***\n***\n')
        
        time.sleep(1)
"""
   

 
