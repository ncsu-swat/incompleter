# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74107311/attributeerror-legacycursorresult-object-has-no-attribute-user-name
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from dataclasses import fields
    _l_(629098)

except ImportError:
    pass
try:
    import datetime
    _l_(629100)

except ImportError:
    pass
try:
    import json
    _l_(629102)

except ImportError:
    pass
try:
    from typing_extensions import Required
    _l_(629104)

except ImportError:
    pass
try:
    from unittest import result
    _l_(629106)

except ImportError:
    pass
try:
    from sqlalchemy import DateTime
    _l_(629108)

except ImportError:
    pass
try:
    from email.policy import default, strict
    _l_(629110)

except ImportError:
    pass
try:
    from flask import Flask, jsonify, request, make_response
    _l_(629112)

except ImportError:
    pass
try:
    from flask_sqlalchemy import SQLAlchemy
    _l_(629114)

except ImportError:
    pass
try:
    from flask_migrate import Migrate
    _l_(629116)

except ImportError:
    pass
try:
    from sqlalchemy.sql import text, func
    _l_(629118)

except ImportError:
    pass
try:
    from flask_marshmallow import Marshmallow
    _l_(629120)

except ImportError:
    pass
try:
    from marshmallow import Schema, fields, validates, ValidationError, validate
    _l_(629122)

except ImportError:
    pass
try:
    from sqlalchemy.sql import select, insert, bindparam
    _l_(629124)

except ImportError:
    pass
try:
    from sqlalchemy.dialects.postgresql import UUID
    _l_(629126)

except ImportError:
    pass
try:
    import uuid
    _l_(629128)

except ImportError:
    pass
try:
    from werkzeug.security import generate_password_hash,check_password_hash
    _l_(629130)

except ImportError:
    pass
try:
    from sqlalchemy import create_engine
    _l_(629132)

except ImportError:
    pass
try:
    import logging
    _l_(629134)

except ImportError:
    pass
try:
    from functools import wraps
    _l_(629136)

except ImportError:
    pass
try:
    import jwt
    _l_(629138)

except ImportError:
    pass

engine = _c_(629140, _n_(629139, "create_engine", lambda: create_engine), 'mysql://root:admin@172.17.0.2:3306/flask')
_l_(629141)


app = _c_(629144, _n_(629142, "Flask", lambda: Flask), _n_(629143, "_name_", lambda: _name_))
_l_(629145)

_a_(629147, _n_(629146, "app", lambda: app), "config")['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@172.17.0.2:3306/flask'
_l_(629148)
_a_(629150, _n_(629149, "app", lambda: app), "config")['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
_l_(629151)
# app.config['SECRET_KEY'] = 'thisissecret'
_a_(629153, _n_(629152, "app", lambda: app), "config")['SECRET_KEY'] = 'super-secret' 
_l_(629154) 
db = _c_(629157, _n_(629155, "SQLAlchemy", lambda: SQLAlchemy), _n_(629156, "app", lambda: app))
_l_(629158)
ma= _c_(629161, _n_(629159, "Marshmallow", lambda: Marshmallow), _n_(629160, "app", lambda: app))
_l_(629162)
migrate = _c_(629166, _n_(629163, "Migrate", lambda: Migrate), _n_(629164, "app", lambda: app), _n_(629165, "db", lambda: db))
_l_(629167)
# jwt = JWTManager(app)









class User(_a_(629169, _n_(629168, "db", lambda: db), "Model")):
    _l_(629236)

    id = _c_(629174, _a_(629171, _n_(629170, "db", lambda: db), "Column"), _a_(629173, _n_(629172, "db", lambda: db), "Integer"), primary_key=True)
    _l_(629175)
    user_name = _c_(629181, _a_(629177, _n_(629176, "db", lambda: db), "Column"), _c_(629180, _a_(629179, _n_(629178, "db", lambda: db), "String"), 100), nullable=False)
    _l_(629182)
    password = _c_(629188, _a_(629184, _n_(629183, "db", lambda: db), "Column"), _c_(629187, _a_(629186, _n_(629185, "db", lambda: db), "String"), 100), nullable=False)
    _l_(629189)
    email_address = _c_(629195, _a_(629191, _n_(629190, "db", lambda: db), "Column"), _c_(629194, _a_(629193, _n_(629192, "db", lambda: db), "String"), 80), unique=True, nullable=False)
    _l_(629196)
    dob = _c_(629201, _a_(629198, _n_(629197, "db", lambda: db), "Column"), _a_(629200, _n_(629199, "db", lambda: db), "DateTime"), nullable=True)
    _l_(629202)
    address = _c_(629208, _a_(629204, _n_(629203, "db", lambda: db), "Column"), _c_(629207, _a_(629206, _n_(629205, "db", lambda: db), "String"), 200))
    _l_(629209)
    uid = _c_(629215, _a_(629211, _n_(629210, "db", lambda: db), "Column"), _c_(629214, _a_(629213, _n_(629212, "db", lambda: db), "Text"), length=16), nullable = False)
    _l_(629216)

    def _init_(self, user_name, password, email_address, dob, address, uid):
        _l_(629235)

        _n_(629217, "self", lambda: self).user_name = _n_(629218, "user_name", lambda: user_name)
        _l_(629219)
        _n_(629220, "self", lambda: self).password = _n_(629221, "password", lambda: password)
        _l_(629222)
        _n_(629223, "self", lambda: self).email_address = _n_(629224, "email_address", lambda: email_address)
        _l_(629225)
        _n_(629226, "self", lambda: self).dob = _n_(629227, "dob", lambda: dob)
        _l_(629228)
        _n_(629229, "self", lambda: self).address = _n_(629230, "address", lambda: address)
        _l_(629231)
        _n_(629232, "self", lambda: self).uid = _n_(629233, "uid", lambda: uid)
        _l_(629234)

# User Schema
class UserSchema(_n_(629237, "Schema", lambda: Schema)):
    _l_(629287)

    _c_(629239, _n_(629238, "print", lambda: print), "Scehma")
    _l_(629240)

    user_name = _c_(629246, _a_(629242, _n_(629241, "fields", lambda: fields), "String"), required=True, validate=_c_(629245, _a_(629244, _n_(629243, "validate", lambda: validate), "Length"), min=5))
    _l_(629247)
    password = _c_(629250, _a_(629249, _n_(629248, "fields", lambda: fields), "String"))
    _l_(629251)
    # email_address = fields.String(required=True, error_messages={"required": " email_address is required. "})
    email_address = _c_(629254, _a_(629253, _n_(629252, "fields", lambda: fields), "String"))
    _l_(629255)
    dob = _c_(629258, _a_(629257, _n_(629256, "fields", lambda: fields), "DateTime"))
    _l_(629259)
    address = _c_(629262, _a_(629261, _n_(629260, "fields", lambda: fields), "String"))
    _l_(629263)
    uid = _c_(629266, _a_(629265, _n_(629264, "fields", lambda: fields), "UUID"), error_messages={'null': 'Sorry, Id field cannot be null', 'invalid_uuid': 'Sorry, Id field must be a valid UUID'})
    _l_(629267)

    _c_(629269, _n_(629268, "print", lambda: print), "access")
    _l_(629270)

    @_c_(629272, _n_(629271, "validates", lambda: validates), 'dob')
    def is_not_in_future(self,value):
        _l_(629284)

        """'value' is the datetime parsed from time_created by marshmallow"""
        now = _c_(629276, _a_(629275, _a_(629274, _n_(629273, "datetime", lambda: datetime), "datetime"), "now"))
        _l_(629277)
        if _n_(629278, "value", lambda: value) > _n_(629279, "now", lambda: now):
            _l_(629283)

            raise _c_(629281, _n_(629280, "ValidationError", lambda: ValidationError), "Can't create notes in the future!")
            _l_(629282)

    class Meta:
        _l_(629286)

        # Fields to show when sending data
        fields = ('id','user_name', 'password', 'email_address', 'dob', 'address', 'uid')   
        _l_(629285)   


#init Schema

user_schema = _c_(629289, _n_(629288, "UserSchema", lambda: UserSchema))
_l_(629290)
users_scehma = _c_(629292, _n_(629291, "UserSchema", lambda: UserSchema), many=True)
_l_(629293)

@_c_(629296, _a_(629295, _n_(629294, "app", lambda: app), "route"), '/login', methods=['POST'])
def login():
    _l_(629388)

    # print("login") 
    # # request_data= user_schema.load(request.get_json()) 
    request_data = _c_(629299, _a_(629298, _n_(629297, "request", lambda: request), "get_json"))
    _l_(629300)
    user_name=_n_(629301, "request_data", lambda: request_data)['user_name']
    _l_(629302)
    password=_n_(629303, "request_data", lambda: request_data)['password']
    _l_(629304)
    # conn = engine.connect()
    # data=conn.execute("""SELECT user_name, password, uid FROM user WHERE user_name = user_name""",{"user_name": user_name})
    # user = data.mappings().all()
    # print(user)
    #   return jsonify({'Message':'login user'})

    auth= _c_(629310, _a_(629306, _n_(629305, "user_schema", lambda: user_schema), "load"), _c_(629309, _a_(629308, _n_(629307, "request", lambda: request), "get_json")))
    _l_(629311)
    if not _n_(629312, "auth", lambda: auth) or not _c_(629315, _a_(629314, _n_(629313, "auth", lambda: auth), "get"), 'user_name') or not _c_(629318, _a_(629317, _n_(629316, "auth", lambda: auth), "get"), 'password'):
        _l_(629322)

        aux = _c_(629320, _n_(629319, "make_response", lambda: make_response), 'Could not verify!', 401, {'WWW-Authenticate': 'Basic-realm= "Login required!"'})
        _l_(629321)
        return aux

    conn = _c_(629325, _a_(629324, _n_(629323, "engine", lambda: engine), "connect"))
    _l_(629326)
    # sql= text(f"SELECT id, user_name, email_address, dob, uid FROM user WHERE user_name = '{auth['user_name']}' and password = '{auth['password']}'")
    result = _c_(629333, _a_(629328, _n_(629327, "conn", lambda: conn), "execute"), _c_(629330, _n_(629329, "text", lambda: text), "SELECT id, user_name, email_address, dob, uid FROM user WHERE user_name = :user_name and password = :password"), [{"user_name": _n_(629331, "user_name", lambda: user_name), "password": _n_(629332, "password", lambda: password)}],)
    _l_(629334)
    _c_(629339, _n_(629335, "print", lambda: print), _c_(629338, _a_(629337, _n_(629336, "result", lambda: result), "all")))
    _l_(629340)
    for row in _n_(629341, "result", lambda: result):
        _l_(629355)

        _c_(629353, _n_(629342, "print", lambda: print), f"id: {_a_(629344, _n_(629343, 'row', lambda: row), 'id')}  user_name: {_a_(629346, _n_(629345, 'row', lambda: row), 'user_name')} email_address: {_a_(629348, _n_(629347, 'row', lambda: row), 'email_address')} dob: {_a_(629350, _n_(629349, 'row', lambda: row), 'dob')} uid: {_a_(629352, _n_(629351, 'row', lambda: row), 'uid')}")
        _l_(629354)
    # rows= conn.execute(sql)
    # for result in rows:
    #     print(f"result : {result} ")
    

   
    
    if _n_(629356, "user_name", lambda: user_name) != _a_(629358, _n_(629357, "result", lambda: result), "user_name")  :
        _l_(629362)

        aux = _c_(629360, _n_(629359, "make_response", lambda: make_response), 'Could not verify user, Please signup!', 401, {'WWW-Authenticate': 'Basic-realm= "No user found!"'})
        _l_(629361)
        return aux

    if _c_(629369, _n_(629363, "check_password_hash", lambda: check_password_hash), _a_(629365, _n_(629364, "result", lambda: result), "password"), _c_(629368, _a_(629367, _n_(629366, "auth", lambda: auth), "get"), 'password')):
        _l_(629384)

        token = _c_(629376, _a_(629371, _n_(629370, "jwt", lambda: jwt), "encode"), {'uid': _a_(629373, _n_(629372, "result", lambda: result), "uid")}, _a_(629375, _n_(629374, "app", lambda: app), "config")['SECRET_KEY'], 'HS256')
        _l_(629377)
        aux = _c_(629382, _n_(629378, "make_response", lambda: make_response), _c_(629381, _n_(629379, "jsonify", lambda: jsonify), {'token': _n_(629380, "token", lambda: token)}), 201)
        _l_(629383)
        return aux
    aux = _c_(629386, _n_(629385, "make_response", lambda: make_response), 'Could not verify password!', 403, {'WWW-Authenticate': 'Basic-realm= "Wrong Password!"'})
    _l_(629387)

    return aux


if _n_(629389, "_name_", lambda: _name_) == '_main_':
    _l_(629394)

    _c_(629392, _a_(629391, _n_(629390, "app", lambda: app), "run"), debug=True)
    _l_(629393)