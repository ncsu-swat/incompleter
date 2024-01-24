# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/7050894/nameerror-name-self-is-not-defined-when-passing-attribute-as-parameter-to-met
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pyPdf import PdfFileWriter, PdfFileReader
    _l_(420867)

except ImportError:
    pass
try:
    import re
    _l_(420869)

except ImportError:
    pass
try:
    import time
    _l_(420871)

except ImportError:
    pass

class PdfGet():
    _l_(421005)

    def __init__(self):
        _l_(420876)

        _c_(420874, _a_(420873, _n_(420872, "self", lambda: self), "initialize"))
        _l_(420875)

    def initialize(self):
        _l_(420942)

        while True:
            _l_(420941)

            raw_args = _c_(420880, _a_(420879, _c_(420878, _n_(420877, "input", lambda: input), 'Welcome to PdfGet...\n***Please Enter Arugments (infile,outfile,start_page,end_page) OR type "quit" to exit***\n'), "strip")) 
            _l_(420881) 
            if _c_(420884, _a_(420883, _n_(420882, "raw_args", lambda: raw_args), "lower")) == 'quit':
                _l_(420886)

                break
                _l_(420885)
            _c_(420888, _n_(420887, "print", lambda: print), "Converting Pdf...")
            _l_(420889)
            _n_(420890, "self", lambda: self).args = _c_(420894, _a_(420892, _n_(420891, "re", lambda: re), "split"), r',| ',_n_(420893, "raw_args", lambda: raw_args))
            _l_(420895)
            _c_(420900, _a_(420897, _n_(420896, "self", lambda: self), "opener"), *_a_(420899, _n_(420898, "self", lambda: self), "args")[0:1])
            _l_(420901)
            if _c_(420905, _n_(420902, "len", lambda: len), _a_(420904, _n_(420903, "self", lambda: self), "args"))== 4:
                _l_(420929)

                _c_(420910, _a_(420907, _n_(420906, "self", lambda: self), "pageoutput"), *_a_(420909, _n_(420908, "self", lambda: self), "args")[1:])
                _l_(420911)
            elif _c_(420915, _n_(420912, "len", lambda: len), _a_(420914, _n_(420913, "self", lambda: self), "args")) == 3:
                _l_(420928)

                _c_(420920, _a_(420917, _n_(420916, "self", lambda: self), "pageoutput"), *_a_(420919, _n_(420918, "self", lambda: self), "args")[1:3])
                _l_(420921)
            else:
                _c_(420926, _a_(420923, _n_(420922, "self", lambda: self), "pageoutput"), *_a_(420925, _n_(420924, "self", lambda: self), "args")[1:2])
                _l_(420927)
            _c_(420931, _n_(420930, "print", lambda: print), "Successfuly Converted!")
            _l_(420932)
            nextiter = _c_(420936, _a_(420935, _c_(420934, _n_(420933, "input", lambda: input), 'Convert Another PDF? (Type "yes" or "no")'), "lower"))
            _l_(420937)
            if _n_(420938, "nextiter", lambda: nextiter) == 'no':
                _l_(420940)

                break
                _l_(420939)

    def opener(self,infile):
        _l_(420969)

        _n_(420943, "self", lambda: self).output = _c_(420945, _n_(420944, "PdfFileWriter", lambda: PdfFileWriter))
        _l_(420946)
        _n_(420947, "self", lambda: self).pdf = _c_(420952, _n_(420948, "PdfFileReader", lambda: PdfFileReader), _c_(420951, _n_(420949, "open", lambda: open), _n_(420950, "infile", lambda: infile), "rb"))
        _l_(420953)
        _n_(420954, "self", lambda: self).pagenum = _c_(420958, _a_(420957, _a_(420956, _n_(420955, "self", lambda: self), "pdf"), "getNumPages"))
        _l_(420959)
        _n_(420960, "self", lambda: self).lastpage = _a_(420962, _n_(420961, "self", lambda: self), "pagenum")+1
        _l_(420963)
        _c_(420967, _n_(420964, "print", lambda: print), _a_(420966, _n_(420965, "self", lambda: self), "lastpage"))
        _l_(420968)

    def pageoutput(self,outfile,start_page=0,end_page=_a_(420970, self, "lastpage")):
        _l_(421004)

        for i in _c_(420978, _n_(420971, "range", lambda: range), _c_(420974, _n_(420972, "int", lambda: int), _n_(420973, "start_page", lambda: start_page))-1,_c_(420977, _n_(420975, "int", lambda: int), _n_(420976, "end_page", lambda: end_page))):
            _l_(420989)

            _c_(420987, _a_(420981, _a_(420980, _n_(420979, "self", lambda: self), "output"), "addPage"), _c_(420986, _a_(420984, _a_(420983, _n_(420982, "self", lambda: self), "pdf"), "getPage"), _n_(420985, "i", lambda: i)))    
            _l_(420988)    
        outputStream = _c_(420992, _n_(420990, "open", lambda: open), _n_(420991, "outfile", lambda: outfile), "wb")
        _l_(420993)
        _c_(420998, _a_(420996, _a_(420995, _n_(420994, "self", lambda: self), "output"), "write"), _n_(420997, "outputStream", lambda: outputStream))
        _l_(420999)
        _c_(421002, _a_(421001, _n_(421000, "outputStream", lambda: outputStream), "close"))
        _l_(421003)

if _n_(421006, "__name__", lambda: __name__) == "__main__":
    _l_(421014)

    _c_(421008, _n_(421007, "PdfGet", lambda: PdfGet))
    _l_(421009)
    _c_(421012, _a_(421011, _n_(421010, "time", lambda: time), "sleep"), 5)
    _l_(421013)