# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59111440/python3-cannot-import-local-module-due-to-filenotfounderror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import urllib.request, re, os
    _l_(529342)

except ImportError:
    pass

def getKey(url, path):
    _l_(529349)

    _c_(529347, _a_(529344, _a_(529343, urllib, "request"), "urlretrieve"), _n_(529345, "url", lambda: url), 'C:\\code\\'+_n_(529346, "path", lambda: path))
    _l_(529348)

def readFiles(keyFile, targetFile, outfile):
    _l_(529385)

    infile = _n_(529350, "keyFile", lambda: keyFile)                                            # read in the input file name
    _l_(529351)                                            # read in the input file name
    infd = _c_(529354, _n_(529352, "open", lambda: open), 'C:\\code\\'+_n_(529353, "infile", lambda: infile),"r")                     # open the file and create the file descriptor infd
    _l_(529355)                     # open the file and create the file descriptor infd

    key = _c_(529358, _a_(529357, _n_(529356, "infd", lambda: infd), "read"))
    _l_(529359)
    key = _c_(529362, _a_(529361, _n_(529360, "key", lambda: key), "strip"), '\n')
    _l_(529363)
    #print('key= '+key)

    infile = _n_(529364, "targetFile", lambda: targetFile)
    _l_(529365)
    infd = _c_(529368, _n_(529366, "open", lambda: open), 'C:\\code\\'+_n_(529367, "infile", lambda: infile), "r")
    _l_(529369)
    ptext = _c_(529374, _a_(529373, _c_(529372, _a_(529371, _n_(529370, "infd", lambda: infd), "read")), "strip"), '\n')
    _l_(529375)

    _a_(529377, _n_(529376, "infd", lambda: infd), "close")
    _l_(529378)

    _c_(529383, _n_(529379, "xor", lambda: xor), _n_(529380, "outfile", lambda: outfile), _n_(529381, "ptext", lambda: ptext), _n_(529382, "key", lambda: key))
    _l_(529384)

def xor(outfile, ptext, key):
    _l_(529439)

    outfd = _c_(529388, _n_(529386, "open", lambda: open), 'C:\\code\\'+_n_(529387, "outfile", lambda: outfile), "w")
    _l_(529389)

    pLength = _c_(529392, _n_(529390, "len", lambda: len), _n_(529391, "ptext", lambda: ptext))
    _l_(529393)

    #get the length of the plaintext and cut the key into the same size
    keyChunks = [_n_(529394, "key", lambda: key)[_n_(529395, "i", lambda: i):_n_(529396, "i", lambda: i)+_n_(529397, "pLength", lambda: pLength)] for i in _c_(529403, _n_(529398, "range", lambda: range), 0, _c_(529401, _n_(529399, "len", lambda: len), _n_(529400, "key", lambda: key)), _n_(529402, "pLength", lambda: pLength))]
    _l_(529404)

    i = 0
    _l_(529405)

    while _n_(529406, "i", lambda: i) < _c_(529409, _n_(529407, "len", lambda: len), _n_(529408, "keyChunks", lambda: keyChunks)):
        _l_(529424)

        a = _c_(529412, _n_(529410, "int", lambda: int), _n_(529411, "ptext", lambda: ptext))
        _l_(529413)
        b = _c_(529417, _n_(529414, "int", lambda: int), _n_(529415, "keyChunks", lambda: keyChunks)[_n_(529416, "i", lambda: i)])
        _l_(529418)

        out = _n_(529419, "a", lambda: a) ^ _n_(529420, "b", lambda: b)
        _l_(529421)

        i=_n_(529422, "i", lambda: i)+1
        _l_(529423)

    outfd = _c_(529427, _n_(529425, "open", lambda: open), 'C:\\code\\'+_n_(529426, "outfile", lambda: outfile), "w")
    _l_(529428)
    _c_(529434, _a_(529430, _n_(529429, "outfd", lambda: outfd), "write"), _c_(529433, _n_(529431, "str", lambda: str), _n_(529432, "out", lambda: out)))
    _l_(529435)
    _a_(529437, _n_(529436, "outfd", lambda: outfd), "close")
    _l_(529438)

def cleanup(targetFile):
    _l_(529445)

    _c_(529443, _a_(529441, _n_(529440, "os", lambda: os), "remove"), _n_(529442, "targetFile", lambda: targetFile))
    _l_(529444)


def enc():
    _l_(529457)

    outfile = 'affk.xor'
    _l_(529446)
    _c_(529448, _n_(529447, "getKey", lambda: getKey), 'http://192.168.56.10/sym.key', 'sym.key')
    _l_(529449)
    _c_(529452, _n_(529450, "readFiles", lambda: readFiles), 'sym.key', 'affk.txt', _n_(529451, "outfile", lambda: outfile))
    _l_(529453)
    _c_(529455, _n_(529454, "cleanup", lambda: cleanup), 'C:/code/affk.txt')
    _l_(529456)

def dec():
    _l_(529472)

    outfile = 'affk.txt'
    _l_(529458)
    _c_(529460, _n_(529459, "getKey", lambda: getKey), 'http://192.168.56.10/sym.key', 'sym.key')
    _l_(529461)
    _c_(529464, _n_(529462, "readFiles", lambda: readFiles), 'sym.key', 'affk.xor', _n_(529463, "outfile", lambda: outfile))
    _l_(529465)
    _c_(529467, _n_(529466, "cleanup", lambda: cleanup), 'C:/code/affk.xor')
    _l_(529468)
    _c_(529470, _n_(529469, "cleanup", lambda: cleanup), 'C:/code/sym.key')
    _l_(529471)

_c_(529474, _n_(529473, "enc", lambda: enc))
_l_(529475)
#dec()