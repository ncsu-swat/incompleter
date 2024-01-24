# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63815059/running-command-with-subprocess-raises-filenotfounderror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import subprocess
    _l_(565852)

except ImportError:
    pass
image_name = "alpine:3.10"
_l_(565853)
scan_image = _c_(565856, _a_(565854, "trivy -q image -f json {}", "format"), _n_(565855, "image_name", lambda: image_name))
_l_(565857)
scan_result = _c_(565865, _a_(565864, _c_(565863, _a_(565859, _n_(565858, "subprocess", lambda: subprocess), "check_output"), _c_(565862, _a_(565861, _n_(565860, "scan_image", lambda: scan_image), "split"))), "decode"), 'utf-8')
_l_(565866)