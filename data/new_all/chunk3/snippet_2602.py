# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69692529/typeerror-object-of-type-foo-is-not-json-serializable-in-array
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import flask
    _l_(560192)

except ImportError:
    pass
try:
    from flask import request, jsonify
    _l_(560194)

except ImportError:
    pass

app = _c_(560198, _a_(560196, _n_(560195, "flask", lambda: flask), "Flask"), _n_(560197, "__name__", lambda: __name__))
_l_(560199)
_a_(560201, _n_(560200, "app", lambda: app), "config")["DEBUG"] = True
_l_(560202)

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas'},
    {'id': 2,
     'title': 'Dhalgren'}
]
_l_(560203)

@_c_(560206, _a_(560205, _n_(560204, "app", lambda: app), "route"), '/', methods=['GET'])
def home():
    _l_(560208)

    aux = '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''
    _l_(560207)
    return aux

# A route to return all of the available entries in our catalog.
@_c_(560211, _a_(560210, _n_(560209, "app", lambda: app), "route"), '/api/v1/resources/books/all', methods=['GET'])
def api_all():
    _l_(560216)

    aux = _c_(560214, _n_(560212, "jsonify", lambda: jsonify), _n_(560213, "books", lambda: books))
    _l_(560215)
    return aux

_c_(560219, _a_(560218, _n_(560217, "app", lambda: app), "run"))
_l_(560220)