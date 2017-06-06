from urllib.request import urlopen
import json

#apiUrl = "http://www.nhtsa.gov/webapi/api/SafetyRatings"
result = urlopen("http://webservices.lib.harvard.edu/rest/v2/classic/holdings/014472259/brief?jsonp=result").read().decode('utf8') #{record_format}/{source}/{id}

#apiParam = "/modelyear/1995"
#param = "014472259/brief"

#outputFormat = "?format=json"
#outputForm = "?jsonp = result"

#Combine all three variables to make up the complete request URL


#code below is only to handle JSON response object/format
#use equivalent sets of commands to handle xml response object/format

json_obj = json.loads(result)

print (json_obj)

#Load the Result (vehicle collection) from the JSON response
#print('------------------------------')
#print('           Result             ')
#print('------------------------------')
for objectCollection in json_obj['result']:
    # Loop each vehicle in the results collection
    for line in objectCollection.iteritems():
        print (line)
    #for safetyRatingAttribute, safetyRatingValue in objectCollection.iteritems():
    #    print safetyRatingAttribute, ": ", safetyRatingValue
        
