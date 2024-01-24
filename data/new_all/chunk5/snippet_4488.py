# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56689224/python-dict-datatype-error-while-after-reading-message-from-aws-sqs-and-put-it-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(697273)

except ImportError:
    pass
try:
    import boto3
    _l_(697275)

except ImportError:
    pass

dynamodb = _c_(697278, _a_(697277, _n_(697276, "boto3", lambda: boto3), "resource"), 'dynamodb')
_l_(697279)
dynamoTable = _c_(697282, _a_(697281, _n_(697280, "dynamodb", lambda: dynamodb), "Table"), 'message')
_l_(697283)

def lambda_handler(event, context):
    _l_(697302)

    for record in _n_(697284, "event", lambda: event)['Records']:
        _l_(697301)

        data1 = _n_(697285, "record", lambda: record)["body"]
        _l_(697286)
        jsondata1 = _c_(697290, _a_(697288, _n_(697287, "json", lambda: json), "loads"), _n_(697289, "data1", lambda: data1))
        _l_(697291)
        _c_(697294, _n_(697292, "print", lambda: print), _n_(697293, "jsondata1", lambda: jsondata1))
        _l_(697295)
        _c_(697299, _a_(697297, _n_(697296, "dynamoTable", lambda: dynamoTable), "put_item"), Item=_n_(697298, "jsondata1", lambda: jsondata1))      
        _l_(697300)      