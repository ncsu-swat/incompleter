# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53847237/audiosegment-and-bytesio-module-gives-filenotfounderror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import boto3
    _l_(571733)

except ImportError:
    pass
try:
    from pydub import AudioSegment
    _l_(571735)

except ImportError:
    pass
try:
    import io
    _l_(571737)

except ImportError:
    pass
client = _c_(571740, _a_(571739, _n_(571738, "boto3", lambda: boto3), "client"), 's3')
_l_(571741)
obj = _c_(571744, _a_(571743, _n_(571742, "client", lambda: client), "get_object"), Bucket='<BucketName>', Key='<FileName>')
_l_(571745)
data = _c_(571751, _a_(571747, _n_(571746, "io", lambda: io), "BytesIO"), _c_(571750, _a_(571749, _n_(571748, "obj", lambda: obj)['Body'], "read")))
_l_(571752)
sound1 = _c_(571756, _a_(571754, _n_(571753, "AudioSegment", lambda: AudioSegment), "from_file"), _n_(571755, "data", lambda: data))
_l_(571757)