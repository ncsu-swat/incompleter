# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53825116/i-keep-getting-this-error-attributeerror-module-admin-has-no-attribute-run
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class BankSystem(_n_(423504, "object", lambda: object)):
    _l_(423855)

    def __init__(self):
        _l_(423513)

        _n_(423505, "self", lambda: self).accounts_list = []
        _l_(423506)
        _n_(423507, "self", lambda: self).admins_list = []
        _l_(423508)
        _c_(423511, _a_(423510, _n_(423509, "self", lambda: self), "load_bank_data"))
        _l_(423512)

    def load_bank_data(self):
        _l_(423567)


        # create customers
        account_no = 1234
        _l_(423514)
        customer_1 = _c_(423517, _n_(423515, "CustomerAccount", lambda: CustomerAccount), "Adam", "Smith", ["14", "Wilcot Street", "Bath", "B5 5RT"], _n_(423516, "account_no", lambda: account_no), 5000.00)
        _l_(423518)
        _c_(423523, _a_(423521, _a_(423520, _n_(423519, "self", lambda: self), "accounts_list"), "append"), _n_(423522, "customer_1", lambda: customer_1))
        _l_(423524)

        account_no += 5678
        _l_(423525)
        customer_2 = _c_(423528, _n_(423526, "CustomerAccount", lambda: CustomerAccount), "David", "White", ["60", "Holborn Viaduct", "London", "EC1A 2FD"], _n_(423527, "account_no", lambda: account_no),
                                     3200.00)
        _l_(423529)
        _c_(423534, _a_(423532, _a_(423531, _n_(423530, "self", lambda: self), "accounts_list"), "append"), _n_(423533, "customer_2", lambda: customer_2))
        _l_(423535)

        account_no += 3456
        _l_(423536)
        customer_3 = _c_(423539, _n_(423537, "CustomerAccount", lambda: CustomerAccount), "Alice", "Churchil", ["5", "Cardigan Street", "Birmingham", "B4 7BD"], _n_(423538, "account_no", lambda: account_no),
                                     18000.00)
        _l_(423540)
        _c_(423545, _a_(423543, _a_(423542, _n_(423541, "self", lambda: self), "accounts_list"), "append"), _n_(423544, "customer_3", lambda: customer_3))
        _l_(423546)

        account_no += 6789
        _l_(423547)
        customer_4 = _c_(423550, _n_(423548, "CustomerAccount", lambda: CustomerAccount), "Ali", "Abdallah", ["44", "Churchill Way West", "Basingstoke", "RG21 6YR"],
                                     _n_(423549, "account_no", lambda: account_no), 40.00)
        _l_(423551)
        _c_(423556, _a_(423554, _a_(423553, _n_(423552, "self", lambda: self), "accounts_list"), "append"), _n_(423555, "customer_4", lambda: customer_4))
        _l_(423557)

        # create admins
        admin_1 = _c_(423559, _n_(423558, "Admin", lambda: Admin), "Taran", "Basi", ["224", "Kenpas Highway", "Coventry", "CV3 6PB"], 224, "Kenpas Highway", "Coventry", "CV3 6PB", "1", "pass", True)
        _l_(423560)
        _c_(423565, _a_(423563, _a_(423562, _n_(423561, "self", lambda: self), "admins_list"), "append"), _n_(423564, "admin_1", lambda: admin_1))
        _l_(423566)

    def search_admins_by_name(self, admin_username):
        _l_(423590)

        # STEP A.2
        found_admin = None
        _l_(423568)
        for a in _a_(423570, _n_(423569, "self", lambda: self), "admins_list"):
            _l_(423581)

            username = _c_(423573, _a_(423572, _n_(423571, "a", lambda: a), "get_username"))
            _l_(423574)
            if _n_(423575, "username", lambda: username) == _n_(423576, "admin_username", lambda: admin_username):
                _l_(423580)

                found_admin = _n_(423577, "a", lambda: a)
                _l_(423578)
                break
                _l_(423579)
        if _n_(423582, "found_admin", lambda: found_admin) == None:
            _l_(423587)

            _c_(423585, _n_(423583, "print", lambda: print), "\n ❌❌ The Admin %s does not exist! Please try again.\n" % _n_(423584, "admin_username", lambda: admin_username))
            _l_(423586)
        aux = _n_(423588, "found_admin", lambda: found_admin)
        _l_(423589)
        return aux

    def search_customers_by_name(self, customer_lname):
        _l_(423613)

        # STEP A.3
        found_customer = None
        _l_(423591)
        for c in _a_(423593, _n_(423592, "self", lambda: self), "accounts_list"):
            _l_(423604)

            lastname = _c_(423596, _a_(423595, _n_(423594, "c", lambda: c), "get_last_name"))
            _l_(423597)
            if _n_(423598, "lastname", lambda: lastname) == _n_(423599, "customer_lname", lambda: customer_lname):
                _l_(423603)

                found_customer = _n_(423600, "c", lambda: c)
                _l_(423601)
                break
                _l_(423602)
        if _n_(423605, "found_customer", lambda: found_customer) == None:
            _l_(423610)

            _c_(423608, _n_(423606, "print", lambda: print), "\n The customer %s does not exist! Try again...\n" % _n_(423607, "customer_lname", lambda: customer_lname))
            _l_(423609)
        aux = _n_(423611, "found_customer", lambda: found_customer)
        _l_(423612)
        return aux

    def main_menu(self):
        _l_(423645)

        # print the options you have
        _c_(423615, _n_(423614, "print", lambda: print))
        _l_(423616)
        _c_(423618, _n_(423617, "print", lambda: print))
        _l_(423619)
        _c_(423621, _n_(423620, "print", lambda: print), "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        _l_(423622)
        _c_(423624, _n_(423623, "print", lambda: print), "Welcome to the Python Bank System")
        _l_(423625)
        _c_(423627, _n_(423626, "print", lambda: print), "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        _l_(423628)
        _c_(423630, _n_(423629, "print", lambda: print), "1) Admin login")
        _l_(423631)
        _c_(423633, _n_(423632, "print", lambda: print), "2) Quit Python Bank System")
        _l_(423634)
        _c_(423636, _n_(423635, "print", lambda: print), " ")
        _l_(423637)
        option = _c_(423641, _n_(423638, "int", lambda: int), _c_(423640, _n_(423639, "input", lambda: input), "Choose your option: "))
        _l_(423642)
        aux = _n_(423643, "option", lambda: option)
        _l_(423644)
        return aux

    def run_main_options(self):
        _l_(423684)

        loop = 1
        _l_(423646)
        while _n_(423647, "loop", lambda: loop) == 1:
            _l_(423680)

            choice = _c_(423650, _a_(423649, _n_(423648, "self", lambda: self), "main_menu"))
            _l_(423651)
            if _n_(423652, "choice", lambda: choice) == 1:
                _l_(423679)

                username = _c_(423654, _n_(423653, "input", lambda: input), "\n Please input admin username: ")
                _l_(423655)
                password = _c_(423657, _n_(423656, "input", lambda: input), "\n Please input admin password: ")
                _l_(423658)
                msg, admin_obj = _c_(423663, _a_(423660, _n_(423659, "self", lambda: self), "admin_login"), _n_(423661, "username", lambda: username), _n_(423662, "password", lambda: password))
                _l_(423664)
                _c_(423667, _n_(423665, "print", lambda: print), _n_(423666, "msg", lambda: msg))
                _l_(423668)
                if _n_(423669, "admin_obj", lambda: admin_obj) != None:
                    _l_(423675)

                    _c_(423673, _a_(423671, _n_(423670, "self", lambda: self), "run_admin_options"), _n_(423672, "admin_obj", lambda: admin_obj))
                    _l_(423674)
            elif _n_(423676, "choice", lambda: choice) == 2:
                _l_(423678)

                loop = 0
                _l_(423677)
        _c_(423682, _n_(423681, "print", lambda: print), "\n Thank-You for stopping by the bank!")
        _l_(423683)

    def transferMoney(self, sender_lname, receiver_lname, receiver_account_no, amount):
        _l_(423686)

        # ToDo
        pass
        _l_(423685)

    def admin_login(self, username, password):
        _l_(423704)

        # STEP A.1
        found_admin = _c_(423690, _a_(423688, _n_(423687, "self", lambda: self), "search_admins_by_name"), _n_(423689, "username", lambda: username))
        _l_(423691)
        msg = "\n ❌ Login failed"
        _l_(423692)
        if _n_(423693, "found_admin", lambda: found_admin) != None:
            _l_(423700)

            if _c_(423696, _a_(423695, _n_(423694, "found_admin", lambda: found_admin), "get_password")) == _n_(423697, "password", lambda: password):
                _l_(423699)

                msg = "\n ✔ Login successful"
                _l_(423698)
        aux = _n_(423701, "msg", lambda: msg), _n_(423702, "found_admin", lambda: found_admin)
        _l_(423703)
        return aux

    def admin_menu(self, admin_obj):
        _l_(423748)

        # print the options you have
        _c_(423706, _n_(423705, "print", lambda: print), " ")
        _l_(423707)
        _c_(423715, _n_(423708, "print", lambda: print), "Welcome Admin %s %s! Available options are:" % (_c_(423711, _a_(423710, _n_(423709, "admin_obj", lambda: admin_obj), "get_first_name")), _c_(423714, _a_(423713, _n_(423712, "admin_obj", lambda: admin_obj), "get_last_name"))))
        _l_(423716)
        _c_(423718, _n_(423717, "print", lambda: print), "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        _l_(423719)
        _c_(423721, _n_(423720, "print", lambda: print), "1) Transfer money")
        _l_(423722)
        _c_(423724, _n_(423723, "print", lambda: print), "2) Customer account operations & profile settings")
        _l_(423725)
        _c_(423727, _n_(423726, "print", lambda: print), "3) Delete customer")
        _l_(423728)
        _c_(423730, _n_(423729, "print", lambda: print), "4) Print all customers detail")
        _l_(423731)
        _c_(423733, _n_(423732, "print", lambda: print), "5) Update admin information")
        _l_(423734)
        _c_(423736, _n_(423735, "print", lambda: print), "6) Sign out")
        _l_(423737)
        _c_(423739, _n_(423738, "print", lambda: print), " ")
        _l_(423740)
        option = _c_(423744, _n_(423741, "int", lambda: int), _c_(423743, _n_(423742, "input", lambda: input), "Choose your option: "))
        _l_(423745)
        aux = _n_(423746, "option", lambda: option)
        _l_(423747)
        return aux

    def run_admin_options(self, admin_obj):
        _l_(423837)

        loop = 1
        _l_(423749)
        while _n_(423750, "loop", lambda: loop) == 1:
            _l_(423836)

            choice = _c_(423754, _a_(423752, _n_(423751, "self", lambda: self), "admin_menu"), _n_(423753, "admin_obj", lambda: admin_obj))
            _l_(423755)
            if _n_(423756, "choice", lambda: choice) == 1:
                _l_(423835)

                sender_lname = _c_(423758, _n_(423757, "input", lambda: input), "\n Please input sender surname: ")
                _l_(423759)
                amount = _c_(423763, _n_(423760, "float", lambda: float), _c_(423762, _n_(423761, "input", lambda: input), "\n Please input the amount to be transferred: "))
                _l_(423764)
                receiver_lname = _c_(423766, _n_(423765, "input", lambda: input), "\n Please input receiver surname: ")
                _l_(423767)
                receiver_account_no = _c_(423769, _n_(423768, "input", lambda: input), "\n Please input receiver account number: ")
                _l_(423770)
                _c_(423777, _a_(423772, _n_(423771, "self", lambda: self), "transferMoney"), _n_(423773, "sender_lname", lambda: sender_lname), _n_(423774, "receiver_lname", lambda: receiver_lname), _n_(423775, "receiver_account_no", lambda: receiver_account_no), _n_(423776, "amount", lambda: amount))
                _l_(423778)

            elif _n_(423779, "choice", lambda: choice) == 2:
                _l_(423834)

                # STEP A.4
                customer_name = _c_(423781, _n_(423780, "input", lambda: input), "\n Please input customer surname :\n")
                _l_(423782)
                customer_account = _c_(423786, _a_(423784, _n_(423783, "self", lambda: self), "search_customers_by_name"), _n_(423785, "customer_name", lambda: customer_name))
                _l_(423787)
                if _n_(423788, "customer_account", lambda: customer_account) != None:
                    _l_(423793)

                    _c_(423791, _a_(423790, _n_(423789, "customer_account", lambda: customer_account), "run_account_options"))
                    _l_(423792)

            elif _n_(423794, "choice", lambda: choice) == 3:
                _l_(423833)

                # STEP A.5
                customer_name = _c_(423796, _n_(423795, "input", lambda: input), "\n input customer surname you want to delete: ")
                _l_(423797)
                customer_account = _c_(423801, _a_(423799, _n_(423798, "self", lambda: self), "search_customers_by_name"), _n_(423800, "customer_name", lambda: customer_name))
                _l_(423802)
                if _n_(423803, "customer_account", lambda: customer_account) != None:
                    _l_(423814)

                    _c_(423808, _a_(423806, _a_(423805, _n_(423804, "self", lambda: self), "accounts_list"), "remove"), _n_(423807, "customer_account", lambda: customer_account))
                    _l_(423809)
                    _c_(423812, _n_(423810, "print", lambda: print), "%s was successfully deleted!" % _n_(423811, "customer_name", lambda: customer_name))
                    _l_(423813)

            elif _n_(423815, "choice", lambda: choice) == 4:
                _l_(423832)

                # STEP A.6
                _c_(423818, _a_(423817, _n_(423816, "self", lambda: self), "print_all_accounts_details"))
                _l_(423819)

            elif _n_(423820, "choice", lambda: choice) == 5:
                _l_(423831)

                _c_(423823, _a_(423822, _n_(423821, "admin", lambda: admin), "run_admin_options"))
                _l_(423824)

            elif _n_(423825, "choice", lambda: choice) == 6:
                _l_(423830)

                loop = 0
                _l_(423826)
                _c_(423828, _n_(423827, "print", lambda: print), "\n You have successfully logged out")
                _l_(423829)

    def print_all_accounts_details(self):
        _l_(423854)

        # list related operation - move to main.py
        i = 0
        _l_(423838)
        for c in _a_(423840, _n_(423839, "self", lambda: self), "accounts_list"):
            _l_(423853)

            i += 1
            _l_(423841)
            _c_(423844, _n_(423842, "print", lambda: print), '\n %d. ' % _n_(423843, "i", lambda: i), end=' ')
            _l_(423845)
            _c_(423848, _a_(423847, _n_(423846, "c", lambda: c), "print_details"))
            _l_(423849)
            _c_(423851, _n_(423850, "print", lambda: print), "------------------------")
            _l_(423852)


app = _c_(423857, _n_(423856, "BankSystem", lambda: BankSystem))
_l_(423858)
_c_(423861, _a_(423860, _n_(423859, "app", lambda: app), "run_main_options"))
_l_(423862)