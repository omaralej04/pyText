# -*- coding: utf-8 -*-
from appJar import gui
import defs

newClass = defs.Definitions()

def guiLoad():
    loadWin = gui("DefaultTitle")

    loadWin.setGeom("20x20")
    loadWin.setResizable(True)

    loadWin.addScrolledTextArea("Text")

    loadWin.setBg("white")
    loadWin.setFont("15")

    def exit(name):
        loadWin.stop()

    loadWin.addButton("Exit", exit)

    print "Loaded GUI started"
    print "Returned to ext %r" % newClass.pathFile()
    loadWin.go()
