# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67034884/typeerrorhash-must-be-unicode-or-bytes-not-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
    _l_(643411)

except ImportError:
    pass
try:
    from flask_mysqldb import MySQL
    _l_(643413)

except ImportError:
    pass
try:
    from wtforms import Form,StringField,TextAreaField,PasswordField,validators
    _l_(643415)

except ImportError:
    pass
try:
    from passlib.hash import sha256_crypt
    _l_(643417)

except ImportError:
    pass

class RegisterForm(_n_(643418, "Form", lambda: Form)):
    _l_(643449)

    name = _c_(643423, _n_(643419, "StringField", lambda: StringField), "Name Surname",validators=[_c_(643422, _a_(643421, _n_(643420, "validators", lambda: validators), "Length"), min=4,max=25)])
    _l_(643424)
    username = _c_(643429, _n_(643425, "StringField", lambda: StringField), "Username",validators=[_c_(643428, _a_(643427, _n_(643426, "validators", lambda: validators), "Length"), min=5,max=35)])
    _l_(643430)
    email = _c_(643435, _n_(643431, "StringField", lambda: StringField), "Email Adress",validators=[_c_(643434, _a_(643433, _n_(643432, "validators", lambda: validators), "Email"), message = "Please enter a valid email.")])
    _l_(643436)
    password = _c_(643444, _n_(643437, "PasswordField", lambda: PasswordField), "Password:",validators=[
        _c_(643440, _a_(643439, _n_(643438, "validators", lambda: validators), "DataRequired"), message = "Please enter an email."),
        _c_(643443, _a_(643442, _n_(643441, "validators", lambda: validators), "EqualTo"), fieldname="confirm",message = "Your password doesn't match")
    ])
    _l_(643445)
    confirm = _c_(643447, _n_(643446, "PasswordField", lambda: PasswordField), "Verify Password")
    _l_(643448)

class LoginForm(_n_(643450, "Form", lambda: Form)):
    _l_(643457)

    username =_c_(643452, _n_(643451, "StringField", lambda: StringField), "Username")
    _l_(643453)
    password =_c_(643455, _n_(643454, "PasswordField", lambda: PasswordField), "Password")
    _l_(643456)



app = _c_(643460, _n_(643458, "Flask", lambda: Flask), _n_(643459, "__name__", lambda: __name__)) #Flask objesi oluşturuyoruz.
_l_(643461) #Flask objesi oluşturuyoruz.
_n_(643462, "app", lambda: app).secret_key= "ybblog"
_l_(643463)

_a_(643465, _n_(643464, "app", lambda: app), "config")["MYSQL_HOST"] = "localhost"
_l_(643466)
_a_(643468, _n_(643467, "app", lambda: app), "config")["MYSQL_USER"] = "root"
_l_(643469)
_a_(643471, _n_(643470, "app", lambda: app), "config")["MYSQL_PASSWORD"] =""
_l_(643472)
_a_(643474, _n_(643473, "app", lambda: app), "config")["MYSQL_DB"] ="ybblog"
_l_(643475)
_a_(643477, _n_(643476, "app", lambda: app), "config")["MYSQL_CURSORCLASS"] = "DictCursor"
_l_(643478)

mysql = _c_(643481, _n_(643479, "MySQL", lambda: MySQL), _n_(643480, "app", lambda: app))
_l_(643482)

@_c_(643485, _a_(643484, _n_(643483, "app", lambda: app), "route"), "/")
def index():
    _l_(643489)

    aux = _c_(643487, _n_(643486, "render_template", lambda: render_template), "index.html")
    _l_(643488)
    return aux

@_c_(643492, _a_(643491, _n_(643490, "app", lambda: app), "route"), "/about")
def about():
    _l_(643496)

    aux = _c_(643494, _n_(643493, "render_template", lambda: render_template), "about.html")
    _l_(643495)
    return aux


@_c_(643499, _a_(643498, _n_(643497, "app", lambda: app), "route"), "/register",methods =["GET","POST"])    
def register():
    _l_(643569)

    form =_c_(643503, _n_(643500, "RegisterForm", lambda: RegisterForm), _a_(643502, _n_(643501, "request", lambda: request), "form"))
    _l_(643504)

    if _a_(643506, _n_(643505, "request", lambda: request), "method") == "POST" and _c_(643509, _a_(643508, _n_(643507, "form", lambda: form), "validate")):
        _l_(643565)

        name = _a_(643512, _a_(643511, _n_(643510, "form", lambda: form), "name"), "data") 
        _l_(643513) 
        username = _a_(643516, _a_(643515, _n_(643514, "form", lambda: form), "username"), "data")
        _l_(643517)
        email = _a_(643520, _a_(643519, _n_(643518, "form", lambda: form), "email"), "data") 
        _l_(643521) 
        password = _c_(643527, _a_(643523, _n_(643522, "sha256_crypt", lambda: sha256_crypt), "encrypt"), _a_(643526, _a_(643525, _n_(643524, "form", lambda: form), "password"), "data"))
        _l_(643528)
        cursor = _c_(643532, _a_(643531, _a_(643530, _n_(643529, "mysql", lambda: mysql), "connection"), "cursor"))
        _l_(643533)
        
        query = "Insert into users(name,email,username,password) VALUES(%s,%s,%s,%s)"
        _l_(643534)
        
        _c_(643542, _a_(643536, _n_(643535, "cursor", lambda: cursor), "execute"), _n_(643537, "query", lambda: query),(_n_(643538, "name", lambda: name),_n_(643539, "email", lambda: email),_n_(643540, "username", lambda: username),_n_(643541, "password", lambda: password)))
        _l_(643543)
        _c_(643547, _a_(643546, _a_(643545, _n_(643544, "mysql", lambda: mysql), "connection"), "commit"))
        _l_(643548)

        _c_(643551, _a_(643550, _n_(643549, "cursor", lambda: cursor), "close"))
        _l_(643552)
        
        _c_(643554, _n_(643553, "flash", lambda: flash), "Login is succesful.","success")
        _l_(643555)
        aux = _c_(643559, _n_(643556, "redirect", lambda: redirect), _c_(643558, _n_(643557, "url_for", lambda: url_for), "index"))
        _l_(643560)

        return aux
    else:
        aux = _c_(643563, _n_(643561, "render_template", lambda: render_template), "register.html",form = _n_(643562, "form", lambda: form))
        _l_(643564)
        return aux
    aux = _c_(643567, _n_(643566, "render_template", lambda: render_template), "login.html")
    _l_(643568)

    return aux


@_c_(643572, _a_(643571, _n_(643570, "app", lambda: app), "route"), "/login", methods=["GET","POST"])
def login():
    _l_(643643)

    form = _c_(643576, _n_(643573, "LoginForm", lambda: LoginForm), _a_(643575, _n_(643574, "request", lambda: request), "form"))
    _l_(643577)
    
    if _a_(643579, _n_(643578, "request", lambda: request), "method") == "POST" :
        _l_(643638)

        username = _a_(643582, _a_(643581, _n_(643580, "form", lambda: form), "username"), "data")
        _l_(643583)
        password_entered = _a_(643586, _a_(643585, _n_(643584, "form", lambda: form), "password"), "data")
        _l_(643587)

        cursor = _c_(643591, _a_(643590, _a_(643589, _n_(643588, "mysql", lambda: mysql), "connection"), "cursor"))
        _l_(643592)

        query = "Select * From users where username = %s"
        _l_(643593)
        result = _c_(643598, _a_(643595, _n_(643594, "cursor", lambda: cursor), "execute"), _n_(643596, "query", lambda: query),(_n_(643597, "username", lambda: username),))
        _l_(643599)

        if _n_(643600, "result", lambda: result) > 0:
            _l_(643637)

            data = _c_(643603, _a_(643602, _n_(643601, "cursor", lambda: cursor), "fetchone"))
            _l_(643604)
            real_password = _n_(643605, "data", lambda: data)["password"]
            _l_(643606)
            if _c_(643611, _a_(643608, _n_(643607, "sha256_crypt", lambda: sha256_crypt), "verify"), _n_(643609, "password_entered", lambda: password_entered),_n_(643610, "real_password", lambda: real_password)):
                _l_(643628)

                _c_(643613, _n_(643612, "flash", lambda: flash), "Login is succesful.","success")
                _l_(643614)
                aux = _c_(643618, _n_(643615, "redirect", lambda: redirect), _c_(643617, _n_(643616, "url_for", lambda: url_for), "index"))
                _l_(643619)
                return aux
            else:
                _c_(643621, _n_(643620, "flash", lambda: flash), "Wrong password.","danger")
                _l_(643622)
                aux = _c_(643626, _n_(643623, "redirect", lambda: redirect), _c_(643625, _n_(643624, "url_for", lambda: url_for), "login"))    
                _l_(643627)    
                return aux    

        else:
            _c_(643630, _n_(643629, "flash", lambda: flash), "There is no such user.","danger")
            _l_(643631)
            aux = _c_(643635, _n_(643632, "redirect", lambda: redirect), _c_(643634, _n_(643633, "url_for", lambda: url_for), "login"))
            _l_(643636)
            return aux
    aux = _c_(643641, _n_(643639, "render_template", lambda: render_template), "login.html",form=_n_(643640, "form", lambda: form))    
    _l_(643642)    


    return aux    



if _n_(643644, "__name__", lambda: __name__) == "__main__":
    _l_(643649)

    _c_(643647, _a_(643646, _n_(643645, "app", lambda: app), "run"), debug=True)
    _l_(643648)