import requests

target = 'http://xpo6.com/wp-content/uploads/2015/01/stop-word-list.txt'

with open ('stop-word-list.txt', 'w') as sw:
    response = requests.get(target)
    response.raise_for_status()

    stoplist = response.text

    for line in stoplist:
        sw.write(line)
        
    
