# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51391849/typeerror-resultproxy-object-does-not-support-indexing-when-trying-to-store-u
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(385452, _a_(385451, _n_(385450, "app", lambda: app), "route"), "/signin",methods=["GET","POST"])
def signin():
    _l_(385501)

    # LOG A USER IN
    #forget any user_id
    _c_(385455, _a_(385454, _n_(385453, "session", lambda: session), "clear"))
    _l_(385456)

    if _a_(385458, _n_(385457, "request", lambda: request), "method") == "GET":
        _l_(385500)

        aux = _c_(385460, _n_(385459, "render_template", lambda: render_template), "login.html")
        _l_(385461)
        return aux

    else:
        user_name = _c_(385465, _a_(385464, _a_(385463, _n_(385462, "request", lambda: request), "form"), "get"), "username")
        _l_(385466)

        # ensure username is provided
        if not _c_(385470, _a_(385469, _a_(385468, _n_(385467, "request", lambda: request), "form"), "get"), "username"):
            _l_(385478)

            aux = "must provide username"
            _l_(385471)
            return aux

        # ensure password is provided
        elif not _c_(385475, _a_(385474, _a_(385473, _n_(385472, "request", lambda: request), "form"), "get"), "password"):
            _l_(385477)

            aux = "must provide password"
            _l_(385476)
            return aux


        # query the database for the username
        rows = _c_(385482, _a_(385480, _n_(385479, "db", lambda: db), "execute"), "SELECT * FROM users where username = :username",{"username":_n_(385481, "user_name", lambda: user_name)})
        _l_(385483)

        # ensure username exists 
        if _c_(385486, _n_(385484, "len", lambda: len), _n_(385485, "rows", lambda: rows)) != 1 or not _c_(385494, _a_(385488, _n_(385487, "pwd_context", lambda: pwd_context), "verify"), _c_(385492, _a_(385491, _a_(385490, _n_(385489, "request", lambda: request), "form"), "get"), "password"),_n_(385493, "rows", lambda: rows)[0]["hash"]):
            _l_(385496)

            aux = "Invalid username"
            _l_(385495)
            return aux

        # remember which user has logged in 
        _n_(385497, "session", lambda: session)["user_id"] = _n_(385498, "rows", lambda: rows)[0]["id"]
        _l_(385499)