# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47901868/typeerror-restaurantmenu-missing-1-required-positional-argument-restaurant
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask,render_template
    _l_(618927)

except ImportError:
    pass
try:
    from sqlalchemy import create_engine
    _l_(618929)

except ImportError:
    pass
try:
    from sqlalchemy.orm import sessionmaker
    _l_(618931)

except ImportError:
    pass
try:
    from database_setup import Base, Restaurant, MenuItem
    _l_(618933)

except ImportError:
    pass

app = _c_(618936, _n_(618934, "Flask", lambda: Flask), _n_(618935, "__name__", lambda: __name__))
_l_(618937)

engine = _c_(618939, _n_(618938, "create_engine", lambda: create_engine), 'sqlite:///restaurantmenu.db')
_l_(618940)
_a_(618942, _n_(618941, "Base", lambda: Base), "metadata").bind = _n_(618943, "engine", lambda: engine)
_l_(618944)

DBSession = _c_(618947, _n_(618945, "sessionmaker", lambda: sessionmaker), bind=_n_(618946, "engine", lambda: engine))
_l_(618948)
session = _c_(618950, _n_(618949, "DBSession", lambda: DBSession))
_l_(618951)


@_c_(618954, _a_(618953, _n_(618952, "app", lambda: app), "route"), '/')
@_c_(618957, _a_(618956, _n_(618955, "app", lambda: app), "route"), '/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    _l_(618980)

    restaurant = _c_(618964, _a_(618962, _c_(618961, _a_(618959, _n_(618958, "session", lambda: session), "query"), _n_(618960, "Restaurant", lambda: Restaurant)), "filter_by"), id=_n_(618963, "restaurant_id", lambda: restaurant_id))
    _l_(618965)
    items = _c_(618973, _a_(618970, _c_(618969, _a_(618967, _n_(618966, "session", lambda: session), "query"), _n_(618968, "MenuItem", lambda: MenuItem)), "filter_by"), restaurant_id=_a_(618972, _n_(618971, "restaurant", lambda: restaurant), "id"))
    _l_(618974)
    aux = _c_(618978, _n_(618975, "render_template", lambda: render_template), 'menu.html',restaurant=_n_(618976, "restaurant", lambda: restaurant),items=_n_(618977, "items", lambda: items))
    _l_(618979)

    return aux

# Task 1: Create route for newMenuItem function here


@_c_(618983, _a_(618982, _n_(618981, "app", lambda: app), "route"), '/restaurant/<int:restaurant_id>/new/')
def newMenuItem(restaurant_id):
    _l_(618985)

    aux = "page to create a new menu item. Task 1 complete!"
    _l_(618984)
    return aux

# Task 2: Create route for editMenuItem function here


@_c_(618988, _a_(618987, _n_(618986, "app", lambda: app), "route"), '/restaurant/<int:restaurant_id>/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    _l_(618990)

    aux = "page to edit a menu item. Task 2 complete!"
    _l_(618989)
    return aux

# Task 3: Create a route for deleteMenuItem function here


@_c_(618993, _a_(618992, _n_(618991, "app", lambda: app), "route"), '/restaurant/<int:restaurant_id>/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    _l_(618995)

    aux = "page to delete a menu item. Task 3 complete!"
    _l_(618994)
    return aux


if _n_(618996, "__name__", lambda: __name__) == '__main__':
    _l_(619003)

    _n_(618997, "app", lambda: app).debug = True
    _l_(618998)
    _c_(619001, _a_(619000, _n_(618999, "app", lambda: app), "run"), host='0.0.0.0', port=5000)
    _l_(619002)