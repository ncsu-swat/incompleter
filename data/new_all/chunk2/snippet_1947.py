# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76185529/it-keeps-given-the-error-attributeerror-nonetype-object-has-no-attribute-get
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import boto3
    _l_(425984)

except ImportError:
    pass
InstanceIds = ['I-1234', 'I-2345', 'I-6789']
_l_(425985)
ec2 = _c_(425988, _a_(425987, _n_(425986, "boto3", lambda: boto3), "resource"), 'ec2')
_l_(425989)
for inst in _n_(425990, "InstanceIds", lambda: InstanceIds):
    _l_(426039)

    instance_response = _c_(425994, _a_(425992, _n_(425991, "ec2", lambda: ec2), "Instance"), _n_(425993, "inst", lambda: inst))
    _l_(425995)
    if _n_(425996, "instance_response", lambda: instance_response) is None:
        _l_(426038)

        _c_(425999, _n_(425997, "print", lambda: print), _n_(425998, "instance_response", lambda: instance_response), " has a value of None")
        _l_(426000)
    else:
        instance_tags = _a_(426002, _n_(426001, "instance_response", lambda: instance_response), "tags")
        _l_(426003)
        for item in _n_(426004, "instance_tags", lambda: instance_tags):
            _l_(426009)

            if _n_(426005, "item", lambda: item)['Key'] == 'Environment':
                _l_(426008)

                val = _n_(426006, "item", lambda: item)['Value']
                _l_(426007)
        pattern = _c_(426014, _a_(426011, _n_(426010, "re", lambda: re), "compile"), r'\bpr\w*', _a_(426013, _n_(426012, "re", lambda: re), "IGNORECASE"))
        _l_(426015)
        matches = _c_(426019, _a_(426017, _n_(426016, "pattern", lambda: pattern), "findall"), _n_(426018, "val", lambda: val))
        _l_(426020)
        if _n_(426021, "matches", lambda: matches):
            _l_(426037)

            _c_(426025, _n_(426022, "print", lambda: print), "Prod Tag exists in ", _n_(426023, "inst", lambda: inst), _n_(426024, "val", lambda: val))
            _l_(426026)
        else:
            _c_(426030, _a_(426028, _n_(426027, "nonPRD_tags_exists_instances", lambda: nonPRD_tags_exists_instances), "append"), _n_(426029, "inst", lambda: inst))
            _l_(426031)
            _c_(426035, _n_(426032, "print", lambda: print), "Prod Tag doesn't exists in ", _n_(426033, "inst", lambda: inst), _n_(426034, "val", lambda: val)) 
            _l_(426036) 
_c_(426042, _n_(426040, "print", lambda: print), _n_(426041, "nonPRD_tags_exists_instances", lambda: nonPRD_tags_exists_instances)) 
_l_(426043) 