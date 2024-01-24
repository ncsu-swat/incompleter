# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63123537/aws-ssm-python-boto3-create-hybrid-activation-expirationdate-type-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import boto3
    _l_(543693)

except ImportError:
    pass
try:
    import datetime
    _l_(543695)

except ImportError:
    pass

client = _c_(543698, _a_(543697, _n_(543696, "boto3", lambda: boto3), "client"), 'ssm')
_l_(543699)
current_date = _c_(543703, _a_(543702, _a_(543701, _n_(543700, "datetime", lambda: datetime), "date"), "today"))
_l_(543704)
creation_date = _c_(543707, _a_(543706, _n_(543705, "current_date", lambda: current_date), "strftime"), '%Y%m%d')
_l_(543708)
end_date = _n_(543709, "current_date", lambda: current_date) + _c_(543712, _a_(543711, _n_(543710, "datetime", lambda: datetime), "timedelta"), days=30)
_l_(543713)
y = _a_(543715, _n_(543714, "end_date", lambda: end_date), "year")
_l_(543716)
m = _a_(543718, _n_(543717, "end_date", lambda: end_date), "month")
_l_(543719)
d = _a_(543721, _n_(543720, "end_date", lambda: end_date), "day")
_l_(543722)
divisions = ['div1', 'div2', 'div3']
_l_(543723)

#def lambda_handler(event, context):

for x in _n_(543724, "divisions", lambda: divisions):
    _l_(543740)

    _c_(543734, _a_(543726, _n_(543725, "client", lambda: client), "create_activation"), Description = (_n_(543727, "x", lambda: x) + '-' + 'creation_date'),
        #DefaultInstanceName = 'string',
        IamRole = 'MySSMServiceRole',
        RegistrationLimit = 200,
        ExpirationDate = _c_(543732, _n_(543728, "datetime", lambda: datetime), _n_(543729, "y", lambda: y), _n_(543730, "m", lambda: m), _n_(543731, "d", lambda: d)),
        Tags=[
            {
                'Key': 'Division',
                'Value': _n_(543733, "x", lambda: x)
            },
        ]
    )
    _l_(543735)
    _c_(543738, _n_(543736, "print", lambda: print), '\n ' + _n_(543737, "x", lambda: x) + '-creation_date was create.')
    _l_(543739)