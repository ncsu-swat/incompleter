# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66897035/attributeerror-hashlib-hash-object-has-no-attribute-startswith
# import libraries
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
      import hashlib
      _l_(435395)

except ImportError:
      pass
try:
      import random
      _l_(435397)

except ImportError:
      pass
try:
      import string
      _l_(435399)

except ImportError:
      pass
try:
      import json
      _l_(435401)

except ImportError:
      pass
try:
      import binascii
      _l_(435403)

except ImportError:
      pass
try:
      import numpy as np
      _l_(435405)

except ImportError:
      pass
try:
      import pandas as pd
      _l_(435407)

except ImportError:
      pass
try:
      import pylab as pl
      _l_(435409)

except ImportError:
      pass
try:
      import logging
      _l_(435411)

except ImportError:
      pass
try:
      import datetime
      _l_(435413)

except ImportError:
      pass
try:
      import collections
      _l_(435415)

except ImportError:
      pass
try:
      import Cryptodome
      _l_(435417)

except ImportError:
      pass
try:
      import Cryptodome.Random
      _l_(435419)

except ImportError:
      pass
try:
      from Cryptodome.Hash import SHA
      _l_(435421)

except ImportError:
      pass
try:
      from Cryptodome.PublicKey import RSA
      _l_(435423)

except ImportError:
      pass
try:
      from Cryptodome.Signature import PKCS1_v1_5
      _l_(435425)

except ImportError:
      pass


transactions = []
_l_(435426)
last_block_hash = ""
_l_(435427)
TPCoins = []
_l_(435428)

def sha256(message):
      _l_(435438)

      aux = _c_(435436, _a_(435435, _c_(435434, _a_(435430, _n_(435429, "hashlib", lambda: hashlib), "sha256"), _c_(435433, _a_(435432, _n_(435431, "message", lambda: message), "encode"), 'ascii')), "hexdigest"))
      _l_(435437)
      return aux

class Client:
      _l_(435476)

      def __init__(self):
            _l_(435463)

            random = _a_(435442, _c_(435441, _a_(435440, _a_(435439, Cryptodome, "Random"), "new")), "read")
            _l_(435443)
            _n_(435444, "self", lambda: self)._private_key = _c_(435448, _a_(435446, _n_(435445, "RSA", lambda: RSA), "generate"), 1024, _n_(435447, "random", lambda: random))
            _l_(435449)
            _n_(435450, "self", lambda: self)._public_key = _c_(435454, _a_(435453, _a_(435452, _n_(435451, "self", lambda: self), "_private_key"), "publickey"))
            _l_(435455)
            _n_(435456, "self", lambda: self)._signer = _c_(435461, _a_(435458, _n_(435457, "PKCS1_v1_5", lambda: PKCS1_v1_5), "new"), _a_(435460, _n_(435459, "self", lambda: self), "_private_key"))
            _l_(435462)

      @_n_(435464, "property", lambda: property)
      def identity(self):
            _l_(435475)

            aux = _c_(435473, _a_(435472, _c_(435471, _a_(435466, _n_(435465, "binascii", lambda: binascii), "hexlify"), _c_(435470, _a_(435469, _a_(435468, _n_(435467, "self", lambda: self), "_public_key"), "exportKey"), format='DER')), "decode"), 'ascii')
            _l_(435474)
            return aux

class Transaction:
      _l_(435619)

      def __init__(self, sender, recipient, value):
            _l_(435492)

            _n_(435477, "self", lambda: self).sender = _n_(435478, "sender", lambda: sender)
            _l_(435479)
            _n_(435480, "self", lambda: self).recipient = _n_(435481, "recipient", lambda: recipient)
            _l_(435482)
            _n_(435483, "self", lambda: self).value = _n_(435484, "value", lambda: value)
            _l_(435485)
            _n_(435486, "self", lambda: self).time = _c_(435490, _a_(435489, _a_(435488, _n_(435487, "datetime", lambda: datetime), "datetime"), "now")) 
            _l_(435491) 

      def to_dict(self):
            _l_(435512)

            if _a_(435494, _n_(435493, "self", lambda: self), "sender") == "Genesis":
                  _l_(435500)

                  identity = "Genesis"
                  _l_(435495)
            else:
               identity = _a_(435498, _a_(435497, _n_(435496, "self", lambda: self), "sender"), "identity")
               _l_(435499)
            aux = _c_(435510, _a_(435502, _n_(435501, "collections", lambda: collections), "OrderedDict"), {
               'sender': _n_(435503, "identity", lambda: identity),
               'recipient': _a_(435505, _n_(435504, "self", lambda: self), "recipient"),
               'value': _a_(435507, _n_(435506, "self", lambda: self), "value"),
               'time' : _a_(435509, _n_(435508, "self", lambda: self), "time")})
            _l_(435511)

            return aux

      def sign_transaction(self):
            _l_(435543)

            private_key = _a_(435515, _a_(435514, _n_(435513, "self", lambda: self), "sender"), "_private_key")
            _l_(435516)
            signer = _c_(435520, _a_(435518, _n_(435517, "PKCS1_v1_5", lambda: PKCS1_v1_5), "new"), _n_(435519, "private_key", lambda: private_key))
            _l_(435521)
            h = _c_(435531, _a_(435523, _n_(435522, "SHA", lambda: SHA), "new"), _c_(435530, _a_(435529, _c_(435528, _n_(435524, "str", lambda: str), _c_(435527, _a_(435526, _n_(435525, "self", lambda: self), "to_dict"))), "encode"), 'utf8'))
            _l_(435532)
            aux = _c_(435541, _a_(435540, _c_(435539, _a_(435534, _n_(435533, "binascii", lambda: binascii), "hexlify"), _c_(435538, _a_(435536, _n_(435535, "signer", lambda: signer), "sign"), _n_(435537, "h", lambda: h))), "decode"), 'ascii')
            _l_(435542)
            return aux

      def display_transaction(transaction):
            _l_(435580)

            #for transaction in transactions:
            dict = _c_(435546, _a_(435545, _n_(435544, "transaction", lambda: transaction), "to_dict"))
            _l_(435547)
            _c_(435550, _n_(435548, "print", lambda: print), "sender: " + _n_(435549, "dict", lambda: dict)['sender'])
            _l_(435551)
            _c_(435553, _n_(435552, "print", lambda: print), '-----')
            _l_(435554)
            _c_(435557, _n_(435555, "print", lambda: print), "recipient: " + _n_(435556, "dict", lambda: dict)['recipient'])
            _l_(435558)
            _c_(435560, _n_(435559, "print", lambda: print), '-----')
            _l_(435561)
            _c_(435566, _n_(435562, "print", lambda: print), "value: " + _c_(435565, _n_(435563, "str", lambda: str), _n_(435564, "dict", lambda: dict)['value']))
            _l_(435567)
            _c_(435569, _n_(435568, "print", lambda: print), '-----')
            _l_(435570)
            _c_(435575, _n_(435571, "print", lambda: print), "time: " + _c_(435574, _n_(435572, "str", lambda: str), _n_(435573, "dict", lambda: dict)['time']))
            _l_(435576)
            _c_(435578, _n_(435577, "print", lambda: print), '-----')
            _l_(435579)

      def dump_blockchain (self):
            _l_(435618)

            _c_(435587, _n_(435581, "print", lambda: print), "Number of blocks in the chain: " + _c_(435586, _n_(435582, "str", lambda: str), _c_(435585, _n_(435583, "len", lambda: len), _n_(435584, "self", lambda: self))))
            _l_(435588)
            for x in _c_(435593, _n_(435589, "range", lambda: range), _c_(435592, _n_(435590, "len", lambda: len), _n_(435591, "TPCoins", lambda: TPCoins))):
                  _l_(435617)

                  block_temp = _n_(435594, "TPCoins", lambda: TPCoins)[_n_(435595, "x", lambda: x)]
                  _l_(435596)
                  _c_(435601, _n_(435597, "print", lambda: print), "block # " + _c_(435600, _n_(435598, "str", lambda: str), _n_(435599, "x", lambda: x)))
                  _l_(435602)
                  for transaction in _a_(435604, _n_(435603, "block_temp", lambda: block_temp), "verified_transactions"):
                        _l_(435613)

                        _c_(435608, _a_(435606, _n_(435605, "Transaction", lambda: Transaction), "display_transaction"), _n_(435607, "transaction", lambda: transaction))
                        _l_(435609)
                        _c_(435611, _n_(435610, "print", lambda: print), '--------------')
                        _l_(435612)
                  _c_(435615, _n_(435614, "print", lambda: print), '=====================================')
                  _l_(435616)

class Block:
      _l_(435665)

      def __init__(self):
            _l_(435626)

            _n_(435620, "self", lambda: self).verified_transactions = []
            _l_(435621)
            _n_(435622, "self", lambda: self).previous_block_hash = ""
            _l_(435623)
            _n_(435624, "self", lambda: self).Nonce = ""
            _l_(435625)

      def mine(message, difficulty=1):
            _l_(435664)

            assert _n_(435627, "difficulty", lambda: difficulty) >= 1
            _l_(435628)
            prefix = '1' * _n_(435629, "difficulty", lambda: difficulty)
            _l_(435630)
            for i in _c_(435632, _n_(435631, "range", lambda: range), 1000):
                  _l_(435663)

                  digest = _c_(435647, _a_(435634, _n_(435633, "hashlib", lambda: hashlib), "sha256"), _c_(435641, _a_(435640, _c_(435639, _n_(435635, "str", lambda: str), _c_(435638, _n_(435636, "hash", lambda: hash), _n_(435637, "message", lambda: message))), "encode"), 'utf-8') + _c_(435646, _a_(435645, _c_(435644, _n_(435642, "str", lambda: str), _n_(435643, "i", lambda: i)), "encode"), 'utf-8'))
                  _l_(435648)
                  if _c_(435652, _a_(435650, _n_(435649, "digest", lambda: digest), "startswith"), _n_(435651, "prefix", lambda: prefix)):
                        _l_(435660)

                        _c_(435658, _n_(435653, "print", lambda: print), "after " + _c_(435656, _n_(435654, "str", lambda: str), _n_(435655, "i", lambda: i)) + " iterations found nonce: "+ _n_(435657, "digest", lambda: digest))
                        _l_(435659)
                  aux = _n_(435661, "digest", lambda: digest)
                  _l_(435662)
                  return aux


#genesis block & users initialisation
Thomas = _c_(435667, _n_(435666, "Client", lambda: Client))
_l_(435668)
IoT_Sensor = _c_(435670, _n_(435669, "Client", lambda: Client))
_l_(435671)
Node = _c_(435673, _n_(435672, "Client", lambda: Client))
_l_(435674)
IoT_Device = _c_(435676, _n_(435675, "Client", lambda: Client))
_l_(435677)
t0 = _c_(435681, _n_(435678, "Transaction", lambda: Transaction), "Genesis",_a_(435680, _n_(435679, "Thomas", lambda: Thomas), "identity"),200.0)
_l_(435682)
block0 = _c_(435684, _n_(435683, "Block", lambda: Block))
_l_(435685)
_n_(435686, "block0", lambda: block0).previous_block_hash = None
_l_(435687)
Nonce = None
_l_(435688)
_c_(435693, _a_(435691, _a_(435690, _n_(435689, "block0", lambda: block0), "verified_transactions"), "append"), _n_(435692, "t0", lambda: t0))
_l_(435694)
digest = _c_(435697, _n_(435695, "hash", lambda: hash), _n_(435696, "block0", lambda: block0))
_l_(435698)
last_block_hash = _n_(435699, "digest", lambda: digest)
_l_(435700)
_c_(435704, _a_(435702, _n_(435701, "TPCoins", lambda: TPCoins), "append"), _n_(435703, "block0", lambda: block0))
_l_(435705)
_c_(435709, _a_(435707, _n_(435706, "Transaction", lambda: Transaction), "dump_blockchain"), _n_(435708, "TPCoins", lambda: TPCoins))
_l_(435710)
_c_(435713, _a_(435712, _n_(435711, "Block", lambda: Block), "mine"), "test message", 2)
_l_(435714)