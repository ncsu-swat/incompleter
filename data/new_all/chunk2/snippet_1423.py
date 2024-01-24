# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60395009/typeerror-argument-should-be-integer-or-none-not-str-error-while-making-sign
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter
    _l_(424348)

except ImportError:
    pass
try:
    from tkinter import messagebox
    _l_(424350)

except ImportError:
    pass
try:
    from tkinter import StringVar
    _l_(424352)

except ImportError:
    pass


class panel:
    _l_(424755)

    def ask(self):
        _l_(424416)

        ask = _c_(424355, _a_(424354, _n_(424353, "tkinter", lambda: tkinter), "Tk"))
        _l_(424356)
        _c_(424359, _a_(424358, _n_(424357, "ask", lambda: ask), "title"), "Input")
        _l_(424360)
        _c_(424363, _a_(424362, _n_(424361, "ask", lambda: ask), "geometry"), "300x100")
        _l_(424364)

        def y():
            _l_(424373)

            _c_(424367, _a_(424366, _n_(424365, "ask", lambda: ask), "destroy"))
            _l_(424368)
            _c_(424371, _a_(424370, _n_(424369, "self", lambda: self), "login"))
            _l_(424372)
        def n():
            _l_(424382)

            _c_(424376, _a_(424375, _n_(424374, "ask", lambda: ask), "destroy"))
            _l_(424377)
            _c_(424380, _a_(424379, _n_(424378, "self", lambda: self), "signup"))
            _l_(424381)


        stat = _c_(424386, _a_(424384, _n_(424383, "tkinter", lambda: tkinter), "Label"), _n_(424385, "ask", lambda: ask) , text = "Are You An Existing User?")
        _l_(424387)
        _c_(424390, _a_(424389, _n_(424388, "stat", lambda: stat), "grid"), row = 0 , column = 0)
        _l_(424391)
        yes = _c_(424396, _a_(424393, _n_(424392, "tkinter", lambda: tkinter), "Button"), _n_(424394, "ask", lambda: ask), text = "Yes" , bg = "Blue" , fg = "Black" , command = _n_(424395, "y", lambda: y), bd = 5 )
        _l_(424397)
        _c_(424400, _a_(424399, _n_(424398, "yes", lambda: yes), "grid"), row = 1 , column = 1)
        _l_(424401)
        no = _c_(424406, _a_(424403, _n_(424402, "tkinter", lambda: tkinter), "Button"), _n_(424404, "ask", lambda: ask), text = "No" , bg = "Blue", fg = "Black" , command = _n_(424405, "n", lambda: n), bd = 5)
        _l_(424407)
        _c_(424410, _a_(424409, _n_(424408, "no", lambda: no), "grid"), row = 1 , column = 2)
        _l_(424411)

        _c_(424414, _a_(424413, _n_(424412, "ask", lambda: ask), "mainloop"))
        _l_(424415)

    def signup(self):
        _l_(424648)

        window = _c_(424419, _a_(424418, _n_(424417, "tkinter", lambda: tkinter), "Tk"))
        _l_(424420)
        _c_(424423, _a_(424422, _n_(424421, "window", lambda: window), "title"), "Registration Form")
        _l_(424424)
        _c_(424427, _a_(424426, _n_(424425, "window", lambda: window), "geometry"), "300x300")
        _l_(424428)

        var = _c_(424430, _n_(424429, "StringVar", lambda: StringVar))
        _l_(424431)

        def callback():
            _l_(424532)

            file = _c_(424433, _n_(424432, "open", lambda: open), "information.txt", "a")
            _l_(424434)
            _c_(424437, _a_(424436, _n_(424435, "file", lambda: file), "write"), "\r")
            _l_(424438)
            _c_(424441, _a_(424440, _n_(424439, "file", lambda: file), "write"), "Data: ")
            _l_(424442)
            _c_(424448, _a_(424444, _n_(424443, "file", lambda: file), "write"), _c_(424447, _a_(424446, _n_(424445, "firstname1", lambda: firstname1), "get")))
            _l_(424449)
            _c_(424452, _a_(424451, _n_(424450, "file", lambda: file), "write"), " ")
            _l_(424453)
            _c_(424459, _a_(424455, _n_(424454, "file", lambda: file), "write"), _c_(424458, _a_(424457, _n_(424456, "lastname1", lambda: lastname1), "get")))
            _l_(424460)
            _c_(424463, _a_(424462, _n_(424461, "file", lambda: file), "write"), "\n")
            _l_(424464)
            _c_(424470, _a_(424466, _n_(424465, "file", lambda: file), "write"), _c_(424469, _a_(424468, _n_(424467, "firstname1", lambda: firstname1), "get")))
            _l_(424471)
            _c_(424474, _a_(424473, _n_(424472, "file", lambda: file), "write"), "\n")
            _l_(424475)
            _c_(424481, _a_(424477, _n_(424476, "file", lambda: file), "write"), _c_(424480, _a_(424479, _n_(424478, "lastname1", lambda: lastname1), "get")))
            _l_(424482)
            _c_(424485, _a_(424484, _n_(424483, "file", lambda: file), "write"), "\n")
            _l_(424486)
            _c_(424492, _a_(424488, _n_(424487, "file", lambda: file), "write"), _c_(424491, _a_(424490, _n_(424489, "email1", lambda: email1), "get")))
            _l_(424493)
            _c_(424496, _a_(424495, _n_(424494, "file", lambda: file), "write"), "\n")
            _l_(424497)
            _c_(424503, _a_(424499, _n_(424498, "file", lambda: file), "write"), _c_(424502, _a_(424501, _n_(424500, "password1", lambda: password1), "get")))
            _l_(424504)
            _c_(424507, _a_(424506, _n_(424505, "file", lambda: file), "write"), "\n")
            _l_(424508)
            _c_(424514, _a_(424510, _n_(424509, "file", lambda: file), "write"), _c_(424513, _a_(424512, _n_(424511, "var", lambda: var), "get")))
            _l_(424515)
            _c_(424518, _a_(424517, _n_(424516, "file", lambda: file), "write"), "\r")
            _l_(424519)
            _c_(424522, _a_(424521, _n_(424520, "file", lambda: file), "close"))
            _l_(424523)
            _c_(424526, _a_(424525, _n_(424524, "messagebox", lambda: messagebox), "showinfo"), "Signup", "You have Successfully Signed Up")
            _l_(424527)
            _c_(424530, _a_(424529, _n_(424528, "self", lambda: self), "login"))
            _l_(424531)

        firstname = _c_(424536, _a_(424534, _n_(424533, "tkinter", lambda: tkinter), "Label"), _n_(424535, "window", lambda: window), text= "First Name", bg = "Black",fg = "White")
        _l_(424537)
        _c_(424540, _a_(424539, _n_(424538, "firstname", lambda: firstname), "grid"), row= 0, column= 0)
        _l_(424541)
        firstname1= _c_(424545, _a_(424543, _n_(424542, "tkinter", lambda: tkinter), "Entry"), _n_(424544, "window", lambda: window),bd= 5)
        _l_(424546)
        _c_(424549, _a_(424548, _n_(424547, "firstname1", lambda: firstname1), "grid"), row= 0 , column = 1)
        _l_(424550)
        lastname = _c_(424554, _a_(424552, _n_(424551, "tkinter", lambda: tkinter), "Label"), _n_(424553, "window", lambda: window), text = "Last Name", bg = "Black", fg = "White")
        _l_(424555)
        _c_(424558, _a_(424557, _n_(424556, "lastname", lambda: lastname), "grid"), row = 1, column = 0)
        _l_(424559)
        lastname1= _c_(424563, _a_(424561, _n_(424560, "tkinter", lambda: tkinter), "Entry"), _n_(424562, "window", lambda: window), bd = 5)
        _l_(424564)
        _c_(424567, _a_(424566, _n_(424565, "lastname1", lambda: lastname1), "grid"), row = 1, column = 1)
        _l_(424568)

        email = _c_(424572, _a_(424570, _n_(424569, "tkinter", lambda: tkinter), "Label"), _n_(424571, "window", lambda: window), text = "Email", bg = "Black", fg = "White")
        _l_(424573)
        _c_(424576, _a_(424575, _n_(424574, "email", lambda: email), "grid"), row = 2, column = 0)
        _l_(424577)
        email1 = _c_(424581, _a_(424579, _n_(424578, "tkinter", lambda: tkinter), "Entry"), _n_(424580, "window", lambda: window), bd = 5)
        _l_(424582)
        _c_(424585, _a_(424584, _n_(424583, "email1", lambda: email1), "grid"), row = 2 , column = 1)
        _l_(424586)

        password = _c_(424590, _a_(424588, _n_(424587, "tkinter", lambda: tkinter), "Label"), _n_(424589, "window", lambda: window), text = "Password" , bg = "Black", fg = "White")
        _l_(424591)
        _c_(424594, _a_(424593, _n_(424592, "password", lambda: password), "grid"), row = 3 , column = 0)
        _l_(424595)
        password1= _c_(424599, _a_(424597, _n_(424596, "tkinter", lambda: tkinter), "Entry"), _n_(424598, "window", lambda: window), bd = 5)
        _l_(424600)
        _c_(424603, _a_(424602, _n_(424601, "password1", lambda: password1), "grid"), row = 3 , column = 1)
        _l_(424604)

        gender= _c_(424608, _a_(424606, _n_(424605, "tkinter", lambda: tkinter), "Label"), _n_(424607, "window", lambda: window), text = "Gender", bg = "Black", fg = "White")
        _l_(424609)
        _c_(424612, _a_(424611, _n_(424610, "gender", lambda: gender), "grid"), row = 4 , column = 0)
        _l_(424613)
        male = _c_(424618, _a_(424615, _n_(424614, "tkinter", lambda: tkinter), "Radiobutton"), _n_(424616, "window", lambda: window),text= "Male" , value = "Male", variable = _n_(424617, "var", lambda: var) )
        _l_(424619)
        _c_(424622, _a_(424621, _n_(424620, "male", lambda: male), "grid"), row = 4 , column = 1 , sticky = "nsew")
        _l_(424623)
        female = _c_(424628, _a_(424625, _n_(424624, "tkinter", lambda: tkinter), "Radiobutton"), _n_(424626, "window", lambda: window),text= "Female" , value= "Female" , variable = _n_(424627, "var", lambda: var))
        _l_(424629)
        _c_(424632, _a_(424631, _n_(424630, "female", lambda: female), "grid"), row = 4, column = 2 , sticky = "nsew")
        _l_(424633)



        button = _c_(424638, _a_(424635, _n_(424634, "tkinter", lambda: tkinter), "Button"), _n_(424636, "window", lambda: window), text = "Submit" ,command = _n_(424637, "callback", lambda: callback) , bg = "Blue", fg = "White" , height = 2, width = 14)
        _l_(424639)
        _c_(424642, _a_(424641, _n_(424640, "button", lambda: button), "grid"), row = 5  , column = 1 , rowspan= 315)
        _l_(424643)



        _c_(424646, _a_(424645, _n_(424644, "window", lambda: window), "mainloop"))
        _l_(424647)

    def login(self):
        _l_(424754)

        signin = _c_(424651, _a_(424650, _n_(424649, "tkinter", lambda: tkinter), "Tk"))
        _l_(424652)
        _c_(424655, _a_(424654, _n_(424653, "signin", lambda: signin), "title"), "Sign In")
        _l_(424656)
        _c_(424659, _a_(424658, _n_(424657, "signin", lambda: signin), "geometry"), "300x300")
        _l_(424660)

        def callback():
            _l_(424703)

            file = _c_(424662, _n_(424661, "open", lambda: open), "information.txt" , "r")
            _l_(424663)
            e = _c_(424669, _a_(424665, _n_(424664, "file", lambda: file), "read"), _c_(424668, _a_(424667, _n_(424666, "x1", lambda: x1), "get")))
            _l_(424670)
            _c_(424673, _n_(424671, "print", lambda: print), _n_(424672, "e", lambda: e))
            _l_(424674)
            p = _c_(424680, _a_(424676, _n_(424675, "file", lambda: file), "read"), _c_(424679, _a_(424678, _n_(424677, "y1", lambda: y1), "get")))
            _l_(424681)
            _c_(424684, _n_(424682, "print", lambda: print), _n_(424683, "p", lambda: p))
            _l_(424685)
            if _n_(424686, "e", lambda: e) in _n_(424687, "file", lambda: file) and _n_(424688, "p", lambda: p) in _n_(424689, "file", lambda: file):
                _l_(424698)

                _c_(424692, _a_(424691, _n_(424690, "messagebox", lambda: messagebox), "showinfo"), "SignIn Notification", "You are Successfully Signed In")
                _l_(424693)
            else:
                _c_(424696, _a_(424695, _n_(424694, "messagebox", lambda: messagebox), "showerror"), "Error", "Email or Password is Incorrect")
                _l_(424697)
            _c_(424701, _a_(424700, _n_(424699, "file", lambda: file), "close"))
            _l_(424702)


        x = _c_(424707, _a_(424705, _n_(424704, "tkinter", lambda: tkinter), "Label"), _n_(424706, "signin", lambda: signin), text = "Email", bg = "Black", fg = "White" )
        _l_(424708)
        _c_(424711, _a_(424710, _n_(424709, "x", lambda: x), "grid"), row =  0 , column = 0)
        _l_(424712)
        x1 = _c_(424720, _n_(424713, "StringVar", lambda: StringVar), _c_(424719, _a_(424718, _c_(424717, _a_(424715, _n_(424714, "tkinter", lambda: tkinter), "Entry"), _n_(424716, "signin", lambda: signin), bd = 5), "grid"), row = 0 , column = 1))
        _l_(424721)
        y = _c_(424725, _a_(424723, _n_(424722, "tkinter", lambda: tkinter), "Label"), _n_(424724, "signin", lambda: signin), text = "Password", bg = "Black", fg = "White")
        _l_(424726)
        _c_(424729, _a_(424728, _n_(424727, "y", lambda: y), "grid"), row = 1 , column = 0)
        _l_(424730)
        y1 = _c_(424738, _n_(424731, "StringVar", lambda: StringVar), _c_(424737, _a_(424736, _c_(424735, _a_(424733, _n_(424732, "tkinter", lambda: tkinter), "Entry"), _n_(424734, "signin", lambda: signin), bd = 5), "grid"), row = 1 , column = 1))
        _l_(424739)


        login = _c_(424744, _a_(424741, _n_(424740, "tkinter", lambda: tkinter), "Button"), _n_(424742, "signin", lambda: signin), text = "Sign In" , bd = 5, bg = "Blue" , fg = "Black", height = 2 , width = 10, command = _n_(424743, "callback", lambda: callback) )
        _l_(424745)
        _c_(424748, _a_(424747, _n_(424746, "login", lambda: login), "grid"), row  = 2 , column = 1, rowspan = 2)
        _l_(424749)

        _c_(424752, _a_(424751, _n_(424750, "signin", lambda: signin), "mainloop"))
        _l_(424753)


def main():
    _l_(424763)

    p  = _c_(424757, _n_(424756, "panel", lambda: panel))
    _l_(424758)
    _c_(424761, _a_(424760, _n_(424759, "p", lambda: p), "ask"))
    _l_(424762)
_c_(424765, _n_(424764, "main", lambda: main))
_l_(424766)