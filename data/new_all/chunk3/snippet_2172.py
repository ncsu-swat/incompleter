# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59919041/attributeerror-module-boto3-has-no-attribute-client-error-while-trying-to
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import boto3
    _l_(573843)

except ImportError:
    pass
try:
    import json
    _l_(573845)

except ImportError:
    pass

client = _c_(573848, _a_(573847, _n_(573846, "boto3", lambda: boto3), "client"), 'lambda')
_l_(573849)

response = _c_(573852, _a_(573851, _n_(573850, "client", lambda: client), "create_function"), Code={
},
Description='Test LambdaFunction using boto3 SDK',
FunctionName='TestLambda',
# is of the form of the name of your source file and then name of your function handler
Handler='lambda_function.lambda_handler',
MemorySize=128,
Publish=True,
# replace with the actual arn of the execution role you created
Role='arn:aws:iam::xxxxxxxxxx:role/TestRole',
Runtime='python3.7',
Timeout=15,
VpcConfig={
    'SubnetIds': [
        'subnet-xxxxxx',
        'subnet-xxxxxx'
    ],
    'SecurityGroupIds': [
        'sg-xxxxx66',
    ],
    'VpcId': 'vpc-xxxxx'
  },
)
_l_(573853)