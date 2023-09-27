# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
   import ssl
   _l_(1538887)

except ImportError:
   pass

try:
   _l_(1538897)

   _create_unverified_https_context = _a_(1538889, _n_(1538888, "ssl", lambda: ssl), "_create_unverified_context")
   _l_(1538890)
except _n_(1538891, "AttributeError", lambda: AttributeError):
   _l_(1538893)

   # Legacy Python that doesn't verify HTTPS certificates by default
   pass
   _l_(1538892)
else:
    # Handle target environment that doesn't support HTTPS verification
    _n_(1538894, "ssl", lambda: ssl)._create_default_https_context = _n_(1538895, "_create_unverified_https_context", lambda: _create_unverified_https_context)
    _l_(1538896)

