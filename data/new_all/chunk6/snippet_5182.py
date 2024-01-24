# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65705471/concatenating-dataframes-read-from-multiple-aws-s3-bucket-generate-nonetype-erro
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
bucket = _c_(354994, _a_(354993, _n_(354992, "s3", lambda: s3), "Bucket"), 'my bucket')
_l_(354995)
try:
    import io
    _l_(354997)

except ImportError:
    pass
prefix_objs = _c_(355001, _a_(355000, _a_(354999, _n_(354998, "bucket", lambda: bucket), "objects"), "filter"), Prefix="folder/prefix")
_l_(355002)

df = []
_l_(355003)

for obj in _n_(355004, "prefix_objs", lambda: prefix_objs):
    _l_(355027)

    key = _a_(355006, _n_(355005, "obj", lambda: obj), "key")
    _l_(355007)
    body = _c_(355012, _a_(355011, _c_(355010, _a_(355009, _n_(355008, "obj", lambda: obj), "get"))['Body'], "read"))
    _l_(355013)
    temp = _c_(355020, _a_(355015, _n_(355014, "pd", lambda: pd), "read_csv"), _c_(355019, _a_(355017, _n_(355016, "io", lambda: io), "BytesIO"), _n_(355018, "body", lambda: body)), encoding='utf8',sep=",")        
    _l_(355021)        
    _c_(355025, _a_(355023, _n_(355022, "df", lambda: df), "append"), _n_(355024, "temp", lambda: temp))
    _l_(355026)