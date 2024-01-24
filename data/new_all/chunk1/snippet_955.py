# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67089815/flask-image-cant-upload-filenotfounderror-errno-2-no-such-file-or-directory
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(390808, _a_(390807, _n_(390806, "app", lambda: app), "route"), '/upload',methods=['POST'])
def upload():
    _l_(390858)

    title = _a_(390810, _n_(390809, "request", lambda: request), "form")['title']
    _l_(390811)
    context = _a_(390813, _n_(390812, "request", lambda: request), "form")['text']
    _l_(390814)
    author = _a_(390816, _n_(390815, "request", lambda: request), "form")['author']
    _l_(390817)
    img=_a_(390819, _n_(390818, "request", lambda: request), "files")['img']
    _l_(390820)
    path = _c_(390828, _a_(390823, _a_(390822, _n_(390821, "os", lambda: os), "path"), "join"), _a_(390825, _n_(390824, "app", lambda: app), "root_path"),'/images',_a_(390827, _n_(390826, "img", lambda: img), "filename"))
    _l_(390829)
    _c_(390833, _a_(390831, _n_(390830, "img", lambda: img), "save"), _n_(390832, "path", lambda: path))
    _l_(390834)

    new=_c_(390840, _n_(390835, "Posts", lambda: Posts), title=_n_(390836, "title", lambda: title),context=_n_(390837, "context", lambda: context),image=_n_(390838, "path", lambda: path),author=_n_(390839, "author", lambda: author))
    _l_(390841)
    _c_(390846, _a_(390844, _a_(390843, _n_(390842, "db", lambda: db), "session"), "add"), _n_(390845, "new", lambda: new))
    _l_(390847)
    _c_(390851, _a_(390850, _a_(390849, _n_(390848, "db", lambda: db), "session"), "commit"))
    _l_(390852)
    aux = _c_(390856, _n_(390853, "redirect", lambda: redirect), _c_(390855, _n_(390854, "url_for", lambda: url_for), 'blog'))
    _l_(390857)

    return aux