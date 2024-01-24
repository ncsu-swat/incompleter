# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71898053/amazon-web-scraping-attributeerror-nonetype-object-has-no-attribute-text
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
applelist = []
_l_(582042)

apples = _c_(582045, _a_(582044, _n_(582043, "soup", lambda: soup), "find_all"), 'div', {'class': 'sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20'})
_l_(582046)

for item in _n_(582047, "apples", lambda: apples):
    _l_(582065)

    apple = {
        'title': _a_(582051, _c_(582050, _a_(582049, _n_(582048, "item", lambda: item), "find"), 'span', {'class':'a-size-base-plus a-color-base a-text-normal'}), "text"),
        'link': 'https://www.amazon.com' + _c_(582054, _a_(582053, _n_(582052, "item", lambda: item), "find"), 'a', {'class':'a-link-normal s-underline-textjknderline-link-text s-link-style a-text-normal'})['href'],
        'rating': _a_(582058, _c_(582057, _a_(582056, _n_(582055, "item", lambda: item), "find"), 'i', {'class':'a-icon-alt'}), "text"),
        }
    _l_(582059)
    _c_(582063, _a_(582061, _n_(582060, "applelist", lambda: applelist), "append"), _n_(582062, "apple", lambda: apple))
    _l_(582064)

df = _c_(582069, _a_(582067, _n_(582066, "pd", lambda: pd), "DataFrame"), _n_(582068, "applelist", lambda: applelist))
_l_(582070)
_c_(582073, _a_(582072, _n_(582071, "df", lambda: df), "to_csv"), 'file.csv')
_l_(582074)