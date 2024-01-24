# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59110653/typeerror-bytearray-object-cannot-be-interpreted-as-an-integer
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class ChunkingRequestHandler(_n_(381758, "BaseHTTPRequestHandler", lambda: BaseHTTPRequestHandler)):
    _l_(381833)

    ALWAYS_SEND_SOME = False
    _l_(381759)
    ALLOW_GZIP = False
    _l_(381760)
    protocol_version = 'HTTP/1.1'
    _l_(381761)
    def do_GET(self):
        _l_(381832)

        ae = _c_(381765, _a_(381764, _a_(381763, _n_(381762, "self", lambda: self), "headers"), "get"), 'accept-encoding') or ''
        _l_(381766)

        # send some headers
        _c_(381769, _a_(381768, _n_(381767, "self", lambda: self), "send_response"), 200)
        _l_(381770)
        _c_(381773, _a_(381772, _n_(381771, "self", lambda: self), "send_header"), 'Transfer-Encoding', 'chunked')
        _l_(381774)
        _c_(381777, _a_(381776, _n_(381775, "self", lambda: self), "send_header"), 'Content-type', 'audio/x-wav')
        _l_(381778)

        _c_(381781, _a_(381780, _n_(381779, "self", lambda: self), "end_headers"))
        _l_(381782)

        data = _c_(381785, _n_(381783, "bytearray", lambda: bytearray), _n_(381784, "wav_header", lambda: wav_header))
        _l_(381786)
        _c_(381795, _a_(381788, _n_(381787, "data", lambda: data), "append"), _c_(381794, _n_(381789, "bytearray", lambda: bytearray), _c_(381793, _a_(381791, _n_(381790, "stream", lambda: stream), "read"), _n_(381792, "CHUNK", lambda: CHUNK))))
        _l_(381796)
        _c_(381799, _n_(381797, "print", lambda: print), _n_(381798, "data", lambda: data))
        _l_(381800)
        _c_(381808, _a_(381803, _a_(381802, _n_(381801, "self", lambda: self), "wfile"), "write"), b"%X\r\n%s\r\n" % (_c_(381806, _n_(381804, "len", lambda: len), _n_(381805, "data", lambda: data)), _n_(381807, "data", lambda: data)))
        _l_(381809)

        while True:
            _l_(381826)

            data = _c_(381815, _n_(381810, "bytearray", lambda: bytearray), _c_(381814, _a_(381812, _n_(381811, "stream", lambda: stream), "read"), _n_(381813, "CHUNK", lambda: CHUNK)))
            _l_(381816)
            _c_(381824, _a_(381819, _a_(381818, _n_(381817, "self", lambda: self), "wfile"), "write"), b"%X\r\n%s\r\n" % (_c_(381822, _n_(381820, "len", lambda: len), _n_(381821, "data", lambda: data)), _n_(381823, "data", lambda: data)))
            _l_(381825)

        # send the chunked trailer
        _c_(381830, _a_(381829, _a_(381828, _n_(381827, "self", lambda: self), "wfile"), "write"), '0\r\n\r\n')
        _l_(381831)