import httplib
from datetime import datetime
import time


class httpgetter:
    
    def __init__(self, ipaddress, urlpage):
        self.ipaddress = ipaddress
        self.urlpage = urlpage
        self.conn = httplib.HTTPConnection(self.ipaddress)

    def getResponse(self):
        self.conn.request("GET", self.urlpage)
        response = self.conn.getresponse()

        return (response)
    
def main():
    stokehttp = httpgetter('192.168.1.50', '/index.html')

    while 1:
        resp = stokehttp.getResponse()
        
        data = resp.read()

        now = datetime.now()
    
        stokerOutFile = "Stoker" + now.strftime('%Y%m%d%H%M%S') + '.skr'
    
        f = open(stokerOutFile, 'w')

        f.write(data)

        f.close()
    
        time.sleep(60)
    
if __name__ == '__main__':
    main()
