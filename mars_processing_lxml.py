'''
This is a revised version of the MARS processing script that uses lxml only. It appears (from limited testing) to be free from the truncation bug that occurred in some cases with the original BeautifulSoup script. This version does not process the R07 NAMES report, and only processes the 650 portion of the R07 SUBJECTS report.

mars_processing_lxml.py

Script for converting selected MARS report HTML pages to CSV files.
Created May 2014 for Harvard Library ITS MARS Reports Pilot Project

GW -- used >> Py 2to3.py -w C:\Users\walden\Desktop\PyNew\mars_processing_lxml.py
'''
import codecs
import csv
import datetime
import requests
from lxml import html
from tkinter import *
 
'''
GUI DISPLAY FOR USER INPUT
This section creates a GUI to prompt the user to select a report name and date.
It really should be rewritten as a class.
'''
root = Tk()
 
widgets = []
 
reportnames = [
    ('R04 Authority Delete Report','R04_Authority_Delete_Report_AUTHS'),
    ('R06 LC Subjects','R06_Partially_Matched_Headings_LC_Subjects'),
    #('R07 Unmatched Names','R07_Unmatched_NAMES'), #This report has been removed from pilot project
    ('R07 Unmatched Subjects','R07_Unmatched_SUBJECTS'),
    ('R13 Suspicious Filing Indicators','R13_Suspicious_Filing_Indicators'),
    ('R14 Possible Leading Articles','R14_Possible_Leading_Articles'),
    ('R25 Unrecognized $z Subfields','R25_Unrecognized_$z_Subfields')
    ]
 
# Sets previous month as default month/year menu selections
'''
Commands should be added here or where requests gets the HTML below to handle invalid dates.
If 'Mar 2014' is selected in 'Feb 2014', this code currently creates an empty CSV file with no warning
'''
current_year = datetime.date.today().strftime("%Y")
previous_year = int(current_year) - 1
years = (current_year, previous_year)
previous_month = int(datetime.date.today().strftime("%m")) - 1
if previous_month < 1: # In Jan., sets default date as Dec. of previous year
    previous_month = 12
    current_year = previous_year
previous_month = str(previous_month)
# months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
menu_months = []
months = [('1', 'jan'),('2','feb'),('3','mar'),
        ('4','apr'),('5','may'),('6','jun'),
        ('7','jul'),('8','aug'),('9','sep'),
        ('10','oct'),('11','nov'),('12','dec')]
 
for (key, value) in months:
    menu_months.append(value)
    if previous_month in key:
        default_month = value
 
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
 
widget1 = OptionMenu(root, var1, *years)
widget1['menu'].config(relief = FLAT)
widget1.pack(fill=X) 
 
widget2 = OptionMenu(root, var2, *menu_months).pack(fill=X)
 
for (key, value) in reportnames:
    widget3 = Radiobutton(root, text=key,
                       indicatoron = 0,
                       offrelief = FLAT,
                       overrelief = FLAT,
                       bg = '#80cdc1',
                       selectcolor = '#f6e8c3',
                       pady = 10,
                       variable = var3,
                       value=value,
                       ).pack(anchor=NW,fill=X)
 
var1.set(current_year)
var2.set(default_month)
var3.set('R04_Authority_Delete_Report_AUTHS')
 
def state():
    widgets.append(var1.get())
    widgets.append(var2.get())
    widgets.append(var3.get())
    root.destroy()
 
Button(root, command=state, text='Create Report').pack(fill=X)
 
root.title('MARS Reports')
 
#Code--next 7 lines--for positioning window correctly from https://bbs.archlinux.org/viewtopic.php?id=149559
root.withdraw()
root.update_idletasks()
 
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry('300x375+%d+%d' % (x, y))
root.deiconify()
 
root.mainloop()
 
'''
GET REPORT URLS FROM MARS INDEX PAGE
This section identifies the matching report pages from the report index page for the selected month and saves the HTML for BS processing.
'''
print ('mars_reports.py is running ...')
 
report = widgets[2]
url = 'http://lms01.harvard.edu/mars-reports/' + widgets[1] + '-' + widgets[0][-2:] + '-data/'
r = requests.get(url)
doc = html.fromstring(r.text)
 
links = doc.xpath('//a/@href')
 
output_data = []
pages = []
 
for link in links:
    if link.startswith(report):
        if link.endswith('.htm'):
            link = url + link
            r = requests.get(link)
            doc = html.fromstring(r.text)
            pages.append(doc)
'''
EXTRACT REPORT DATA
This section extracts data for a CSV file based on the type of report selected.
'''
if report == 'R04_Authority_Delete_Report_AUTHS': #Report structure for R04 is not like the other reports so this report is handled separately
    for page in pages:
 
        trs = page.xpath('//table/tr[@class="rec-compare-row"]')
        for tr in trs:
            line_data = []
            undiffs = []
            tds = tr.xpath('./td[@class]')
            for td in tds:
                chgfield = td.xpath('./div[@class="chgfield"]//text()') #Get changed field
                fields = td.xpath('./div[@class="field"]')
                if chgfield:
                    for field in fields:
                        if '001' in field.xpath('.//text()')[0]: #Get LCCN from 001
                            lccn = field.xpath('.//text()')[2]
                        if '008' in field.xpath('.//text()')[0]: #Get 008 byte 32 to filter undifferentiated names
                            undiff = field.xpath('.//text()')[2]
                            undiff = undiff[32]
                            undiffs.append(undiff)
                    tag = chgfield[0] #Get field tag
                    ind = chgfield[1] #Get indidcators
                    fielddata = chgfield[2:] #Get the rest of the field
                    fielddata = ' '.join(fielddata)
                else: #Create blank values if there is not a replacement record
                    lccn = ''
                    undiff = ''
                    undiffs.append(undiff)
                    tag = ''
                    ind = ''
                    fielddata = 'No replacement found' #and mark the record as such
                line_data.append(lccn)
                line_data.append(tag)
                line_data.append(ind)
                line_data.append(fielddata)
            if undiffs[0] != 'b': #Only add report data to CSV output if not for an undifferentiated name
                output_data.append(line_data)
 
else: #All reports except R04
    for page in pages:
 
        if report == 'R06_Partially_Matched_Headings_LC_Subjects':
            trs = page.xpath('//table[@id]/tr') #Must distinguish between tables for R06 only
        else:
            trs = page.xpath('//table/tr')
 
        for tr in trs:
            line_data = []
        
            try:
                bib = tr.xpath('./td[@class="ctl_no"]/text()')[0]
            except IndexError: #Set bib as blank if value is missing
                bib = ''
       
            tag = tr.xpath('./td[@class="tag"]/text()')[0]
            ind = tr.xpath('./td[@class="ind"]/text()')[0]
 
            fielddata = tr.xpath('./td[@class="fielddata"]//text()') #Get the entire field
            fielddata = ' '.join(fielddata)
             
            if report == 'R06_Partially_Matched_Headings_LC_Subjects':
                validity = []
                invalid = tr.xpath('./td[@class="fielddata"]//span[@class="invalid" or @class="partly_valid"]//text()') #Get valid/partly_valid (red/brown) subfields for R06
                invalid = ' '.join(invalid)
                if invalid:
                    for class_attr in tr.xpath('./td[@class="fielddata"]//span/@class'): #Get the invalid/partly_valid class designator
                        if class_attr != "submark" and class_attr != "valid":
                            validity.append(class_attr)
                    validity = ', '.join(validity)
                    line_data = [bib, tag, ind, fielddata, invalid, validity] #Append only lines with invalid/partly_valid subfields
            
            elif report == 'R07_Unmatched_SUBJECTS':
                if tag == '650':
 #Only include 650s for R07 report
                    line_data = [bib, tag, ind, fielddata]
            elif report == 'R25_Unrecognized_$z_Subfields':
                invalid = tr.xpath('./td[@class="fielddata"]//b//text()') #Get the bold (invalid) subfields for R25
                invalid = ' '.join(invalid)
                if invalid:
                    line_data = [bib, tag, ind, fielddata, invalid] #Append only lines with invalid subfields
            else:
 #For other reports create a 4-item list
                line_data = [bib, tag, ind, fielddata]
            if line_data:
                output_data.append(line_data)
'''
SET HEADERS
This section sets the headers for the CSV file.
'''
if report == 'R04_Authority_Delete_Report_AUTHS':
   header = ['LCCN (D)','Tag (D)','Inds (D)','Heading (Deleted)','LCCN (N)','Tag (N)','Inds (N)','Heading (New)']
elif report == 'R06_Partially_Matched_Headings_LC_Subjects':
   header = ['Bib No', 'Tag','Ind', 'Field Data', 'Unmatched Subfield','Unmatched Type']
elif report == 'R07_Unmatched_NAMES':
   header = ['Bib No','Tag','Ind','Field Data','Add. Tag','Add. Ind','Add. Field Data']
elif report == 'R25_Unrecognized_$z_Subfields':
   header = ['Bib No', 'Tag','Ind', 'Field Data', 'Unrecognized $z']
else:
   header = ['Bib No', 'Tag','Ind', 'Field Data']
'''
WRITE TO CSV
This section writes the data to a CSV file.
 
Warning: If the CSV file is opened directly in Excel, leading zeros will be stripped.
This affects the Bib No, Tag, and Ind columns in particular.
There is probably an easy solution to this, but I have not found it.
My temporary solution has been to:
1. Open Excel
2. Open the CSV file in Excel using the Text Import Wizard
   Step 1: Delimited (Original Data Type). Leave File Origin as is.
   Step 2: Comma (Delimiters); uncheck Tab, if checked
   Step 3: Text (Column Data Format) for all columns
   Step 4: Finish 
'''
f = report + '_' + widgets[0] + '_' + widgets[1] + '.csv'
with open(f,'wb') as output:
   output.write(codecs.BOM_UTF8)
   writer = csv.writer(output,quoting=csv.QUOTE_ALL,quotechar='"')
   writer.writerow(header)
   for data in output_data:
       writer.writerow([i.encode('utf-8') for i in data])
 
 
print((f + ' has been created'))


#Christine Fernsebner Eslao
#I've scripted some quick, sloppy python to append to the end of Vernica's elegant MARS processing script, to grab bib data via the Presto API (instead of Cognos) and re-write the CSV to include language code:

def grabPresto():

    from xml.dom.minidom import parseString
    import time
    enhanced_output_data = [] # Data that will be written to the CSV file is saved in this list
      
    for data in output_data:
        mods_url = 'http://webservices.lib.harvard.edu/rest/mods/hollis/' + data[0] #construct url for presto api
        presto = requests.get(mods_url)
        if presto.status_code == 200:
            try:
                mods_xml = parseString(presto.text.encode('ascii', 'ignore'))
                language = mods_xml.getElementsByTagName('languageTerm')[0].firstChild.data
                data.append(language)
                #print language
            except AttributeError:
                data.append('error: missing language code')
                #print 'error: missing language code'
            else:
                data.append('error: ' + str(presto.status_code))
                #print 'error: ' + str(presto.status_code)
                enhanced_output_data += [data]
                time.sleep(1)
  
    header.append('Language Code')
    with open(f,'wb') as output:
        output.write(codecs.BOM_UTF8)
        writer = csv.writer(output,quoting=csv.QUOTE_ALL,quotechar='"')
        writer.writerow(header)
        for data in enhanced_output_data:
            writer.writerow([i.encode('utf-8') for i in data])
