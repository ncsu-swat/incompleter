# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49971390/valueerror-not-enough-values-to-unpack-expected-3-got-2-typeerror-must-be
# Team manager welcome screen, date & time
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(693300, _n_(693299, "print", lambda: print), "Welcome to San Angelo's Softball Team Roster")
_l_(693301)
_c_(693303, _n_(693302, "print", lambda: print), "This program keeps the most up-to-date information")
_l_(693304)
_c_(693306, _n_(693305, "print", lambda: print), "Today's Date: April 23, 2018")
_l_(693307)
_c_(693309, _n_(693308, "print", lambda: print), "Current Time: 0900\n")
_l_(693310)

# Create a dictionary named "team_members"
team_members = {}
_l_(693311)

# Provides Menu Screen
menu_selection = _c_(693313, _n_(693312, "print_menu", lambda: print_menu))
_l_(693314)

# Create while loop repeating the main menu.
while _n_(693315, "menu_selection", lambda: menu_selection) != 9:
    _l_(693363)


    if _n_(693316, "menu_selection", lambda: menu_selection) == 1:
        _l_(693359)

        _c_(693319, _n_(693317, "print_members", lambda: print_members), _n_(693318, "team_members", lambda: team_members))
        _l_(693320)

    elif _n_(693321, "menu_selection", lambda: menu_selection) == 2:
        _l_(693358)

        team_members = _c_(693324, _n_(693322, "add_members", lambda: add_members), _n_(693323, "team_members", lambda: team_members))
        _l_(693325)

    elif _n_(693326, "menu_selection", lambda: menu_selection) == 3:
        _l_(693357)

        team_members = _c_(693329, _n_(693327, "remove_members", lambda: remove_members), _n_(693328, "team_members", lambda: team_members))
        _l_(693330)

    elif _n_(693331, "menu_selection", lambda: menu_selection) == 4:
        _l_(693356)

        team_members = _c_(693334, _n_(693332, "edit_members", lambda: edit_members), _n_(693333, "team_members", lambda: team_members))
        _l_(693335)

    elif _n_(693336, "menu_selection", lambda: menu_selection) == 5:
        _l_(693355)

        filename = _c_(693338, _n_(693337, "input", lambda: input), "Enter Desired Filename: ")
        _l_(693339)
        _c_(693343, _n_(693340, "save_members", lambda: save_members), _n_(693341, "team_members", lambda: team_members), _n_(693342, "filename", lambda: filename))
        _l_(693344)

    elif _n_(693345, "menu_selection", lambda: menu_selection) == 6:
        _l_(693354)

        filename = _c_(693347, _n_(693346, "input", lambda: input), "Enter Existing Filename: ")
        _l_(693348)
        _c_(693352, _n_(693349, "load_members", lambda: load_members), _n_(693350, "team_members", lambda: team_members), _n_(693351, "filename", lambda: filename))
        _l_(693353)

    menu_selection = _c_(693361, _n_(693360, "print_menu", lambda: print_menu))
    _l_(693362)

_c_(693365, _n_(693364, "print", lambda: print), "Thank You For Updating San Angelo's Softball Team Roster!")
_l_(693366)