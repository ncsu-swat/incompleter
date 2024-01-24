# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70895962/python-aws-boto3-returning-nonetype-error
#!/usr/bin/python3

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import boto3
    _l_(620329)

except ImportError:
    pass
try:
    import botocore
    _l_(620331)

except ImportError:
    pass

boto3_session = _c_(620333, _n_(620332, "create_boto3_session", lambda: create_boto3_session), profile_name='some_profile')
_l_(620334)
ec2_resource = _c_(620337, _a_(620336, _n_(620335, "boto3_session", lambda: boto3_session), "resource"), "ec2", region_name='some_region')
_l_(620338)
ec2_instances = _c_(620342, _a_(620341, _a_(620340, _n_(620339, "ec2_resource", lambda: ec2_resource), "instances"), "all"))
_l_(620343)
for ec2_instance in _n_(620344, "ec2_instances", lambda: ec2_instances):
    _l_(620355)

    tags = _c_(620347, _n_(620345, "getattr", lambda: getattr), _n_(620346, "ec2_instance", lambda: ec2_instance), 'tags', [])
    _l_(620348)
    for tag in _n_(620349, "tags", lambda: tags):
        _l_(620354)

        _c_(620352, _n_(620350, "print", lambda: print), _n_(620351, "tag", lambda: tag))
        _l_(620353)