# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/28112952/attributeerror-tuple-object-has-no-attribute-encode-when-inserting-data-usi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import mysql.connector
    _l_(448886)

except ImportError:
    pass

# ...

# Connect to MySQL Database and send user_input data to 'user' TABLE.
cnx = _c_(448889, _a_(448888, _a_(448887, mysql, "connector"), "connect"), user='root', password='ash123', host='localhost', database='user_data_db')
_l_(448890)
cursor = _c_(448893, _a_(448892, _n_(448891, "cnx", lambda: cnx), "cursor"))
_l_(448894)

query = ("INSERT INTO user (user_id, first_name, last_name, age, postcode,  email_address)"
         "VALUES (%s, %s, %s, %s, %s, %s)", (_n_(448895, "user_id", lambda: user_id), _n_(448896, "firstname", lambda: firstname), _n_(448897, "lastname", lambda: lastname), _n_(448898, "age", lambda: age), _n_(448899, "postcode", lambda: postcode), _n_(448900, "email", lambda: email))) 
_l_(448901) 

_c_(448905, _a_(448903, _n_(448902, "cursor", lambda: cursor), "execute"), _n_(448904, "query", lambda: query))
_l_(448906)
_c_(448908, _n_(448907, "print", lambda: print), "Executed Successfully")
_l_(448909)

_c_(448912, _a_(448911, _n_(448910, "cursor", lambda: cursor), "close"))
_l_(448913)
_c_(448916, _a_(448915, _n_(448914, "cnx", lambda: cnx), "close"))
_l_(448917)