# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48887526/streamfield-typeerror-bool-object-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class CardBlock(_n_(621581, "StructBlock", lambda: StructBlock)):
    _l_(621590)

    image = _c_(621582, ImageChooserBlock)
    _l_(621583)
    heading = _c_(621584, CharBlock, classname="full title")
    _l_(621585)
    caption = _c_(621586, RichTextBlock)
    _l_(621587)
    class Meta:
        _l_(621589)

        icon = 'image'
        _l_(621588)

class HomePage(_n_(621591, "Page", lambda: Page)):
    _l_(621606)

    intro = _c_(621592, RichTextField, blank=True)
    _l_(621593)
    showcase_title = _c_(621594, RichTextField, blank=True)
    _l_(621595)
    card = _c_(621598, StreamField, [('card', _c_(621597, _n_(621596, "CardBlock", lambda: CardBlock)))], default=True)
    _l_(621599)

    content_panels = _a_(621600, Page, "content_panels") + [
        _c_(621601, FieldPanel, 'intro', classname="full"),
        _c_(621604, MultiFieldPanel, [
            _c_(621602, FieldPanel, 'showcase_title'),
            _c_(621603, StreamFieldPanel, 'card'),
        ]),
    ]
    _l_(621605)