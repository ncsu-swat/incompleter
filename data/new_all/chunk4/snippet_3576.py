# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72029962/typeerror-rename-src-should-be-string-bytes-or-os-pathlike-not-io-bufferedr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for files in _c_(596148, _a_(596146, _n_(596145, "glob", lambda: glob), "glob"), _n_(596147, "path", lambda: path)+"/*.pdf"):
    _l_(596225)

    with _c_(596151, _n_(596149, "open", lambda: open), _n_(596150, "files", lambda: files), 'rb') as pdf_file:
        _l_(596224)

    
        read_pdf = _c_(596155, _a_(596153, _n_(596152, "PyPDF2", lambda: PyPDF2), "PdfFileReader"), _n_(596154, "pdf_file", lambda: pdf_file))
        _l_(596156)
        page = _c_(596159, _a_(596158, _n_(596157, "read_pdf", lambda: read_pdf), "getPage"), 0-1)
        _l_(596160)
        text = _c_(596163, _a_(596162, _n_(596161, "page", lambda: page), "extractText"))
        _l_(596164)
        text = _c_(596169, _a_(596165, " ", "join"), _c_(596168, _a_(596167, _n_(596166, "text", lambda: text), "split")))
        _l_(596170)

        start = ['from']
        _l_(596171)
        end = ['to']
        _l_(596172)
        text = _c_(596177, _n_(596173, "get_keyword", lambda: get_keyword), _n_(596174, "start", lambda: start), _n_(596175, "end", lambda: end), _n_(596176, "text", lambda: text))
        _l_(596178)
        DateList = [_n_(596179, "text", lambda: text)]
        _l_(596180)
        _c_(596183, _n_(596181, "print", lambda: print), _n_(596182, "text", lambda: text))
        _l_(596184)
        #pdf_file.close()
        
        _c_(596191, _a_(596186, _n_(596185, "os", lambda: os), "rename"), _n_(596187, "pdf_file", lambda: pdf_file),_c_(596190, _n_(596188, "str", lambda: str), _n_(596189, "i", lambda: i))+".pdf")
        _l_(596192)
    
        _c_(596201, _a_(596194, _n_(596193, "tabula", lambda: tabula), "convert_into"), _c_(596197, _n_(596195, "str", lambda: str), _n_(596196, "i", lambda: i))+".pdf", _c_(596200, _n_(596198, "str", lambda: str), _n_(596199, "i", lambda: i))+".csv", output_format="csv", pages='all')
        _l_(596202)
        
        _c_(596206, _a_(596204, _n_(596203, "xlist", lambda: xlist), "append"), _n_(596205, "DateList", lambda: DateList))
        _l_(596207)
        _c_(596216, _a_(596209, _n_(596208, "xlist", lambda: xlist), "append"), _c_(596215, _a_(596211, _n_(596210, "pd", lambda: pd), "read_csv"), _c_(596214, _n_(596212, "str", lambda: str), _n_(596213, "i", lambda: i))))
        _l_(596217)
        xmerged = _c_(596220, _a_(596219, _n_(596218, "pd", lambda: pd), "DataFrame"))
        _l_(596221)
        i=_n_(596222, "i", lambda: i)+1        
        _l_(596223)        