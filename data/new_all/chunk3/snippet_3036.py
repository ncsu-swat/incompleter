# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52389994/encrypting-text-with-cesar-cipher-str-replace-gives-typeerror-cant-convert-n
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import argparse
    _l_(561575)

except ImportError:
    pass

def parse_command_line():
    _l_(561614)

    parser=_c_(561578, _a_(561577, _n_(561576, "argparse", lambda: argparse), "ArgumentParser"))
    _l_(561579)
    _c_(561583, _a_(561581, _n_(561580, "parser", lambda: parser), "add_argument"), "infile",type=_n_(561582, "str", lambda: str),help="input file to be encrypted or decrypted")
    _l_(561584)

    _c_(561588, _a_(561586, _n_(561585, "parser", lambda: parser), "add_argument"), "-o outfile_path","--outfile outfile_path",type=_n_(561587, "str", lambda: str),help="output file")
    _l_(561589)
    _c_(561593, _a_(561591, _n_(561590, "parser", lambda: parser), "add_argument"), "-k KEY","--key KEY",type=_n_(561592, "int", lambda: int),default=1,help="encryption/decryption key (must be positive) (default= 1)")
    _l_(561594)
    _c_(561597, _a_(561596, _n_(561595, "parser", lambda: parser), "add_argument"), "-d","--decrypt",action="store_true",help="decrypt the input file")
    _l_(561598)
    _c_(561601, _a_(561600, _n_(561599, "parser", lambda: parser), "add_argument"), "-a","--all",action="store_false",help="decrypt using all keys [1, 25], save outputs in different files. (useful in case the key is lost orunknown)")
    _l_(561602)
    _c_(561605, _a_(561604, _n_(561603, "parser", lambda: parser), "add_argument"), "-v","--verbose",action="store_true",help="Verbose mode")
    _l_(561606)

    args=_c_(561609, _a_(561608, _n_(561607, "parser", lambda: parser), "parse_args"))
    _l_(561610)
    aux = _n_(561611, "args", lambda: args) 
    _l_(561612) 
    return aux 
    pass
    _l_(561613)



def transform(message, key, decrypt):
    _l_(561635)


    #TODO: Your code goes here
    if _n_(561615, "decrypt", lambda: decrypt):
        _l_(561631)

        for i in _n_(561616, "message", lambda: message):
            _l_(561630)

            temp=_c_(561620, _n_(561617, "shift", lambda: shift), _n_(561618, "i", lambda: i),_n_(561619, "key", lambda: key))
            _l_(561621)
            transformed_message=_c_(561626, _a_(561623, _n_(561622, "message", lambda: message), "replace"), _n_(561624, "i", lambda: i),_n_(561625, "temp", lambda: temp),1)
            _l_(561627)
            message=_n_(561628, "transformed_message", lambda: transformed_message)
            _l_(561629)
    aux = _n_(561632, "transformed_message", lambda: transformed_message)
    _l_(561633)
    return aux
    pass
    _l_(561634)
def shift(char, key):
    _l_(561673)

    # ordered lower case alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    _l_(561636)

    # will contain shifted lower case alphabet
    shifted_alphabet = ''
    _l_(561637)
    for i in _c_(561642, _n_(561638, "range", lambda: range), _c_(561641, _n_(561639, "len", lambda: len), _n_(561640, "alphabet", lambda: alphabet))):
        _l_(561648)

        shifted_alphabet = _n_(561643, "shifted_alphabet", lambda: shifted_alphabet) + _n_(561644, "alphabet", lambda: alphabet)[(_n_(561645, "i", lambda: i) + _n_(561646, "key", lambda: key)) % 26]
        _l_(561647)

    if _c_(561651, _a_(561650, _n_(561649, "char", lambda: char), "isalpha")):
        _l_(561672)

        char_index = _c_(561657, _a_(561653, _n_(561652, "alphabet", lambda: alphabet), "index"), _c_(561656, _a_(561655, _n_(561654, "char", lambda: char), "lower")))
        _l_(561658)
        shifted_char = _n_(561659, "shifted_alphabet", lambda: shifted_alphabet)[_n_(561660, "char_index", lambda: char_index)]
        _l_(561661)

        # keep char's case (upper or lower)
        if _c_(561664, _a_(561663, _n_(561662, "char", lambda: char), "isupper")):
            _l_(561671)

            aux = _c_(561667, _a_(561666, _n_(561665, "shifted_char", lambda: shifted_char), "upper"))
            _l_(561668)
            return aux
        else:
            aux = _n_(561669, "shifted_char", lambda: shifted_char)
            _l_(561670)
            return aux

def main():
    _l_(561709)

    # parse command line arguments
    args = _c_(561675, _n_(561674, "parse_command_line", lambda: parse_command_line))
    _l_(561676)

    # key is specified
    if not _a_(561678, _n_(561677, "args", lambda: args), "all"):
        _l_(561708)

        # encrypt/decrypt content of infile
        outstring = _c_(561685, _n_(561679, "transform", lambda: transform), _n_(561680, "instring", lambda: instring), _a_(561682, _n_(561681, "args", lambda: args), "key"), _a_(561684, _n_(561683, "args", lambda: args), "decrypt"))
        _l_(561686)

        # write content of outstring to outfile
        _c_(561691, _n_(561687, "write_file", lambda: write_file), _n_(561688, "outstring", lambda: outstring), _a_(561690, _n_(561689, "args", lambda: args), "outfile"))
        _l_(561692)

    # key is not specified, try all keys from 1 to 25 to decrypt infile
    else:
        for k in _c_(561694, _n_(561693, "range", lambda: range), 1, 26):
            _l_(561707)

            # decrypt content of infile
            outstring = _c_(561698, _n_(561695, "transform", lambda: transform), _n_(561696, "instring", lambda: instring), _n_(561697, "k", lambda: k), True)
            _l_(561699)

            # write content of outstring to outfile
            _c_(561705, _n_(561700, "write_file", lambda: write_file), _n_(561701, "outstring", lambda: outstring), "decrypted_by_" + _c_(561704, _n_(561702, "str", lambda: str), _n_(561703, "k", lambda: k)) + ".txt")
            _l_(561706)

if _n_(561710, "__name__", lambda: __name__) == '__main__':
    _l_(561714)

    _c_(561712, _n_(561711, "main", lambda: main))
    _l_(561713)