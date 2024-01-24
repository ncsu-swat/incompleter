# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67034884/typeerrorhash-must-be-unicode-or-bytes-not-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
    _l_(580554)

except ImportError:
    pass
try:
    from flask_mysqldb import MySQL
    _l_(580556)

except ImportError:
    pass
try:
    from wtforms import Form,StringField,TextAreaField,PasswordField,validators
    _l_(580558)

except ImportError:
    pass
try:
    from passlib.hash import sha256_crypt
    _l_(580560)

except ImportError:
    pass

class RegisterForm(_n_(580561, "Form", lambda: Form)):
    _l_(580592)

    name = _c_(580566, _n_(580562, "StringField", lambda: StringField), "Name Surname",validators=[_c_(580565, _a_(580564, _n_(580563, "validators", lambda: validators), "Length"), min=4,max=25)])
    _l_(580567)
    username = _c_(580572, _n_(580568, "StringField", lambda: StringField), "Username",validators=[_c_(580571, _a_(580570, _n_(580569, "validators", lambda: validators), "Length"), min=5,max=35)])
    _l_(580573)
    email = _c_(580578, _n_(580574, "StringField", lambda: StringField), "Email Adress",validators=[_c_(580577, _a_(580576, _n_(580575, "validators", lambda: validators), "Email"), message = "Please enter a valid email.")])
    _l_(580579)
    password = _c_(580587, _n_(580580, "PasswordField", lambda: PasswordField), "Password:",validators=[
        _c_(580583, _a_(580582, _n_(580581, "validators", lambda: validators), "DataRequired"), message = "Please enter an email."),
        _c_(580586, _a_(580585, _n_(580584, "validators", lambda: validators), "EqualTo"), fieldname="confirm",message = "Your password doesn't match")
    ])
    _l_(580588)
    confirm = _c_(580590, _n_(580589, "PasswordField", lambda: PasswordField), "Verify Password")
    _l_(580591)

class LoginForm(_n_(580593, "Form", lambda: Form)):
    _l_(580600)

    username =_c_(580595, _n_(580594, "StringField", lambda: StringField), "Username")
    _l_(580596)
    password =_c_(580598, _n_(580597, "PasswordField", lambda: PasswordField), "Password")
    _l_(580599)



app = _c_(580603, _n_(580601, "Flask", lambda: Flask), _n_(580602, "__name__", lambda: __name__)) #Flask objesi oluşturuyoruz.
_l_(580604) #Flask objesi oluşturuyoruz.
_n_(580605, "app", lambda: app).secret_key= "ybblog"
_l_(580606)

_a_(580608, _n_(580607, "app", lambda: app), "config")["MYSQL_HOST"] = "localhost"
_l_(580609)
_a_(580611, _n_(580610, "app", lambda: app), "config")["MYSQL_USER"] = "root"
_l_(580612)
_a_(580614, _n_(580613, "app", lambda: app), "config")["MYSQL_PASSWORD"] =""
_l_(580615)
_a_(580617, _n_(580616, "app", lambda: app), "config")["MYSQL_DB"] ="ybblog"
_l_(580618)
_a_(580620, _n_(580619, "app", lambda: app), "config")["MYSQL_CURSORCLASS"] = "DictCursor"
_l_(580621)

mysql = _c_(580624, _n_(580622, "MySQL", lambda: MySQL), _n_(580623, "app", lambda: app))
_l_(580625)

@_c_(580628, _a_(580627, _n_(580626, "app", lambda: app), "route"), "/")
def index():
    _l_(580632)

    aux = _c_(580630, _n_(580629, "render_template", lambda: render_template), "index.html")
    _l_(580631)
    return aux

@_c_(580635, _a_(580634, _n_(580633, "app", lambda: app), "route"), "/about")
def about():
    _l_(580639)

    aux = _c_(580637, _n_(580636, "render_template", lambda: render_template), "about.html")
    _l_(580638)
    return aux


@_c_(580642, _a_(580641, _n_(580640, "app", lambda: app), "route"), "/register",methods =["GET","POST"])    
def register():
    _l_(580712)

    form =_c_(580646, _n_(580643, "RegisterForm", lambda: RegisterForm), _a_(580645, _n_(580644, "request", lambda: request), "form"))
    _l_(580647)

    if _a_(580649, _n_(580648, "request", lambda: request), "method") == "POST" and _c_(580652, _a_(580651, _n_(580650, "form", lambda: form), "validate")):
        _l_(580708)

        name = _a_(580655, _a_(580654, _n_(580653, "form", lambda: form), "name"), "data") 
        _l_(580656) 
        username = _a_(580659, _a_(580658, _n_(580657, "form", lambda: form), "username"), "data")
        _l_(580660)
        email = _a_(580663, _a_(580662, _n_(580661, "form", lambda: form), "email"), "data") 
        _l_(580664) 
        password = _c_(580670, _a_(580666, _n_(580665, "sha256_crypt", lambda: sha256_crypt), "encrypt"), _a_(580669, _a_(580668, _n_(580667, "form", lambda: form), "password"), "data"))
        _l_(580671)
        cursor = _c_(580675, _a_(580674, _a_(580673, _n_(580672, "mysql", lambda: mysql), "connection"), "cursor"))
        _l_(580676)
        
        query = "Insert into users(name,email,username,password) VALUES(%s,%s,%s,%s)"
        _l_(580677)
        
        _c_(580685, _a_(580679, _n_(580678, "cursor", lambda: cursor), "execute"), _n_(580680, "query", lambda: query),(_n_(580681, "name", lambda: name),_n_(580682, "email", lambda: email),_n_(580683, "username", lambda: username),_n_(580684, "password", lambda: password)))
        _l_(580686)
        _c_(580690, _a_(580689, _a_(580688, _n_(580687, "mysql", lambda: mysql), "connection"), "commit"))
        _l_(580691)

        _c_(580694, _a_(580693, _n_(580692, "cursor", lambda: cursor), "close"))
        _l_(580695)
        
        _c_(580697, _n_(580696, "flash", lambda: flash), "Login is succesful.","success")
        _l_(580698)
        aux = _c_(580702, _n_(580699, "redirect", lambda: redirect), _c_(580701, _n_(580700, "url_for", lambda: url_for), "index"))
        _l_(580703)

        return aux
    else:
        aux = _c_(580706, _n_(580704, "render_template", lambda: render_template), "register.html",form = _n_(580705, "form", lambda: form))
        _l_(580707)
        return aux
    aux = _c_(580710, _n_(580709, "render_template", lambda: render_template), "login.html")
    _l_(580711)

    return aux


@_c_(580715, _a_(580714, _n_(580713, "app", lambda: app), "route"), "/login", methods=["GET","POST"])
def login():
    _l_(580786)

    form = _c_(580719, _n_(580716, "LoginForm", lambda: LoginForm), _a_(580718, _n_(580717, "request", lambda: request), "form"))
    _l_(580720)
    
    if _a_(580722, _n_(580721, "request", lambda: request), "method") == "POST" :
        _l_(580781)

        username = _a_(580725, _a_(580724, _n_(580723, "form", lambda: form), "username"), "data")
        _l_(580726)
        password_entered = _a_(580729, _a_(580728, _n_(580727, "form", lambda: form), "password"), "data")
        _l_(580730)

        cursor = _c_(580734, _a_(580733, _a_(580732, _n_(580731, "mysql", lambda: mysql), "connection"), "cursor"))
        _l_(580735)

        query = "Select * From users where username = %s"
        _l_(580736)
        result = _c_(580741, _a_(580738, _n_(580737, "cursor", lambda: cursor), "execute"), _n_(580739, "query", lambda: query),(_n_(580740, "username", lambda: username),))
        _l_(580742)

        if _n_(580743, "result", lambda: result) > 0:
            _l_(580780)

            data = _c_(580746, _a_(580745, _n_(580744, "cursor", lambda: cursor), "fetchone"))
            _l_(580747)
            real_password = _n_(580748, "data", lambda: data)["password"]
            _l_(580749)
            if _c_(580754, _a_(580751, _n_(580750, "sha256_crypt", lambda: sha256_crypt), "verify"), _n_(580752, "password_entered", lambda: password_entered),_n_(580753, "real_password", lambda: real_password)):
                _l_(580771)

                _c_(580756, _n_(580755, "flash", lambda: flash), "Login is succesful.","success")
                _l_(580757)
                aux = _c_(580761, _n_(580758, "redirect", lambda: redirect), _c_(580760, _n_(580759, "url_for", lambda: url_for), "index"))
                _l_(580762)
                return aux
            else:
                _c_(580764, _n_(580763, "flash", lambda: flash), "Wrong password.","danger")
                _l_(580765)
                aux = _c_(580769, _n_(580766, "redirect", lambda: redirect), _c_(580768, _n_(580767, "url_for", lambda: url_for), "login"))    
                _l_(580770)    
                return aux    

        else:
            _c_(580773, _n_(580772, "flash", lambda: flash), "There is no such user.","danger")
            _l_(580774)
            aux = _c_(580778, _n_(580775, "redirect", lambda: redirect), _c_(580777, _n_(580776, "url_for", lambda: url_for), "login"))
            _l_(580779)
            return aux
    aux = _c_(580784, _n_(580782, "render_template", lambda: render_template), "login.html",form=_n_(580783, "form", lambda: form))    
    _l_(580785)    


    return aux    



if _n_(580787, "__name__", lambda: __name__) == "__main__":
    _l_(580792)

    _c_(580790, _a_(580789, _n_(580788, "app", lambda: app), "run"), debug=True)
    _l_(580791)