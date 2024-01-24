#Source: https://stackoverflow.com/questions/59524510/typeerror-object-of-type-io-textiowrapper-has-no-len
from Crypto.Protocol.KDF import scrypt
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class transmitter():

    def __init__(self):

        self.random_password = None
        self.message_plain = True
        self.key = None
        self.salt = None

        self.password_option()
        self.text_option()
        self.encrypt()


    def password_option(self):

        while ( self.random_password == None ):

            random = input("\nDo you want to generate a random symmetric key? (y/n)\n\n>>> ").strip().lower()

            if random == "y":
                self.random_password = True
                self.random()

            elif random == "n":
                self.random_password = False
                self.random()

            else:
                pass

    def text_option(self):

        if self.message_plain:

            question = input("\nHow will you enter your message?\n\n[1] file\n\n[2] directly in the program\n\n>>> ").strip()

            if question == "1":
                path = input("\nEnter the file path\n\n>>> ")
                name = path.split("\\")[-1]
                with open(name,mode = "r") as self.message_plain:
                    self.message_plain.read().encode("utf-8")

            elif question == "2":
                self.message_plain = input("\nEnter your message\n\n>>> ").strip()
                self.message_plain = self.message_plain.encode("utf-8")


    def random(self):

        if self.random_password:
            password = "password".encode("utf-8")
            self.salt = get_random_bytes(16)
            self.key = scrypt(password, self.salt, 16, N=2**14, r=8, p=1)

        else:
            password = input("\nEnter your password\n\n>>> ").strip()
            self.salt = get_random_bytes(16)
            self.key = scrypt(password.encode("utf-8"), self.salt, 16, N=2**14, r=8, p=1)


    def encrypt(self):

        cipher = AES.new(self.key,AES.MODE_GCM)
        cipher.update(b"header")
        cipher_text,tag_mac = cipher.encrypt_and_digest(self.message_plain)
        transmitted_message = cipher_text,tag_mac,self.salt,cipher.nonce
        Receptor(transmitted_message)

class receiver():

    def __init__(self,received_message):
        # nonce = aes_cipher.nonce
        self.cipher_text,self.tag_mac,self.salt,self.nonce = received_message
        self.decrypt(self.cipher_text,self.tag_mac,self.salt,self.nonce)

    def decrypt(self,cipher_text,tag_mac,salt,nonce):

        try:
            password = input("\nEnter your password\n\n>>> ").strip()
            decryption_key = scrypt(password.encode("utf-8"), salt, 16, N=2**14, r=8, p=1)
            cipher = AES.new(decryption_key,AES.MODE_GCM,nonce)
            cipher.update(b"header")
            plain_text = cipher.decrypt_and_verify(cipher_text,tag_mac)
            plain_text = plain_text.decode("utf-8")
            print(f"\nText -> {plain_text}\n")

        except ValueError:
            print("\nAn error has occurred..\n")

if __name__ == '__main__':
    init = transmitter()