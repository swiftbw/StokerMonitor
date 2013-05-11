import httplib
import StokerHTMLParser
from datetime import datetime
import time


conn = httplib.HTTPConnection("192.168.1.50")

while 1:
    conn.request("GET", "/index.html")
    r1 = conn.getresponse()

    data = r1.read()
    print r1.status, r1.reason
    print data

    now = datetime.now()
    
    stokerOutFile = "Stoker" + now.strftime('%Y%m%d%H%M%S')
    
    f = open(stokerOutFile, 'w')

    f.write(data)

    f.close()
    
        #par = StokerHTMLParser.StokerHTMLParser()
    time.sleep(60)
    

par.feed(data)

