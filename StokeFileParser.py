import string


filename = '/users/swiftb/StokerMonitor/20130528Ribs/Stoker20130527151638'

f = open(filename, 'r')

filestring = f.read()

bge = filestring.find('BGE')

bgevaluestart = filestring.find('<td>', bge)+4
bgevalueend = filestring.find('</td>', bgevaluestart)

print bgevaluestart, bgevalueend
print filestring[bgevaluestart:bgevalueend]
