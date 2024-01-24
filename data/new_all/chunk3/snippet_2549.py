# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71985551/breezypythongui-addradiobuttongroup-throwing-unexpected-attributeerror-str-ob
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from breezypythongui import EasyFrame
    _l_(527120)

except ImportError:
    pass
try:
    from tkinter import HORIZONTAL
    _l_(527122)

except ImportError:
    pass

class RadioButtonDemo(_n_(527123, "EasyFrame", lambda: EasyFrame)):
    _l_(527183)

    """When the Display button is pressed, shows the label
    of the selected radio button.  The button group has a
    horizontal alignment."""

    def __init__(self):
        _l_(527172)

        """Sets up the window and widgets."""
        _c_(527127, _a_(527125, _n_(527124, "EasyFrame", lambda: EasyFrame), "__init__"), _n_(527126, "self", lambda: self), "Radio Button Demo")
        _l_(527128)

        # Add the button group
        _n_(527129, "self", lambda: self).group = _c_(527133, _a_(527131, _n_(527130, "self", lambda: self), "addRadiobuttonGroup"), row=1, column=0,
                                              columnspan=4,
                                              orient=_n_(527132, "HORIZONTAL", lambda: HORIZONTAL))
        _l_(527134)

        # Add the radio buttons to the group
        _c_(527138, _a_(527137, _a_(527136, _n_(527135, "self", lambda: self), "group"), "addRadiobutton"), "Freshman")
        _l_(527139)
        _c_(527143, _a_(527142, _a_(527141, _n_(527140, "self", lambda: self), "group"), "addRadiobutton"), "Sophomore")
        _l_(527144)
        _c_(527148, _a_(527147, _a_(527146, _n_(527145, "self", lambda: self), "group"), "addRadiobutton"), "Junior")
        _l_(527149)
        defaultRB = _c_(527153, _a_(527152, _a_(527151, _n_(527150, "self", lambda: self), "group"), "addRadiobutton"), "Senior")
        _l_(527154)

        # Select one of the buttons in the group
        _c_(527159, _a_(527157, _a_(527156, _n_(527155, "self", lambda: self), "group"), "setSelectedButton"), _n_(527158, "defaultRB", lambda: defaultRB))
        _l_(527160)

        # Output field and command button for the results
        _n_(527161, "self", lambda: self).output = _c_(527164, _a_(527163, _n_(527162, "self", lambda: self), "addTextField"), "", row=0, column=1)
        _l_(527165)
        _c_(527170, _a_(527167, _n_(527166, "self", lambda: self), "addButton"), "Display", row=0, column=0,
                       command=_a_(527169, _n_(527168, "self", lambda: self), "display"))
        _l_(527171)

    # Event handling method

    def display(self):
        _l_(527182)

        """Displays the selected button's label in the text field."""
        _c_(527180, _a_(527175, _a_(527174, _n_(527173, "self", lambda: self), "output"), "setText"), _c_(527179, _a_(527178, _a_(527177, _n_(527176, "self", lambda: self), "group"), "getSelectedButton"))["value"])
        _l_(527181)


def main():
    _l_(527189)

    _c_(527187, _a_(527186, _c_(527185, _n_(527184, "RadioButtonDemo", lambda: RadioButtonDemo)), "mainloop"))
    _l_(527188)


if _n_(527190, "__name__", lambda: __name__) == "__main__":
    _l_(527194)

    _c_(527192, _n_(527191, "main", lambda: main))
    _l_(527193)