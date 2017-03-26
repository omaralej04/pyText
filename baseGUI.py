# -*- coding: utf-8 -*-
from appJar import gui
from base.baseFile import LoadNew
from defs import pyQuote

killMain = 'mainWin.stop()'
loadNewC = LoadNew()  # Assign var for LoadNew class
mainWin = None


# function to close win.go()
def closeWin():
    print "Closing window"
    exec killMain
    print "Closed."


# Basic Load/New GUI
def guiStart():

    global mainWin
    # Name of GUI
    mainWin = gui("pyTextMenu")

    # Setting Background color
    mainWin.setBgImage("img/Geometry_Bg.jpg")

    # Default size
    mainWin.setGeom("400x300")
    mainWin.setResizable(False)

    # Default Title
    mainWin.addLabel("Title", "pyTextMenu!")
    mainWin.addLabel("Subtitle", pyQuote)

    # Default Font size
    mainWin.setFont("14")

    # Value of btn exit
    def exit(name):
        mainWin.stop()
        print "User pressed exit!"

    # Basic structure for baseFile.py
    def loadNew(name):
        if name == "Load":
            print "LOADED"
            closeWin()
            loadNewC.loadFile()  # Open file name dialog
        elif name == "New":
            print "NEW"
            closeWin()
            loadNewC.newFile()
        else:
            print "Fatal error Loading/Saving"

    # Adding the buttons to the GUI
    mainWin.addButtons(["Load", "New"], loadNew)
    mainWin.addButton("Exit", exit)

    # Starting the GUI
    print "GUI started."  # Debugging
    mainWin.go()
