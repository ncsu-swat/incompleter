# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65705471/concatenating-dataframes-read-from-multiple-aws-s3-bucket-generate-nonetype-erro
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
bucket = _c_(371910, _a_(371909, _n_(371908, "s3", lambda: s3), "Bucket"), 'mybucket')
_l_(371911)
try:
    import io
    _l_(371913)

except ImportError:
    pass
prefix_objs = _c_(371917, _a_(371916, _a_(371915, _n_(371914, "bucket", lambda: bucket), "objects"), "filter"), Prefix="folder/file_prefix")
_l_(371918)

df = _c_(371921, _a_(371920, _n_(371919, "pd", lambda: pd), "DataFrame"))
_l_(371922)

for obj in _n_(371923, "prefix_objs", lambda: prefix_objs):
    _l_(371949)

    key = _a_(371925, _n_(371924, "obj", lambda: obj), "key")
    _l_(371926)
    body = _c_(371931, _a_(371930, _c_(371929, _a_(371928, _n_(371927, "obj", lambda: obj), "get"))['Body'], "read"))
    _l_(371932)
    temp = _c_(371939, _a_(371934, _n_(371933, "pd", lambda: pd), "read_csv"), _c_(371938, _a_(371936, _n_(371935, "io", lambda: io), "BytesIO"), _n_(371937, "body", lambda: body)), sep=",",encoding='utf8')        
    _l_(371940)        
    frame =[_n_(371941, "df", lambda: df),_n_(371942, "temp", lambda: temp)]
    _l_(371943)
    df = _c_(371947, _a_(371945, _n_(371944, "pd", lambda: pd), "concat"), _n_(371946, "frame", lambda: frame))
    _l_(371948)