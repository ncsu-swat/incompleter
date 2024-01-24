# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53632379/attributeerror-builtin-function-or-method-object-has-no-attribute-addlayout
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class UIWidget(_a_(447136, _n_(447135, "QtWidgets", lambda: QtWidgets), "QWidget")):
    _l_(447321)

    def __init__(self, parent=None):
        _l_(447212)

        _c_(447142, _a_(447140, _n_(447137, "super", lambda: super)(_n_(447138, "UIWidget", lambda: UIWidget), _n_(447139, "self", lambda: self)), "__init__"), _n_(447141, "parent", lambda: parent))        
        _l_(447143)        
        # Initialize tab screen
        _n_(447144, "self", lambda: self).tabs = _c_(447147, _a_(447146, _n_(447145, "QtWidgets", lambda: QtWidgets), "QTabWidget"))
        _l_(447148)
        _n_(447149, "self", lambda: self).tab1 = _c_(447152, _a_(447151, _n_(447150, "QtWidgets", lambda: QtWidgets), "QWidget"))        
        _l_(447153)        

        # Add tabs
        _c_(447159, _a_(447156, _a_(447155, _n_(447154, "self", lambda: self), "tabs"), "addTab"), _a_(447158, _n_(447157, "self", lambda: self), "tab1"), "Face")
        _l_(447160)

        _n_(447161, "self", lambda: self).display = _c_(447163, _n_(447162, "PlayStreaming", lambda: PlayStreaming))
        _l_(447164)
        # Create first tab
        _c_(447167, _a_(447166, _n_(447165, "self", lambda: self), "createGridLayout"))
        _l_(447168)
        _a_(447170, _n_(447169, "self", lambda: self), "tab1").layout = _c_(447173, _a_(447172, _n_(447171, "QtWidgets", lambda: QtWidgets), "QVBoxLayout"))
        _l_(447174)
        _c_(447181, _a_(447178, _a_(447177, _a_(447176, _n_(447175, "self", lambda: self), "tab1"), "layout"), "addWidget"), _a_(447180, _n_(447179, "self", lambda: self), "display"), stretch=1)
        _l_(447182)
        _c_(447189, _a_(447186, _a_(447185, _a_(447184, _n_(447183, "self", lambda: self), "tab1"), "layout"), "addWidget"), _a_(447188, _n_(447187, "self", lambda: self), "horizontalGroupBox"))
        _l_(447190)
        _c_(447197, _a_(447193, _a_(447192, _n_(447191, "self", lambda: self), "tab1"), "setLayout"), _a_(447196, _a_(447195, _n_(447194, "self", lambda: self), "tab1"), "layout"))
        _l_(447198)

        # Add tabs to widget
        _n_(447199, "self", lambda: self).layout = _c_(447203, _a_(447201, _n_(447200, "QtWidgets", lambda: QtWidgets), "QVBoxLayout"), _n_(447202, "self", lambda: self))
        _l_(447204)
        _c_(447210, _a_(447207, _a_(447206, _n_(447205, "self", lambda: self), "layout"), "addWidget"), _a_(447209, _n_(447208, "self", lambda: self), "tabs"))
        _l_(447211)

    def createGridLayout(self):
        _l_(447320)

        hlay1 = _c_(447215, _a_(447214, _n_(447213, "QtWidgets", lambda: QtWidgets), "QVBoxLayout"))   
        _l_(447216)   
        _n_(447217, "self", lambda: self).horizontalGroupBox = _c_(447220, _a_(447219, _n_(447218, "QtWidgets", lambda: QtWidgets), "QGroupBox"), "")
        _l_(447221)
        _c_(447225, _a_(447224, _a_(447223, _n_(447222, "self", lambda: self), "horizontalGroupBox"), "setStyleSheet"), "QGroupBox{ background-color: red; border: none;}")          
        _l_(447226)          
        _n_(447227, "self", lambda: self).ScaleUpButton=_c_(447230, _a_(447229, _n_(447228, "QtWidgets", lambda: QtWidgets), "QPushButton"), 'ScaleUp')
        _l_(447231)
        _c_(447239, _a_(447235, _a_(447234, _a_(447233, _n_(447232, "self", lambda: self), "ScaleUpButton"), "clicked"), "connect"), _a_(447238, _a_(447237, _n_(447236, "self", lambda: self), "display"), "scaleupSignal"))
        _l_(447240)
        _c_(447245, _a_(447242, _n_(447241, "hlay1", lambda: hlay1), "addWidget"), _a_(447244, _n_(447243, "self", lambda: self), "ScaleUpButton")) 
        _l_(447246) 
        _n_(447247, "self", lambda: self).ScaleDownButton=_c_(447250, _a_(447249, _n_(447248, "QtWidgets", lambda: QtWidgets), "QPushButton"), 'ScaleDown')
        _l_(447251)
        _c_(447259, _a_(447255, _a_(447254, _a_(447253, _n_(447252, "self", lambda: self), "ScaleDownButton"), "clicked"), "connect"), _a_(447258, _a_(447257, _n_(447256, "self", lambda: self), "display"), "scaledownSignal"))
        _l_(447260)
        _c_(447265, _a_(447262, _n_(447261, "hlay1", lambda: hlay1), "addWidget"), _a_(447264, _n_(447263, "self", lambda: self), "ScaleDownButton")) 
        _l_(447266) 
        _n_(447267, "self", lambda: self).resetButton=_c_(447270, _a_(447269, _n_(447268, "QtWidgets", lambda: QtWidgets), "QPushButton"), 'Reset')
        _l_(447271)
        _c_(447276, _a_(447273, _n_(447272, "hlay1", lambda: hlay1), "addWidget"), _a_(447275, _n_(447274, "self", lambda: self), "resetButton"))
        _l_(447277)
        _c_(447285, _a_(447281, _a_(447280, _a_(447279, _n_(447278, "self", lambda: self), "resetButton"), "clicked"), "connect"), _a_(447284, _a_(447283, _n_(447282, "self", lambda: self), "display"), "resetallarraysSignal"))
        _l_(447286)
        _n_(447287, "self", lambda: self).RecognizeButton=_c_(447290, _a_(447289, _n_(447288, "QtWidgets", lambda: QtWidgets), "QPushButton"), 'Recognize')
        _l_(447291)
        _c_(447299, _a_(447295, _a_(447294, _a_(447293, _n_(447292, "self", lambda: self), "RecognizeButton"), "clicked"), "connect"), _a_(447298, _a_(447297, _n_(447296, "self", lambda: self), "display"), "send_signal"))
        _l_(447300)
        _c_(447305, _a_(447302, _n_(447301, "hlay1", lambda: hlay1), "addWidget"), _a_(447304, _n_(447303, "self", lambda: self), "RecognizeButton"))             
        _l_(447306)             
        _c_(447311, _a_(447309, _a_(447308, _n_(447307, "self", lambda: self), "layout"), "addLayout"), _n_(447310, "hlay1", lambda: hlay1))
        _l_(447312)
        _c_(447318, _a_(447315, _a_(447314, _n_(447313, "self", lambda: self), "horizontalGroupBox"), "setLayout"), _a_(447317, _n_(447316, "self", lambda: self), "layout"))
        _l_(447319)