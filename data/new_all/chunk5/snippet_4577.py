# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55153695/typeerror-not-supported-between-instances-of-str-and-int-having-this
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for file in _c_(676365, _a_(676364, _n_(676363, "os", lambda: os), "listdir"), 'csv/'):
    _l_(676384)


    filename = _c_(676368, _a_(676366, 'csv/{}', "format"), _n_(676367, "file", lambda: file))
    _l_(676369)

    _c_(676372, _n_(676370, "print", lambda: print), _n_(676371, "filename", lambda: filename))
    _l_(676373)

    df = _c_(676377, _a_(676375, _n_(676374, "pd", lambda: pd), "read_table"), _n_(676376, "filename", lambda: filename),skiprows=3,sep=';')
    _l_(676378)

    df1=_a_(676380, _n_(676379, "df", lambda: df), "loc")[(_n_(676381, "df", lambda: df)['#timestamp'] <= 0) & (_n_(676382, "df", lambda: df)['#timestamp'] >=-5)]
    _l_(676383)