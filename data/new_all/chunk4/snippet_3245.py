# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76755756/typeerror-argument-2-must-be-a-connection-cursor-or-none-in-psycopg2
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def connect_with_retry(alias):
    _l_(621306)

    """
    Try to establish a database connection with retry.
    :param alias: Alias of the database
    :return: psycopg2.extensions.connection object if successful, otherwise raise exception
    """
    attempt = 1
    _l_(621217)
    retry_count = _n_(621218, "PGBOUNCER_RETRY_COUNT", lambda: PGBOUNCER_RETRY_COUNT)
    _l_(621219)
    retry_delay = _n_(621220, "PGBOUNCER_RETRY_DELAY", lambda: PGBOUNCER_RETRY_DELAY)
    _l_(621221)
    conn_string = _c_(621224, _a_(621223, _n_(621222, "os", lambda: os), "getenv"), 'DATABASE_URL')
    _l_(621225)

    try:
        _l_(621256)

        url_parts = _c_(621229, _a_(621227, _n_(621226, "urlparse", lambda: urlparse), "urlparse"), _n_(621228, "conn_string", lambda: conn_string))
        _l_(621230)
        username = _a_(621232, _n_(621231, "url_parts", lambda: url_parts), "username")
        _l_(621233)
        password = _a_(621235, _n_(621234, "url_parts", lambda: url_parts), "password")
        _l_(621236)
        host = _a_(621238, _n_(621237, "url_parts", lambda: url_parts), "hostname")
        _l_(621239)
        port = _a_(621241, _n_(621240, "url_parts", lambda: url_parts), "port")
        _l_(621242)
        database_name = _c_(621246, _a_(621245, _a_(621244, _n_(621243, "url_parts", lambda: url_parts), "path"), "lstrip"), '/')
        _l_(621247)
    except _n_(621248, "Exception", lambda: Exception) as ex:
        _l_(621255)

        _c_(621252, _a_(621250, _n_(621249, "logger", lambda: logger), "error"), f"Error parsing database URL: {_n_(621251, 'ex', lambda: ex)}")
        _l_(621253)
        # Set default values or raise an exception if appropriate
        username = password = host = port = database_name = None
        _l_(621254)

    while True:
        _l_(621305)

        try:
            _l_(621304)

            _c_(621262, _a_(621258, _n_(621257, "logger", lambda: logger), "debug"), f"Trying to make a connection with database: username - {_n_(621259, 'username', lambda: username)}, host - {_n_(621260, 'host', lambda: host)}, database_name - {_n_(621261, 'database_name', lambda: database_name)}"
            )
            _l_(621263)
            conn = _c_(621272, _a_(621265, _n_(621264, "psycopg2", lambda: psycopg2), "connect"), dbname=_n_(621266, "database_name", lambda: database_name),
                user=_n_(621267, "username", lambda: username),
                password=_n_(621268, "password", lambda: password),
                host=_n_(621269, "host", lambda: host),
                port=_n_(621270, "port", lambda: port),
                connect_timeout=_n_(621271, "retry_delay", lambda: retry_delay),
            )
            _l_(621273)
            _c_(621277, _a_(621275, _n_(621274, "logger", lambda: logger), "info"), f"Connections details {_n_(621276, 'conn', lambda: conn)}")
            _l_(621278)
            aux = _n_(621279, "conn", lambda: conn)
            _l_(621280)
            return aux
        except (_a_(621282, _n_(621281, "psycopg2", lambda: psycopg2), "OperationalError"), _a_(621284, _n_(621283, "psycopg2", lambda: psycopg2), "DatabaseError")) as ex:
            _l_(621303)

            attempt += 1
            _l_(621285)
            if _n_(621286, "attempt", lambda: attempt) > _n_(621287, "retry_count", lambda: retry_count):
                _l_(621295)

                _c_(621290, _a_(621289, _n_(621288, "logger", lambda: logger), "info"), f"Database connection retry max-limit exceeded")
                _l_(621291)
                raise _c_(621293, _n_(621292, "ConnectionError", lambda: ConnectionError), "Failed to establish a database connection")
                _l_(621294)
            _c_(621301, _a_(621297, _n_(621296, "logger", lambda: logger), "info"), f"Connection failed, retrying in {_n_(621298, 'retry_delay', lambda: retry_delay)} seconds... (Attempt {_n_(621299, 'attempt', lambda: attempt)}/{_n_(621300, 'retry_count', lambda: retry_count)})"
            )
            _l_(621302)


DATABASES = {}
_l_(621307)
_n_(621308, "DATABASES", lambda: DATABASES)["default"] = _c_(621311, _a_(621310, _n_(621309, "dj_database_url", lambda: dj_database_url), "config"))
_l_(621312)
_n_(621313, "DATABASES", lambda: DATABASES)["default"]["ENGINE"] = "psqlextra.backend"
_l_(621314)
_n_(621315, "DATABASES", lambda: DATABASES)["default"]["OPTIONS"] = {
    'connection_factory': lambda alias: _c_(621317, _n_(621316, "connect_with_retry", lambda: connect_with_retry), "default")
}
_l_(621318)
POSTGRES_EXTRA_DB_BACKEND_BASE = "core.database_backend"
_l_(621319)