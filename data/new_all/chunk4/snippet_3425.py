# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74600131/pytesseract-pytesseract-has-no-attribute-pytesseract-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from passporteye import read_mrz
    _l_(634238)

except ImportError:
    pass
try:
    from pytesseract import pytesseract
    _l_(634240)

except ImportError:
    pass

_a_(634242, _n_(634241, "pytesseract", lambda: pytesseract), "pytesseract").tesseract_cmd = r'C:\\Users\\*<username>*\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'
_l_(634243)

# Process image
mrz = _c_(634245, _n_(634244, "read_mrz", lambda: read_mrz), "C:\\Users\\*<username>*\\Documents\\UiPath\\imageExtract\\Data\\image1.jpeg")
_l_(634246)


# Obtain image
mrz_data = _c_(634249, _a_(634248, _n_(634247, "mrz", lambda: mrz), "to_dict"))
_l_(634250)

# Printing extracted data
_c_(634253, _n_(634251, "print", lambda: print), 'Nationality :'+ _n_(634252, "mrz_data", lambda: mrz_data)['nationality'])
_l_(634254)
_c_(634257, _n_(634255, "print", lambda: print), 'Given Name :'+ _n_(634256, "mrz_data", lambda: mrz_data)['names'])
_l_(634258)
_c_(634261, _n_(634259, "print", lambda: print), 'Surname :'+ _n_(634260, "mrz_data", lambda: mrz_data)['surname'])
_l_(634262)
_c_(634265, _n_(634263, "print", lambda: print), 'Passport type :'+ _n_(634264, "mrz_data", lambda: mrz_data)['type'])
_l_(634266)
_c_(634269, _n_(634267, "print", lambda: print), 'Date of birth :'+ _n_(634268, "mrz_data", lambda: mrz_data)['date_of_birth'])
_l_(634270)
_c_(634273, _n_(634271, "print", lambda: print), 'ID Number :'+ _n_(634272, "mrz_data", lambda: mrz_data)['personal_number'])
_l_(634274)
_c_(634277, _n_(634275, "print", lambda: print), 'Gender :'+_n_(634276, "mrz_data", lambda: mrz_data)['sex'])
_l_(634278)
_c_(634281, _n_(634279, "print", lambda: print), 'Expiration date :'+ _n_(634280, "mrz_data", lambda: mrz_data)['expiration_date'])
_l_(634282)