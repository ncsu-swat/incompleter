# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/34593638/filenotfounderror-when-creating-new-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(454275)

except ImportError:
    pass

for dirname, dirs, filename in _c_(454278, _a_(454277, _n_(454276, "os", lambda: os), "walk"), "."):
    _l_(454340)

    for file in _n_(454279, "filename", lambda: filename):
        _l_(454339)

        thefile = _c_(454285, _a_(454282, _a_(454281, _n_(454280, "os", lambda: os), "path"), "join"), _n_(454283, "dirname", lambda: dirname),_n_(454284, "file", lambda: file))
        _l_(454286)
        source = _c_(454289, _n_(454287, "open", lambda: open), _n_(454288, "thefile", lambda: thefile),'rb')
        _l_(454290)
        data = _c_(454293, _a_(454292, _n_(454291, "source", lambda: source), "read"))
        _l_(454294)
        _c_(454297, _a_(454296, _n_(454295, "source", lambda: source), "close"))
        _l_(454298)
        Newpath = "C:\\Users\kemburaj.kemburaj-PC\Documents\\backup\\" #paste the backup directory path, please check escape characters
        _l_(454299) #paste the backup directory path, please check escape characters
        if not _c_(454304, _a_(454302, _a_(454301, _n_(454300, "os", lambda: os), "path"), "exists"), _n_(454303, "Newpath", lambda: Newpath)):
            _l_(454310)

            _c_(454308, _a_(454306, _n_(454305, "os", lambda: os), "makedirs"), _n_(454307, "Newpath", lambda: Newpath))
            _l_(454309)
        file = _c_(454316, _a_(454313, _a_(454312, _n_(454311, "os", lambda: os), "path"), "join"), _n_(454314, "Newpath", lambda: Newpath),_n_(454315, "thefile", lambda: thefile)[2:]) #copy this py file in the directory which is to be backed up
        _l_(454317) #copy this py file in the directory which is to be backed up
        _c_(454320, _n_(454318, "print", lambda: print), _n_(454319, "file", lambda: file))
        _l_(454321)
        fhand = _c_(454324, _n_(454322, "open", lambda: open), _n_(454323, "file", lambda: file),'wb')
        _l_(454325)
        _c_(454329, _a_(454327, _n_(454326, "fhand", lambda: fhand), "write"), _n_(454328, "data", lambda: data))
        _l_(454330)
        _c_(454333, _a_(454332, _n_(454331, "fhand", lambda: fhand), "close"))
        _l_(454334)
        _c_(454337, _n_(454335, "print", lambda: print), "\n\nBackup >",_n_(454336, "file", lambda: file))
        _l_(454338)