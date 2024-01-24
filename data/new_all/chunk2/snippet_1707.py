# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61526938/filenotfounderror-errno-2-no-such-file-or-directory-cant-solve-a-path-prob
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
table_url = 'https://resource-cms.springernature.com/springer-cms/rest/v1/content/17858272/data/v4'
_l_(472910)

table = 'table_' + _c_(472913, _a_(472912, _n_(472911, "table_url", lambda: table_url), "split"), '/')[-1] + '.xlsx'
_l_(472914)
table_path = _c_(472920, _a_(472917, _a_(472916, _n_(472915, "os", lambda: os), "path"), "join"), _n_(472918, "folder", lambda: folder), _n_(472919, "table", lambda: table))
_l_(472921)
if not _c_(472926, _a_(472924, _a_(472923, _n_(472922, "os", lambda: os), "path"), "exists"), _n_(472925, "table_path", lambda: table_path)):
    _l_(472942)

    books = _c_(472930, _a_(472928, _n_(472927, "pd", lambda: pd), "read_excel"), _n_(472929, "table_url", lambda: table_url))
    _l_(472931)
    # Save table
    _c_(472935, _a_(472933, _n_(472932, "books", lambda: books), "to_excel"), _n_(472934, "table_path", lambda: table_path))
    _l_(472936)
else:
    books = _c_(472940, _a_(472938, _n_(472937, "pd", lambda: pd), "read_excel"), _n_(472939, "table_path", lambda: table_path), index_col=0, header=0)
    _l_(472941)