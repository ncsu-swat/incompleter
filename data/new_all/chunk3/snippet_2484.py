# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75966522/attributeerror-function-object-has-no-attribute-args
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask, request
    _l_(543420)

except ImportError:
    pass
try:
    from flask import Flask, render_template
    _l_(543422)

except ImportError:
    pass
try:
    from flask_paginate import Pagination, get_page_parameter
    _l_(543424)

except ImportError:
    pass
try:
    import mysql.connector
    _l_(543426)

except ImportError:
    pass

app = _c_(543429, _n_(543427, "Flask", lambda: Flask), _n_(543428, "__name__", lambda: __name__))
_l_(543430)

_a_(543432, _n_(543431, "app", lambda: app), "config")['SECRET_KEY'] = 'your_secret_key'
_l_(543433)
_a_(543435, _n_(543434, "app", lambda: app), "config")['MYSQL_USER'] = 'root'
_l_(543436)
_a_(543438, _n_(543437, "app", lambda: app), "config")['MYSQL_PASSWORD'] = ''
_l_(543439)
_a_(543441, _n_(543440, "app", lambda: app), "config")['MYSQL_HOST'] = 'localhost'
_l_(543442)
_a_(543444, _n_(543443, "app", lambda: app), "config")['MYSQL_DB'] = 'test'
_l_(543445)

db = _c_(543456, _a_(543447, _a_(543446, mysql, "connector"), "connect"), user=_a_(543449, _n_(543448, "app", lambda: app), "config")['MYSQL_USER'], password=_a_(543451, _n_(543450, "app", lambda: app), "config")['MYSQL_PASSWORD'],
                             host=_a_(543453, _n_(543452, "app", lambda: app), "config")['MYSQL_HOST'], database=_a_(543455, _n_(543454, "app", lambda: app), "config")['MYSQL_DB'])
_l_(543457)
cursor = _c_(543460, _a_(543459, _n_(543458, "db", lambda: db), "cursor"))
_l_(543461)

@_c_(543464, _a_(543463, _n_(543462, "app", lambda: app), "route"), '/')
def thumbnails():
    _l_(543503)

    # Retrieve the image URLs from the database
    _c_(543467, _a_(543466, _n_(543465, "cursor", lambda: cursor), "execute"), 'SELECT * FROM sheet1')
    _l_(543468)
    rows = _c_(543471, _a_(543470, _n_(543469, "cursor", lambda: cursor), "fetchall"))
    _l_(543472)
    
   
    
    # Paginate the image URLs
    page = _c_(543477, _n_(543473, "int", lambda: int), _a_(543476, _a_(543475, _n_(543474, "request", lambda: request), "args"), "get")['page']) if 'page' in _a_(543479, _n_(543478, "request", lambda: request), "args") else 1
    _l_(543480)
    per_page = 12
    _l_(543481)
    offset = (_n_(543482, "page", lambda: page) - 1) * _n_(543483, "per_page", lambda: per_page)
    _l_(543484)
    pagination = _c_(543491, _n_(543485, "Pagination", lambda: Pagination), page=_n_(543486, "page", lambda: page), per_page=_n_(543487, "per_page", lambda: per_page), total=_c_(543490, _n_(543488, "len", lambda: len), _n_(543489, "image_urls", lambda: image_urls)), css_framework='bootstrap4')
    _l_(543492)
    image_urls = _n_(543493, "image_urls", lambda: image_urls)[_n_(543494, "offset", lambda: offset):_n_(543495, "offset", lambda: offset)+_n_(543496, "per_page", lambda: per_page)]
    _l_(543497)
    aux = _c_(543501, _n_(543498, "render_template", lambda: render_template), 'index.html', rows=_n_(543499, "rows", lambda: rows),pagination=_n_(543500, "pagination", lambda: pagination))
    _l_(543502)
    
 
    
    # Pass the image URLs and pagination object to the template
    return aux



if _n_(543504, "__name__", lambda: __name__) == "__main__":
    _l_(543509)

    _c_(543507, _a_(543506, _n_(543505, "app", lambda: app), "run"), debug=True,port=5000)
    _l_(543508)