# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73864920/kivy-python-3-8-if-statement-in-canvas-returns-attributeerror-nonetype-ob
# Using kivy 2.0.0 and Python 3.8

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import kivy
    _l_(639396)

except ImportError:
    pass
try:
    from kivy.config import Config
    _l_(639398)

except ImportError:
    pass
try:
    from kivy.app import App
    _l_(639400)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(639402)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import ScreenManager, Screen
    _l_(639404)

except ImportError:
    pass
try:
    from kivy.properties import NumericProperty, ObjectProperty, BooleanProperty
    _l_(639406)

except ImportError:
    pass
try:
    from kivy.storage.jsonstore import JsonStore
    _l_(639408)

except ImportError:
    pass

_c_(639411, _a_(639410, _n_(639409, "kivy", lambda: kivy), "require"), '2.0.0')  # Version of Kivy)
_l_(639412)  # Version of Kivy)
_c_(639415, _a_(639414, _n_(639413, "Config", lambda: Config), "set"), 'graphics', 'width', '360')  # (New Android smartphones e.g. OnePlus 7 series, iPhone X,
_l_(639416)  # (New Android smartphones e.g. OnePlus 7 series, iPhone X,
_c_(639419, _a_(639418, _n_(639417, "Config", lambda: Config), "set"), 'graphics', 'height', '640')  # 11 and 12 series, upsampled)
_l_(639420)  # 11 and 12 series, upsampled)
store = _c_(639422, _n_(639421, "JsonStore", lambda: JsonStore), 'user_data.json')  # For saving high score and wallet
_l_(639423)  # For saving high score and wallet
root_widget = _c_(639426, _a_(639425, _n_(639424, "Builder", lambda: Builder), "load_file"), 'layout.kv')
_l_(639427)

# os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'  # If necessary, uncomment to prevent OpenGL error


class GameWidget(_n_(639428, "Screen", lambda: Screen)):
    _l_(639543)


    score = _c_(639430, _n_(639429, "NumericProperty", lambda: NumericProperty), 0)  # Current score
    _l_(639431)  # Current score
    highscore = _c_(639436, _n_(639432, "NumericProperty", lambda: NumericProperty), _c_(639435, _a_(639434, _n_(639433, "store", lambda: store), "get"), 'highscore')['score'])  # High score
    _l_(639437)  # High score
    old_highscore = _c_(639442, _n_(639438, "NumericProperty", lambda: NumericProperty), _c_(639441, _a_(639440, _n_(639439, "store", lambda: store), "get"), 'highscore')['score'])  # Previous high score for comparison
    _l_(639443)  # Previous high score for comparison
    broke_record = _c_(639445, _n_(639444, "BooleanProperty", lambda: BooleanProperty), False)  # For checking if a new high score is achieved
    _l_(639446)  # For checking if a new high score is achieved

    wallet = _c_(639451, _n_(639447, "NumericProperty", lambda: NumericProperty), _c_(639450, _a_(639449, _n_(639448, "store", lambda: store), "get"), 'wallet')['coins'])  # Amount of coins that user has collected
    _l_(639452)  # Amount of coins that user has collected
    wallet_label = _c_(639454, _n_(639453, "ObjectProperty", lambda: ObjectProperty))  # In-game label where wallet is viewed
    _l_(639455)  # In-game label where wallet is viewed
    old_wallet = wallet  # Used for count_coins() function
    _l_(639456)  # Used for count_coins() function

    coins = _c_(639458, _n_(639457, "NumericProperty", lambda: NumericProperty), 0)  # Amount of coins earned in current level
    _l_(639459)  # Amount of coins earned in current level

    # Update the wallet
    def pay_coins(self):
        _l_(639485)


        if _a_(639461, _n_(639460, "self", lambda: self), "game_finish"):
            _l_(639484)


            _n_(639462, "self", lambda: self).wallet += _n_(639463, "self", lambda: self).coins
            _l_(639464)
            _c_(639469, _a_(639466, _n_(639465, "store", lambda: store), "put"), "wallet", coins=_a_(639468, _n_(639467, "self", lambda: self), "wallet"))
            _l_(639470)
            _n_(639471, "self", lambda: self).wallet = _c_(639474, _a_(639473, _n_(639472, "store", lambda: store), "get"), "wallet")["coins"]
            _l_(639475)
            _c_(639479, _n_(639476, "print", lambda: print), "Wallet: %s" % _a_(639478, _n_(639477, "self", lambda: self), "wallet"))
            _l_(639480)
            _n_(639481, "self", lambda: self).old_wallet -= _n_(639482, "self", lambda: self).coins
            _l_(639483)

    # Function to visually show the coins being added to the wallet
    def count_coins(self, dt):
        _l_(639493)


        if _a_(639487, _n_(639486, "self", lambda: self), "coins") >= 1:
            _l_(639492)

            _n_(639488, "self", lambda: self).coins -= 1
            _l_(639489)
            _n_(639490, "self", lambda: self).old_wallet += 1
            _l_(639491)

    # Check if new high score is achieved
    def check_score(self):
        _l_(639517)


        if _a_(639495, _n_(639494, "self", lambda: self), "score") > _a_(639497, _n_(639496, "self", lambda: self), "highscore"):
            _l_(639516)

            _c_(639502, _a_(639499, _n_(639498, "store", lambda: store), "put"), "highscore", score=_a_(639501, _n_(639500, "self", lambda: self), "score"))
            _l_(639503)
            _n_(639504, "self", lambda: self).highscore = _c_(639507, _a_(639506, _n_(639505, "store", lambda: store), "get"), "highscore")["score"]
            _l_(639508)

            _n_(639509, "self", lambda: self).broke_record = True
            _l_(639510)

            _c_(639512, _n_(639511, "print", lambda: print), 'new high!')
            _l_(639513)
        else:
            _n_(639514, "self", lambda: self).broke_record = False
            _l_(639515)

    # Reset all variables
    def reload(self):
        _l_(639542)


        _n_(639518, "self", lambda: self).score = 0
        _l_(639519)
        _n_(639520, "self", lambda: self).highscore = _c_(639523, _a_(639522, _n_(639521, "store", lambda: store), "get"), "highscore")["score"]
        _l_(639524)
        _n_(639525, "self", lambda: self).old_highscore = _a_(639527, _n_(639526, "self", lambda: self), "highscore")
        _l_(639528)
        _n_(639529, "self", lambda: self).broke_record = False
        _l_(639530)

        _n_(639531, "self", lambda: self).wallet = _c_(639534, _a_(639533, _n_(639532, "store", lambda: store), "get"), "wallet")["coins"]
        _l_(639535)
        _n_(639536, "self", lambda: self).old_wallet = _a_(639538, _n_(639537, "self", lambda: self), "wallet")
        _l_(639539)

        _n_(639540, "self", lambda: self).coins = 0
        _l_(639541)


class Menu(_n_(639544, "Screen", lambda: Screen)):
    _l_(639546)

    pass
    _l_(639545)


class WindowManager(_n_(639547, "ScreenManager", lambda: ScreenManager)):
    _l_(639549)

    pass
    _l_(639548)


class MyApp(_n_(639550, "App", lambda: App)):
    _l_(639558)

    WindowManager = _c_(639552, _n_(639551, "WindowManager", lambda: WindowManager))
    _l_(639553)

    def build(self):
        _l_(639557)

        aux = _a_(639555, _n_(639554, "self", lambda: self), "WindowManager")
        _l_(639556)

        return aux

_c_(639562, _a_(639561, _c_(639560, _n_(639559, "MyApp", lambda: MyApp)), "run"))
_l_(639563)