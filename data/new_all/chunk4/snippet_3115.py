# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44243530/typeerror-when-creating-a-sha512-hash-using-pycryto
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
signature = _n_(606884, "f", lambda: f)[:_n_(606885, "signatureLength", lambda: signatureLength)]
_l_(606886)
f = _c_(606888, _n_(606887, "open", lambda: open), 'lib/publicKey.pem','rb')
_l_(606889)
publicKey = _c_(606895, _a_(606891, _n_(606890, "RSA", lambda: RSA), "importKey"), _c_(606894, _a_(606893, _n_(606892, "f", lambda: f), "read")))
_l_(606896)
hash = _c_(606901, _a_(606898, _n_(606897, "SHA512", lambda: SHA512), "new"), _n_(606899, "f", lambda: f)[_n_(606900, "signatureLength", lambda: signatureLength):])
_l_(606902)
verification = _c_(606906, _a_(606904, _n_(606903, "PKCS1_PSS", lambda: PKCS1_PSS), "new"), _n_(606905, "publicKey", lambda: publicKey))
_l_(606907)