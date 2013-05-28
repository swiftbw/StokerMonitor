import string



class StokeFileParser():
    filestring = None
    def __init__(self, filename):
        f = open(filename, 'r')

        self.filestring = f.read()

    def getValueForKey(self, key):
        keystr = self.filestring.find(key)
        keyvaluestart = self.filestring.find('<td>', keystr)+4
        keyvalueend = self.filestring.find('</td>', keyvaluestart)

        return(self.filestring[keyvaluestart:keyvalueend])


def main():
    filename = '/users/swiftb/StokerMonitor/20130528Ribs/Stoker20130527151638'

    sfp = StokeFileParser(filename)
    print 'BGE' + ' ' + sfp.getValueForKey('BGE')
    print 'MEAT2' + ' ' + sfp.getValueForKey('MEAT2')

if __name__ == '__main__':
    main()

    
