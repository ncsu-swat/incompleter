# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42701877/str-find-typeerror-unsupported-operand-types-for-int-and-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(618318)

except ImportError:
    pass
master = _c_(618320, _n_(618319, "Tk", lambda: Tk))
_l_(618321)
_c_(618324, _a_(618323, _n_(618322, "master", lambda: master), "title"), "Caeser Cipher Program")
_l_(618325)
_c_(618328, _a_(618327, _n_(618326, "master", lambda: master), "geometry"), "300x200")
_l_(618329)

frame1 = _c_(618332, _n_(618330, "Frame", lambda: Frame), _n_(618331, "master", lambda: master))
_l_(618333)
frame2 = _c_(618336, _n_(618334, "Frame", lambda: Frame), _n_(618335, "master", lambda: master))
_l_(618337)
frame3 = _c_(618340, _n_(618338, "Frame", lambda: Frame), _n_(618339, "master", lambda: master))
_l_(618341)
frame4 = _c_(618344, _n_(618342, "Frame", lambda: Frame), _n_(618343, "master", lambda: master))
_l_(618345)
frame5 = _c_(618348, _n_(618346, "Frame", lambda: Frame), _n_(618347, "master", lambda: master))
_l_(618349)
frame6 = _c_(618352, _n_(618350, "Frame", lambda: Frame), _n_(618351, "master", lambda: master))
_l_(618353)


global encryptedText
_l_(618354)
global file
_l_(618355)
global shiftKey
_l_(618356)
file = ""
_l_(618357)
encryptedText = ""
_l_(618358)
removeSpaces = ""
_l_(618359)
def Start():
    _l_(618390)

    _c_(618362, _a_(618361, _n_(618360, "frame1", lambda: frame1), "grid"))
    _l_(618363)
    Question = _c_(618366, _n_(618364, "Label", lambda: Label), _n_(618365, "frame1", lambda: frame1), text = "Would you like to encrypt or decrypt a statement?\n\n\n")
    _l_(618367)
    _c_(618370, _a_(618369, _n_(618368, "Question", lambda: Question), "grid"), row = 0, column = 1)
    _l_(618371)
    ButtonPlace1 = _c_(618375, _n_(618372, "Button", lambda: Button), _n_(618373, "frame1", lambda: frame1), text = "Encrypt", command = _n_(618374, "EncryptChosen", lambda: EncryptChosen))
    _l_(618376)
    ButtonPlace2 = _c_(618380, _n_(618377, "Button", lambda: Button), _n_(618378, "frame1", lambda: frame1), text = "Decrypt", command = _n_(618379, "decrypt_command", lambda: decrypt_command))
    _l_(618381)
    _c_(618384, _a_(618383, _n_(618382, "ButtonPlace1", lambda: ButtonPlace1), "place"), x = 75, y = 50, anchor = "c")
    _l_(618385)
    _c_(618388, _a_(618387, _n_(618386, "ButtonPlace2", lambda: ButtonPlace2), "place"), x = 175, y = 50, anchor = "c")
    _l_(618389)

def EncryptChosen():
    _l_(618606)

    _c_(618393, _a_(618392, _n_(618391, "frame1", lambda: frame1), "destroy"))
    _l_(618394)
    _c_(618397, _a_(618396, _n_(618395, "frame2", lambda: frame2), "grid"))
    _l_(618398)
    Question = _c_(618401, _n_(618399, "Label", lambda: Label), _n_(618400, "frame2", lambda: frame2), text = "What would you like to shift it by?\t\t\t\n\n\n\n\n ")
    _l_(618402)
    ButtonPlace3 = _c_(618405, _n_(618403, "Entry", lambda: Entry), _n_(618404, "frame2", lambda: frame2))
    _l_(618406)
    def SubmitEncryptionKey():
        _l_(618588)

        shiftKey = _c_(618409, _a_(618408, _n_(618407, "ButtonPlace3", lambda: ButtonPlace3), "get"))
        _l_(618410)
        _c_(618413, _a_(618412, _n_(618411, "frame2", lambda: frame2), "destroy"))
        _l_(618414)
        _c_(618417, _a_(618416, _n_(618415, "frame3", lambda: frame3), "grid"))
        _l_(618418)
        Question = _c_(618421, _n_(618419, "Label", lambda: Label), _n_(618420, "frame3", lambda: frame3), text = "What would you like it to say?\t\t\t\n\n\n\n\n" )
        _l_(618422)
        ButtonPlace5 = _c_(618425, _n_(618423, "Entry", lambda: Entry), _n_(618424, "frame3", lambda: frame3))
        _l_(618426)
        def SubmitText():
            _l_(618570)

            file = _c_(618429, _a_(618428, _n_(618427, "ButtonPlace5", lambda: ButtonPlace5), "get"))
            _l_(618430)
            _c_(618433, _a_(618432, _n_(618431, "frame3", lambda: frame3), "destroy"))
            _l_(618434)
            _c_(618437, _a_(618436, _n_(618435, "frame4", lambda: frame4), "grid"))
            _l_(618438)
            Question = _c_(618441, _n_(618439, "Label", lambda: Label), _n_(618440, "frame4", lambda: frame4), text = "Would you like to remove spaces?\t\t\t\n\n\n\n\n")
            _l_(618442)
            _c_(618445, _a_(618444, _n_(618443, "Question", lambda: Question), "grid"), row = 0, column = 1)
            _l_(618446)
            def doRemoveSpaces():
                _l_(618454)

                global spacesStatement
                _l_(618447)
                global removeSpaces
                _l_(618448)
                spacesStatement = "spaces will be removed"
                _l_(618449)
                removeSpaces = "True"
                _l_(618450)
                _c_(618452, _n_(618451, "ReadyToEncrypt", lambda: ReadyToEncrypt))
                _l_(618453)
            ButtonPlace7 = _c_(618458, _n_(618455, "Button", lambda: Button), _n_(618456, "frame4", lambda: frame4), text = "Yes", command = _n_(618457, "doRemoveSpaces", lambda: doRemoveSpaces))
            _l_(618459)
            def doNotRemoveSpaces():
                _l_(618467)

                global spacesStatement
                _l_(618460)
                global removeSpaces
                _l_(618461)
                spacesStatement = "spaces will not be removed"
                _l_(618462)
                removeSpaces = "False"
                _l_(618463)
                _c_(618465, _n_(618464, "ReadyToEncrypt", lambda: ReadyToEncrypt))
                _l_(618466)
            ButtonPlace8 = _c_(618471, _n_(618468, "Button", lambda: Button), _n_(618469, "frame4", lambda: frame4), text = "No", command = _n_(618470, "doNotRemoveSpaces", lambda: doNotRemoveSpaces))
            _l_(618472)
            def ReadyToEncrypt():
                _l_(618561)

                _c_(618475, _a_(618474, _n_(618473, "frame4", lambda: frame4), "destroy"))
                _l_(618476)
                _c_(618479, _a_(618478, _n_(618477, "frame5", lambda: frame5), "grid"))
                _l_(618480)
                Question = _c_(618486, _n_(618481, "Label", lambda: Label), _n_(618482, "frame5", lambda: frame5), text = _n_(618483, "file", lambda: file) + "\n will be encrypted by " + _n_(618484, "shiftKey", lambda: shiftKey) + " and \n" + _n_(618485, "spacesStatement", lambda: spacesStatement) + ".\t\t\t\n\n\n\n")
                _l_(618487)
                _c_(618490, _a_(618489, _n_(618488, "Question", lambda: Question), "grid"), row = 0, column = 1)
                _l_(618491)
                def encryptSetup():
                    _l_(618551)


                    def encrypt(character):
                        _l_(618517)

                        alphabet = 'abcdefghijklmnopqrstuvwxyz '
                        _l_(618492)
                        character = _c_(618495, _a_(618494, _n_(618493, "character", lambda: character), "lower"))
                        _l_(618496)
                        if _c_(618499, _a_(618498, _n_(618497, "character", lambda: character), "isalpha")):
                            _l_(618516)

                            position = _c_(618505, _a_(618503, _c_(618502, _n_(618500, "str", lambda: str), _n_(618501, "alphabet", lambda: alphabet)), "find"), _n_(618504, "character", lambda: character)) + _n_(618506, "shiftKey", lambda: shiftKey)
                            _l_(618507)
                            if _n_(618508, "position", lambda: position) > 25:
                                _l_(618510)

                                position -= 26 
                                _l_(618509) 
                            aux = _n_(618511, "alphabet", lambda: alphabet)[_n_(618512, "position", lambda: position)]
                            _l_(618513)
                            return aux
                        else:
                            aux = _n_(618514, "character", lambda: character)
                            _l_(618515)
                            return aux

                    for line in _n_(618518, "file", lambda: file):
                        _l_(618527)

                        for c in _n_(618519, "line", lambda: line):
                            _l_(618526)

                            global encryptedText
                            _l_(618520)
                            encryptedText = _n_(618521, "encryptedText", lambda: encryptedText) + _c_(618524, _n_(618522, "encrypt", lambda: encrypt), _n_(618523, "c", lambda: c))
                            _l_(618525)

                    if _n_(618528, "removeSpaces", lambda: removeSpaces) == "True":
                        _l_(618533)

                        encryptedText = _c_(618531, _a_(618530, _n_(618529, "encryptedText", lambda: encryptedText), "replace"), " ","")
                        _l_(618532)
                    _c_(618536, _a_(618535, _n_(618534, "frame5", lambda: frame5), "destroy"))
                    _l_(618537)
                    _c_(618540, _a_(618539, _n_(618538, "frame6", lambda: frame6), "grid"))
                    _l_(618541)
                    Question = _c_(618545, _n_(618542, "Label", lambda: Label), _n_(618543, "frame6", lambda: frame6), text = "Here is your encrypted message: \n" + _n_(618544, "encryptedText", lambda: encryptedText))
                    _l_(618546)
                    _c_(618549, _a_(618548, _n_(618547, "Question", lambda: Question), "grid"), row = 0, column = 1)    
                    _l_(618550)    

                ButtonPlace9 = _c_(618555, _n_(618552, "Button", lambda: Button), _n_(618553, "frame5", lambda: frame5), text = "Encrypt!", command = _n_(618554, "encryptSetup", lambda: encryptSetup))
                _l_(618556)
                _c_(618559, _a_(618558, _n_(618557, "ButtonPlace9", lambda: ButtonPlace9), "place"), x=175,y=50)
                _l_(618560)
            _c_(618564, _a_(618563, _n_(618562, "ButtonPlace7", lambda: ButtonPlace7), "place"), x = 75, y = 50, anchor = "c")
            _l_(618565)
            _c_(618568, _a_(618567, _n_(618566, "ButtonPlace8", lambda: ButtonPlace8), "place"), x = 175, y = 50, anchor = "c")
            _l_(618569)
        ButtonPlace6 = _c_(618574, _n_(618571, "Button", lambda: Button), _n_(618572, "frame3", lambda: frame3), text = "Submit", command = _n_(618573, "SubmitText", lambda: SubmitText))
        _l_(618575)
        _c_(618578, _a_(618577, _n_(618576, "Question", lambda: Question), "grid"), row = 0, column = 1)
        _l_(618579)
        _c_(618582, _a_(618581, _n_(618580, "ButtonPlace5", lambda: ButtonPlace5), "place"), x=50,y=50)
        _l_(618583)
        _c_(618586, _a_(618585, _n_(618584, "ButtonPlace6", lambda: ButtonPlace6), "place"), x=175,y=45)
        _l_(618587)
    ButtonPlace4 = _c_(618592, _n_(618589, "Button", lambda: Button), _n_(618590, "frame2", lambda: frame2), text = "Submit", command = _n_(618591, "SubmitEncryptionKey", lambda: SubmitEncryptionKey))
    _l_(618593)
    _c_(618596, _a_(618595, _n_(618594, "Question", lambda: Question), "grid"), row = 0, column = 1)
    _l_(618597)
    _c_(618600, _a_(618599, _n_(618598, "ButtonPlace3", lambda: ButtonPlace3), "place"), x=50,y=50)
    _l_(618601)
    _c_(618604, _a_(618603, _n_(618602, "ButtonPlace4", lambda: ButtonPlace4), "place"), x=175,y=45)
    _l_(618605)



_c_(618609, _a_(618608, _n_(618607, "frame1", lambda: frame1), "grid"))
_l_(618610)
Question = _c_(618613, _n_(618611, "Label", lambda: Label), _n_(618612, "frame1", lambda: frame1), text = "Would you like to encrypt or decrypt a statement?\n\n\n")
_l_(618614)
_c_(618617, _a_(618616, _n_(618615, "Question", lambda: Question), "grid"), row = 0, column = 1)
_l_(618618)
ButtonPlace1 = _c_(618622, _n_(618619, "Button", lambda: Button), _n_(618620, "frame1", lambda: frame1), text = "Encrypt", command = _n_(618621, "EncryptChosen", lambda: EncryptChosen))
_l_(618623)
ButtonPlace2 = _c_(618626, _n_(618624, "Button", lambda: Button), _n_(618625, "frame1", lambda: frame1), text = "Decrypt", command = "")
_l_(618627)
_c_(618630, _a_(618629, _n_(618628, "ButtonPlace1", lambda: ButtonPlace1), "place"), x = 75, y = 50, anchor = "c")
_l_(618631)
_c_(618634, _a_(618633, _n_(618632, "ButtonPlace2", lambda: ButtonPlace2), "place"), x = 175, y = 50, anchor = "c")
_l_(618635)

_c_(618638, _a_(618637, _n_(618636, "master", lambda: master), "loop"))
_l_(618639)