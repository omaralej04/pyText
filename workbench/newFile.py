# -*- coding: utf-8 -*-
from appJar import gui


def guiNew():
    newWin = gui("New File")

    newWin.setGeom("800x600")
    newWin.setResizable(True)

    newWin.addLabel("Default", "Title")

    newWin.setBg("white")
    newWin.setFont("15")

    def exit(name):
        newWin.stop()

    newWin.addButton("Exit", exit)

    newWin.go()
