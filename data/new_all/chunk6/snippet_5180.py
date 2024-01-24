# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65705471/concatenating-dataframes-read-from-multiple-aws-s3-bucket-generate-nonetype-erro
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
bucket = _c_(362128, _a_(362127, _n_(362126, "s3", lambda: s3), "Bucket"), 'my bucket')
_l_(362129)
try:
    import io
    _l_(362131)

except ImportError:
    pass
prefix_objs = _c_(362135, _a_(362134, _a_(362133, _n_(362132, "bucket", lambda: bucket), "objects"), "filter"), Prefix="folder/prefix")
_l_(362136)

df = []
_l_(362137)

for obj in _n_(362138, "prefix_objs", lambda: prefix_objs):
    _l_(362161)

    key = _a_(362140, _n_(362139, "obj", lambda: obj), "key")
    _l_(362141)
    body = _c_(362146, _a_(362145, _c_(362144, _a_(362143, _n_(362142, "obj", lambda: obj), "get"))['Body'], "read"))
    _l_(362147)
    temp = _c_(362154, _a_(362149, _n_(362148, "pd", lambda: pd), "read_csv"), _c_(362153, _a_(362151, _n_(362150, "io", lambda: io), "BytesIO"), _n_(362152, "body", lambda: body)), encoding='utf8',sep=",")        
    _l_(362155)        
    _c_(362159, _a_(362157, _n_(362156, "df", lambda: df), "append"), _n_(362158, "temp", lambda: temp))
    _l_(362160)