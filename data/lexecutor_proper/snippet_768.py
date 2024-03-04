# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2759067/rename-multiple-files-in-a-directory-in-python
#List all files in the directory
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
file_list = _c_(64769, _a_(64768, _n_(64767, "os", lambda: os), "listdir"), "/Users/tedfuller/Desktop/prank/")
_l_(64770)
_c_(64773, _n_(64771, "print", lambda: print), _n_(64772, "file_list", lambda: file_list))
_l_(64774)

#Change current working directory and print out it's location
working_location = _c_(64777, _a_(64776, _n_(64775, "os", lambda: os), "chdir"), "/Users/tedfuller/Desktop/prank/")
_l_(64778)
working_location = _c_(64781, _a_(64780, _n_(64779, "os", lambda: os), "getcwd"))
_l_(64782)
_c_(64785, _n_(64783, "print", lambda: print), _n_(64784, "working_location", lambda: working_location))
_l_(64786)

#Rename all the files in that directory
for file_name in _n_(64787, "file_list", lambda: file_list):
    _l_(64801)

    _c_(64799, _a_(64789, _n_(64788, "os", lambda: os), "rename"), _n_(64790, "file_name", lambda: file_name), _c_(64798, _a_(64792, _n_(64791, "file_name", lambda: file_name), "translate"), _c_(64797, _a_(64794, _n_(64793, "str", lambda: str), "maketrans"), "","",_a_(64796, _n_(64795, "string", lambda: string), "digits"))))
    _l_(64800)

