# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69659778/handlerlambda-handler-missing-on-module-lambda-function-errortype-run
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import boto3
    _l_(467699)

except ImportError:
    pass
try:
    from datetime import datetime, timedelta
    _l_(467701)

except ImportError:
    pass
try:
    from dateutil.tz import tzutc, UTC
    _l_(467703)

except ImportError:
    pass

BUCKET = 'my-bucket'
_l_(467704)
TOPIC_ARN = 'arn:aws:sns:ap-southeast-2:123456789012:Old-File-Warning'
_l_(467705)

s3_resource = _c_(467708, _a_(467707, _n_(467706, "boto3", lambda: boto3), "resource"), 's3')
_l_(467709)
sns_resource = _c_(467712, _a_(467711, _n_(467710, "boto3", lambda: boto3), "resource"), 'sns')
_l_(467713)
sns_topic = _c_(467717, _a_(467715, _n_(467714, "sns_resource", lambda: sns_resource), "Topic"), _n_(467716, "TOPIC_ARN", lambda: TOPIC_ARN))
_l_(467718)

for object in _c_(467725, _a_(467724, _a_(467723, _c_(467722, _a_(467720, _n_(467719, "s3_resource", lambda: s3_resource), "Bucket"), _n_(467721, "BUCKET", lambda: BUCKET)), "objects"), "filter"), Prefix='folder1/folder2/'):
    _l_(467744)

    if _a_(467727, _n_(467726, "object", lambda: object), "last_modified") > _c_(467732, _a_(467729, _n_(467728, "datetime", lambda: datetime), "now"), _c_(467731, _n_(467730, "tzutc", lambda: tzutc))) - _c_(467734, _n_(467733, "timedelta", lambda: timedelta), hours = 1):
        _l_(467743)

        message = f"Object {_a_(467736, _n_(467735, 'object', lambda: object), 'key')} is more than 1 hour old!"
        _l_(467737)
        _c_(467741, _a_(467739, _n_(467738, "sns_topic", lambda: sns_topic), "publish"), Message=_n_(467740, "message", lambda: message))
        _l_(467742)