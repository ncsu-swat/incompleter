# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67930156/sending-raw-transaction-from-web3py-typeerror-lambda-missing-4-required-po
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
t = _c_(401850, _a_(401835, _a_(401834, _a_(401833, _n_(401832, "w3", lambda: w3), "eth"), "account"), "sign_transaction"), _c_(401848, _a_(401840, _c_(401839, _a_(401838, _a_(401837, _n_(401836, "test_contract", lambda: test_contract), "functions"), "edit"), "test"), "buildTransaction"), {
        "nonce": _c_(401847, _a_(401843, _a_(401842, _n_(401841, "w3", lambda: w3), "eth"), "get_transaction_count"), _a_(401846, _a_(401845, _n_(401844, "w3", lambda: w3), "eth"), "default_account"))
    }
), _n_(401849, "pkey", lambda: pkey))
_l_(401851)
_c_(401856, _a_(401854, _a_(401853, _n_(401852, "w3", lambda: w3), "eth"), "send_raw_transaction"), _n_(401855, "t", lambda: t))
_l_(401857)