# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72377436/attributeerror-partially-initialized-module-boto3-has-no-attribute-session
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import boto3
    _l_(469199)

except ImportError:
    pass
aws_mg_con=_c_(469203, _a_(469202, _a_(469201, _n_(469200, "boto3", lambda: boto3), "session"), "Session"), profile_name='demo_user')
_l_(469204)
iam_con=_c_(469207, _a_(469206, _n_(469205, "aws_mg_con", lambda: aws_mg_con), "resource"), 'iam')
_l_(469208)