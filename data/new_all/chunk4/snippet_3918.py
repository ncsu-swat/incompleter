# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65322686/why-am-i-receiving-either-a-typeerror-or-unicode-decode-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def read_file(filename):
    _l_(605013)

    '''procedure to open a file and read its contents'''
    _l_(605001)
    #open a file
    file = _c_(605004, _n_(605002, "open", lambda: open), _n_(605003, "filename", lambda: filename), 'r')
    _l_(605005)
    #read the file
    filetext = _c_(605008, _a_(605007, _n_(605006, "file", lambda: file), "read"))
    _l_(605009)
    #close the file
    _a_(605011, _n_(605010, "file", lambda: file), "close")
    _l_(605012)

#read the file 'passwords.txt'
_c_(605015, _n_(605014, "read_file", lambda: read_file), 'passwords.txt')
_l_(605016)

#convert file contents into a common hash
def hash_text(filename):
    _l_(605046)

    ''' Function takes contents of the file passwords.txt and converts it to
        SHA1, saving result in a new file'''
    _l_(605017)
    #read the passwords.txt file
    _c_(605019, _n_(605018, "read_file", lambda: read_file), 'passwords.txt')
    _l_(605020)
    try:
        import hashlib
        _l_(605022)

    except ImportError:
        pass
    #hash whatever file is input 
    hash_object = _c_(605026, _a_(605024, _n_(605023, "hashlib", lambda: hashlib), "sha1"), _n_(605025, "filename", lambda: filename))
    _l_(605027)
    hex_dig = _c_(605030, _a_(605029, _n_(605028, "hash_object", lambda: hash_object), "hexdigest"))
    _l_(605031)
    _c_(605034, _n_(605032, "print", lambda: print), _n_(605033, "hex_dig", lambda: hex_dig))
    _l_(605035)
    #create a new file to store the hashed passwords in
    hash_store = _c_(605037, _n_(605036, "open", lambda: open), "hashwords.txt", "x", "a")
    _l_(605038)
    #write to the file
    hashedtext = _c_(605041, _a_(605040, _n_(605039, "hash_store", lambda: hash_store), "append"))
    _l_(605042)
    #close the file
    _a_(605044, _n_(605043, "hash_store", lambda: hash_store), "close")
    _l_(605045)

#run the function
_c_(605048, _n_(605047, "hash_text", lambda: hash_text), 'passwords.txt')
_l_(605049)