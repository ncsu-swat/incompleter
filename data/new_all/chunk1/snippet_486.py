# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55943016/docker-error-filenotfounderror-errno-2
#!/usr/bin/python3

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask, jsonify, request, abort
    _l_(387629)

except ImportError:
    pass
try:
    from flask_restful import Api, Resource
    _l_(387631)

except ImportError:
    pass
try:
    import jsonpickle
    _l_(387633)

except ImportError:
    pass

app = _c_(387636, _n_(387634, "Flask", lambda: Flask), _n_(387635, "__name__", lambda: __name__))
_l_(387637)
api = _c_(387640, _n_(387638, "Api", lambda: Api), _n_(387639, "app", lambda: app))
_l_(387641)

# Creating an empty dictionary and initializing user id to 0.. will increment every time a person makes a POST request.
# This is bad practice but only using it for the example. Most likely you will be pulling this information from a
# database.
user_dict = {}
_l_(387642)
user_id = 0
_l_(387643)


# Define a class and pass it a Resource. These methods require an ID
class User(_n_(387644, "Resource", lambda: Resource)):
    _l_(387679)

    @_n_(387645, "staticmethod", lambda: staticmethod)
    def get(path_user_id):
        _l_(387662)

        if _n_(387646, "path_user_id", lambda: path_user_id) not in _n_(387647, "user_dict", lambda: user_dict):
            _l_(387651)

            _c_(387649, _n_(387648, "abort", lambda: abort), 400)
            _l_(387650)
        aux = _c_(387660, _n_(387652, "jsonify", lambda: jsonify), _c_(387659, _a_(387654, _n_(387653, "jsonpickle", lambda: jsonpickle), "encode"), _c_(387658, _a_(387656, _n_(387655, "user_dict", lambda: user_dict), "get"), _n_(387657, "path_user_id", lambda: path_user_id), "This user does not exist")))
        _l_(387661)

        return aux

    @_n_(387663, "staticmethod", lambda: staticmethod)
    def put(path_user_id):
        _l_(387671)

        _c_(387669, _n_(387664, "update_and_add_user_helper", lambda: update_and_add_user_helper), _n_(387665, "path_user_id", lambda: path_user_id), _c_(387668, _a_(387667, _n_(387666, "request", lambda: request), "get_json")))
        _l_(387670)

    @_n_(387672, "staticmethod", lambda: staticmethod)
    def delete(path_user_id):
        _l_(387678)

        _c_(387676, _a_(387674, _n_(387673, "user_dict", lambda: user_dict), "pop"), _n_(387675, "path_user_id", lambda: path_user_id), None)
        _l_(387677)


# Get all users and add new users
class UserList(_n_(387680, "Resource", lambda: Resource)):
    _l_(387702)

    @_n_(387681, "staticmethod", lambda: staticmethod)
    def get():
        _l_(387689)

        aux = _c_(387687, _n_(387682, "jsonify", lambda: jsonify), _c_(387686, _a_(387684, _n_(387683, "jsonpickle", lambda: jsonpickle), "encode"), _n_(387685, "user_dict", lambda: user_dict)))
        _l_(387688)
        return aux

    @_n_(387690, "staticmethod", lambda: staticmethod)
    def post():
        _l_(387701)

        global user_id
        _l_(387691)
        user_id = _n_(387692, "user_id", lambda: user_id) + 1
        _l_(387693)
        _c_(387699, _n_(387694, "update_and_add_user_helper", lambda: update_and_add_user_helper), _n_(387695, "user_id", lambda: user_id), _c_(387698, _a_(387697, _n_(387696, "request", lambda: request), "get_json")))
        _l_(387700)


# Since post and put are doing pretty much the same thing, I extracted the logic from both and put it in a separate
# method to follow DRY principles.
def update_and_add_user_helper(u_id, request_payload):
    _l_(387726)

    name = _n_(387703, "request_payload", lambda: request_payload)["name"]
    _l_(387704)
    age = _n_(387705, "request_payload", lambda: request_payload)["age"]
    _l_(387706)
    address = _n_(387707, "request_payload", lambda: request_payload)["address"]
    _l_(387708)
    city = _n_(387709, "request_payload", lambda: request_payload)["city"]
    _l_(387710)
    state = _n_(387711, "request_payload", lambda: request_payload)["state"]
    _l_(387712)
    zip_code = _n_(387713, "request_payload", lambda: request_payload)["zip"]
    _l_(387714)
    _n_(387715, "user_dict", lambda: user_dict)[_n_(387716, "u_id", lambda: u_id)] = _c_(387724, _n_(387717, "Person", lambda: Person), _n_(387718, "name", lambda: name), _n_(387719, "age", lambda: age), _n_(387720, "address", lambda: address), _n_(387721, "city", lambda: city), _n_(387722, "state", lambda: state), _n_(387723, "zip_code", lambda: zip_code))
    _l_(387725)


# Represents a user's information
class Person:
    _l_(387746)

    def __init__(self, name, age, address, city, state, zip_code):
        _l_(387745)

        _n_(387727, "self", lambda: self).name = _n_(387728, "name", lambda: name)
        _l_(387729)
        _n_(387730, "self", lambda: self).age = _n_(387731, "age", lambda: age)
        _l_(387732)
        _n_(387733, "self", lambda: self).address = _n_(387734, "address", lambda: address)
        _l_(387735)
        _n_(387736, "self", lambda: self).city = _n_(387737, "city", lambda: city)
        _l_(387738)
        _n_(387739, "self", lambda: self).state = _n_(387740, "state", lambda: state)
        _l_(387741)
        _n_(387742, "self", lambda: self).zip_code = _n_(387743, "zip_code", lambda: zip_code)
        _l_(387744)


# Add a resource to the api. You need to give the class name and the URI.
_c_(387750, _a_(387748, _n_(387747, "api", lambda: api), "add_resource"), _n_(387749, "User", lambda: User), "/users/<int:path_user_id>")
_l_(387751)
_c_(387755, _a_(387753, _n_(387752, "api", lambda: api), "add_resource"), _n_(387754, "UserList", lambda: UserList), "/users")
_l_(387756)

if _n_(387757, "__name__", lambda: __name__) == "__main__":
    _l_(387762)

    _c_(387760, _a_(387759, _n_(387758, "app", lambda: app), "run"), debug=True)
    _l_(387761)