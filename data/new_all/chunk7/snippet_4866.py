# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44511613/python-file-read-questions-filenotfounderror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
file_path ='D:\summer2017\4\pi2.txt'
_l_(670804)
with _c_(670806, _n_(670805, "open", lambda: open), 'pi2.txt')as file_object:
    _l_(670817)

    content1=_c_(670809, _a_(670808, _n_(670807, "file_object", lambda: file_object), "read"))
    _l_(670810)
    _c_(670815, _n_(670811, "print", lambda: print), _c_(670814, _a_(670813, _n_(670812, "content1", lambda: content1), "rstrip")))
    _l_(670816)
#it works and print 3.14****
#D:\summer2017 is this project folder


file_path =r'F:\test\123.txt'
_l_(670818)
with _c_(670820, _n_(670819, "open", lambda: open), '123.txt')as file_object:
    _l_(670831)

    content1=_c_(670823, _a_(670822, _n_(670821, "file_object", lambda: file_object), "read"))
    _l_(670824)
    _c_(670829, _n_(670825, "print", lambda: print), _c_(670828, _a_(670827, _n_(670826, "content1", lambda: content1), "rstrip")))
    _l_(670830)
#FileNotFoundError: [Errno 2] No such file or directory: '123.txt'
# i create a 123.txt in F:\test
# but it can not read

file_path =r'F:\test\pi2.txt'
_l_(670832)
with _c_(670834, _n_(670833, "open", lambda: open), 'pi2.txt')as file_object:
    _l_(670845)

    content1=_c_(670837, _a_(670836, _n_(670835, "file_object", lambda: file_object), "read"))
    _l_(670838)
    _c_(670843, _n_(670839, "print", lambda: print), _c_(670842, _a_(670841, _n_(670840, "content1", lambda: content1), "rstrip")))
    _l_(670844)
# i create another pi2.txt in F:\test
# now it can be found
# in this txt there are some random alphabet and nums but not 3.14****
# but it also print the pi num