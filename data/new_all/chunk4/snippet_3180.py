# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/21923652/typeerror-directoryclass-object-is-not-subscriptable-tried-de-subscripting-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class directoryClass():
   _l_(613690)

                        # to define a directory in which we may encase files.
   Child = {}
   _l_(613687)
   Parent = ''
   _l_(613688)
   Referance = ''
   _l_(613689)

my_picObject = _c_(613692, _n_(613691, "directoryClass", lambda: directoryClass))
_l_(613693)
my_docObject = _c_(613695, _n_(613694, "directoryClass", lambda: directoryClass))
_l_(613696)
userObject = _c_(613698, _n_(613697, "directoryClass", lambda: directoryClass))
_l_(613699)
usersObject = _c_(613701, _n_(613700, "directoryObject", lambda: directoryObject))
_l_(613702)

def my_picObj():
   _l_(613713)

   my_picObject = _c_(613704, _n_(613703, "directoryClass", lambda: directoryClass))
   _l_(613705)
   _n_(613706, "my_picObject", lambda: my_picObject).Child = {'"Hello World.py"' : {'DataType' : 'Read', 'Information' : 'World'}}
   _l_(613707)
   _n_(613708, "my_picObject", lambda: my_picObject).Parent = _n_(613709, "userObject", lambda: userObject)
   _l_(613710)
   _n_(613711, "my_picObject", lambda: my_picObject).Referance = 'My Pictures'
   _l_(613712)

def my_docObj():
   _l_(613724)

   my_docObject = _c_(613715, _n_(613714, "directoryClass", lambda: directoryClass))
   _l_(613716)
   _n_(613717, "my_docObject", lambda: my_docObject).Child = {'Input.py' : {'DataType' : 'Read', 'Information' : 'Hello World'}}
   _l_(613718)
   _n_(613719, "my_docObject", lambda: my_docObject).Parent = _n_(613720, "userObject", lambda: userObject)
   _l_(613721)
   _n_(613722, "my_docObject", lambda: my_docObject).Reference = 'My Documents'
   _l_(613723)

def userObj():
   _l_(613737)

   userObject = _c_(613726, _n_(613725, "directoryClass", lambda: directoryClass))
   _l_(613727)
   _n_(613728, "userObject", lambda: userObject).Child = {'"My Documents"' : _n_(613729, "my_docObject", lambda: my_docObject), '"My Pictures"' : _n_(613730, "my_picObject", lambda: my_picObject)}
   _l_(613731)
   _n_(613732, "userObject", lambda: userObject).Parent = _n_(613733, "usersObject", lambda: usersObject)
   _l_(613734)
   _n_(613735, "userObject", lambda: userObject).Referance = 'User'
   _l_(613736)

def usersObj():
   _l_(613748)

   usersObject = _c_(613739, _n_(613738, "directoryClass", lambda: directoryClass))
   _l_(613740)
   _n_(613741, "usersObject", lambda: usersObject).Child = {'User' : _n_(613742, "userObject", lambda: userObject)}
   _l_(613743)
   _n_(613744, "usersObject", lambda: usersObject).Parent = 'None'
   _l_(613745)
   _n_(613746, "usersObject", lambda: usersObject).Referance = 'Users'
   _l_(613747)

_c_(613750, _n_(613749, "my_picObj", lambda: my_picObj))
_l_(613751)
_c_(613753, _n_(613752, "my_docObj", lambda: my_docObj))
_l_(613754)
_c_(613756, _n_(613755, "userObj", lambda: userObj))
_l_(613757)
_c_(613759, _n_(613758, "usersObj", lambda: usersObj))
_l_(613760)

print = _a_(613762, _n_(613761, "usersObject", lambda: usersObject), "Child")['User']['"My Pictures"']['"Hello World.py"']['Information'] #Error Occurs here
_l_(613763) #Error Occurs here

_c_(613766, _n_(613764, "print", lambda: print), _n_(613765, "print", lambda: print))
_l_(613767)