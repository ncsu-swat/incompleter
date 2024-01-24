# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74878801/attributeerror-dict-object-has-no-attribute-instance-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def status_ec2_instance(instanceIds_list, region_Name):
    _l_(550451)

    ec2 = _c_(550375, _a_(550373, _n_(550372, "boto3", lambda: boto3), "resource"), 'ec2', region_name=_n_(550374, "region_Name", lambda: region_Name))
    _l_(550376)
    ec2_client = _c_(550380, _a_(550378, _n_(550377, "boto3", lambda: boto3), "client"), 'ec2', region_name=_n_(550379, "region_Name", lambda: region_Name))
    _l_(550381)
    _c_(550384, _n_(550382, "print", lambda: print), _n_(550383, "instanceIds_list", lambda: instanceIds_list))
    _l_(550385)
    a=_n_(550386, "instanceIds_list", lambda: instanceIds_list)[0]
    _l_(550387)
    _c_(550390, _n_(550388, "print", lambda: print), _n_(550389, "a", lambda: a))
    _l_(550391)
    #response=ec2_client.describe_instances(InstanceIds=instanceIds_list)
    response = _c_(550395, _a_(550393, _n_(550392, "ec2_client", lambda: ec2_client), "describe_instances"), Filters=[
        {
            'Name': 'private-ip-address',
            'Values': [
                _n_(550394, "a", lambda: a),
            ]    
        }
    ])
    _l_(550396)
    for ec2 in _n_(550397, "response", lambda: response)['Reservations'][0]['Instances']:
        _l_(550442)

        instanceIds = _n_(550398, "ec2", lambda: ec2)['InstanceId']
        _l_(550399)
        _c_(550402, _n_(550400, "print", lambda: print), _n_(550401, "instanceIds", lambda: instanceIds))
        _l_(550403)
        response=_c_(550407, _a_(550405, _n_(550404, "ec2_client", lambda: ec2_client), "start_instances"), InstanceIds=[_n_(550406, "instanceIds", lambda: instanceIds)])
        _l_(550408)
        _c_(550413, _n_(550409, "print", lambda: print), 'started your instances: ' + _c_(550412, _n_(550410, "str", lambda: str), _n_(550411, "instanceIds", lambda: instanceIds)))
        _l_(550414)
        instance_started = []
        _l_(550415)
        _c_(550418, _n_(550416, "print", lambda: print), _n_(550417, "instanceIds", lambda: instanceIds))
        _l_(550419)
        instance_response = _c_(550423, _a_(550421, _n_(550420, "ec2", lambda: ec2), "Instance"), [_n_(550422, "instanceIds", lambda: instanceIds)])
        _l_(550424)
        instance_state = _a_(550426, _n_(550425, "instance_response", lambda: instance_response), "state")
        _l_(550427)
        if _n_(550428, "instance_state", lambda: instance_state)['Name'] == 'running'and _n_(550429, "instance", lambda: instance) not in _n_(550430, "instance_started", lambda: instance_started):
            _l_(550441)

            _c_(550434, _a_(550432, _n_(550431, "instance_started", lambda: instance_started), "append"), _n_(550433, "instance", lambda: instance))
            _l_(550435)
            _c_(550439, _n_(550436, "print", lambda: print), _n_(550437, "instance", lambda: instance),_n_(550438, "instance_state", lambda: instance_state)['Name'])
            _l_(550440)
    _c_(550447, _n_(550443, "print", lambda: print), "started instances ",_c_(550446, _n_(550444, "str", lambda: str), _n_(550445, "instance_started", lambda: instance_started)))
    _l_(550448)
    aux = _n_(550449, "instance_started", lambda: instance_started)
    _l_(550450)
    return aux

if _n_(550452, "__name__", lambda: __name__) == "__main__":
    _l_(550464)

    PrivateIP = _a_(550454, _n_(550453, "sys", lambda: sys), "argv")[1]
    _l_(550455)
    region_Name = "us-east-1"
    _l_(550456)
    #instanceIds_list = [instanceIds]
    instanceIds_list = [_n_(550457, "PrivateIP", lambda: PrivateIP)]
    _l_(550458)
    status_list=_c_(550462, _n_(550459, "status_ec2_instance", lambda: status_ec2_instance), _n_(550460, "instanceIds_list", lambda: instanceIds_list), _n_(550461, "region_Name", lambda: region_Name))
    _l_(550463)