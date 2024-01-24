# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46052752/using-aes-encrypt-get-raise-typeerroronly-byte-strings-can-be-passed-to-c-code
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import base64
    _l_(395362)

except ImportError:
    pass
try:
    import boto3
    _l_(395364)

except ImportError:
    pass
try:
    from Crypto.Cipher import AES
    _l_(395366)

except ImportError:
    pass


PAD = lambda s: _n_(395367, "s", lambda: s) + (32 - _c_(395370, _n_(395368, "len", lambda: len), _n_(395369, "s", lambda: s)) % 32) * ' '
_l_(395371)


def get_arn(aws_data):
    _l_(395376)

    aux = _c_(395374, _a_(395372, 'arn:aws:kms:{region}:{account_number}:key/{key_id}', "format"), **_n_(395373, "aws_data", lambda: aws_data))
    _l_(395375)
    return aux


def encrypt_data(aws_data, plaintext_message):
    _l_(395415)

    kms_client = _c_(395380, _a_(395378, _n_(395377, "boto3", lambda: boto3), "client"), 'kms',
        region_name=_n_(395379, "aws_data", lambda: aws_data)['region'])
    _l_(395381)

    data_key = _c_(395385, _a_(395383, _n_(395382, "kms_client", lambda: kms_client), "generate_data_key"), KeyId=_n_(395384, "aws_data", lambda: aws_data)['key_id'],
        KeySpec='AES_256')
    _l_(395386)

    cipher_text_blob = _c_(395389, _a_(395388, _n_(395387, "data_key", lambda: data_key), "get"), 'CiphertextBlob')
    _l_(395390)
    plaintext_key = _c_(395393, _a_(395392, _n_(395391, "data_key", lambda: data_key), "get"), 'Plaintext')
    _l_(395394)

    # Note, does not use IV or specify mode... for demo purposes only.
    cypher = _c_(395400, _a_(395396, _n_(395395, "AES", lambda: AES), "new"), _n_(395397, "plaintext_key", lambda: plaintext_key), _a_(395399, _n_(395398, "AES", lambda: AES), "MODE_ECB"))
    _l_(395401)
    encrypted_data = _c_(395410, _a_(395403, _n_(395402, "base64", lambda: base64), "b64encode"), _c_(395409, _a_(395405, _n_(395404, "cypher", lambda: cypher), "encrypt"), _c_(395408, _n_(395406, "PAD", lambda: PAD), _n_(395407, "plaintext_message", lambda: plaintext_message))))
    _l_(395411)
    aux = _n_(395412, "encrypted_data", lambda: encrypted_data), _n_(395413, "cipher_text_blob", lambda: cipher_text_blob)
    _l_(395414)

    # Need to preserve both of these data elements
    return aux



def main():
    _l_(395429)

    # Add your account number / region / KMS Key ID here.
    aws_data = {
        'region': 'eu-west-1',
        'account_number': '701177775058',
        'key_id': 'd67e033d-83ac-4b5e-93d4-aa6cdc3e292e',
    }
    _l_(395416)

    # And your super secret message to envelope encrypt...
    plaintext = _c_(395418, _n_(395417, "PAD", lambda: PAD), 'Hello, World!')
    _l_(395419)

    # Store encrypted_data & cipher_text_blob in your persistent storage. You will need them both later.
    encrypted_data, cipher_text_blob = _c_(395423, _n_(395420, "encrypt_data", lambda: encrypt_data), _n_(395421, "aws_data", lambda: aws_data), _n_(395422, "plaintext", lambda: plaintext))
    _l_(395424)
    _c_(395427, _n_(395425, "print", lambda: print), _n_(395426, "encrypted_data", lambda: encrypted_data))
    _l_(395428)


if _n_(395430, "__name__", lambda: __name__) == '__main__':
    _l_(395434)

    _c_(395432, _n_(395431, "main", lambda: main))
    _l_(395433)