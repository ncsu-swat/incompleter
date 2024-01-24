# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50421623/python-3-tkinter-nameerror-name-price-overall-release-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
price_overall_release = 0
_l_(681317)
# A definition for adding and subtracting to the price at the bottom.
def release_button(add_or_sub, game_id):
    _l_(681408)

    global price_overall_release
    _l_(681318)
    if _n_(681319, "add_or_sub", lambda: add_or_sub) == "add":
        _l_(681407)

        _n_(681320, "price_releases", lambda: price_releases)[_n_(681321, "game_id", lambda: game_id)] = _c_(681325, _n_(681322, "float", lambda: float), _n_(681323, "price_releases", lambda: price_releases)[_n_(681324, "game_id", lambda: game_id)])
        _l_(681326)
        price_overall_release = _n_(681327, "price_overall_release", lambda: price_overall_release) + _n_(681328, "price_releases", lambda: price_releases)[_n_(681329, "game_id", lambda: game_id)]
        _l_(681330)
        _n_(681331, "price_releases", lambda: price_releases)[_n_(681332, "game_id", lambda: game_id)] = _c_(681336, _n_(681333, "str", lambda: str), _n_(681334, "price_releases", lambda: price_releases)[_n_(681335, "game_id", lambda: game_id)])
        _l_(681337)

        # Declare and show.
        price_overall_release = _c_(681340, _n_(681338, "str", lambda: str), _n_(681339, "price_overall_release", lambda: price_overall_release))
        _l_(681341)
        label_overallprice_releases = _c_(681347, _n_(681342, "Label", lambda: Label), _n_(681343, "new_release_window", lambda: new_release_window), text="$"+_n_(681344, "price_overall_release", lambda: price_overall_release),
                            bg = _n_(681345, "releases_price_colour", lambda: releases_price_colour), fg = "black", relief = "sunken", borderwidth = 1, font = _n_(681346, "gui_font_10", lambda: gui_font_10))
        _l_(681348)
        amount_ordered_release = _c_(681354, _n_(681349, "Label", lambda: Label), _n_(681350, "new_release_window", lambda: new_release_window), text = _n_(681351, "amount_release", lambda: amount_release),
                            bg = _n_(681352, "releases_price_colour", lambda: releases_price_colour), fg = "black", borderwidth = 1, font = _n_(681353, "gui_font_10", lambda: gui_font_10))
        _l_(681355)

        _c_(681359, _a_(681357, _n_(681356, "label_overallprice_releases", lambda: label_overallprice_releases), "grid"), row = 12, column = 3, padx = 7.5, pady = _n_(681358, "space_between", lambda: space_between)) # +
        _l_(681360) # +
        price_overall_release = _c_(681363, _n_(681361, "float", lambda: float), _n_(681362, "price_overall_release", lambda: price_overall_release))
        _l_(681364)
        aux = _n_(681365, "price_overall_release", lambda: price_overall_release)
        _l_(681366)

        return aux
    else:
        _n_(681367, "price_releases", lambda: price_releases)[_n_(681368, "game_id", lambda: game_id)] = _c_(681372, _n_(681369, "float", lambda: float), _n_(681370, "price_releases", lambda: price_releases)[_n_(681371, "game_id", lambda: game_id)])
        _l_(681373)
        price_overall_release = _n_(681374, "price_overall_release", lambda: price_overall_release) - _n_(681375, "price_releases", lambda: price_releases)[_n_(681376, "game_id", lambda: game_id)]
        _l_(681377)
        _n_(681378, "price_releases", lambda: price_releases)[_n_(681379, "game_id", lambda: game_id)] = _c_(681383, _n_(681380, "str", lambda: str), _n_(681381, "price_releases", lambda: price_releases)[_n_(681382, "game_id", lambda: game_id)])
        _l_(681384)

        # Declare and show.
        price_overall_release = _c_(681387, _n_(681385, "str", lambda: str), _n_(681386, "price_overall_release", lambda: price_overall_release))
        _l_(681388)
        label_overallprice_releases = _c_(681394, _n_(681389, "Label", lambda: Label), _n_(681390, "new_release_window", lambda: new_release_window), text="$"+_n_(681391, "price_overall_release", lambda: price_overall_release),
                            bg = _n_(681392, "releases_price_colour", lambda: releases_price_colour), fg = "black", relief = "sunken", borderwidth = 1, font = _n_(681393, "gui_font_10", lambda: gui_font_10))
        _l_(681395)

        _c_(681399, _a_(681397, _n_(681396, "label_overallprice_releases", lambda: label_overallprice_releases), "grid"), row = 12, column = 3, padx = 7.5, pady = _n_(681398, "space_between", lambda: space_between)) # +
        _l_(681400) # +
        price_overall_release = _c_(681403, _n_(681401, "float", lambda: float), _n_(681402, "price_overall_release", lambda: price_overall_release))
        _l_(681404)
        aux = _n_(681405, "price_overall_release", lambda: price_overall_release)
        _l_(681406)

        return aux

# Buttons.
releases_button_colour_add = ("forestgreen")
_l_(681409)
releases_button_colour_sub = ("firebrick")
_l_(681410)
#   1._________ 
button_game1_add = _c_(681416, _n_(681411, "Button", lambda: Button), _n_(681412, "new_release_window", lambda: new_release_window), text = "+", bg = _n_(681413, "releases_button_colour_add", lambda: releases_button_colour_add), font = "Helvetica 10", fg = "white",
                      width = 2, command = lambda: _c_(681415, _n_(681414, "release_button", lambda: release_button), "add", 3))
_l_(681417)
button_game1_sub = _c_(681423, _n_(681418, "Button", lambda: Button), _n_(681419, "new_release_window", lambda: new_release_window), text = "-", bg = _n_(681420, "releases_button_colour_sub", lambda: releases_button_colour_sub), font = "Helvetica 10", fg = "white",
                      width = 2, command = lambda: _c_(681422, _n_(681421, "release_button", lambda: release_button), "sub", 3))
_l_(681424)
#   2._________
button_game2_add = _c_(681430, _n_(681425, "Button", lambda: Button), _n_(681426, "new_release_window", lambda: new_release_window), text = "+", bg = _n_(681427, "releases_button_colour_add", lambda: releases_button_colour_add), font = "Helvetica 10", fg = "white",
                      width = 2, command = lambda: _c_(681429, _n_(681428, "release_button", lambda: release_button), "add", 4))
_l_(681431)
button_game2_sub = _c_(681437, _n_(681432, "Button", lambda: Button), _n_(681433, "new_release_window", lambda: new_release_window), text = "-", bg = _n_(681434, "releases_button_colour_sub", lambda: releases_button_colour_sub), font = "Helvetica 10", fg = "white",
                      width = 2, command = lambda: _c_(681436, _n_(681435, "release_button", lambda: release_button), "sub", 4))
_l_(681438)