# -*- coding: utf-8 -*-
# Importing Base file for GUI
import baseGUI


def main():
    baseGUI.guiStart()  # Starting the GUI (Menu)
    pass

if __name__ == "__main__":
    # Calling the GUI with console logs for Debug
    print "Starting GUI..."
    main()
    print "Killed."  # When main stops being active!
