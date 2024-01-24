# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/27453945/where-is-this-typeerror-coming-from
#New User for EPM#
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(664533)

except ImportError:
    pass
try:
    import platform
    _l_(664535)

except ImportError:
    pass
try:
    import sys
    _l_(664537)

except ImportError:
    pass
try:
    from math import *
    _l_(664539)

except ImportError:
    pass
try:
    from PyQt4 import QtCore, QtGui
    _l_(664541)

except ImportError:
    pass
__version__ = '1.0.0'
_l_(664542)



class NewUser(_a_(664544, _n_(664543, "QtGui", lambda: QtGui), "QDialog")):
    _l_(664957)

    def __init__(self, parent):
        _l_(664556)

        _c_(664550, _a_(664548, _n_(664545, "super", lambda: super)(_n_(664546, "NewUser", lambda: NewUser), _n_(664547, "self", lambda: self)), "__init__"), _n_(664549, "parent", lambda: parent))
        _l_(664551)

        _c_(664554, _a_(664553, _n_(664552, "self", lambda: self), "initUi"))
        _l_(664555)

    def initUi(self):
        _l_(664781)


        global name, email, setPass, passRepeat, nameEdit, emailEdit
        _l_(664557)
        global setPassEdit, passRepeatEdit, ccIssueEdit, dbIssueEdit
        _l_(664558)
        global pinEdit, ccIssueChkBx1, ccIssueChkBx2, adminChkBx
        _l_(664559)
        global saveBtn, cancelBtn
        _l_(664560)

        name = _c_(664564, _a_(664562, _n_(664561, "QtGui", lambda: QtGui), "QLabel"), 'Name: ', _n_(664563, "self", lambda: self))
        _l_(664565)
        email = _c_(664569, _a_(664567, _n_(664566, "QtGui", lambda: QtGui), "QLabel"), 'Email: ', _n_(664568, "self", lambda: self))
        _l_(664570)
        setPass = _c_(664574, _a_(664572, _n_(664571, "QtGui", lambda: QtGui), "QLabel"), 'Set Password: ', _n_(664573, "self", lambda: self))
        _l_(664575)
        passRepeat = _c_(664579, _a_(664577, _n_(664576, "QtGui", lambda: QtGui), "QLabel"), 'Repeat Password', _n_(664578, "self", lambda: self))
        _l_(664580)

        nameEdit = _c_(664584, _a_(664582, _n_(664581, "QtGui", lambda: QtGui), "QLineEdit"), _n_(664583, "self", lambda: self))
        _l_(664585)
        emailEdit = _c_(664589, _a_(664587, _n_(664586, "QtGui", lambda: QtGui), "QLineEdit"), _n_(664588, "self", lambda: self))
        _l_(664590)
        setPassEdit = _c_(664594, _a_(664592, _n_(664591, "QtGui", lambda: QtGui), "QLineEdit"), _n_(664593, "self", lambda: self))
        _l_(664595)
        passRepeatEdit = _c_(664599, _a_(664597, _n_(664596, "QtGui", lambda: QtGui), "QLineEdit"), _n_(664598, "self", lambda: self))
        _l_(664600)
        ccIssueEdit = _c_(664604, _a_(664602, _n_(664601, "QtGui", lambda: QtGui), "QLineEdit"), _n_(664603, "self", lambda: self))
        _l_(664605)
        dbIssueEdit = _c_(664609, _a_(664607, _n_(664606, "QtGui", lambda: QtGui), "QLineEdit"), _n_(664608, "self", lambda: self))
        _l_(664610)
        pinEdit = _c_(664614, _a_(664612, _n_(664611, "QtGui", lambda: QtGui), "QLineEdit"), 'PIN', _n_(664613, "self", lambda: self))
        _l_(664615)
        cvcEdit = _c_(664619, _a_(664617, _n_(664616, "QtGui", lambda: QtGui), "QLineEdit"), 'CVC', _n_(664618, "self", lambda: self))
        _l_(664620)

        ccIssueChkBx1 = _c_(664624, _a_(664622, _n_(664621, "QtGui", lambda: QtGui), "QCheckBox"), 'Credit Card Issued', _n_(664623, "self", lambda: self))
        _l_(664625)
        ccIssueChkBx2 = _c_(664629, _a_(664627, _n_(664626, "QtGui", lambda: QtGui), "QCheckBox"), 'Debit Card Issued', _n_(664628, "self", lambda: self))
        _l_(664630)
        adminChkBx = _c_(664634, _a_(664632, _n_(664631, "QtGui", lambda: QtGui), "QCheckBox"), 'Make Admin', _n_(664633, "self", lambda: self))
        _l_(664635)

        saveBtn = _c_(664639, _a_(664637, _n_(664636, "QtGui", lambda: QtGui), "QPushButton"), 'Save and Close', _n_(664638, "self", lambda: self))
        _l_(664640)
        cancelBtn = _c_(664644, _a_(664642, _n_(664641, "QtGui", lambda: QtGui), "QPushButton"), 'Cancel', _n_(664643, "self", lambda: self))
        _l_(664645)

        ui = _c_(664648, _a_(664647, _n_(664646, "QtGui", lambda: QtGui), "QGridLayout"))
        _l_(664649)

        _c_(664653, _a_(664651, _n_(664650, "ui", lambda: ui), "addWidget"), _n_(664652, "name", lambda: name), 1, 0)
        _l_(664654)
        _c_(664658, _a_(664656, _n_(664655, "ui", lambda: ui), "addWidget"), _n_(664657, "email", lambda: email), 2, 0)
        _l_(664659)
        _c_(664663, _a_(664661, _n_(664660, "ui", lambda: ui), "addWidget"), _n_(664662, "setPass", lambda: setPass), 3, 0)
        _l_(664664)
        _c_(664668, _a_(664666, _n_(664665, "ui", lambda: ui), "addWidget"), _n_(664667, "passRepeat", lambda: passRepeat), 4, 0)
        _l_(664669)
        _c_(664673, _a_(664671, _n_(664670, "ui", lambda: ui), "addWidget"), _n_(664672, "nameEdit", lambda: nameEdit), 1, 1, 1, 4)
        _l_(664674)
        _c_(664678, _a_(664676, _n_(664675, "ui", lambda: ui), "addWidget"), _n_(664677, "emailEdit", lambda: emailEdit), 2, 1, 1, 4)
        _l_(664679)
        _c_(664683, _a_(664681, _n_(664680, "ui", lambda: ui), "addWidget"), _n_(664682, "setPassEdit", lambda: setPassEdit), 3, 1, 1, 4)
        _l_(664684)
        _c_(664688, _a_(664686, _n_(664685, "ui", lambda: ui), "addWidget"), _n_(664687, "passRepeatEdit", lambda: passRepeatEdit), 4, 1, 1, 4)
        _l_(664689)
        _c_(664693, _a_(664691, _n_(664690, "ui", lambda: ui), "addWidget"), _n_(664692, "ccIssueEdit", lambda: ccIssueEdit), 5, 1, 1, 3)
        _l_(664694)
        _c_(664698, _a_(664696, _n_(664695, "ui", lambda: ui), "addWidget"), _n_(664697, "cvcEdit", lambda: cvcEdit), 5, 4, 1, 1)
        _l_(664699)
        _c_(664703, _a_(664701, _n_(664700, "ui", lambda: ui), "addWidget"), _n_(664702, "dbIssueEdit", lambda: dbIssueEdit), 6, 1, 1, 3)
        _l_(664704)
        _c_(664708, _a_(664706, _n_(664705, "ui", lambda: ui), "addWidget"), _n_(664707, "pinEdit", lambda: pinEdit), 6, 4, 1, 1)
        _l_(664709)
        _c_(664713, _a_(664711, _n_(664710, "ui", lambda: ui), "addWidget"), _n_(664712, "ccIssueChkBx1", lambda: ccIssueChkBx1), 5, 0)
        _l_(664714)
        _c_(664718, _a_(664716, _n_(664715, "ui", lambda: ui), "addWidget"), _n_(664717, "ccIssueChkBx2", lambda: ccIssueChkBx2), 6, 0)
        _l_(664719)
        _c_(664723, _a_(664721, _n_(664720, "ui", lambda: ui), "addWidget"), _n_(664722, "adminChkBx", lambda: adminChkBx), 7, 4)
        _l_(664724)
        _c_(664728, _a_(664726, _n_(664725, "ui", lambda: ui), "addWidget"), _n_(664727, "saveBtn", lambda: saveBtn), 7, 0)
        _l_(664729)
        _c_(664733, _a_(664731, _n_(664730, "ui", lambda: ui), "addWidget"), _n_(664732, "cancelBtn", lambda: cancelBtn), 7, 1)
        _l_(664734)

        _c_(664740, _a_(664737, _a_(664736, _n_(664735, "ccIssueChkBx1", lambda: ccIssueChkBx1), "stateChanged"), "connect"), _a_(664739, _n_(664738, "self", lambda: self), "ccEn"))
        _l_(664741)
        _c_(664747, _a_(664744, _a_(664743, _n_(664742, "ccIssueChkBx2", lambda: ccIssueChkBx2), "stateChanged"), "connect"), _a_(664746, _n_(664745, "self", lambda: self), "dbEn"))
        _l_(664748)

        _c_(664754, _a_(664751, _a_(664750, _n_(664749, "saveBtn", lambda: saveBtn), "clicked"), "connect"), _a_(664753, _n_(664752, "self", lambda: self), "save"))
        _l_(664755)

        _c_(664758, _a_(664757, _n_(664756, "self", lambda: self), "ccEn"))
        _l_(664759)
        _c_(664762, _a_(664761, _n_(664760, "self", lambda: self), "dbEn"))
        _l_(664763)

        _c_(664767, _a_(664765, _n_(664764, "self", lambda: self), "setLayout"), _n_(664766, "ui", lambda: ui))
        _l_(664768)
        _c_(664771, _a_(664770, _n_(664769, "self", lambda: self), "resize"), 400, 300)
        _l_(664772)
        _c_(664775, _a_(664774, _n_(664773, "self", lambda: self), "center"))
        _l_(664776)
        _c_(664779, _a_(664778, _n_(664777, "self", lambda: self), "show"))
        _l_(664780)

    def ccEn(self):
        _l_(664794)


        if _c_(664784, _a_(664783, _n_(664782, "ccIssueChkBx1", lambda: ccIssueChkBx1), "isChecked")):
            _l_(664793)

            _c_(664787, _a_(664786, _n_(664785, "ccIssueEdit", lambda: ccIssueEdit), "setEnabled"), True)
            _l_(664788)
        else:
            _c_(664791, _a_(664790, _n_(664789, "ccIssueEdit", lambda: ccIssueEdit), "setEnabled"), False)
            _l_(664792)

    def dbEn(self):
        _l_(664815)


        if _c_(664797, _a_(664796, _n_(664795, "ccIssueChkBx2", lambda: ccIssueChkBx2), "isChecked")):
            _l_(664814)

            _c_(664800, _a_(664799, _n_(664798, "dbIssueEdit", lambda: dbIssueEdit), "setEnabled"), True)
            _l_(664801)
            _c_(664804, _a_(664803, _n_(664802, "pinEdit", lambda: pinEdit), "setEnabled"), True)
            _l_(664805)
        else:
            _c_(664808, _a_(664807, _n_(664806, "dbIssueEdit", lambda: dbIssueEdit), "setEnabled"), False)
            _l_(664809)
            _c_(664812, _a_(664811, _n_(664810, "pinEdit", lambda: pinEdit), "setEnabled"), False)
            _l_(664813)

    def save(self, userName, userEmail, userPass, userCC=None, userCVC=None,
            userDB=None, userPin=None, isAdmin=False):
        _l_(664931)


        userName = _c_(664819, _a_(664818, _a_(664817, _n_(664816, "self", lambda: self), "nameEdit"), "text"))
        _l_(664820)
        userEmail = _c_(664824, _a_(664823, _a_(664822, _n_(664821, "self", lambda: self), "emailEdit"), "text"))
        _l_(664825)

        if _c_(664829, _a_(664828, _a_(664827, _n_(664826, "self", lambda: self), "setPassEdit"), "text")) == _c_(664833, _a_(664832, _a_(664831, _n_(664830, "self", lambda: self), "passRepeatEdit"), "text")):
            _l_(664840)

            userPass = _c_(664837, _a_(664836, _a_(664835, _n_(664834, "self", lambda: self), "setPassEdit"), "text"))
            _l_(664838)
        else:
            pass #Throw error here
            _l_(664839) #Throw error here

        if _c_(664844, _a_(664843, _a_(664842, _n_(664841, "self", lambda: self), "ccIssueChkBx1"), "isChecked")):
            _l_(664886)

            if _c_(664848, _n_(664845, "len", lambda: len), _a_(664847, _n_(664846, "self", lambda: self), "ccIssueEdit")) == 15 and _c_(664852, _n_(664849, "len", lambda: len), _a_(664851, _n_(664850, "self", lambda: self), "cvcEdit")) == 4:
                _l_(664885)

                userCC = _c_(664856, _a_(664855, _a_(664854, _n_(664853, "self", lambda: self), "ccIssueEdit"), "text"))
                _l_(664857)
                userCVC = _c_(664861, _a_(664860, _a_(664859, _n_(664858, "self", lambda: self), "cvcEdit"), "text"))
                _l_(664862)
                ccType = 'AMEX'
                _l_(664863)
            elif _c_(664867, _n_(664864, "len", lambda: len), _a_(664866, _n_(664865, "self", lambda: self), "ccIssueEdit")) == 16 and _c_(664871, _n_(664868, "len", lambda: len), _a_(664870, _n_(664869, "self", lambda: self), "cvcEdit")) == 3:
                _l_(664884)

                userCC = _c_(664875, _a_(664874, _a_(664873, _n_(664872, "self", lambda: self), "ccIssueEdit"), "text"))
                _l_(664876)
                userCVC = _c_(664880, _a_(664879, _a_(664878, _n_(664877, "self", lambda: self), "cvcEdit"), "text"))
                _l_(664881)
                ccType = 'MC/Visa'
                _l_(664882)
            else:
                pass #Throw error here
                _l_(664883) #Throw error here

        if _c_(664890, _a_(664889, _a_(664888, _n_(664887, "self", lambda: self), "ccIssueChkBx2"), "isChecked")):
            _l_(664911)

            if _c_(664894, _n_(664891, "len", lambda: len), _a_(664893, _n_(664892, "self", lambda: self), "dbIssueEdit")) == 16 and _c_(664898, _n_(664895, "len", lambda: len), _a_(664897, _n_(664896, "self", lambda: self), "pinEdit")) == 4:
                _l_(664910)

                userDB = _c_(664902, _a_(664901, _a_(664900, _n_(664899, "self", lambda: self), "dbIssueEdit"), "text"))
                _l_(664903)
                userPin = _c_(664907, _a_(664906, _a_(664905, _n_(664904, "self", lambda: self), "pinEdit"), "text"))
                _l_(664908)
            else:
                pass #Throw error here
                _l_(664909) #Throw error here

        if _c_(664915, _a_(664914, _a_(664913, _n_(664912, "self", lambda: self), "adminChkBx"), "isChecked")):
            _l_(664917)

            isAdmin = True
            _l_(664916)

        userSave = _c_(664929, _a_(664919, _n_(664918, "newUser", lambda: newUser), "Save"), _n_(664920, "userName", lambda: userName), _n_(664921, "userEmail", lambda: userEmail), _n_(664922, "userPass", lambda: userPass), _n_(664923, "userCC", lambda: userCC), _n_(664924, "userCVC", lambda: userCVC),
            _n_(664925, "ccType", lambda: ccType), _n_(664926, "userDB", lambda: userDB), _n_(664927, "userPin", lambda: userPin), _n_(664928, "isAdmin", lambda: isAdmin))
        _l_(664930)

    def center(self):
        _l_(664956)


        qr = _c_(664934, _a_(664933, _n_(664932, "self", lambda: self), "frameGeometry"))
        _l_(664935)
        cp = _c_(664942, _a_(664941, _c_(664940, _a_(664939, _c_(664938, _a_(664937, _n_(664936, "QtGui", lambda: QtGui), "QDesktopWidget")), "availableGeometry")), "center"))
        _l_(664943)
        _c_(664947, _a_(664945, _n_(664944, "qr", lambda: qr), "moveCenter"), _n_(664946, "cp", lambda: cp))
        _l_(664948)
        _c_(664954, _a_(664950, _n_(664949, "self", lambda: self), "move"), _c_(664953, _a_(664952, _n_(664951, "qr", lambda: qr), "topLeft")))
        _l_(664955)



class Save(_n_(664958, "object", lambda: object)):
    _l_(665003)

    '''Creates a User Object'''
    _l_(664959)

    def __init__(self, userName, userEmail, userPass, userCC, userCVC, ccType,
        userDB, userPin, isAdmin):
        _l_(664964)


        _c_(664962, _a_(664961, _n_(664960, "self", lambda: self), "create"))
        _l_(664963)

    def create(self):
        _l_(665002)


        list = [_n_(664965, "userName", lambda: userName), _n_(664966, "userEmail", lambda: userEmail), _n_(664967, "userPass", lambda: userPass), _n_(664968, "userCC", lambda: userCC), _n_(664969, "userCVC", lambda: userCVC), _n_(664970, "ccType", lambda: ccType), _n_(664971, "userDB", lambda: userDB),
            _n_(664972, "userPin", lambda: userPin), _n_(664973, "isAdmin", lambda: isAdmin)]
        _l_(664974)

        dirName = _c_(664978, _n_(664975, "str", lambda: str), _a_(664977, _n_(664976, "self", lambda: self), "userName"))
        _l_(664979)
        _c_(664983, _a_(664981, _n_(664980, "os", lambda: os), "mkdir"), _n_(664982, "dirName", lambda: dirName))
        _l_(664984)
        _c_(664988, _a_(664986, _n_(664985, "os", lambda: os), "chdir"), _n_(664987, "dirName", lambda: dirName))
        _l_(664989)

        fileName = _c_(664991, _n_(664990, "open", lambda: open), 'profile.txt', 'wb')
        _l_(664992)
        for i in _n_(664993, "list", lambda: list):
            _l_(665001)

            _c_(664999, _a_(664995, _n_(664994, "fileName", lambda: fileName), "write"), _c_(664998, _n_(664996, "str", lambda: str), _n_(664997, "i", lambda: i)))
            _l_(665000)