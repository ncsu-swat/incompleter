# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59524510/typeerror-object-of-type-io-textiowrapper-has-no-len
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from Crypto.Protocol.KDF import scrypt
    _l_(402273)

except ImportError:
    pass
try:
    from Crypto.Cipher import AES
    _l_(402275)

except ImportError:
    pass
try:
    from Crypto.Random import get_random_bytes
    _l_(402277)

except ImportError:
    pass

class transmitter():
    _l_(402438)


    def __init__(self):
        _l_(402298)


        _n_(402278, "self", lambda: self).random_password = None
        _l_(402279)
        _n_(402280, "self", lambda: self).message_plain = True
        _l_(402281)
        _n_(402282, "self", lambda: self).key = None
        _l_(402283)
        _n_(402284, "self", lambda: self).salt = None
        _l_(402285)

        _c_(402288, _a_(402287, _n_(402286, "self", lambda: self), "password_option"))
        _l_(402289)
        _c_(402292, _a_(402291, _n_(402290, "self", lambda: self), "text_option"))
        _l_(402293)
        _c_(402296, _a_(402295, _n_(402294, "self", lambda: self), "encrypt"))
        _l_(402297)


    def password_option(self):
        _l_(402326)


        while ( _a_(402300, _n_(402299, "self", lambda: self), "random_password") == None ):
            _l_(402325)


            random = _c_(402306, _a_(402305, _c_(402304, _a_(402303, _c_(402302, _n_(402301, "input", lambda: input), "\nDo you want to generate a random symmetric key? (y/n)\n\n>>> "), "strip")), "lower"))
            _l_(402307)

            if _n_(402308, "random", lambda: random) == "y":
                _l_(402324)

                _n_(402309, "self", lambda: self).random_password = True
                _l_(402310)
                _c_(402313, _a_(402312, _n_(402311, "self", lambda: self), "random"))
                _l_(402314)

            elif _n_(402315, "random", lambda: random) == "n":
                _l_(402323)

                _n_(402316, "self", lambda: self).random_password = False
                _l_(402317)
                _c_(402320, _a_(402319, _n_(402318, "self", lambda: self), "random"))
                _l_(402321)

            else:
                pass
                _l_(402322)

    def text_option(self):
        _l_(402371)


        if _a_(402328, _n_(402327, "self", lambda: self), "message_plain"):
            _l_(402370)


            question = _c_(402332, _a_(402331, _c_(402330, _n_(402329, "input", lambda: input), "\nHow will you enter your message?\n\n[1] file\n\n[2] directly in the program\n\n>>> "), "strip"))
            _l_(402333)

            if _n_(402334, "question", lambda: question) == "1":
                _l_(402369)

                path = _c_(402336, _n_(402335, "input", lambda: input), "\nEnter the file path\n\n>>> ")
                _l_(402337)
                name = _c_(402340, _a_(402339, _n_(402338, "path", lambda: path), "split"), "\\")[-1]
                _l_(402341)
                with _c_(402344, _n_(402342, "open", lambda: open), _n_(402343, "name", lambda: name),mode = "r") as _a_(402346, _n_(402345, "self", lambda: self), "message_plain"):
                    _l_(402354)

                    _c_(402352, _a_(402351, _c_(402350, _a_(402349, _a_(402348, _n_(402347, "self", lambda: self), "message_plain"), "read")), "encode"), "utf-8")
                    _l_(402353)

            elif _n_(402355, "question", lambda: question) == "2":
                _l_(402368)

                _n_(402356, "self", lambda: self).message_plain = _c_(402360, _a_(402359, _c_(402358, _n_(402357, "input", lambda: input), "\nEnter your message\n\n>>> "), "strip"))
                _l_(402361)
                _n_(402362, "self", lambda: self).message_plain = _c_(402366, _a_(402365, _a_(402364, _n_(402363, "self", lambda: self), "message_plain"), "encode"), "utf-8")
                _l_(402367)


    def random(self):
        _l_(402407)


        if _a_(402373, _n_(402372, "self", lambda: self), "random_password"):
            _l_(402406)

            password = _c_(402375, _a_(402374, "password", "encode"), "utf-8")
            _l_(402376)
            _n_(402377, "self", lambda: self).salt = _c_(402379, _n_(402378, "get_random_bytes", lambda: get_random_bytes), 16)
            _l_(402380)
            _n_(402381, "self", lambda: self).key = _c_(402386, _n_(402382, "scrypt", lambda: scrypt), _n_(402383, "password", lambda: password), _a_(402385, _n_(402384, "self", lambda: self), "salt"), 16, N=2**14, r=8, p=1)
            _l_(402387)

        else:
            password = _c_(402391, _a_(402390, _c_(402389, _n_(402388, "input", lambda: input), "\nEnter your password\n\n>>> "), "strip"))
            _l_(402392)
            _n_(402393, "self", lambda: self).salt = _c_(402395, _n_(402394, "get_random_bytes", lambda: get_random_bytes), 16)
            _l_(402396)
            _n_(402397, "self", lambda: self).key = _c_(402404, _n_(402398, "scrypt", lambda: scrypt), _c_(402401, _a_(402400, _n_(402399, "password", lambda: password), "encode"), "utf-8"), _a_(402403, _n_(402402, "self", lambda: self), "salt"), 16, N=2**14, r=8, p=1)
            _l_(402405)


    def encrypt(self):
        _l_(402437)


        cipher = _c_(402414, _a_(402409, _n_(402408, "AES", lambda: AES), "new"), _a_(402411, _n_(402410, "self", lambda: self), "key"),_a_(402413, _n_(402412, "AES", lambda: AES), "MODE_GCM"))
        _l_(402415)
        _c_(402418, _a_(402417, _n_(402416, "cipher", lambda: cipher), "update"), b"header")
        _l_(402419)
        cipher_text,tag_mac = _c_(402424, _a_(402421, _n_(402420, "cipher", lambda: cipher), "encrypt_and_digest"), _a_(402423, _n_(402422, "self", lambda: self), "message_plain"))
        _l_(402425)
        transmitted_message = _n_(402426, "cipher_text", lambda: cipher_text),_n_(402427, "tag_mac", lambda: tag_mac),_a_(402429, _n_(402428, "self", lambda: self), "salt"),_a_(402431, _n_(402430, "cipher", lambda: cipher), "nonce")
        _l_(402432)
        _c_(402435, _n_(402433, "Receptor", lambda: Receptor), _n_(402434, "transmitted_message", lambda: transmitted_message))
        _l_(402436)

class receiver():
    _l_(402503)


    def __init__(self,received_message):
        _l_(402457)

        # nonce = aes_cipher.nonce
        _n_(402439, "self", lambda: self).cipher_text,_n_(402440, "self", lambda: self).tag_mac,_n_(402441, "self", lambda: self).salt,_n_(402442, "self", lambda: self).nonce = _n_(402443, "received_message", lambda: received_message)
        _l_(402444)
        _c_(402455, _a_(402446, _n_(402445, "self", lambda: self), "decrypt"), _a_(402448, _n_(402447, "self", lambda: self), "cipher_text"),_a_(402450, _n_(402449, "self", lambda: self), "tag_mac"),_a_(402452, _n_(402451, "self", lambda: self), "salt"),_a_(402454, _n_(402453, "self", lambda: self), "nonce"))
        _l_(402456)

    def decrypt(self,cipher_text,tag_mac,salt,nonce):
        _l_(402502)


        try:
            _l_(402501)

            password = _c_(402461, _a_(402460, _c_(402459, _n_(402458, "input", lambda: input), "\nEnter your password\n\n>>> "), "strip"))
            _l_(402462)
            decryption_key = _c_(402468, _n_(402463, "scrypt", lambda: scrypt), _c_(402466, _a_(402465, _n_(402464, "password", lambda: password), "encode"), "utf-8"), _n_(402467, "salt", lambda: salt), 16, N=2**14, r=8, p=1)
            _l_(402469)
            cipher = _c_(402476, _a_(402471, _n_(402470, "AES", lambda: AES), "new"), _n_(402472, "decryption_key", lambda: decryption_key),_a_(402474, _n_(402473, "AES", lambda: AES), "MODE_GCM"),_n_(402475, "nonce", lambda: nonce))
            _l_(402477)
            _c_(402480, _a_(402479, _n_(402478, "cipher", lambda: cipher), "update"), b"header")
            _l_(402481)
            plain_text = _c_(402486, _a_(402483, _n_(402482, "cipher", lambda: cipher), "decrypt_and_verify"), _n_(402484, "cipher_text", lambda: cipher_text),_n_(402485, "tag_mac", lambda: tag_mac))
            _l_(402487)
            plain_text = _c_(402490, _a_(402489, _n_(402488, "plain_text", lambda: plain_text), "decode"), "utf-8")
            _l_(402491)
            _c_(402494, _n_(402492, "print", lambda: print), f"\nText -> {_n_(402493, 'plain_text', lambda: plain_text)}\n")
            _l_(402495)

        except _n_(402496, "ValueError", lambda: ValueError):
            _l_(402500)

            _c_(402498, _n_(402497, "print", lambda: print), "\nAn error has occurred..\n")
            _l_(402499)

if _n_(402504, "__name__", lambda: __name__) == '__main__':
    _l_(402508)

    init = _c_(402506, _n_(402505, "transmitter", lambda: transmitter))
    _l_(402507)