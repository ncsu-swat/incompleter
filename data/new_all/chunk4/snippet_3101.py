# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46050732/aws-encrypt-typeerror-cant-concat-str-to-bytes
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import base64
    _l_(610151)

except ImportError:
    pass
try:
    import boto3
    _l_(610153)

except ImportError:
    pass
try:
    from Crypto.Cipher import AES
    _l_(610155)

except ImportError:
    pass

PAD = lambda s: _n_(610156, "s", lambda: s) + (32 - _c_(610159, _n_(610157, "len", lambda: len), _n_(610158, "s", lambda: s)) % 32) * ' '
_l_(610160)


def get_arn(aws_data):
    _l_(610165)

    aux = _c_(610163, _a_(610161, 'arn:aws:kms:{region}:{account_number}:key/{key_id}', "format"), **_n_(610162, "aws_data", lambda: aws_data))
    _l_(610164)
    return aux


def encrypt_data(aws_data, plaintext_message):
    _l_(610204)

    kms_client = _c_(610169, _a_(610167, _n_(610166, "boto3", lambda: boto3), "client"), 'kms',
        region_name=_n_(610168, "aws_data", lambda: aws_data)['region'])
    _l_(610170)

    data_key = _c_(610174, _a_(610172, _n_(610171, "kms_client", lambda: kms_client), "generate_data_key"), KeyId=_n_(610173, "aws_data", lambda: aws_data)['key_id'],
        KeySpec='AES_256')
    _l_(610175)

    cipher_text_blob = _c_(610178, _a_(610177, _n_(610176, "data_key", lambda: data_key), "get"), 'CiphertextBlob')
    _l_(610179)
    plaintext_key = _c_(610182, _a_(610181, _n_(610180, "data_key", lambda: data_key), "get"), 'Plaintext')
    _l_(610183)

    # Note, does not use IV or specify mode... for demo purposes only.
    cypher = _c_(610189, _a_(610185, _n_(610184, "AES", lambda: AES), "new"), _n_(610186, "plaintext_key", lambda: plaintext_key), _a_(610188, _n_(610187, "AES", lambda: AES), "MODE_EAX"))
    _l_(610190)
    encrypted_data = _c_(610199, _a_(610192, _n_(610191, "base64", lambda: base64), "b64encode"), _c_(610198, _a_(610194, _n_(610193, "cypher", lambda: cypher), "encrypt"), _c_(610197, _n_(610195, "PAD", lambda: PAD), _n_(610196, "plaintext_message", lambda: plaintext_message))))
    _l_(610200)
    aux = _n_(610201, "encrypted_data", lambda: encrypted_data), _n_(610202, "cipher_text_blob", lambda: cipher_text_blob)
    _l_(610203)

    # Need to preserve both of these data elements
    return aux



def main():
    _l_(610216)

    # Add your account number / region / KMS Key ID here.
    aws_data = {
        'region': 'eu-west-1',
        'account_number': '70117777xxxx',
        'key_id': 'xxxxxxx-83ac-4b5e-93d4-xxxxxxxx',
    }
    _l_(610205)

    # And your super secret message to envelope encrypt...
    plaintext = b'Hello, World!'
    _l_(610206)

    # Store encrypted_data & cipher_text_blob in your persistent storage. You will need them both later.
    encrypted_data, cipher_text_blob = _c_(610210, _n_(610207, "encrypt_data", lambda: encrypt_data), _n_(610208, "aws_data", lambda: aws_data), _n_(610209, "plaintext", lambda: plaintext))
    _l_(610211)
    _c_(610214, _n_(610212, "print", lambda: print), _n_(610213, "encrypted_data", lambda: encrypted_data))
    _l_(610215)


if _n_(610217, "__name__", lambda: __name__) == '__main__':
    _l_(610221)

    _c_(610219, _n_(610218, "main", lambda: main))
    _l_(610220)