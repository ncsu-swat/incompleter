# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62856777/deploying-flask-app-with-postgresql-and-getting-attributeerror-nonetype-objec
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
app = _c_(698447, _n_(698445, "Flask", lambda: Flask), _n_(698446, "__name__", lambda: __name__))
_l_(698448)

# Ensure responses aren't cached
@_a_(698450, _n_(698449, "app", lambda: app), "after_request")
def after_request(response):
    _l_(698462)

    _a_(698452, _n_(698451, "response", lambda: response), "headers")["Cache-Control"] = "no-cache, no-store, must-revalidate"
    _l_(698453)
    _a_(698455, _n_(698454, "response", lambda: response), "headers")["Expires"] = 0
    _l_(698456)
    _a_(698458, _n_(698457, "response", lambda: response), "headers")["Pragma"] = "no-cache"
    _l_(698459)
    aux = _n_(698460, "response", lambda: response)
    _l_(698461)
    return aux


##where to find the database and initialize SQLAlchemy
_a_(698464, _n_(698463, "app", lambda: app), "config")['SQLALCHEMY_DATABASE_URI'] = _c_(698468, _a_(698467, _a_(698466, _n_(698465, "os", lambda: os), "environ"), "get"), 'DATABASE_URL')
_l_(698469)
_a_(698471, _n_(698470, "app", lambda: app), "config")['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
_l_(698472)
db = _c_(698475, _n_(698473, "SQLAlchemy", lambda: SQLAlchemy), _n_(698474, "app", lambda: app)) 
_l_(698476) 


##option to tell SQLALchemy that for every model it should just 
#look at the columns that already exist in the table. This is called reflecting
_c_(698483, _a_(698480, _a_(698479, _a_(698478, _n_(698477, "db", lambda: db), "Model"), "metadata"), "reflect"), _a_(698482, _n_(698481, "db", lambda: db), "engine"))
_l_(698484)

class Congress(_a_(698486, _n_(698485, "db", lambda: db), "Model")):
    _l_(698495)

    __tablename__ = 'sen'
    _l_(698487)
    __table_args__ = { 'extend_existing': True }
    _l_(698488)
    id = _c_(698493, _a_(698490, _n_(698489, "db", lambda: db), "Column"), _a_(698492, _n_(698491, "db", lambda: db), "Text"), primary_key=True) 
    _l_(698494) 