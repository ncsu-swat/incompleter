# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/32045794/s3fs-typeerror-cant-concat-bytes-to-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import fs.s3fs
    _l_(691573)

except ImportError:
    pass
myfs = _c_(691580, _a_(691575, _a_(691574, fs, "s3fs"), "S3FS"), _n_(691576, "bucket", lambda: bucket), _n_(691577, "prefix", lambda: prefix), _n_(691578, "aws_access_ke", lambda: aws_access_ke), _n_(691579, "aws_secret_key", lambda: aws_secret_key))
_l_(691581)
_c_(691584, _a_(691583, _n_(691582, "myfs", lambda: myfs), "listdir"))
_l_(691585)