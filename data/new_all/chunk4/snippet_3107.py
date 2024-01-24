# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45685446/attributeerror-str-object-has-no-attribute-build-shift-dict
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import string
    _l_(624225)

except ImportError:
    pass


### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    _l_(624254)

    '''
    file_name (string): the name of the file containing 
    the list of words to load    

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    _l_(624226)
    _c_(624228, _n_(624227, "print", lambda: print), 'Loading word list from file...')
    _l_(624229)
    # inFile: file
    in_file = _c_(624232, _n_(624230, "open", lambda: open), _n_(624231, "file_name", lambda: file_name), 'r')
    _l_(624233)
    # line: string
    line = _c_(624236, _a_(624235, _n_(624234, "in_file", lambda: in_file), "readline"))
    _l_(624237)
    # word_list: list of strings
    word_list = _c_(624240, _a_(624239, _n_(624238, "line", lambda: line), "split"))
    _l_(624241)
    _c_(624246, _n_(624242, "print", lambda: print), '  ', _c_(624245, _n_(624243, "len", lambda: len), _n_(624244, "word_list", lambda: word_list)), 'words loaded.')
    _l_(624247)
    _c_(624250, _a_(624249, _n_(624248, "in_file", lambda: in_file), "close"))
    _l_(624251)
    aux = _n_(624252, "word_list", lambda: word_list)
    _l_(624253)
    return aux


### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    _l_(624267)

    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    _l_(624255)
    word = _c_(624258, _a_(624257, _n_(624256, "word", lambda: word), "lower"))
    _l_(624259)
    word = _c_(624262, _a_(624261, _n_(624260, "word", lambda: word), "strip"), " !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    _l_(624263)
    aux = _n_(624264, "word", lambda: word) in _n_(624265, "word_list", lambda: word_list)
    _l_(624266)
    return aux


### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    _l_(624283)

    """
    Returns: a joke in encrypted text.
    """
    f = _c_(624269, _n_(624268, "open", lambda: open), "story.txt", "r")
    _l_(624270)
    story = _c_(624275, _n_(624271, "str", lambda: str), _c_(624274, _a_(624273, _n_(624272, "f", lambda: f), "read")))
    _l_(624276)
    _c_(624279, _a_(624278, _n_(624277, "f", lambda: f), "close"))
    _l_(624280)
    aux = _n_(624281, "story", lambda: story)
    _l_(624282)
    return aux


WORDLIST_FILENAME = 'words.txt'
_l_(624284)


class Message(_n_(624285, "object", lambda: object)):
    _l_(624374)

    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        _l_(624295)

        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        _l_(624286)
        _n_(624287, "self", lambda: self).message_text = _n_(624288, "text", lambda: text)
        _l_(624289)
        _n_(624290, "self", lambda: self).valid_words = _c_(624293, _n_(624291, "load_words", lambda: load_words), _n_(624292, "WORDLIST_FILENAME", lambda: WORDLIST_FILENAME))
        _l_(624294)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        _l_(624300)

        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        _l_(624296)
        aux = _a_(624298, _n_(624297, "self", lambda: self), "message_text")
        _l_(624299)
        return aux

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        _l_(624305)

        '''
        Used to safely access a copy of self.valid_words outside of the class

        Returns: a COPY of self.valid_words
        '''
        _l_(624301)
        aux = _a_(624303, _n_(624302, "self", lambda: self), "valid_words")[:]
        _l_(624304)
        return aux

    def build_shift_dict(shift):
        _l_(624348)

        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        _l_(624306)
        assert 0 <= _n_(624307, "shift", lambda: shift) < 26
        _l_(624308)
        shifted_dict = {}
        _l_(624309)

        def shift_letters(shift, text):
            _l_(624333)

            for i in _c_(624314, _n_(624310, "range", lambda: range), _c_(624313, _n_(624311, "len", lambda: len), _n_(624312, "text", lambda: text))):
                _l_(624332)

                if _n_(624315, "i", lambda: i) < _n_(624316, "shift", lambda: shift):
                    _l_(624331)

                    _n_(624317, "shifted_dict", lambda: shifted_dict)[_n_(624318, "text", lambda: text)[_n_(624319, "i", lambda: i)]] = _n_(624320, "text", lambda: text)[26 - _n_(624321, "shift", lambda: shift) + _n_(624322, "i", lambda: i)]
                    _l_(624323)
                else:
                    _n_(624324, "shifted_dict", lambda: shifted_dict)[_n_(624325, "text", lambda: text)[_n_(624326, "i", lambda: i)]] = _n_(624327, "text", lambda: text)[_n_(624328, "i", lambda: i) - _n_(624329, "shift", lambda: shift)]
                    _l_(624330)

        _c_(624338, _n_(624334, "shift_letters", lambda: shift_letters), _n_(624335, "shift", lambda: shift), _a_(624337, _n_(624336, "string", lambda: string), "ascii_lowercase"))
        _l_(624339)
        _c_(624344, _n_(624340, "shift_letters", lambda: shift_letters), _n_(624341, "shift", lambda: shift), _a_(624343, _n_(624342, "string", lambda: string), "ascii_uppercase"))
        _l_(624345)
        aux = _n_(624346, "shifted_dict", lambda: shifted_dict)
        _l_(624347)
        return aux

    def apply_shift(self, shift):
        _l_(624373)

        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        _l_(624349)

        shifted_dict = _c_(624353, _a_(624351, _n_(624350, "self", lambda: self), "build_shift_dict"), _n_(624352, "shift", lambda: shift))
        _l_(624354)
        result = ""
        _l_(624355)
        for i in _a_(624357, _n_(624356, "self", lambda: self), "message_text"):
            _l_(624370)

            if _n_(624358, "i", lambda: i) not in _a_(624360, _n_(624359, "string", lambda: string), "ascii_lowercase") and _n_(624361, "i", lambda: i) not in _a_(624363, _n_(624362, "string", lambda: string), "ascii_uppercase"):
                _l_(624369)

                result += _n_(624364, "i", lambda: i)
                _l_(624365)
            else:
                result += _n_(624366, "shifted_dict", lambda: shifted_dict)[_n_(624367, "i", lambda: i)]
                _l_(624368)
        aux = _n_(624371, "result", lambda: result)
        _l_(624372)
        return aux


class PlaintextMessage(_n_(624375, "Message", lambda: Message)):
    _l_(624433)

    def __init__(self, text, shift):
        _l_(624396)

        '''
        Initializes a PlaintextMessage object        

        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        _l_(624376)
        _n_(624377, "self", lambda: self).text = _n_(624378, "text", lambda: text)
        _l_(624379)
        _n_(624380, "self", lambda: self).shift = _n_(624381, "shift", lambda: shift)
        _l_(624382)
        _n_(624383, "self", lambda: self).encrypting_dict = _c_(624387, _a_(624385, _n_(624384, "Message", lambda: Message), "build_shift_dict"), _n_(624386, "shift", lambda: shift))
        _l_(624388)
        _n_(624389, "self", lambda: self).message_text_encrypted = _c_(624394, _a_(624391, _n_(624390, "Message", lambda: Message), "apply_shift"), _n_(624392, "text", lambda: text), _n_(624393, "shift", lambda: shift))
        _l_(624395)

    def get_shift(self):
        _l_(624401)

        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        _l_(624397)
        aux = _a_(624399, _n_(624398, "self", lambda: self), "shift")
        _l_(624400)
        return aux

    def get_encrypting_dict(self):
        _l_(624406)

        '''
        Used to safely access a copy self.encrypting_dict outside of the class

        Returns: a COPY of self.encrypting_dict
        '''
        _l_(624402)
        aux = _a_(624404, _n_(624403, "self", lambda: self), "encrypting_dict")
        _l_(624405)
        return aux

    def get_message_text_encrypted(self):
        _l_(624412)

        '''
        Used to safely access self.message_text_encrypted outside of the class

        Returns: self.message_text_encrypted
        '''
        _l_(624407)
        aux = _c_(624410, _a_(624409, _n_(624408, "self", lambda: self), "message_text_encrypted"))
        _l_(624411)
        return aux

    def change_shift(self, shift):
        _l_(624432)

        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        _l_(624413)
        assert 0 <= _n_(624414, "shift", lambda: shift) < 26
        _l_(624415)
        _n_(624416, "self", lambda: self).shift = _n_(624417, "shift", lambda: shift)
        _l_(624418)
        _n_(624419, "self", lambda: self).encrypting_dict = _c_(624423, _a_(624421, _n_(624420, "Message", lambda: Message), "build_shift_dict"), _n_(624422, "shift", lambda: shift))
        _l_(624424)
        _n_(624425, "self", lambda: self).message_text_encrypted = _c_(624430, _a_(624427, _n_(624426, "Message", lambda: Message), "apply_shift"), _n_(624428, "text", lambda: text), _n_(624429, "shift", lambda: shift))
        _l_(624431)


class CiphertextMessage(_n_(624434, "Message", lambda: Message)):
    _l_(624461)

    def __init__(self, text):
        _l_(624439)

        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        _l_(624435)
        _n_(624436, "self", lambda: self).message = _n_(624437, "Message", lambda: Message)
        _l_(624438)

    def decrypt_message(self):
        _l_(624460)

        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        _l_(624440)
        for i in _c_(624442, _n_(624441, "range", lambda: range), 26):
            _l_(624459)

            decrypted = _c_(624448, _a_(624444, _n_(624443, "Message", lambda: Message), "apply_shift"), _a_(624446, _n_(624445, "self", lambda: self), "message") , _n_(624447, "i", lambda: i))
            _l_(624449)
            for word in _n_(624450, "decrypted", lambda: decrypted) :
                _l_(624458)

                if _n_(624451, "word", lambda: word) in _a_(624453, _n_(624452, "Message", lambda: Message), "valid_words") :
                    _l_(624457)

                    aux = (_n_(624454, "i", lambda: i) , _n_(624455, "decrypted", lambda: decrypted))
                    _l_(624456)
                    return aux


# Example test case (PlaintextMessage)
plaintext = _c_(624463, _n_(624462, "PlaintextMessage", lambda: PlaintextMessage), 'hello', 2)
_l_(624464)
_c_(624466, _n_(624465, "print", lambda: print), 'Expected Output: jgnnq')
_l_(624467)
_c_(624472, _n_(624468, "print", lambda: print), 'Actual Output:', _c_(624471, _a_(624470, _n_(624469, "plaintext", lambda: plaintext), "get_message_text_encrypted")))
_l_(624473)

# Example test case (CiphertextMessage)
ciphertext = _c_(624475, _n_(624474, "CiphertextMessage", lambda: CiphertextMessage), 'jgnnq')
_l_(624476)
_c_(624478, _n_(624477, "print", lambda: print), 'Expected Output:', (24, 'hello'))
_l_(624479)
_c_(624484, _n_(624480, "print", lambda: print), 'Actual Output:', _c_(624483, _a_(624482, _n_(624481, "ciphertext", lambda: ciphertext), "decrypt_message")))
_l_(624485)