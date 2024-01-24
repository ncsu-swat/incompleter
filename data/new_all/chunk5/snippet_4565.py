# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55480813/how-to-fix-attributeerror-nonetype-object-has-no-attribute-id-and-self-asse
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.template.loader import render_to_string
    _l_(690019)

except ImportError:
    pass
try:
    from django.urls import resolve, reverse_lazy
    _l_(690021)

except ImportError:
    pass
try:
    from django.test import TestCase
    _l_(690023)

except ImportError:
    pass
try:
    from django.http import HttpRequest
    _l_(690025)

except ImportError:
    pass
try:
    from lists.views import home_page
    _l_(690027)

except ImportError:
    pass
try:
    from lists.models import Item, List
    _l_(690029)

except ImportError:
    pass

class HomePageTest(_n_(690030, "TestCase", lambda: TestCase)):
    _l_(690075)


    def test_uses_home_template(self):
        _l_(690041)

        response = _c_(690034, _a_(690033, _a_(690032, _n_(690031, "self", lambda: self), "client"), "get"), '/')
        _l_(690035)
        _c_(690039, _a_(690037, _n_(690036, "self", lambda: self), "assertTemplateUsed"), _n_(690038, "response", lambda: response), 'home.html')
        _l_(690040)

    def test_displays_all_list_items(self):
        _l_(690060)

        _c_(690045, _a_(690044, _a_(690043, _n_(690042, "Item", lambda: Item), "objects"), "create"), text='itemey 1')
        _l_(690046)
        # Item.objects.create(text='itemey 2')

        response = _c_(690050, _a_(690049, _a_(690048, _n_(690047, "self", lambda: self), "client"), "get"), '/')
        _l_(690051)

        _c_(690058, _a_(690053, _n_(690052, "self", lambda: self), "assertIn"), 'item', _c_(690057, _a_(690056, _a_(690055, _n_(690054, "response", lambda: response), "content"), "decode")))
        _l_(690059)

    def test_only_saves_items_when_necessary(self):
        _l_(690074)

        _c_(690064, _a_(690063, _a_(690062, _n_(690061, "self", lambda: self), "client"), "get"), '/')
        _l_(690065)
        _c_(690072, _a_(690067, _n_(690066, "self", lambda: self), "assertEqual"), _c_(690071, _a_(690070, _a_(690069, _n_(690068, "Item", lambda: Item), "objects"), "count")), 0)
        _l_(690073)


class ListViewTest(_n_(690076, "TestCase", lambda: TestCase)):
    _l_(690139)


    def test_uses_list_template(self):
        _l_(690094)

        list_ = _c_(690080, _a_(690079, _a_(690078, _n_(690077, "List", lambda: List), "objects"), "create"))
        _l_(690081)
        response = _c_(690087, _a_(690084, _a_(690083, _n_(690082, "self", lambda: self), "client"), "get"), f'/lists/{_a_(690086, _n_(690085, "list_", lambda: list_), "id")}/')
        _l_(690088)
        _c_(690092, _a_(690090, _n_(690089, 'self', lambda: self), 'assertTemplateUsed'), _n_(690091, 'response', lambda: response), 'list.html')
        _l_(690093)

    def test_displays_only_items_for_that_list(self):
        _l_(690118)

        correct_list = _c_(690098, _a_(690097, _a_(690096, _n_(690095, 'List', lambda: List), 'objects'), 'create'))
        _l_(690099)
        _c_(690104, _a_(690102, _a_(690101, _n_(690100, 'Item', lambda: Item), 'objects'), 'create'), text='item', list=_n_(690103, 'correct_list', lambda: correct_list))
        _l_(690105)
        # Item.objects.create(text='itemey 2', list=correct_list)

        response = _c_(690111, _a_(690108, _a_(690107, _n_(690106, 'self', lambda: self), 'client'), 'get'), f'/lists/{_a_(690110, _n_(690109, "correct_list", lambda: correct_list), "id")}/')
        _l_(690112)

        _c_(690116, _a_(690114, _n_(690113, 'self', lambda: self), 'assertContains'), _n_(690115, 'response', lambda: response), 'item')
        _l_(690117)


    def test_passes_correct_list_to_template(self):
        _l_(690138)

        correct_list = _c_(690122, _a_(690121, _a_(690120, _n_(690119, 'List', lambda: List), 'objects'), 'create'))
        _l_(690123)
        response = _c_(690129, _a_(690126, _a_(690125, _n_(690124, 'self', lambda: self), 'client'), 'get'), f'/lists/{_a_(690128, _n_(690127, "correct_list", lambda: correct_list), "id")}/')
        _l_(690130)
        _c_(690136, _a_(690132, _n_(690131, 'self', lambda: self), 'assertEqual'), _a_(690134, _n_(690133, 'response', lambda: response), 'context')['list'], _n_(690135, 'correct_list', lambda: correct_list))
        _l_(690137)


class ListAndItemModelsTest(_n_(690140, 'TestCase', lambda: TestCase)):
    _l_(690226)


    def test_saving_and_retrieving_items(self):
        _l_(690225)

        list_ = _c_(690142, _n_(690141, 'List', lambda: List))
        _l_(690143)
        _c_(690146, _a_(690145, _n_(690144, 'list_', lambda: list_), 'save'))
        _l_(690147)

        first_item = _c_(690149, _n_(690148, 'Item', lambda: Item))
        _l_(690150)
        _n_(690151, 'first_item', lambda: first_item).text = 'The first (ever) list item'
        _l_(690152)
        _n_(690153, 'first_item', lambda: first_item).list = _n_(690154, 'list_', lambda: list_)
        _l_(690155)
        _c_(690158, _a_(690157, _n_(690156, 'first_item', lambda: first_item), 'save'))
        _l_(690159)

        second_item = _c_(690161, _n_(690160, 'Item', lambda: Item))
        _l_(690162)
        _n_(690163, 'second_item', lambda: second_item).text = 'Item the second'
        _l_(690164)
        _n_(690165, 'second_item', lambda: second_item).list = _n_(690166, 'list_', lambda: list_)
        _l_(690167)
        _c_(690170, _a_(690169, _n_(690168, 'second_item', lambda: second_item), 'save'))
        _l_(690171)

        saved_list = _c_(690175, _a_(690174, _a_(690173, _n_(690172, 'List', lambda: List), 'objects'), 'first'))
        _l_(690176)
        _c_(690181, _a_(690178, _n_(690177, 'self', lambda: self), 'assertEqual'), _n_(690179, 'saved_list', lambda: saved_list), _n_(690180, 'list_', lambda: list_))
        _l_(690182)

        saved_items = _c_(690186, _a_(690185, _a_(690184, _n_(690183, 'Item', lambda: Item), 'objects'), 'all'))
        _l_(690187)
        _c_(690193, _a_(690189, _n_(690188, 'self', lambda: self), 'assertEqual'), _c_(690192, _a_(690191, _n_(690190, 'saved_items', lambda: saved_items), 'count')), 2)
        _l_(690194)

        first_saved_item = _n_(690195, 'saved_items', lambda: saved_items)[0]
        _l_(690196)
        second_saved_item = _n_(690197, 'saved_items', lambda: saved_items)[1]
        _l_(690198)
        _c_(690203, _a_(690200, _n_(690199, 'self', lambda: self), 'assertEqual'), _a_(690202, _n_(690201, 'first_saved_item', lambda: first_saved_item), 'text'), 'The first (ever) list item')
        _l_(690204)
        _c_(690210, _a_(690206, _n_(690205, 'self', lambda: self), 'assertEqual'), _a_(690208, _n_(690207, 'first_saved_item', lambda: first_saved_item), 'list'), _n_(690209, 'list_', lambda: list_))
        _l_(690211)
        _c_(690216, _a_(690213, _n_(690212, 'self', lambda: self), 'assertEqual'), _a_(690215, _n_(690214, 'second_saved_item', lambda: second_saved_item), 'text'), 'Item the second')
        _l_(690217)
        _c_(690223, _a_(690219, _n_(690218, 'self', lambda: self), 'assertEqual'), _a_(690221, _n_(690220, 'second_saved_item', lambda: second_saved_item), 'list'), _n_(690222, 'list_', lambda: list_))
        _l_(690224)

class NewListTest(_n_(690227, 'TestCase', lambda: TestCase)):
    _l_(690271)


    def test_can_save_a_POST_request(self):
        _l_(690252)

        _c_(690231, _a_(690230, _a_(690229, _n_(690228, 'self', lambda: self), 'client'), 'post'), 'lists/new', {'item_text': 'A new list item'})
        _l_(690232)
        new_item = _c_(690236, _a_(690235, _a_(690234, _n_(690233, 'Item', lambda: Item), 'objects'), 'first'))
        _l_(690237)
        _c_(690244, _a_(690239, _n_(690238, 'self', lambda: self), 'assertEqual'), _c_(690243, _a_(690242, _a_(690241, _n_(690240, 'Item', lambda: Item), 'objects'), 'count')), 1)
        _l_(690245)
        _c_(690250, _a_(690247, _n_(690246, 'self', lambda: self), 'assertEqual'), _a_(690249, _n_(690248, 'new_item', lambda: new_item), 'text'), 'A new list item')
        _l_(690251)

    def test_redirects_after_POST(self):
        _l_(690270)

        response = _c_(690256, _a_(690255, _a_(690254, _n_(690253, 'self', lambda: self), 'client'), 'post'), '/lists/new', data={'item_text': 'A new list item'})
        _l_(690257)
        new_list = _c_(690261, _a_(690260, _a_(690259, _n_(690258, 'List', lambda: List), 'objects'), 'first'))
        _l_(690262)
        _c_(690268, _a_(690264, _n_(690263, 'self', lambda: self), 'assertRedirects'), _n_(690265, 'response', lambda: response), f'/lists/{_a_(690267, _n_(690266, "new_list", lambda: new_list), "id")}/')
        _l_(690269)

class NewItemTest(_n_(690272, 'TestCase', lambda: TestCase)):
    _l_(690332)


    def test_can_save_a_POST_request_to_an_existing_list(self):
        _l_(690311)

        correct_list = _c_(690276, _a_(690275, _a_(690274, _n_(690273, 'List', lambda: List), 'objects'), 'create'))
        _l_(690277)

        _c_(690283, _a_(690280, _a_(690279, _n_(690278, 'self', lambda: self), 'client'), 'post'), f'/lists/{_a_(690282, _n_(690281, "correct_list", lambda: correct_list), "id")}/add_item',
            data={'item_text': 'A new item for an existing list'}
        )
        _l_(690284)

        _c_(690291, _a_(690286, _n_(690285, 'self', lambda: self), 'assertEqual'), _c_(690290, _a_(690289, _a_(690288, _n_(690287, 'Item', lambda: Item), 'objects'), 'count')), 1)
        _l_(690292)
        new_item = _c_(690296, _a_(690295, _a_(690294, _n_(690293, 'Item', lambda: Item), 'objects'), 'first'))
        _l_(690297)
        _c_(690302, _a_(690299, _n_(690298, 'self', lambda: self), 'assertEqual'), _a_(690301, _n_(690300, 'new_item', lambda: new_item), 'text'), 'A new item for an existing list')
        _l_(690303)
        _c_(690309, _a_(690305, _n_(690304, 'self', lambda: self), 'assertEqual'), _a_(690307, _n_(690306, 'new_item', lambda: new_item), 'list'), _n_(690308, 'correct_list', lambda: correct_list))
        _l_(690310)

    def test_redirects_to_list_view(self):
        _l_(690331)

        correct_list = _c_(690315, _a_(690314, _a_(690313, _n_(690312, 'List', lambda: List), 'objects'), 'create'))
        _l_(690316)
        response = _c_(690322, _a_(690319, _a_(690318, _n_(690317, 'self', lambda: self), 'client'), 'post'), f'/lists/{_a_(690321, _n_(690320, "correct_list", lambda: correct_list), "id")}/add_item',
            data={'item_text': 'A new item for an existing list'}
        )
        _l_(690323)

        _c_(690329, _a_(690325, _n_(690324, 'self', lambda: self), 'assertRedirects'), _n_(690326, 'response', lambda: response), f'/lists/{_a_(690328, _n_(690327, "correct_list", lambda: correct_list), "id")}/')
        _l_(690330)