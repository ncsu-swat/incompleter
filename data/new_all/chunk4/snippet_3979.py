# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64745775/typeerror-insert-expenses-missing-1-required-positional-argument-amt
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import budget_buddy
    _l_(600627)

except ImportError:
    pass


total_money = 0
_l_(600628)


def deposits():
    _l_(600634)

    """Deposits function so we can call it later on"""
    aux = _c_(600632, _n_(600629, "float", lambda: float), _c_(600631, _n_(600630, "input", lambda: input), 'Please enter deposit amount:'))
    _l_(600633)
    return aux


def input_expense_item() -> _n_(600635, "tuple", lambda: tuple):
    _l_(600662)

    """
    Prompt the user to enter an expense type, and the amount for the expense
    :return: Tuple - expense type, amount
    """

    expense_type = _c_(600639, _a_(600638, _c_(600637, _n_(600636, "input", lambda: input), "What is the expense item?\n"), "capitalize"))
    _l_(600640)
    cost = None
    _l_(600641)

    # must ensure that the user provides a valid number! In this case, a valid decimal!
    while not _n_(600642, "cost", lambda: cost):
        _l_(600658)

        temp = _c_(600645, _n_(600643, "input", lambda: input), f"How much was '{_n_(600644, 'expense_type', lambda: expense_type)}'?\n")
        _l_(600646)

        try:
            _l_(600657)

            cost = _c_(600649, _n_(600647, "float", lambda: float), _n_(600648, "temp", lambda: temp))
            _l_(600650)

        except _n_(600651, "ValueError", lambda: ValueError):
            _l_(600656)

            _c_(600654, _n_(600652, "print", lambda: print), f"{_n_(600653, 'temp', lambda: temp)} - was an invalid entry. Please make sure you entered a valid number")
            _l_(600655)
    aux = _n_(600659, "expense_type", lambda: expense_type), _n_(600660, "cost", lambda: cost)
    _l_(600661)

    # This is how to return a tuple. This means you can assign two variables when calling this function as seen below
    return aux


def cash_on_hand():
    _l_(600668)

    """
    Cash_on_hand function, this is asking how much money not in bank
    accounts do you have.
    """
    aux = _c_(600666, _n_(600663, "float", lambda: float), _c_(600665, _n_(600664, "input", lambda: input), 'How much money do you have on hand:'))
    _l_(600667)
    return aux


while True:
    _l_(600708)

    menu_option = _c_(600670, _n_(600669, "input", lambda: input), "What option do you want to do?\n" 
                        "1: Enter deposit\n"
                        "2: Enter cash on hand\n"
                        "3: Enter expenses\n"
                        "4: Monthly Deposit Total\n")
    _l_(600671)
    
    if _n_(600672, "menu_option", lambda: menu_option) == "1":
        _l_(600707)

        deposit_amount = _c_(600674, _n_(600673, "deposits", lambda: deposits))
        _l_(600675)
        #total_money += deposit_amount
        _c_(600679, _a_(600677, _n_(600676, "budget_buddy", lambda: budget_buddy), "insert_deposits"), _n_(600678, "deposit_amount", lambda: deposit_amount))
        _l_(600680)
    elif _n_(600681, "menu_option", lambda: menu_option) == "2":
        _l_(600706)

        cash_amount = _c_(600683, _n_(600682, "cash_on_hand", lambda: cash_on_hand))
        _l_(600684)
        #total_money += cash_amount
        _c_(600688, _a_(600686, _n_(600685, "budget_buddy", lambda: budget_buddy), "insert_cash"), _n_(600687, "cash_amount", lambda: cash_amount))
        _l_(600689)

    elif _n_(600690, "menu_option", lambda: menu_option) == "3":
        _l_(600705)

        #new_expense_type, new_expense_amount = input_expense_item()
        #print(f"The user wants to add {new_expense_type} for ${new_expense_amount}")
        expense_type, cost = _c_(600692, _n_(600691, "input_expense_item", lambda: input_expense_item))
        _l_(600693)
        _c_(600697, _a_(600695, _n_(600694, "budget_buddy", lambda: budget_buddy), "insert_expenses"), _n_(600696, "input_expense_item", lambda: input_expense_item))
        _l_(600698)
    
    elif _n_(600699, "menu_option", lambda: menu_option) == "4":
        _l_(600704)

        _c_(600702, _a_(600701, _n_(600700, "budget_buddy", lambda: budget_buddy), "monthly_deposit_total"))
        _l_(600703)