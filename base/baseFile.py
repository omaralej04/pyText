# -*- coding: utf-8 -*-
import Tkinter
import tkFileDialog
import os
import ctypes
from workbench.extFile import guiLoad
from workbench.newFile import guiNew

in_path = NotImplemented


class LoadNew:
    def __init__(self):
        print "Starting LoadNew Class!"
        pass

    def loadFile(self):
        global in_path
        print "Opening File..."
        Tkinter.Tk().withdraw()  # Close the Tkinter
        in_path = tkFileDialog.askopenfilename()  # Asks for file
        print "File Chosen %r" % in_path
        if in_path == '':
            print "Not a valid file!"
            # Error msg box
            ctypes.windll.user32.MessageBoxW(0, u"The file you chose isn't valid!", u"Attention!", 0)
            os.system('python ./__init__.py')
        else:
            guiLoad()

    def newFile(self):
        print "Creating New File..."
        guiNew()
