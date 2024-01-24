# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57761583/how-to-avoid-a-filenotfounderror-with-os-listdir
# Specify folder name
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
serial = '015'
_l_(438293)

# Specify directory (note - '...' substitute for the full path used back to the drive letter)

root_dir = _c_(438298, _a_(438294, '...\\CleanTemps\\{}\\', "format"), _c_(438297, _n_(438295, "str", lambda: str), _n_(438296, "serial", lambda: serial))) 
_l_(438299) 

#loop
for filename in _c_(438303, _a_(438301, _n_(438300, "os", lambda: os), "listdir"), _n_(438302, "root_dir", lambda: root_dir)):
    _l_(438317)

    if _c_(438306, _a_(438305, _n_(438304, "filename", lambda: filename), "endswith"), '.csv'):
        _l_(438316)


        _c_(438309, _n_(438307, "print", lambda: print), _n_(438308, "filename", lambda: filename))
        _l_(438310)

        # Pull in the file
        df = _c_(438314, _a_(438312, _n_(438311, "pd", lambda: pd), "read_csv"), _n_(438313, "filename", lambda: filename))
        _l_(438315)