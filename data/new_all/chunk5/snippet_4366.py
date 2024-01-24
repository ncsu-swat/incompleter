# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59150717/typeerror-method-object-is-not-subscriptable-python-django
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class QuestionSaveTestCase(_n_(650226, "TestCase", lambda: TestCase)):
    _l_(650280)

    """
        Testing Question.save()
    """

    @_c_(650227, patch, 'qanda.service.elasticsearch.Elasticsearch')
    def test_elasticsearch_upsert_on_save(self, ElasticSearchMock):
        _l_(650279)

        user = _c_(650231, _a_(650230, _a_(650229, _n_(650228, "User", lambda: User), "objects"), "create"), username='unittest',
            password='unittest'
        )
        _l_(650232)
        question_title = 'Unit test'
        _l_(650233)
        question_body = 'Some unit test'
        _l_(650234)
        q = _c_(650239, _n_(650235, "Question", lambda: Question), title=_n_(650236, "question_title", lambda: question_title),
                     question=_n_(650237, "question_body", lambda: question_body),
                     user=_n_(650238, "user", lambda: user))
        _l_(650240)
        _c_(650243, _a_(650242, _n_(650241, "q", lambda: q), "save"))
        _l_(650244)

        _c_(650249, _a_(650246, _n_(650245, "self", lambda: self), "assertIsNotNone"), _a_(650248, _n_(650247, "q", lambda: q), "id"))
        _l_(650250)
        _c_(650255, _a_(650252, _n_(650251, "self", lambda: self), "assertTrue"), _a_(650254, _n_(650253, "ElasticSearchMock", lambda: ElasticSearchMock), "called"))
        _l_(650256)
        mock_client = _a_(650258, _n_(650257, "ElasticSearchMock", lambda: ElasticSearchMock), "return_value")
        _l_(650259)
        _c_(650277, _a_(650262, _a_(650261, _n_(650260, "mock_client", lambda: mock_client), "update"), "assert_called_once_with"), _a_(650264, _n_(650263, "settings", lambda: settings), "ES_IDENX"),
            id=_a_(650266, _n_(650265, "q", lambda: q), "id"),
            body={
                'doc': {
                    '_type': 'doc',
                    'text': _c_(650270, _a_(650267, '{}\n{}', "format"), _n_(650268, "question_title", lambda: question_title), _n_(650269, "question_body", lambda: question_body)),
                    'question_body': _n_(650271, "question_body", lambda: question_body),
                    'title': _n_(650272, "question_title", lambda: question_title),
                    'id': _a_(650274, _n_(650273, "q", lambda: q), "id"),
                    'created': _a_(650276, _n_(650275, "q", lambda: q), "created"),
                },
                'doc_as_upsert': True,
            }
        )
        _l_(650278)