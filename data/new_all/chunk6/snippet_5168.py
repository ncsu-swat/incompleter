# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68814528/total-printsubtotal-tax-tip-typeerror-unsupported-operand-types-for
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
meal_cost = 10.00
_l_(370089)
tax_rate = 0.08
_l_(370090)
tip_rate = 0.20
_l_(370091)

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
 
#When eating at a restaurant in the United States, it's
#customary to have two percentage-based surcharges added on
#top of your bill: sales tax and tip. These percentages are
#both applies to the original cost of the meal. For example,
#a 10.00 meal with 8% sales tax and 20% tip would add 0.80
#for tax (0.08 * 10.00) and 2.00 for tip (0.20 * 10.00).
#
#The variables above create the cost of a meal and identify
#what percentage should be charged for tax and tip.
#
#Add some code below that will print the "receipt" for a
#meal purchase. The receipt should look like this:
#
#Subtotal: 10.00
#Tax: 0.8
#Tip: 2.0
#Total: 12.8
#
#Subtotal is the original value of meal_cost, tax is the
#tax rate times the meal cost, the tip is the tip rate times
#the meal cost, and the total is the sum of all three numbers.
#Don't worry about the number of decimal places; it's fine
#if your code leaves off some numbers (like 0.8 for tax) or
#includes too many decimal places (like 2.121212121 for the tip).

 
#Add your code here!


Subtotal = _c_(370096, _n_(370092, "print", lambda: print), _c_(370095, _n_(370093, "float", lambda: float), _n_(370094, "meal_cost", lambda: meal_cost)))
_l_(370097)
Tax= _c_(370102, _n_(370098, "print", lambda: print), _c_(370101, _n_(370099, "float", lambda: float), _n_(370100, "tax_rate", lambda: tax_rate)*10))
_l_(370103)
Tip = _c_(370108, _n_(370104, "print", lambda: print), _c_(370107, _n_(370105, "float", lambda: float), _n_(370106, "tip_rate", lambda: tip_rate) *100))
_l_(370109)
Total = _c_(370114, _n_(370110, "print", lambda: print), _n_(370111, "Subtotal", lambda: Subtotal) + _n_(370112, "Tax", lambda: Tax) + _n_(370113, "Tip", lambda: Tip))
_l_(370115)