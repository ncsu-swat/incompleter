# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64745775/typeerror-insert-expenses-missing-1-required-positional-argument-amt
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import budget_buddy
    _l_(641281)

except ImportError:
    pass


total_money = 0
_l_(641282)


def deposits():
    _l_(641288)

    """Deposits function so we can call it later on"""
    aux = _c_(641286, _n_(641283, "float", lambda: float), _c_(641285, _n_(641284, "input", lambda: input), 'Please enter deposit amount:'))
    _l_(641287)
    return aux


def input_expense_item() -> _n_(641289, "tuple", lambda: tuple):
    _l_(641316)

    """
    Prompt the user to enter an expense type, and the amount for the expense
    :return: Tuple - expense type, amount
    """

    expense_type = _c_(641293, _a_(641292, _c_(641291, _n_(641290, "input", lambda: input), "What is the expense item?\n"), "capitalize"))
    _l_(641294)
    cost = None
    _l_(641295)

    # must ensure that the user provides a valid number! In this case, a valid decimal!
    while not _n_(641296, "cost", lambda: cost):
        _l_(641312)

        temp = _c_(641299, _n_(641297, "input", lambda: input), f"How much was '{_n_(641298, 'expense_type', lambda: expense_type)}'?\n")
        _l_(641300)

        try:
            _l_(641311)

            cost = _c_(641303, _n_(641301, "float", lambda: float), _n_(641302, "temp", lambda: temp))
            _l_(641304)

        except _n_(641305, "ValueError", lambda: ValueError):
            _l_(641310)

            _c_(641308, _n_(641306, "print", lambda: print), f"{_n_(641307, 'temp', lambda: temp)} - was an invalid entry. Please make sure you entered a valid number")
            _l_(641309)
    aux = _n_(641313, "expense_type", lambda: expense_type), _n_(641314, "cost", lambda: cost)
    _l_(641315)

    # This is how to return a tuple. This means you can assign two variables when calling this function as seen below
    return aux


def cash_on_hand():
    _l_(641322)

    """
    Cash_on_hand function, this is asking how much money not in bank
    accounts do you have.
    """
    aux = _c_(641320, _n_(641317, "float", lambda: float), _c_(641319, _n_(641318, "input", lambda: input), 'How much money do you have on hand:'))
    _l_(641321)
    return aux


while True:
    _l_(641362)

    menu_option = _c_(641324, _n_(641323, "input", lambda: input), "What option do you want to do?\n" 
                        "1: Enter deposit\n"
                        "2: Enter cash on hand\n"
                        "3: Enter expenses\n"
                        "4: Monthly Deposit Total\n")
    _l_(641325)
    
    if _n_(641326, "menu_option", lambda: menu_option) == "1":
        _l_(641361)

        deposit_amount = _c_(641328, _n_(641327, "deposits", lambda: deposits))
        _l_(641329)
        #total_money += deposit_amount
        _c_(641333, _a_(641331, _n_(641330, "budget_buddy", lambda: budget_buddy), "insert_deposits"), _n_(641332, "deposit_amount", lambda: deposit_amount))
        _l_(641334)
    elif _n_(641335, "menu_option", lambda: menu_option) == "2":
        _l_(641360)

        cash_amount = _c_(641337, _n_(641336, "cash_on_hand", lambda: cash_on_hand))
        _l_(641338)
        #total_money += cash_amount
        _c_(641342, _a_(641340, _n_(641339, "budget_buddy", lambda: budget_buddy), "insert_cash"), _n_(641341, "cash_amount", lambda: cash_amount))
        _l_(641343)

    elif _n_(641344, "menu_option", lambda: menu_option) == "3":
        _l_(641359)

        #new_expense_type, new_expense_amount = input_expense_item()
        #print(f"The user wants to add {new_expense_type} for ${new_expense_amount}")
        expense_type, cost = _c_(641346, _n_(641345, "input_expense_item", lambda: input_expense_item))
        _l_(641347)
        _c_(641351, _a_(641349, _n_(641348, "budget_buddy", lambda: budget_buddy), "insert_expenses"), _n_(641350, "input_expense_item", lambda: input_expense_item))
        _l_(641352)
    
    elif _n_(641353, "menu_option", lambda: menu_option) == "4":
        _l_(641358)

        _c_(641356, _a_(641355, _n_(641354, "budget_buddy", lambda: budget_buddy), "monthly_deposit_total"))
        _l_(641357)