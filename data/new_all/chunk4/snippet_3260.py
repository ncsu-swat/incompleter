# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76616348/attributeerror-xyz-object-has-no-attribute-yzx
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from src.invoice_generator.models.client import Client
    _l_(619496)

except ImportError:
    pass


class Seller(_n_(619497, "Client", lambda: Client)):
    _l_(619623)

    """
    Seller model

    Attributes:
        :param name: str - seller name
        :param street: str - seller street
        :param city: str - seller city
        :param postal_code: str - seller postal code
        :param phone: str - seller phone number
        :param email: str - seller email address
        :param nip: str - seller NIP number
        :param regon: str - seller REGON number
        :param bank_account: str - seller bank account number

    Methods:
        :__init__: initialize Seller object
        :__str__: return string representation of Seller object
    """

    def __init__(self, name: _n_(619498, "str", lambda: str), street: _n_(619499, "str", lambda: str), city: _n_(619500, "str", lambda: str), postal_code: _n_(619501, "str", lambda: str), phone: _n_(619502, "str", lambda: str), email: _n_(619503, "str", lambda: str), nip: _n_(619504, "str", lambda: str), regon: _n_(619505, "str", lambda: str), bank_account: _n_(619506, "str", lambda: str)) -> None:
        _l_(619542)

        _c_(619516, _a_(619508, _n_(619507, "super", lambda: super)(), "__init__"), _n_(619509, "name", lambda: name), _n_(619510, "street", lambda: street), _n_(619511, "city", lambda: city), _n_(619512, "postal_code", lambda: postal_code), _n_(619513, "phone", lambda: phone), _n_(619514, "email", lambda: email), _n_(619515, "nip", lambda: nip))
        _l_(619517)
        _n_(619518, "self", lambda: self).regon = _n_(619519, "regon", lambda: regon)
        _l_(619520)
        _n_(619521, "self", lambda: self).bank_account = _n_(619522, "bank_account", lambda: bank_account)
        _l_(619523)

        if not _c_(619526, _a_(619525, _n_(619524, "self", lambda: self), "validate")):
            _l_(619541)

            if not _c_(619529, _a_(619528, _n_(619527, "self", lambda: self), "validate_regon")):
                _l_(619533)

                raise _c_(619531, _n_(619530, "ValueError", lambda: ValueError), 'Invalid REGON number')
                _l_(619532)
            if not _c_(619536, _a_(619535, _n_(619534, "self", lambda: self), "validate_bank_account")):
                _l_(619540)

                raise _c_(619538, _n_(619537, "ValueError", lambda: ValueError), 'Invalid bank account number')
                _l_(619539)

    def __str__(self) -> _n_(619543, "str", lambda: str):
        _l_(619549)

        aux = f'super().__str__(), {_a_(619545, _n_(619544, "self", lambda: self), "regon")}, {_a_(619547, _n_(619546, "self", lambda: self), "bank_account")}'
        _l_(619548)
        return aux

    def validate(self) -> _n_(619550, 'bool', lambda: bool):
        _l_(619561)

        """
        Validate Seller object
        :return: bool - True if Seller object is valid, False otherwise
        """
        aux = _c_(619553, _a_(619552, _n_(619551, 'super', lambda: super)(), 'validate')) and _c_(619556, _a_(619555, _n_(619554, 'self', lambda: self), 'validate_regon')) and _c_(619559, _a_(619558, _n_(619557, 'self', lambda: self), 'validate_bank_account'))
        _l_(619560)
        return aux

    def validate_regon(self) -> _n_(619562, 'bool', lambda: bool):
        _l_(619593)

        """
        Validate REGON number
        :return: bool - True if REGON number is valid, False otherwise
        """
        regon = _c_(619566, _a_(619565, _a_(619564, _n_(619563, 'self', lambda: self), 'regon'), 'replace'), '-', '')
        _l_(619567)
        if _c_(619570, _n_(619568, 'len', lambda: len), _n_(619569, 'regon', lambda: regon)) != 9:
            _l_(619572)

            aux = False
            _l_(619571)
            return aux
        weights = [8, 9, 2, 3, 4, 5, 6, 7]
        _l_(619573)
        check_sum = _c_(619586, _n_(619574, 'sum', lambda: sum), [_c_(619578, _n_(619575, 'int', lambda: int), _n_(619576, 'regon', lambda: regon)[_n_(619577, 'i', lambda: i)]) * _n_(619579, 'weights', lambda: weights)[_n_(619580, 'i', lambda: i)] for i in _c_(619585, _n_(619581, 'range', lambda: range), _c_(619584, _n_(619582, 'len', lambda: len), _n_(619583, 'weights', lambda: weights)))])
        _l_(619587)
        aux = _n_(619588, 'check_sum', lambda: check_sum) % 11 == _c_(619591, _n_(619589, 'int', lambda: int), _n_(619590, 'regon', lambda: regon)[-1])
        _l_(619592)
        return aux

    def validate_bank_account(self) -> _n_(619594, 'bool', lambda: bool):
        _l_(619622)

        """
        Validate bank account number
        :return: bool - True if bank account number is valid, False otherwise
        """
        bank_account = _c_(619598, _a_(619597, _a_(619596, _n_(619595, 'self', lambda: self), 'bank_account'), 'replace'), '-', '')
        _l_(619599)
        if _c_(619602, _n_(619600, 'len', lambda: len), _n_(619601, 'bank_account', lambda: bank_account)) != 26:
            _l_(619604)

            aux = False
            _l_(619603)
            return aux
        weights = [1, 10, 3, 30, 9, 90, 27, 76, 81, 34, 49, 5, 50, 15, 53, 45, 62, 38, 89, 17, 73, 51, 25, 56, 75, 71]
        _l_(619605)
        check_sum = _c_(619618, _n_(619606, 'sum', lambda: sum), [_c_(619610, _n_(619607, 'int', lambda: int), _n_(619608, 'bank_account', lambda: bank_account)[_n_(619609, 'i', lambda: i)]) * _n_(619611, 'weights', lambda: weights)[_n_(619612, 'i', lambda: i)] for i in _c_(619617, _n_(619613, 'range', lambda: range), _c_(619616, _n_(619614, 'len', lambda: len), _n_(619615, 'weights', lambda: weights)))])
        _l_(619619)
        aux = _n_(619620, 'check_sum', lambda: check_sum) % 97 == 1
        _l_(619621)
        return aux