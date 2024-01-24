# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55113041/attributeerror-module-flask-app-has-no-attribute-route
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask, render_template, redirect, url_for, request, session, flash, app, Blueprint, jsonify
    _l_(449170)

except ImportError:
    pass

@_c_(449173, _a_(449172, _n_(449171, "app", lambda: app), "route"), '/autocomplete',methods=['GET'])
def autocomplete():
    _l_(449190)

    database='backbone_test'
    _l_(449174)
    db=_n_(449175, "client", lambda: client)[_n_(449176, "database", lambda: database)]
    _l_(449177)
    all_names=_c_(449183, _n_(449178, "list", lambda: list), _c_(449182, _a_(449181, _a_(449180, _n_(449179, "db", lambda: db), "ids"), "find"), {},{"current_name":1,"_id":0}))
    _l_(449184)
    aux = _c_(449188, _a_(449186, _n_(449185, "json", lambda: json), "dumps"), _n_(449187, "all_names", lambda: all_names)) 
    _l_(449189) 
    return aux 