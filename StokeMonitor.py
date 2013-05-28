#!/usr/bin/python

from Tkinter import *
from tkFileDialog import askopenfilename, askopenfilenames
from StokerHTMLParser import StokerHTMLParser

root = Tk()

filename = askopenfilenames()

print 'Filename is: ' + filename[0]

sp = StokerHTMLParser()

sp.setFileName(filename[0])

sp.loadHTML()

sp.htmlprint()

w = Label(root, text="Hello, World!")

w.pack()

root.mainloop()

