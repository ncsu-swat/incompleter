# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66932143/django-file-not-found-error-when-the-file-is-there
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(597409, _n_(597406, "receiver", lambda: receiver), _n_(597407, "post_save", lambda: post_save), sender=_n_(597408, "Post", lambda: Post))
def create_uuid(sender, instance, created, **kwargs):
  _l_(597462)

  if _n_(597410, "created", lambda: created):
    _l_(597461)

    img_dir = _a_(597413, _a_(597412, _n_(597411, "instance", lambda: instance), "media"), "url")
    _l_(597414)
    img_dir_list = _c_(597417, _a_(597416, _n_(597415, "img_dir", lambda: img_dir), "split"), "/")
    _l_(597418)
    img_ext = _c_(597421, _a_(597420, _n_(597419, "img_dir_list", lambda: img_dir_list)[-1], "split"), ".")[0]
    _l_(597422)
    im = _c_(597426, _a_(597424, _n_(597423, "Image", lambda: Image), "open"), _n_(597425, "img_dir", lambda: img_dir))
    _l_(597427)
    
    new_width = 0
    _l_(597428)
    for x in _c_(597430, _n_(597429, "range", lambda: range), 0, 3):
      _l_(597456)

      new_width += 200
      _l_(597431)
      new_height = _c_(597438, _n_(597432, "int", lambda: int), _n_(597433, "new_width", lambda: new_width)/_a_(597435, _n_(597434, "image", lambda: image), "width") * _a_(597437, _n_(597436, "image", lambda: image), "height"))
      _l_(597439)
      image = _c_(597444, _a_(597441, _n_(597440, "im", lambda: im), "resize"), (_n_(597442, "new_width", lambda: new_width), _n_(597443, "new_height", lambda: new_height)))
      _l_(597445)
      _c_(597454, _a_(597447, _n_(597446, "image", lambda: image), "save"), f"{_a_(597449, _n_(597448, 'settings', lambda: settings), 'MEDIA_URL')}posts/{_n_(597450, 'img', lambda: img)}{_n_(597451, 'new_width', lambda: new_width)}x{_n_(597452, 'new_height', lambda: new_height)}.{_n_(597453, 'img_ext', lambda: img_ext)}")
      _l_(597455)

    _c_(597459, _a_(597458, _n_(597457, "instance", lambda: instance), "save"))
    _l_(597460)