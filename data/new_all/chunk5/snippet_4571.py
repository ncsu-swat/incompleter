# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55480813/how-to-fix-attributeerror-nonetype-object-has-no-attribute-id-and-self-asse
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.template.loader import render_to_string
    _l_(695257)

except ImportError:
    pass
try:
    from django.urls import resolve, reverse_lazy
    _l_(695259)

except ImportError:
    pass
try:
    from django.test import TestCase
    _l_(695261)

except ImportError:
    pass
try:
    from django.http import HttpRequest
    _l_(695263)

except ImportError:
    pass
try:
    from lists.views import home_page
    _l_(695265)

except ImportError:
    pass
try:
    from lists.models import Item, List
    _l_(695267)

except ImportError:
    pass

class HomePageTest(_n_(695268, "TestCase", lambda: TestCase)):
    _l_(695313)


    def test_uses_home_template(self):
        _l_(695279)

        response = _c_(695272, _a_(695271, _a_(695270, _n_(695269, "self", lambda: self), "client"), "get"), '/')
        _l_(695273)
        _c_(695277, _a_(695275, _n_(695274, "self", lambda: self), "assertTemplateUsed"), _n_(695276, "response", lambda: response), 'home.html')
        _l_(695278)

    def test_displays_all_list_items(self):
        _l_(695298)

        _c_(695283, _a_(695282, _a_(695281, _n_(695280, "Item", lambda: Item), "objects"), "create"), text='itemey 1')
        _l_(695284)
        # Item.objects.create(text='itemey 2')

        response = _c_(695288, _a_(695287, _a_(695286, _n_(695285, "self", lambda: self), "client"), "get"), '/')
        _l_(695289)

        _c_(695296, _a_(695291, _n_(695290, "self", lambda: self), "assertIn"), 'item', _c_(695295, _a_(695294, _a_(695293, _n_(695292, "response", lambda: response), "content"), "decode")))
        _l_(695297)

    def test_only_saves_items_when_necessary(self):
        _l_(695312)

        _c_(695302, _a_(695301, _a_(695300, _n_(695299, "self", lambda: self), "client"), "get"), '/')
        _l_(695303)
        _c_(695310, _a_(695305, _n_(695304, "self", lambda: self), "assertEqual"), _c_(695309, _a_(695308, _a_(695307, _n_(695306, "Item", lambda: Item), "objects"), "count")), 0)
        _l_(695311)


class ListViewTest(_n_(695314, "TestCase", lambda: TestCase)):
    _l_(695377)


    def test_uses_list_template(self):
        _l_(695332)

        list_ = _c_(695318, _a_(695317, _a_(695316, _n_(695315, "List", lambda: List), "objects"), "create"))
        _l_(695319)
        response = _c_(695325, _a_(695322, _a_(695321, _n_(695320, "self", lambda: self), "client"), "get"), f'/lists/{_a_(695324, _n_(695323, "list_", lambda: list_), "id")}/')
        _l_(695326)
        _c_(695330, _a_(695328, _n_(695327, 'self', lambda: self), 'assertTemplateUsed'), _n_(695329, 'response', lambda: response), 'list.html')
        _l_(695331)

    def test_displays_only_items_for_that_list(self):
        _l_(695356)

        correct_list = _c_(695336, _a_(695335, _a_(695334, _n_(695333, 'List', lambda: List), 'objects'), 'create'))
        _l_(695337)
        _c_(695342, _a_(695340, _a_(695339, _n_(695338, 'Item', lambda: Item), 'objects'), 'create'), text='item', list=_n_(695341, 'correct_list', lambda: correct_list))
        _l_(695343)
        # Item.objects.create(text='itemey 2', list=correct_list)

        response = _c_(695349, _a_(695346, _a_(695345, _n_(695344, 'self', lambda: self), 'client'), 'get'), f'/lists/{_a_(695348, _n_(695347, "correct_list", lambda: correct_list), "id")}/')
        _l_(695350)

        _c_(695354, _a_(695352, _n_(695351, 'self', lambda: self), 'assertContains'), _n_(695353, 'response', lambda: response), 'item')
        _l_(695355)


    def test_passes_correct_list_to_template(self):
        _l_(695376)

        correct_list = _c_(695360, _a_(695359, _a_(695358, _n_(695357, 'List', lambda: List), 'objects'), 'create'))
        _l_(695361)
        response = _c_(695367, _a_(695364, _a_(695363, _n_(695362, 'self', lambda: self), 'client'), 'get'), f'/lists/{_a_(695366, _n_(695365, "correct_list", lambda: correct_list), "id")}/')
        _l_(695368)
        _c_(695374, _a_(695370, _n_(695369, 'self', lambda: self), 'assertEqual'), _a_(695372, _n_(695371, 'response', lambda: response), 'context')['list'], _n_(695373, 'correct_list', lambda: correct_list))
        _l_(695375)


class ListAndItemModelsTest(_n_(695378, 'TestCase', lambda: TestCase)):
    _l_(695464)


    def test_saving_and_retrieving_items(self):
        _l_(695463)

        list_ = _c_(695380, _n_(695379, 'List', lambda: List))
        _l_(695381)
        _c_(695384, _a_(695383, _n_(695382, 'list_', lambda: list_), 'save'))
        _l_(695385)

        first_item = _c_(695387, _n_(695386, 'Item', lambda: Item))
        _l_(695388)
        _n_(695389, 'first_item', lambda: first_item).text = 'The first (ever) list item'
        _l_(695390)
        _n_(695391, 'first_item', lambda: first_item).list = _n_(695392, 'list_', lambda: list_)
        _l_(695393)
        _c_(695396, _a_(695395, _n_(695394, 'first_item', lambda: first_item), 'save'))
        _l_(695397)

        second_item = _c_(695399, _n_(695398, 'Item', lambda: Item))
        _l_(695400)
        _n_(695401, 'second_item', lambda: second_item).text = 'Item the second'
        _l_(695402)
        _n_(695403, 'second_item', lambda: second_item).list = _n_(695404, 'list_', lambda: list_)
        _l_(695405)
        _c_(695408, _a_(695407, _n_(695406, 'second_item', lambda: second_item), 'save'))
        _l_(695409)

        saved_list = _c_(695413, _a_(695412, _a_(695411, _n_(695410, 'List', lambda: List), 'objects'), 'first'))
        _l_(695414)
        _c_(695419, _a_(695416, _n_(695415, 'self', lambda: self), 'assertEqual'), _n_(695417, 'saved_list', lambda: saved_list), _n_(695418, 'list_', lambda: list_))
        _l_(695420)

        saved_items = _c_(695424, _a_(695423, _a_(695422, _n_(695421, 'Item', lambda: Item), 'objects'), 'all'))
        _l_(695425)
        _c_(695431, _a_(695427, _n_(695426, 'self', lambda: self), 'assertEqual'), _c_(695430, _a_(695429, _n_(695428, 'saved_items', lambda: saved_items), 'count')), 2)
        _l_(695432)

        first_saved_item = _n_(695433, 'saved_items', lambda: saved_items)[0]
        _l_(695434)
        second_saved_item = _n_(695435, 'saved_items', lambda: saved_items)[1]
        _l_(695436)
        _c_(695441, _a_(695438, _n_(695437, 'self', lambda: self), 'assertEqual'), _a_(695440, _n_(695439, 'first_saved_item', lambda: first_saved_item), 'text'), 'The first (ever) list item')
        _l_(695442)
        _c_(695448, _a_(695444, _n_(695443, 'self', lambda: self), 'assertEqual'), _a_(695446, _n_(695445, 'first_saved_item', lambda: first_saved_item), 'list'), _n_(695447, 'list_', lambda: list_))
        _l_(695449)
        _c_(695454, _a_(695451, _n_(695450, 'self', lambda: self), 'assertEqual'), _a_(695453, _n_(695452, 'second_saved_item', lambda: second_saved_item), 'text'), 'Item the second')
        _l_(695455)
        _c_(695461, _a_(695457, _n_(695456, 'self', lambda: self), 'assertEqual'), _a_(695459, _n_(695458, 'second_saved_item', lambda: second_saved_item), 'list'), _n_(695460, 'list_', lambda: list_))
        _l_(695462)

class NewListTest(_n_(695465, 'TestCase', lambda: TestCase)):
    _l_(695509)


    def test_can_save_a_POST_request(self):
        _l_(695490)

        _c_(695469, _a_(695468, _a_(695467, _n_(695466, 'self', lambda: self), 'client'), 'post'), 'lists/new', {'item_text': 'A new list item'})
        _l_(695470)
        new_item = _c_(695474, _a_(695473, _a_(695472, _n_(695471, 'Item', lambda: Item), 'objects'), 'first'))
        _l_(695475)
        _c_(695482, _a_(695477, _n_(695476, 'self', lambda: self), 'assertEqual'), _c_(695481, _a_(695480, _a_(695479, _n_(695478, 'Item', lambda: Item), 'objects'), 'count')), 1)
        _l_(695483)
        _c_(695488, _a_(695485, _n_(695484, 'self', lambda: self), 'assertEqual'), _a_(695487, _n_(695486, 'new_item', lambda: new_item), 'text'), 'A new list item')
        _l_(695489)

    def test_redirects_after_POST(self):
        _l_(695508)

        response = _c_(695494, _a_(695493, _a_(695492, _n_(695491, 'self', lambda: self), 'client'), 'post'), '/lists/new', data={'item_text': 'A new list item'})
        _l_(695495)
        new_list = _c_(695499, _a_(695498, _a_(695497, _n_(695496, 'List', lambda: List), 'objects'), 'first'))
        _l_(695500)
        _c_(695506, _a_(695502, _n_(695501, 'self', lambda: self), 'assertRedirects'), _n_(695503, 'response', lambda: response), f'/lists/{_a_(695505, _n_(695504, "new_list", lambda: new_list), "id")}/')
        _l_(695507)

class NewItemTest(_n_(695510, 'TestCase', lambda: TestCase)):
    _l_(695570)


    def test_can_save_a_POST_request_to_an_existing_list(self):
        _l_(695549)

        correct_list = _c_(695514, _a_(695513, _a_(695512, _n_(695511, 'List', lambda: List), 'objects'), 'create'))
        _l_(695515)

        _c_(695521, _a_(695518, _a_(695517, _n_(695516, 'self', lambda: self), 'client'), 'post'), f'/lists/{_a_(695520, _n_(695519, "correct_list", lambda: correct_list), "id")}/add_item',
            data={'item_text': 'A new item for an existing list'}
        )
        _l_(695522)

        _c_(695529, _a_(695524, _n_(695523, 'self', lambda: self), 'assertEqual'), _c_(695528, _a_(695527, _a_(695526, _n_(695525, 'Item', lambda: Item), 'objects'), 'count')), 1)
        _l_(695530)
        new_item = _c_(695534, _a_(695533, _a_(695532, _n_(695531, 'Item', lambda: Item), 'objects'), 'first'))
        _l_(695535)
        _c_(695540, _a_(695537, _n_(695536, 'self', lambda: self), 'assertEqual'), _a_(695539, _n_(695538, 'new_item', lambda: new_item), 'text'), 'A new item for an existing list')
        _l_(695541)
        _c_(695547, _a_(695543, _n_(695542, 'self', lambda: self), 'assertEqual'), _a_(695545, _n_(695544, 'new_item', lambda: new_item), 'list'), _n_(695546, 'correct_list', lambda: correct_list))
        _l_(695548)

    def test_redirects_to_list_view(self):
        _l_(695569)

        correct_list = _c_(695553, _a_(695552, _a_(695551, _n_(695550, 'List', lambda: List), 'objects'), 'create'))
        _l_(695554)
        response = _c_(695560, _a_(695557, _a_(695556, _n_(695555, 'self', lambda: self), 'client'), 'post'), f'/lists/{_a_(695559, _n_(695558, "correct_list", lambda: correct_list), "id")}/add_item',
            data={'item_text': 'A new item for an existing list'}
        )
        _l_(695561)

        _c_(695567, _a_(695563, _n_(695562, 'self', lambda: self), 'assertRedirects'), _n_(695564, 'response', lambda: response), f'/lists/{_a_(695566, _n_(695565, "correct_list", lambda: correct_list), "id")}/')
        _l_(695568)