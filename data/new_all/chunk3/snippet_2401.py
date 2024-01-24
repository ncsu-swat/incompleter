# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46237181/type-error-when-using-date-from-a-django-form-i-get-combine-argument-1-must
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
my_date = (_a_(551931, _n_(551930, "form", lambda: form), "cleaned_data")['my_date'])
_l_(551932)
#This comes from a Django form

data2 = {
"CashBookEntryData": {
"Type" : "FinanceVoucher",
"CashBookHandle" : { "Number" : 1 },
"AccountHandle" : { "Number" : 5820 },

"Date" : _n_(551933, "my_date", lambda: my_date),

"VoucherNumber" : 100,
"Text" : "Dagenssalg",
"AmountDefaultCurrency" : 0,
"CurrencyHandle" : { "Code" : "DKK" },
"Amount" : _n_(551934, "beloeb_salg", lambda: beloeb_salg),
"DepartmentHandle" : { "Number" : 1 }
}
}
_l_(551935)