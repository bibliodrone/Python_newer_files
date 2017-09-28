
# coding: utf-8

# In[124]:

import requests
import urllib
from lxml.etree import parse

encoding='utf-8'


# In[125]:

#Base url

# request holdings and item availability for items associated with a bibliographic ID
#  url='http://webservices.lib.harvard.edu/rest/v2/classic/holdings/{Hollis ID number}

# request bib info by barcode
#  http://webservices.lib.harvard.edu/rest/classic/barcode/{record_format}/{barcode}

# request hollisplus search
#  url='http://webservices.lib.harvard.edu/rest/v2/hollisplus/search/dc/?q=000922752'

# request hollisclassis search
#  http://webservices.lib.harvard.edu/rest/classic/search/{record_format}/{command}

# request bibliographic information by record id (cite, dc, mods, marc format) 
#  url='http://webservices.lib.harvard.edu/rest/mods/hollis/000922752'

url='http://webservices.lib.harvard.edu/rest/classic/search/marc/ibn=0399125930'


# In[126]:

u = urlopen(url)
#resp = requests.get(url)
#text=resp.text


# In[127]:

doc=parse(url)


# In[135]:

ocn=doc.findtext('//datafield[@tag=035]/subfield[@code]')
print(ocn)


# In[129]:

#parsed=parse(text)


# In[130]:

#print (text)


# In[131]:

#print resp


# In[7]:

print(requests.get(url, data=querystring))


# In[ ]:



