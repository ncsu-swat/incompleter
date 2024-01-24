# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46111203/flask-dynamo-connection-issueattributeerror-dynamo-object-has-no-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask
    _l_(403217)

except ImportError:
    pass
try:
    from flask_dynamo import Dynamo
    _l_(403219)

except ImportError:
    pass
try:
    import os
    _l_(403221)

except ImportError:
    pass
_a_(403223, _n_(403222, "os", lambda: os), "environ")['AWS_ACCESS_KEY_ID'] = ''
_l_(403224)
_a_(403226, _n_(403225, "os", lambda: os), "environ")['AWS_SECRET_ACCESS_KEY'] = ''
_l_(403227)
_a_(403229, _n_(403228, "os", lambda: os), "environ")['AWS_REGION'] = 'ap-south-1'
_l_(403230)
app = _c_(403233, _n_(403231, "Flask", lambda: Flask), _n_(403232, "__name__", lambda: __name__))
_l_(403234)
_a_(403236, _n_(403235, "app", lambda: app), "config")['DYNAMO_TABLES'] = [
{
    'TableName': 'users',
    'KeySchema': [_c_(403238, _n_(403237, "dict", lambda: dict), AttributeName='username', KeyType='HASH')],
    'AttributeDefinitions': [_c_(403240, _n_(403239, "dict", lambda: dict), AttributeName='username', AttributeType='S')],
    'ProvisionedThroughput': _c_(403242, _n_(403241, "dict", lambda: dict), ReadCapacityUnits=5, WriteCapacityUnits=5)
}, {
     'TableName': 'groups',
    'KeySchema': [_c_(403244, _n_(403243, "dict", lambda: dict), AttributeName='name', KeyType='HASH')],
    'AttributeDefinitions': [_c_(403246, _n_(403245, "dict", lambda: dict), AttributeName='name', AttributeType='S')],
    'ProvisionedThroughput': _c_(403248, _n_(403247, "dict", lambda: dict), ReadCapacityUnits=5, WriteCapacityUnits=5)
}
      ]
_l_(403249)
_a_(403251, _n_(403250, "app", lambda: app), "config")['DYNAMO_ENABLE_LOCAL'] = True
_l_(403252)
_a_(403254, _n_(403253, "app", lambda: app), "config")['DYNAMO_LOCAL_HOST'] = 'localhost'
_l_(403255)
_a_(403257, _n_(403256, "app", lambda: app), "config")['DYNAMO_LOCAL_PORT'] = 9000
_l_(403258)
dynamo = _c_(403260, _n_(403259, "Dynamo", lambda: Dynamo))
_l_(403261)