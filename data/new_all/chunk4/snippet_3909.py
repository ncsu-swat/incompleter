# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65462896/typeerror-print-takes-0-positional-arguments-but-1-was-given-highschool-edi
###Program 11 Create a binary file with name and roll no. Search for a given roll number and display the name, if not found display appropriate message.
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pickle
    _l_(605337)

except ImportError:
    pass
try:
    import sys
    _l_(605339)

except ImportError:
    pass
D={}
_l_(605340)
def main(self):
    _l_(605387)

    try:
        _l_(605386)

        no=_c_(605342, _n_(605341, "input", lambda: input), "enter the number of students")
        _l_(605343)
    
        file=_c_(605345, _n_(605344, "open", lambda: open), "studentsdetails.dat", "wb+")
        _l_(605346)
        for i in _c_(605349, _n_(605347, "range", lambda: range), _n_(605348, "no", lambda: no)):
            _l_(605376)

            _c_(605352, _n_(605350, "print", lambda: print), "enter the information of student %d"%_n_(605351, "i", lambda: i))
            _l_(605353)
            _n_(605354, "D", lambda: D)["rollno"]=_c_(605358, _n_(605355, "int", lambda: int), _c_(605357, _n_(605356, "input", lambda: input), "enter the roll number: "))
            _l_(605359)
            _n_(605360, "D", lambda: D)["Sname"]=_c_(605362, _n_(605361, "input", lambda: input), "enter the student name: ")
            _l_(605363)
            _n_(605364, "D", lambda: D)["marks"]=_c_(605368, _n_(605365, "int", lambda: int), _c_(605367, _n_(605366, "input", lambda: input), "enter the marks: "))
            _l_(605369)
            _c_(605374, _a_(605371, _n_(605370, "pickle", lambda: pickle), "dump"), _n_(605372, "D", lambda: D),_n_(605373, "file", lambda: file))
            _l_(605375)
        _c_(605379, _a_(605378, _n_(605377, "file", lambda: file), "close"))
        _l_(605380)
    except:
        _l_(605385)

        _c_(605382, _n_(605381, "input", lambda: input), "there was some error,press any key to continue")
        _l_(605383)
        pass
        _l_(605384)
def print():
    _l_(605407)

    try:
        _l_(605406)

        file=_c_(605389, _n_(605388, "open", lambda: open), "studentsdetails.dat", "rb")
        _l_(605390)
        while True:
            _l_(605400)

            out=_c_(605394, _a_(605392, _n_(605391, "pickle", lambda: pickle), "load"), _n_(605393, "file", lambda: file))
            _l_(605395)
            _c_(605398, _n_(605396, "print", lambda: print), _n_(605397, "out", lambda: out))
            _l_(605399)
    except:
        _l_(605405)

        _c_(605402, _n_(605401, "print", lambda: print), "error try again")
        _l_(605403)
        pass
        _l_(605404)
def search():
    _l_(605440)

    try:
        _l_(605439)

        file=_c_(605409, _n_(605408, "open", lambda: open), "studentsdetails.dat","rb")
        _l_(605410)
        se=_c_(605412, _n_(605411, "input", lambda: input), "enter the roll number to search")
        _l_(605413)
        while True:
            _l_(605429)

            if _n_(605414, "D", lambda: D)["rollno"]==_n_(605415, "se", lambda: se):
                _l_(605428)

                _c_(605418, _n_(605416, "print", lambda: print), "the rollnumber %d the data is:"%_n_(605417, "se", lambda: se))
                _l_(605419)
                _c_(605422, _n_(605420, "print", lambda: print), _n_(605421, "D", lambda: D))
                _l_(605423)
            else:
                _c_(605425, _n_(605424, "print", lambda: print), "no record found")
                _l_(605426)
                break
                _l_(605427)
        _c_(605432, _a_(605431, _n_(605430, "file", lambda: file), "close"))
        _l_(605433)
    except:
        _l_(605438)

        _c_(605435, _n_(605434, "print", lambda: print), "some error occured, try again")
        _l_(605436)
        pass
        _l_(605437)

while True:
    _l_(605462)

    intg=_c_(605442, _n_(605441, "input", lambda: input), "Enter your choice:\n1. Enter data\n2. Print Data\n3.search data\n4. Exit\n")
    _l_(605443)
    if _n_(605444, "intg", lambda: intg)==("1"):
        _l_(605448)

        _c_(605446, _n_(605445, "main", lambda: main))
        _l_(605447)
    if _n_(605449, "intg", lambda: intg)==("2"):
        _l_(605453)

        _c_(605451, _n_(605450, "print", lambda: print))
        _l_(605452)
    if _n_(605454, "intg", lambda: intg)==("3"):
        _l_(605458)

        _c_(605456, _n_(605455, "search", lambda: search))
        _l_(605457)
    if _n_(605459, "intg", lambda: intg)==("4"):
        _l_(605461)

        break
        _l_(605460)