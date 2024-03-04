#Source: https://stackoverflow.com/questions/46052752/using-aes-encrypt-get-raise-typeerroronly-byte-strings-can-be-passed-to-c-code
import base64

import boto3
from Crypto.Cipher import AES


PAD = lambda s: s + (32 - len(s) % 32) * ' '


def get_arn(aws_data):
    return 'arn:aws:kms:{region}:{account_number}:key/{key_id}'.format(**aws_data)


def encrypt_data(aws_data, plaintext_message):
    kms_client = boto3.client(
        'kms',
        region_name=aws_data['region'])

    data_key = kms_client.generate_data_key(
        KeyId=aws_data['key_id'],
        KeySpec='AES_256')

    cipher_text_blob = data_key.get('CiphertextBlob')
    plaintext_key = data_key.get('Plaintext')

    # Note, does not use IV or specify mode... for demo purposes only.
    cypher = AES.new(plaintext_key, AES.MODE_ECB)
    encrypted_data = base64.b64encode(cypher.encrypt(PAD(plaintext_message)))

    # Need to preserve both of these data elements
    return encrypted_data, cipher_text_blob



def main():
    # Add your account number / region / KMS Key ID here.
    aws_data = {
        'region': 'eu-west-1',
        'account_number': '701177775058',
        'key_id': 'd67e033d-83ac-4b5e-93d4-aa6cdc3e292e',
    }

    # And your super secret message to envelope encrypt...
    plaintext = PAD('Hello, World!')

    # Store encrypted_data & cipher_text_blob in your persistent storage. You will need them both later.
    encrypted_data, cipher_text_blob = encrypt_data(aws_data, plaintext)
    print(encrypted_data)


if __name__ == '__main__':
    main()