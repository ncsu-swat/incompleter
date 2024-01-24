# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74912686/question-about-using-multiprocessing-and-slaves-in-python-getting-error-class
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def OnDownloadStudyArchive(output, uri, **request):
    _l_(434454)


    # Offload the call to "SlowComputation" onto one slave process.
    # The GIL is unlocked until the slave sends its answer back.
    host = "Not Defined"
    _l_(434414)
    userprofilejwt = "Not Defined"
    _l_(434415)
    if "headers" in _n_(434416, "request", lambda: request) and "host" in _n_(434417, "request", lambda: request)['headers']:
        _l_(434420)

        host = _n_(434418, "request", lambda: request)['headers']['host']
        _l_(434419)
    if "headers" in _n_(434421, "request", lambda: request) and "userprofilejwt" in _n_(434422, "request", lambda: request)['headers']:
        _l_(434425)

        userprofilejwt = _n_(434423, "request", lambda: request)['headers']['userprofilejwt']
        _l_(434424)
    _c_(434431, _a_(434427, _n_(434426, "logging", lambda: logging), "info"), "STUDY|DOWNLOAD_ARCHIVE|ID=" + _n_(434428, "request", lambda: request)['groups'][0] + "  HOST=" + _n_(434429, "host", lambda: host) + "  PROFILE=  " + _n_(434430, "userprofilejwt", lambda: userprofilejwt))
    _l_(434432)
    uri = _c_(434435, _a_(434434, _n_(434433, "uri", lambda: uri), "replace"), "_slave", '')
    _l_(434436)
    answer = _c_(434443, _a_(434438, _n_(434437, "POOL", lambda: POOL), "apply"), _c_(434441, _n_(434439, "DelegateStudyArchive", lambda: DelegateStudyArchive), _n_(434440, "uri", lambda: uri)), args=_n_(434442, "uri", lambda: (uri)), kwds = {})
    _l_(434444)
    _c_(434447, _a_(434446, _n_(434445, "pool", lambda: pool), "close"))
    _l_(434448)
    _c_(434452, _a_(434450, _n_(434449, "output", lambda: output), "AnswerBuffer"), _n_(434451, "answer", lambda: answer), 'application/zip')
    _l_(434453)

_c_(434458, _a_(434456, _n_(434455, "orthanc", lambda: orthanc), "RegisterRestCallback"), '/studies/(.*)/archive_slave', _n_(434457, "OnDownloadStudyArchive", lambda: OnDownloadStudyArchive))
_l_(434459)