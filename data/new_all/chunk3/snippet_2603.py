# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69692529/typeerror-object-of-type-foo-is-not-json-serializable-in-array
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import flask
    _l_(555905)

except ImportError:
    pass
try:
    from flask import request, jsonify
    _l_(555907)

except ImportError:
    pass
try:
    import uuid
    _l_(555909)

except ImportError:
    pass

app = _c_(555913, _a_(555911, _n_(555910, "flask", lambda: flask), "Flask"), _n_(555912, "__name__", lambda: __name__))
_l_(555914)
_a_(555916, _n_(555915, "app", lambda: app), "config")["DEBUG"] = True
_l_(555917)

class Pet:
    _l_(555929)

    def __init__(self,id, name, dateOfBirth):
        _l_(555928)

        _n_(555918, "self", lambda: self).id = _a_(555920, _n_(555919, "id", lambda: id), "hex")
        _l_(555921)
        _n_(555922, "self", lambda: self).name = _n_(555923, "name", lambda: name)
        _l_(555924)
        _n_(555925, "self", lambda: self).dateOfBirth = _n_(555926, "dateOfBirth", lambda: dateOfBirth)
        _l_(555927)
#    def to_json(obj):
#        return json.dumps(obj, default=lambda obj: obj.__dict__)

# Create some test data for our catalog in the form of a list of dictionaries.
pets = [ _c_(555934, _n_(555930, "Pet", lambda: Pet), _c_(555933, _a_(555932, _n_(555931, "uuid", lambda: uuid), "uuid4")),'Hamster', '02.12.2019' )]
_l_(555935)
_c_(555943, _a_(555937, _n_(555936, "pets", lambda: pets), "append"), _c_(555942, _n_(555938, "Pet", lambda: Pet), _c_(555941, _a_(555940, _n_(555939, "uuid", lambda: uuid), "uuid4")),'Fish', '07.03.1985' ))
_l_(555944)
_c_(555952, _a_(555946, _n_(555945, "pets", lambda: pets), "append"), _c_(555951, _n_(555947, "Pet", lambda: Pet), _c_(555950, _a_(555949, _n_(555948, "uuid", lambda: uuid), "uuid4")),'Dog', '26.11.2000' ))
_l_(555953)
_c_(555961, _a_(555955, _n_(555954, "pets", lambda: pets), "append"), _c_(555960, _n_(555956, "Pet", lambda: Pet), _c_(555959, _a_(555958, _n_(555957, "uuid", lambda: uuid), "uuid4")),'Cat', '17.05.2021' ))
_l_(555962)

@_c_(555965, _a_(555964, _n_(555963, "app", lambda: app), "route"), '/', methods=['GET'])
def home():
    _l_(555967)

    aux = "<h1>Petshop Archive</h1><p>This site is a prototype API for the petshop archive.</p>"
    _l_(555966)
    return aux

# A route to return all of the available entries in our catalog.
@_c_(555970, _a_(555969, _n_(555968, "app", lambda: app), "route"), '/api/v1/resources/pets/all', methods=['GET'])
def api_all():
    _l_(555975)

    aux = _c_(555973, _n_(555971, "jsonify", lambda: jsonify), _n_(555972, "pets", lambda: pets))
    _l_(555974)
    return aux

if _n_(555976, "__name__", lambda: __name__) == '__main__':
    _l_(555981)

    _c_(555979, _a_(555978, _n_(555977, "app", lambda: app), "run"), host='0.0.0.0')
    _l_(555980)