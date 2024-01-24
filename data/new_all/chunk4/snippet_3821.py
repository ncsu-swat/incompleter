# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67133185/sqlite3-flask-discord-bot-dashboard-typeerror-nonetype-object-is-not-subscrip
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(632493, _a_(632492, _n_(632491, "app", lambda: app), "route"), "/serveurs/<int:serveur_id>")
def serveur(serveur_id):
    _l_(632548)

    if 'token' not in _n_(632494, "session", lambda: session):
        _l_(632498)

        aux = _c_(632496, _n_(632495, "redirect", lambda: redirect), "https://discord.com/api/oauth2/authorize?client_id=787982190776287282&redirect_uri=https%3A%2F%2FMEE0-1.devteaming.repl.co%2Foauth%2Fdiscord&response_type=code&scope=identify%20guilds")
        _l_(632497)
        return aux
    serveur_info = _c_(632501, _n_(632499, "get_serveur_info", lambda: get_serveur_info), _n_(632500, "serveur_id", lambda: serveur_id))
    _l_(632502)
    if not _n_(632503, "serveur_info", lambda: serveur_info):
        _l_(632507)

        aux = _c_(632505, _n_(632504, "redirect", lambda: redirect), '/dashboard')
        _l_(632506)
        return aux
    with _c_(632510, _a_(632509, _n_(632508, "sqlite3", lambda: sqlite3), "connect"), "dashboard.sqlite3") as db:
        _l_(632524)

        cursor = _c_(632513, _a_(632512, _n_(632511, "db", lambda: db), "cursor"))
        _l_(632514)
        _c_(632518, _a_(632516, _n_(632515, "cursor", lambda: cursor), "execute"), f"SELECT * FROM dashboardconfig WHERE guilds_id = {_n_(632517, 'serveur_info', lambda: serveur_info)['id']}")
        _l_(632519)
        data = _c_(632522, _a_(632521, _n_(632520, "cursor", lambda: cursor), "fetchone"))
        _l_(632523)
    _c_(632527, _n_(632525, "print", lambda: print), _n_(632526, "data", lambda: data))
    _l_(632528)
    mod = _c_(632531, _n_(632529, "bool", lambda: bool), _n_(632530, "data", lambda: data)[2])
    _l_(632532)
    music = _c_(632535, _n_(632533, "bool", lambda: bool), _n_(632534, "data", lambda: data)[2])
    _l_(632536)
    fun = _c_(632539, _n_(632537, "bool", lambda: bool), _n_(632538, "data", lambda: data)[2])
    _l_(632540)
    aux = _c_(632546, _n_(632541, "render_template", lambda: render_template), "serveur.html", serveur=_n_(632542, "serveur_info", lambda: serveur_info), mod=_n_(632543, "mod", lambda: mod), music=_n_(632544, "music", lambda: music), fun=_n_(632545, "fun", lambda: fun))
    _l_(632547)
    return aux