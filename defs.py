#  File for top level definitions
from random import randint
import base.baseFile

filePath = None


class Definitions:
    def __init__(self):
        print "Definitions Started!"

    def pathFile(self):
        global filePath
        filePath = base.baseFile.in_path
        print "PathFile.def is %r" % filePath
        return filePath

numQuo = randint(0, 6)

if numQuo == 0:
    pyQuote = "Omg it's pyText!"
elif numQuo == 1:
    pyQuote = "Giving text since 2017!"
elif numQuo == 2:
    pyQuote = "Damn, it's workin'"
elif numQuo == 3:
    pyQuote = "Got text?"
elif numQuo == 4:
    pyQuote = "Nice shirt!"
elif numQuo == 5:
    pyQuote = "Runnin' out of ideas here..."
elif numQuo == 6:
    pyQuote = "Almost like Pie"
else:
    print "ERROR on Quote engine!!!"

