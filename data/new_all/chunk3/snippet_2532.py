# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72941940/attributeerror-list-object-has-no-attribute-split-boto3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import boto3
    _l_(535807)

except ImportError:
    pass
account_id = 'accountID'
_l_(535808)
role_name = 'MyRole'
_l_(535809)

def assume_role(role_name, account_id):
    _l_(535835)

    session = _c_(535812, _a_(535811, _n_(535810, "boto3", lambda: boto3), "Session"))
    _l_(535813)
    sts_client = _c_(535816, _a_(535815, _n_(535814, "session", lambda: session), "client"), 'sts')
    _l_(535817)
    assumed_role_object = _c_(535823, _a_(535819, _n_(535818, "sts_client", lambda: sts_client), "assume_role"), RoleArn=f'arn:aws:iam::{_n_(535820, "account_id", lambda: account_id)}:role/{_n_(535821, "role_name", lambda: role_name)}',
        RoleSessionName = f'{_n_(535822, "role_name", lambda: role_name)}-Session'
    )
    _l_(535824)

    assumed_role_credentials = _n_(535825, 'assumed_role_object', lambda: assumed_role_object)['Credentials']
    _l_(535826)

    assumed_session = _c_(535831, _a_(535828, _n_(535827, 'boto3', lambda: boto3), 'Session'), aws_access_key_id=_n_(535829, 'assumed_role_credentials', lambda: assumed_role_credentials)['AccessKeyId'],
        aws_secret_access_key=_n_(535830, 'assumed_role_credentials', lambda: assumed_role_credentials)['SecretAccessKey'],
        aws_session_token=['SessionToken']
    )
    _l_(535832)
    aux = _n_(535833, 'assumed_session', lambda: assumed_session)
    _l_(535834)
    return aux

ec2_role_session = _c_(535839, _n_(535836, 'assume_role', lambda: assume_role), _n_(535837, 'role_name', lambda: role_name), _n_(535838, 'account_id', lambda: account_id))
_l_(535840)
instances = _c_(535846, _a_(535845, _a_(535844, _c_(535843, _a_(535842, _n_(535841, 'ec2_role_session', lambda: ec2_role_session), 'resource'), 'ec2', region_name="us-east-1"), 'instances'), 'all'))
_l_(535847)

for instance in _n_(535848, 'instances', lambda: instances):
    _l_(535854)

    _c_(535852, _n_(535849, 'print', lambda: print), f"Instance ID: {_a_(535851, _n_(535850, 'instance', lambda: instance), 'id')}")
    _l_(535853)