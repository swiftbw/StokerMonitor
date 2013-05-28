from lxml import etree
from StringIO import StringIO
import HTMLParser

class StokerHTMLParser:
    def __init__(self):
        self._filename = None
        self._parser = etree.HTMLParser()
        self._tree = None
    def setFileName(self, name):
        self._filename = name
    
    def loadHTML(self):
        f = open(self._filename)
        _html = f.read()
        
        self._tree = etree.parse(StringIO(_html), self._parser)

    def htmlprint(self):
        result = etree.tostring(self._tree.getroot(), pretty_print=True, method="html")
        print(result)
        print self._tree
        
