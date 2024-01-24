# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65705471/concatenating-dataframes-read-from-multiple-aws-s3-bucket-generate-nonetype-erro
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
bucket = _c_(359872, _a_(359871, _n_(359870, "s3", lambda: s3), "Bucket"), 'mybucket')
_l_(359873)
try:
    import io
    _l_(359875)

except ImportError:
    pass
prefix_objs = _c_(359879, _a_(359878, _a_(359877, _n_(359876, "bucket", lambda: bucket), "objects"), "filter"), Prefix="folder/file_prefix")
_l_(359880)

df = _c_(359883, _a_(359882, _n_(359881, "pd", lambda: pd), "DataFrame"))
_l_(359884)

for obj in _n_(359885, "prefix_objs", lambda: prefix_objs):
    _l_(359911)

    key = _a_(359887, _n_(359886, "obj", lambda: obj), "key")
    _l_(359888)
    body = _c_(359893, _a_(359892, _c_(359891, _a_(359890, _n_(359889, "obj", lambda: obj), "get"))['Body'], "read"))
    _l_(359894)
    temp = _c_(359901, _a_(359896, _n_(359895, "pd", lambda: pd), "read_csv"), _c_(359900, _a_(359898, _n_(359897, "io", lambda: io), "BytesIO"), _n_(359899, "body", lambda: body)), sep=",",encoding='utf8')        
    _l_(359902)        
    frame =[_n_(359903, "df", lambda: df),_n_(359904, "temp", lambda: temp)]
    _l_(359905)
    df = _c_(359909, _a_(359907, _n_(359906, "pd", lambda: pd), "concat"), _n_(359908, "frame", lambda: frame))
    _l_(359910)