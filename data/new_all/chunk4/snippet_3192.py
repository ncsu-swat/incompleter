# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77539653/exception-raised-in-application-typeerror-nonetype-object-is-not-subscriptab
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(604181)

except ImportError:
    pass
try:
    from cs50 import SQL
    _l_(604183)

except ImportError:
    pass
try:
    from flask import Flask, flash, redirect, render_template, request, session
    _l_(604185)

except ImportError:
    pass
try:
    from flask_session import Session
    _l_(604187)

except ImportError:
    pass
try:
    from werkzeug.security import check_password_hash, generate_password_hash
    _l_(604189)

except ImportError:
    pass
try:
    from helpers import apology, login_required, lookup, usd
    _l_(604191)

except ImportError:
    pass

# Configure application
app = _c_(604194, _n_(604192, "Flask", lambda: Flask), _n_(604193, "__name__", lambda: __name__))
_l_(604195)

# Custom filter
_a_(604198, _a_(604197, _n_(604196, "app", lambda: app), "jinja_env"), "filters")["usd"] = _n_(604199, "usd", lambda: usd)
_l_(604200)

# Configure session to use filesystem (instead of signed cookies)
_a_(604202, _n_(604201, "app", lambda: app), "config")["SESSION_PERMANENT"] = False
_l_(604203)
_a_(604205, _n_(604204, "app", lambda: app), "config")["SESSION_TYPE"] = "filesystem"
_l_(604206)
_c_(604209, _n_(604207, "Session", lambda: Session), _n_(604208, "app", lambda: app))
_l_(604210)

# Configure CS50 Library to use SQLite database
db = _c_(604212, _n_(604211, "SQL", lambda: SQL), "sqlite:///finance.db")
_l_(604213)


@_a_(604215, _n_(604214, "app", lambda: app), "after_request")
def after_request(response):
    _l_(604227)

    """Ensure responses aren't cached"""
    _a_(604217, _n_(604216, "response", lambda: response), "headers")["Cache-Control"] = "no-cache, no-store, must-revalidate"
    _l_(604218)
    _a_(604220, _n_(604219, "response", lambda: response), "headers")["Expires"] = 0
    _l_(604221)
    _a_(604223, _n_(604222, "response", lambda: response), "headers")["Pragma"] = "no-cache"
    _l_(604224)
    aux = _n_(604225, "response", lambda: response)
    _l_(604226)
    return aux


@_c_(604230, _a_(604229, _n_(604228, "app", lambda: app), "route"), "/")
@_n_(604231, "login_required", lambda: login_required)
def index():
    _l_(604315)

    """Show portfolio of stocks"""

    # Main variables
    user_id = _n_(604232, "session", lambda: session)["user_id"]
    _l_(604233)
    user_cash = _c_(604237, _a_(604235, _n_(604234, "db", lambda: db), "execute"), "SELECT cash FROM users WHERE id == ?", _n_(604236, "user_id", lambda: user_id))[0]["cash"]
    _l_(604238)
    counter = 0
    _l_(604239)
    shares_total = 0
    _l_(604240)
    user_info = _c_(604244, _a_(604242, _n_(604241, "db", lambda: db), "execute"), "SELECT user_id, symbol, SUM(shares) as shares, price, total, MAX(timestamp) as timestamp FROM info WHERE user_id == ? AND shares > 0 GROUP BY symbol", _n_(604243, "user_id", lambda: user_id))
    _l_(604245)
    counter = _c_(604248, _n_(604246, "len", lambda: len), _n_(604247, "user_info", lambda: user_info))
    _l_(604249)

    # MAIN calculation loop
    if _n_(604250, "counter", lambda: counter) != 0:
        _l_(604314)

        for j in _c_(604252, _n_(604251, "range", lambda: range), 1):
            _l_(604297)

            for i in _c_(604255, _n_(604253, "range", lambda: range), _n_(604254, "counter", lambda: counter)):
                _l_(604288)


                symbol = _n_(604256, "user_info", lambda: user_info)[_n_(604257, "i", lambda: i)]["symbol"]
                _l_(604258)
                price = _c_(604261, _n_(604259, "lookup", lambda: lookup), _n_(604260, "symbol", lambda: symbol))["price"]
                _l_(604262)
                total = _n_(604263, "price", lambda: price) * _n_(604264, "user_info", lambda: user_info)[_n_(604265, "i", lambda: i)]["shares"]
                _l_(604266)
                cash = _n_(604267, "user_cash", lambda: user_cash) - _n_(604268, "total", lambda: total)
                _l_(604269)

                # This if statement means if there is more symbol and shares the do this
                if _n_(604270, "counter", lambda: counter) > 1:
                    _l_(604279)

                    shares_total += _n_(604271, "user_info", lambda: user_info)[_n_(604272, "i", lambda: i)]["total"]
                    _l_(604273)

                elif _n_(604274, "counter", lambda: counter) == 1:
                    _l_(604278)

                    shares_total = _n_(604275, "user_info", lambda: user_info)[_n_(604276, "i", lambda: i)]["total"]
                    _l_(604277)

                _c_(604286, _a_(604281, _n_(604280, "db", lambda: db), "execute"), "UPDATE info SET price == ?, total == ? WHERE user_id == ? AND symbol == ?", _n_(604282, "price", lambda: price), _n_(604283, "total", lambda: total), _n_(604284, "user_id", lambda: user_id), _n_(604285, "symbol", lambda: symbol))
                _l_(604287)

            # Select current cash and then incriment
            cash = _c_(604292, _a_(604290, _n_(604289, "db", lambda: db), "execute"), "SELECT cash FROM users WHERE id == ?", _n_(604291, "user_id", lambda: user_id))[0]["cash"]
            _l_(604293)
            main_total = _n_(604294, "cash", lambda: cash) + _n_(604295, "shares_total", lambda: shares_total)
            _l_(604296)
        aux = _c_(604306, _n_(604298, "render_template", lambda: render_template), "layout.html", user_info = _n_(604299, "user_info", lambda: user_info), i=_n_(604300, "i", lambda: i), counter = _n_(604301, "counter", lambda: counter), total = _n_(604302, "total", lambda: total), price = _n_(604303, "price", lambda: price), tottal = _n_(604304, "main_total", lambda: main_total), cash = _n_(604305, "cash", lambda: cash))
        _l_(604307)

        return aux

    else:
        aux = _c_(604312, _n_(604308, "render_template", lambda: render_template), "layout.html", cash = _n_(604309, "user_cash", lambda: user_cash), tottal = _n_(604310, "user_cash", lambda: user_cash), counter = _n_(604311, "counter", lambda: counter))
        _l_(604313)

        return aux


@_c_(604318, _a_(604317, _n_(604316, "app", lambda: app), "route"), "/buy", methods=["GET", "POST"])
@_n_(604319, "login_required", lambda: login_required)
def buy():
    _l_(604486)

    """Buy shares of stock"""


    if _a_(604321, _n_(604320, "request", lambda: request), "method") == "GET":
        _l_(604485)

        aux = _c_(604323, _n_(604322, "render_template", lambda: render_template), "buy.html")
        _l_(604324)
        return aux

    else:

        user_id = _n_(604325, "session", lambda: session)["user_id"]
        _l_(604326)
        input_shares = _c_(604330, _a_(604329, _a_(604328, _n_(604327, "request", lambda: request), "form"), "get"), "shares")
        _l_(604331)
        cash = _c_(604335, _a_(604333, _n_(604332, "db", lambda: db), "execute"), "SELECT cash FROM users WHERE id == ?", _n_(604334, "user_id", lambda: user_id))[0]["cash"]
        _l_(604336)


        # Erro hendling statements
        try:
            _l_(604349)

            input_shares = _c_(604342, _n_(604337, "int", lambda: int), _c_(604341, _a_(604340, _a_(604339, _n_(604338, "request", lambda: request), "form"), "get"), "shares"))
            _l_(604343)

        except _n_(604344, "ValueError", lambda: ValueError):
            _l_(604348)

            aux = _c_(604346, _n_(604345, "apology", lambda: apology), "shares must be a posative integer", 400)
            _l_(604347)
            return aux

        input_shares = _c_(604352, _n_(604350, "int", lambda: int), _n_(604351, "input_shares", lambda: input_shares))
        _l_(604353)

        if _n_(604354, "input_shares", lambda: input_shares) <= 0:
            _l_(604358)

            aux = _c_(604356, _n_(604355, "apology", lambda: apology), "Shares number should be more then 0")
            _l_(604357)
            return aux

        if _c_(604364, _n_(604359, "lookup", lambda: lookup), _c_(604363, _a_(604362, _a_(604361, _n_(604360, "request", lambda: request), "form"), "get"), "symbol")) is None:
            _l_(604368)

            aux = _c_(604366, _n_(604365, "apology", lambda: apology), "Please enter valid quotes")
            _l_(604367)
            return aux

        price = _c_(604374, _n_(604369, "lookup", lambda: lookup), _c_(604373, _a_(604372, _a_(604371, _n_(604370, "request", lambda: request), "form"), "get"), "symbol"))["price"]
        _l_(604375)

        if _n_(604376, "cash", lambda: cash) < _n_(604377, "price", lambda: price) * _n_(604378, "input_shares", lambda: input_shares):
            _l_(604382)

            aux = _c_(604380, _n_(604379, "apology", lambda: apology), "You don't have enough money")
            _l_(604381)
            return aux

        symbol = _c_(604388, _n_(604383, "lookup", lambda: lookup), _c_(604387, _a_(604386, _a_(604385, _n_(604384, "request", lambda: request), "form"), "get"), "symbol"))["name"]
        _l_(604389)
        shares = _c_(604394, _a_(604391, _n_(604390, "db", lambda: db), "execute"), "SELECT shares FROM info WHERE user_id == ? AND symbol == ?", _n_(604392, "user_id", lambda: user_id), _n_(604393, "symbol", lambda: symbol))
        _l_(604395)

        # This statemen is for error hendling, it's neccesery because if there is no purchase yet
        # It will purchase some shares and then return
        if _c_(604398, _n_(604396, "len", lambda: len), _n_(604397, "shares", lambda: shares)) == 0:
            _l_(604484)


            total = _n_(604399, "price", lambda: price) * _n_(604400, "input_shares", lambda: input_shares)
            _l_(604401)
            cash -= _n_(604402, "total", lambda: total)
            _l_(604403)
            _c_(604408, _a_(604405, _n_(604404, "db", lambda: db), "execute"), "UPDATE users SET cash == ? WHERE id == ?", _n_(604406, "cash", lambda: cash), _n_(604407, "user_id", lambda: user_id))
            _l_(604409)
            _c_(604417, _a_(604411, _n_(604410, "db", lambda: db), "execute"), "INSERT INTO info (user_id, symbol, shares, price, total) VALUES (?, ?, ?, ?, ?)", _n_(604412, "user_id", lambda: user_id), _n_(604413, "symbol", lambda: symbol), _n_(604414, "input_shares", lambda: input_shares), _n_(604415, "price", lambda: price), _n_(604416, "total", lambda: total))
            _l_(604418)
            _c_(604425, _a_(604420, _n_(604419, "db", lambda: db), "execute"), "INSERT INTO history_info (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)", _n_(604421, "user_id", lambda: user_id), _n_(604422, "symbol", lambda: symbol), _n_(604423, "input_shares", lambda: input_shares), _n_(604424, "price", lambda: price))
            _l_(604426)

            _c_(604428, _n_(604427, "flash", lambda: flash), 'You have bought!', 'success')
            _l_(604429)
            aux = _c_(604431, _n_(604430, "redirect", lambda: redirect), "/")
            _l_(604432)
            return aux

        elif _c_(604435, _n_(604433, "len", lambda: len), _n_(604434, "shares", lambda: shares)) > 0:
            _l_(604483)


            # ar dagaviwydes rom sheamowmo len(shares) im shemtxvevashi tu ki romelime stock bevri yidva gayidvis istoria aqvs
            # da unda vnaxot ramdenad sworad gvichvenebs shares[0]["shares"] tavis monacems!!!!!!!!!!!!!!!!!!!!!!!!!

            shares = _c_(604440, _a_(604437, _n_(604436, "db", lambda: db), "execute"), "SELECT shares FROM info WHERE user_id == ? AND symbol == ?", _n_(604438, "user_id", lambda: user_id), _n_(604439, "symbol", lambda: symbol))
            _l_(604441)
            shares = _n_(604442, "shares", lambda: shares)[0]["shares"]
            _l_(604443)

            shares += _n_(604444, "input_shares", lambda: input_shares)
            _l_(604445)

            # Calculate and then Update all of the information into a SQL database
            total = _n_(604446, "price", lambda: price) * _n_(604447, "shares", lambda: shares)
            _l_(604448)

            cash = _n_(604449, "cash", lambda: cash) - _n_(604450, "price", lambda: price) * _n_(604451, "input_shares", lambda: input_shares)
            _l_(604452)

            _c_(604457, _a_(604454, _n_(604453, "db", lambda: db), "execute"), "UPDATE users SET cash == ? WHERE id == ?", _n_(604455, "cash", lambda: cash), _n_(604456, "user_id", lambda: user_id))
            _l_(604458)
            _c_(604467, _a_(604460, _n_(604459, "db", lambda: db), "execute"), "UPDATE info SET symbol == ?, price == ?, shares == ?, total == ? WHERE user_id == ? AND symbol == ?", _n_(604461, "symbol", lambda: symbol), _n_(604462, "price", lambda: price), _n_(604463, "shares", lambda: shares), _n_(604464, "total", lambda: total), _n_(604465, "user_id", lambda: user_id), _n_(604466, "symbol", lambda: symbol))
            _l_(604468)
            _c_(604475, _a_(604470, _n_(604469, "db", lambda: db), "execute"), "INSERT INTO history_info (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)", _n_(604471, "user_id", lambda: user_id), _n_(604472, "symbol", lambda: symbol), _n_(604473, "input_shares", lambda: input_shares), _n_(604474, "price", lambda: price))
            _l_(604476)

            _c_(604478, _n_(604477, "flash", lambda: flash), 'You have bought!', 'success')
            _l_(604479)
            aux = _c_(604481, _n_(604480, "redirect", lambda: redirect), "/")
            _l_(604482)
            return aux


@_c_(604489, _a_(604488, _n_(604487, "app", lambda: app), "route"), "/history")
@_n_(604490, "login_required", lambda: login_required)
def history():
    _l_(604518)

    """Show history of transactions"""

    # Main variables
    user_id = _n_(604491, "session", lambda: session)["user_id"]
    _l_(604492)
    info = _c_(604496, _a_(604494, _n_(604493, "db", lambda: db), "execute"), "SELECT * FROM history_info WHERE user_id == ?", _n_(604495, "user_id", lambda: user_id))
    _l_(604497)
    counter = _c_(604500, _n_(604498, "len", lambda: len), _n_(604499, "info", lambda: info))
    _l_(604501)

    # If there is not purchase yet it will return nothing
    # Main code is inside HTML For loop and if statement
    if not _n_(604502, "info", lambda: info):
        _l_(604517)

        aux = _c_(604505, _n_(604503, "render_template", lambda: render_template), "history.html", info = _n_(604504, "info", lambda: info))
        _l_(604506)
        return aux
    else:
        for i in _c_(604509, _n_(604507, "range", lambda: range), _n_(604508, "counter", lambda: counter)):
            _l_(604516)

            aux = _c_(604514, _n_(604510, "render_template", lambda: render_template), "history.html", info = _n_(604511, "info", lambda: info), i = _n_(604512, "i", lambda: i), counter = _n_(604513, "counter", lambda: counter))
            _l_(604515)
            return aux


@_c_(604521, _a_(604520, _n_(604519, "app", lambda: app), "route"), "/login", methods=["GET", "POST"])
def login():
    _l_(604576)

    """Log user in"""

    # Forget any user_id
    _c_(604524, _a_(604523, _n_(604522, "session", lambda: session), "clear"))
    _l_(604525)

    # User reached route via POST (as by submitting a form via POST)
    if _a_(604527, _n_(604526, "request", lambda: request), "method") == "POST":
        _l_(604575)


        # Ensure username was submitted
        if not _c_(604531, _a_(604530, _a_(604529, _n_(604528, "request", lambda: request), "form"), "get"), "username"):
            _l_(604543)

            aux = _c_(604533, _n_(604532, "apology", lambda: apology), "must provide username", 403)
            _l_(604534)
            return aux

        # Ensure password was submitted
        elif not _c_(604538, _a_(604537, _a_(604536, _n_(604535, "request", lambda: request), "form"), "get"), "password"):
            _l_(604542)

            aux = _c_(604540, _n_(604539, "apology", lambda: apology), "must provide password", 403)
            _l_(604541)
            return aux

        # Query database for username
        rows = _c_(604550, _a_(604545, _n_(604544, "db", lambda: db), "execute"), "SELECT * FROM users WHERE username = ?", _c_(604549, _a_(604548, _a_(604547, _n_(604546, "request", lambda: request), "form"), "get"), "username"))
        _l_(604551)

        # Ensure username exists and password is correct
        if _c_(604554, _n_(604552, "len", lambda: len), _n_(604553, "rows", lambda: rows)) != 1 or not _c_(604561, _n_(604555, "check_password_hash", lambda: check_password_hash), _n_(604556, "rows", lambda: rows)[0]["hash"], _c_(604560, _a_(604559, _a_(604558, _n_(604557, "request", lambda: request), "form"), "get"), "password")):
            _l_(604565)

            aux = _c_(604563, _n_(604562, "apology", lambda: apology), "invalid username and/or password", 403)
            _l_(604564)
            return aux

        # Remember which user has logged in
        _n_(604566, "session", lambda: session)["user_id"] = _n_(604567, "rows", lambda: rows)[0]["id"]
        _l_(604568)
        aux = _c_(604570, _n_(604569, "redirect", lambda: redirect), "/")
        _l_(604571)

        return aux

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        aux = _c_(604573, _n_(604572, "render_template", lambda: render_template), "login.html")
        _l_(604574)
        return aux


@_c_(604579, _a_(604578, _n_(604577, "app", lambda: app), "route"), "/logout")
def logout():
    _l_(604587)

    """Log user out"""

    # Forget any user_id
    _c_(604582, _a_(604581, _n_(604580, "session", lambda: session), "clear"))
    _l_(604583)
    aux = _c_(604585, _n_(604584, "redirect", lambda: redirect), "/")
    _l_(604586)

    # Redirect user to login form
    return aux


@_c_(604590, _a_(604589, _n_(604588, "app", lambda: app), "route"), "/quote", methods=["GET", "POST"])
@_n_(604591, "login_required", lambda: login_required)
def quote():
    _l_(604626)

    """Get stock quote."""
    if _a_(604593, _n_(604592, "request", lambda: request), "method") == "GET":
        _l_(604625)

        aux = _c_(604595, _n_(604594, "render_template", lambda: render_template), "quote.html")
        _l_(604596)
        return aux

    else:
        # save user input and give's it to the lookup function
        symbol = _c_(604602, _n_(604597, "lookup", lambda: lookup), _c_(604601, _a_(604600, _a_(604599, _n_(604598, "request", lambda: request), "form"), "get"), "symbol"))
        _l_(604603)

        # take price from lookup function
        value = _c_(604609, _n_(604604, "lookup", lambda: lookup), _c_(604608, _a_(604607, _a_(604606, _n_(604605, "request", lambda: request), "form"), "get"), "symbol"))
        _l_(604610)

        if _n_(604611, "symbol", lambda: symbol) == None:
            _l_(604615)

            aux = _c_(604613, _n_(604612, "apology", lambda: apology), "You need to sign correct Symbol")
            _l_(604614)
            return aux

        # Take symbol's Name from dict
        symbol = _n_(604616, "symbol", lambda: symbol)["name"]
        _l_(604617)

        # Take Symbol's Price from dict
        value = _n_(604618, "value", lambda: value)["price"]
        _l_(604619)
        aux = _c_(604623, _n_(604620, "render_template", lambda: render_template), "quoted.html", symbol=_n_(604621, "symbol", lambda: symbol), value=_n_(604622, "value", lambda: value))
        _l_(604624)

        return aux


@_c_(604629, _a_(604628, _n_(604627, "app", lambda: app), "route"), "/register", methods=["GET", "POST"])
def register():
    _l_(604712)

    """Register user"""

    _c_(604632, _a_(604631, _n_(604630, "session", lambda: session), "clear"))
    _l_(604633)

    name = _c_(604637, _a_(604636, _a_(604635, _n_(604634, "request", lambda: request), "form"), "get"), "username")
    _l_(604638)
    password = _c_(604642, _a_(604641, _a_(604640, _n_(604639, "request", lambda: request), "form"), "get"), "password")
    _l_(604643)
    confirm = _c_(604647, _a_(604646, _a_(604645, _n_(604644, "request", lambda: request), "form"), "get"), "confirmation")
    _l_(604648)

    # this will count, if there is excist username
    check_users = _c_(604652, _a_(604650, _n_(604649, "db", lambda: db), "execute"), "SELECT COUNT(*) FROM users WHERE username = ?", _n_(604651, "name", lambda: name))
    _l_(604653)

    # if there is match count_value dict will return 1
    count_value = _n_(604654, "check_users", lambda: check_users)[0]['COUNT(*)']
    _l_(604655)

    if _a_(604657, _n_(604656, "request", lambda: request), "method") == "POST":
        _l_(604711)


        # Chek users registration form
        if not _n_(604658, "name", lambda: name):
            _l_(604683)

            aux = _c_(604660, _n_(604659, "apology", lambda: apology), "user’s input is blank")
            _l_(604661)
            return aux

        elif not _n_(604662, "password", lambda: password):
            _l_(604682)

            aux = _c_(604664, _n_(604663, "apology", lambda: apology), "Password input is blank")
            _l_(604665)
            return aux

        elif not _n_(604666, "confirm", lambda: confirm):
            _l_(604681)

            aux = _c_(604668, _n_(604667, "apology", lambda: apology), "Confirm password input is blank")
            _l_(604669)
            return aux

        elif _n_(604670, "password", lambda: password) != _n_(604671, "confirm", lambda: confirm):
            _l_(604680)

            aux = _c_(604673, _n_(604672, "apology", lambda: apology), "Passwords do not match")
            _l_(604674)
            return aux

        elif _n_(604675, "count_value", lambda: count_value) != 0:
            _l_(604679)

            aux = _c_(604677, _n_(604676, "apology", lambda: apology), "Username already exists")
            _l_(604678)
            return aux


        # ransform password into hash
        hashed_password = _c_(604686, _n_(604684, "generate_password_hash", lambda: generate_password_hash), _n_(604685, "password", lambda: password), method='pbkdf2')
        _l_(604687)

        # if there is no apology, then this will insert users information into SQL
        _c_(604692, _a_(604689, _n_(604688, "db", lambda: db), "execute"), "INSERT INTO users(username, hash) VALUES(?, ?)", _n_(604690, "name", lambda: name), _n_(604691, "hashed_password", lambda: hashed_password))
        _l_(604693)

        # Query database for username
        rows = _c_(604697, _a_(604695, _n_(604694, "db", lambda: db), "execute"), "SELECT * FROM users WHERE username = ?", _n_(604696, "name", lambda: name))
        _l_(604698)

        # Remember which user has logged in
        _n_(604699, "session", lambda: session)["user_id"] = _n_(604700, "rows", lambda: rows)[0]["id"]
        _l_(604701)

        # this will let user know that registration succesfully complete
        _c_(604703, _n_(604702, "flash", lambda: flash), 'You have successfully registered!', 'success')
        _l_(604704)
        aux = _c_(604706, _n_(604705, "redirect", lambda: redirect), "/")
        _l_(604707)

        # redirects to homepage
        return aux

    else:
        aux = _c_(604709, _n_(604708, "render_template", lambda: render_template), "register.html")
        _l_(604710)

        return aux


@_c_(604715, _a_(604714, _n_(604713, "app", lambda: app), "route"), "/sell", methods=["GET", "POST"])
@_n_(604716, "login_required", lambda: login_required)
def sell():
    _l_(604809)

    """Sell shares of stock"""

    if _a_(604718, _n_(604717, "request", lambda: request), "method") == "GET":
        _l_(604808)


        user_id = _n_(604719, "session", lambda: session)["user_id"]
        _l_(604720)
        # Insert symbols with DISTINC method inside html section
        # DISTINC avoides repeted symbols it will SELECT's only once
        quotes = _c_(604724, _a_(604722, _n_(604721, "db", lambda: db), "execute"), "SELECT DISTINCT symbol FROM info WHERE user_id == ? AND shares > 0", _n_(604723, "user_id", lambda: user_id))
        _l_(604725)
        aux = _c_(604728, _n_(604726, "render_template", lambda: render_template), "sell.html", quotes = _n_(604727, "quotes", lambda: quotes))
        _l_(604729)

        return aux

    else:

        # Main variables
        user_id = _n_(604730, "session", lambda: session)["user_id"]
        _l_(604731)
        symbol = _c_(604735, _a_(604734, _a_(604733, _n_(604732, "request", lambda: request), "form"), "get"), "symbol")
        _l_(604736)
        input_shares = _c_(604742, _n_(604737, "int", lambda: int), _c_(604741, _a_(604740, _a_(604739, _n_(604738, "request", lambda: request), "form"), "get"), "sell-shares"))
        _l_(604743)

        if _n_(604744, "input_shares", lambda: input_shares) <= 0:
            _l_(604748)

            aux = _c_(604746, _n_(604745, "apology", lambda: apology), "Number should be greater then zero")
            _l_(604747)
            return aux

        # This is how we can have acces into symbol
        # 12: means select chars from 12th char
        # :-2 select last two char which is ' } and removes
        symbol = _n_(604749, "symbol", lambda: symbol)[12:][:-2]
        _l_(604750)
        price = _c_(604753, _n_(604751, "lookup", lambda: lookup), _n_(604752, "symbol", lambda: symbol))["price"]
        _l_(604754)
        cash = _c_(604758, _a_(604756, _n_(604755, "db", lambda: db), "execute"), "SELECT cash FROM users WHERE id == ?", _n_(604757, "user_id", lambda: user_id))[0]["cash"]
        _l_(604759)

        shares = _c_(604764, _a_(604761, _n_(604760, "db", lambda: db), "execute"), "SELECT shares FROM info WHERE user_id ==? AND symbol == ?", _n_(604762, "user_id", lambda: user_id), _n_(604763, "symbol", lambda: symbol))[0]["shares"]
        _l_(604765)

        if _n_(604766, "shares", lambda: shares) < _n_(604767, "input_shares", lambda: input_shares):
            _l_(604771)

            aux = _c_(604769, _n_(604768, "apology", lambda: apology), "You don't have that many quotes")
            _l_(604770)
            return aux

        shares -= _n_(604772, "input_shares", lambda: input_shares)
        _l_(604773)

        # Main calculation and Update SQL data
        profit = _n_(604774, "input_shares", lambda: input_shares) * _n_(604775, "price", lambda: price)
        _l_(604776)
        profit += _n_(604777, "cash", lambda: cash)
        _l_(604778)
        _c_(604786, _a_(604780, _n_(604779, "db", lambda: db), "execute"), "UPDATE info SET shares = shares - ?, total = ? * ? WHERE user_id == ? AND symbol == ?", _n_(604781, "input_shares", lambda: input_shares), _n_(604782, "shares", lambda: shares), _n_(604783, "price", lambda: price), _n_(604784, "user_id", lambda: user_id), _n_(604785, "symbol", lambda: symbol))
        _l_(604787)
        _c_(604792, _a_(604789, _n_(604788, "db", lambda: db), "execute"), "UPDATE users SET cash == ? WHERE id == ?", _n_(604790, "profit", lambda: profit), _n_(604791, "user_id", lambda: user_id))
        _l_(604793)
        _c_(604800, _a_(604795, _n_(604794, "db", lambda: db), "execute"), "INSERT INTO history_info (user_id, symbol, shares, price) VALUES (?, ?, -?, ?)", _n_(604796, "user_id", lambda: user_id), _n_(604797, "symbol", lambda: symbol), _n_(604798, "input_shares", lambda: input_shares), _n_(604799, "price", lambda: price))
        _l_(604801)


        _c_(604803, _n_(604802, "flash", lambda: flash), 'Sold!', 'success')
        _l_(604804)
        aux = _c_(604806, _n_(604805, "redirect", lambda: redirect), "/")
        _l_(604807)

        return aux