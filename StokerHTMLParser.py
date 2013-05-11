from HTMLParser import HTMLParser

class StokerHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag
    def handle_endtag(self, tag):
        print "Encountered an end tag:", tag
    def handle_data(self, data):
        print "Encountered Data:", data

        
