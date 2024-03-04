#Source: https://stackoverflow.com/questions/45762517/attributeerror-rsa-object-has-no-attribute-n
from Rsa import RsaEncryptionAndDecryption
from appJar import gui

app = gui()
rsa = RsaEncryptionAndDecryption.Rsa()

def encode(name):
    msg = app.getEntry('Input to Encode Here')
    if msg != '':
        p, q = rsa.findingPandQ()

        while p == q:
            p, q = rsa.findingPandQ()

        n, e, d = rsa.generate_keys(p, q)

        print(n, e, d)