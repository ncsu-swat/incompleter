# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64660868/lambda-error-typeerror-str-object-does-not-support-item-assignment-traceback
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(414082)

except ImportError:
    pass
try:
    import uuid
    _l_(414084)

except ImportError:
    pass
try:
    import boto3
    _l_(414086)

except ImportError:
    pass

def lambda_handler(event, context):
    _l_(414129)

    
    dynamo_client = _c_(414089, _a_(414088, _n_(414087, "boto3", lambda: boto3), "resource"), 'dynamodb')
    _l_(414090)
    loadeo_carrier_company = _c_(414093, _a_(414092, _n_(414091, "dynamo_client", lambda: dynamo_client), "Table"), 'loadeo_carrier_company')
    _l_(414094)
    
    
    item = {}
    _l_(414095)
    item = _n_(414096, "event", lambda: event)['body']
    _l_(414097)
    _c_(414100, _n_(414098, "print", lambda: print), _n_(414099, "item", lambda: item))
    _l_(414101)
    _n_(414102, "item", lambda: item)['company_id'] = _c_(414107, _n_(414103, "str", lambda: str), _c_(414106, _a_(414105, _n_(414104, "uuid", lambda: uuid), "uuid4")))
    _l_(414108)
    
    _c_(414113, _n_(414109, "print", lambda: print), _c_(414112, _n_(414110, "type", lambda: type), _n_(414111, "item", lambda: item)))
    _l_(414114)
    try:
        _l_(414128)

        _c_(414118, _a_(414116, _n_(414115, "loadeo_carrier_company", lambda: loadeo_carrier_company), "put_item"), Item=_n_(414117, "item", lambda: item)
        )
        _l_(414119)
        aux = {
            "statusCode": 200,
            "headers" : {
                "Access-Control-Allow-Origin" : "*"
            },
            "message": _c_(414122, _a_(414121, _n_(414120, "json", lambda: json), "dumps"), "Record has been inserted"),
            "body": _n_(414123, "item", lambda: item)
        }
        _l_(414124)
        return aux
    except _n_(414125, "Exception", lambda: Exception) as e:
        _l_(414127)

        aux = {
            "statusCode": 500,
            "headers" : {
                "Access-Control-Allow-Origin" : "*"
            },
            "message": "Error: Unable to save record!"
        }
        _l_(414126)
        return aux