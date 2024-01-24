# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60127532/no-matter-what-i-do-i-keep-getting-attributeerror-str-object-has-no-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(526221, _a_(526220, _n_(526219, "portfolio_app", lambda: portfolio_app), "route"), '/postContactForm', methods=['POST'])
def postContactForm():
    _l_(526252)

    #Gets the data sent from frontend  
    ajax_data = _c_(526228, _a_(526223, _n_(526222, "json", lambda: json), "load"), _c_(526227, _a_(526226, _a_(526225, _n_(526224, "request", lambda: request), "data"), "decode"))) 
    _l_(526229) 
    _c_(526232, _n_(526230, "print", lambda: print), _n_(526231, "ajax_data", lambda: ajax_data))
    _l_(526233)

    # Connect to DB
    db = _c_(526235, _n_(526234, "connectToDB", lambda: connectToDB))
    _l_(526236)

    #Choose collection name
    contact_data = _a_(526238, _n_(526237, "db", lambda: db), "contact_data")
    _l_(526239)
    _c_(526242, _n_(526240, "print", lambda: print), _n_(526241, "contact_data", lambda: contact_data))
    _l_(526243)

    #Inserts data into database
    _c_(526247, _a_(526245, _n_(526244, "contact_data", lambda: contact_data), "insert_one"), _n_(526246, "ajax_data", lambda: ajax_data))
    _l_(526248)
    aux = _c_(526250, _n_(526249, "jsonify", lambda: jsonify), {'Success it worked'})
    _l_(526251)

    #Returns data to ajax
    return aux