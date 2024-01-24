# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58179496/logging-error-in-python-3-x-typeerror-a-bytes-like-object-is-required-not-s
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if _n_(406622, "__name__", lambda: __name__) == '__main__':
    _l_(406723)

    config_file = '/source/account_content_recommendation/config/sales_central_config.json'
    _l_(406623)
    try:
        _l_(406722)

        ### Read all the parameters -
        params = _c_(406630, _a_(406625, _n_(406624, "json", lambda: json), "loads"), _c_(406629, _a_(406627, _n_(406626, "hdfs", lambda: hdfs), "read_file"), _n_(406628, "config_file", lambda: config_file)))
        _l_(406631)

        ### Create the logging csv file -
        hdfs_log_path = _n_(406632, "params", lambda: params)["hdfs_log_path"]
        _l_(406633)
        _c_(406637, _a_(406635, _n_(406634, "hdfs", lambda: hdfs), "create_file"), _n_(406636, "hdfs_log_path", lambda: hdfs_log_path), "starting ... ", overwrite = True)
        _l_(406638)
        log_name = 'Account_Content_Matching'
        _l_(406639)


        global stream
        _l_(406640)
        log = _c_(406643, _a_(406642, _n_(406641, "logging", lambda: logging), "getLogger"), 'Acct_Cont_Log')
        _l_(406644)
        stream = _c_(406646, _n_(406645, "BytesIO", lambda: BytesIO))
        _l_(406647)
        handler = _c_(406651, _a_(406649, _n_(406648, "logging", lambda: logging), "StreamHandler"), _n_(406650, "stream", lambda: stream))
        _l_(406652)
        _c_(406657, _a_(406654, _n_(406653, "log", lambda: log), "setLevel"), _a_(406656, _n_(406655, "logging", lambda: logging), "DEBUG"))
        _l_(406658)

        for handle in _a_(406660, _n_(406659, "log", lambda: log), "handlers"):
            _l_(406666)

            _c_(406664, _a_(406662, _n_(406661, "log", lambda: log), "removeHandler"), _n_(406663, "handle", lambda: handle))
            _l_(406665)

        _c_(406670, _a_(406668, _n_(406667, "log", lambda: log), "addHandler"), _n_(406669, "handler", lambda: handler))
        _l_(406671)

        #env = sys.argv[1]
        env = 'dev'
        _l_(406672)
        formatter = _c_(406679, _a_(406674, _n_(406673, "logging", lambda: logging), "Formatter"), _c_(406678, _a_(406675, '{0}| %(asctime)s| {1}| %(module)s| %(funcName)s| %(lineno)d| %(levelname)s| %(message)r', "format"), _n_(406676, "log_name", lambda: log_name), _n_(406677, "env", lambda: env)))
        _l_(406680)
        _c_(406684, _a_(406682, _n_(406681, "handler", lambda: handler), "setFormatter"), _n_(406683, "formatter", lambda: formatter))
        _l_(406685)

        _c_(406688, _a_(406687, _n_(406686, "log", lambda: log), "info"), "starting execution of Account_Content_Matching load")
        _l_(406689)
        #log.info("sys args %s"%(str(sys.argv)))

        def flush_log():
            _l_(406717)

            global stream
            _l_(406690)
            msg = _c_(406693, _a_(406692, _n_(406691, "stream", lambda: stream), "getvalue"))
            _l_(406694)
            _c_(406699, _a_(406696, _n_(406695, "hdfs", lambda: hdfs), "append_file"), _n_(406697, "hdfs_log_path", lambda: hdfs_log_path), _n_(406698, "msg", lambda: msg))
            _l_(406700)
            _c_(406703, _a_(406702, _n_(406701, "stream", lambda: stream), "seek"), 0)
            _l_(406704)
            _c_(406707, _a_(406706, _n_(406705, "stream", lambda: stream), "truncate"), 0)
            _l_(406708)
            _c_(406711, _n_(406709, "print", lambda: print), _n_(406710, "msg", lambda: msg))
            _l_(406712)
            _a_(406715, _a_(406714, _n_(406713, "sys", lambda: sys), "stdout"), "flush")
            _l_(406716)

    except _n_(406718, "Exception", lambda: Exception) as error:
        _l_(406721)

        raise _n_(406719, "error", lambda: error)
        _l_(406720)