# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59792902/mock-patch-results-in-error-typeerror-object-takes-no-parameters-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TestSomething(_n_(561715, "SomeConfigsToBeMixedIn", lambda: SomeConfigsToBeMixedIn)):
    _l_(561776)

    @_c_(561717, _a_(561716, mock, "patch"), 'path.to.BetterParser.parse')
    @_c_(561719, _a_(561718, mock, "patch"), 'path.to.SomeValidator.__new__')
    @_c_(561721, _a_(561720, mock, "patch"), 'path.to.SomeValidator.validate')

    def test_validator_is_called(self, mock_validator_new, mock_parse):
        _l_(561775)

        _n_(561722, "mock_validator_new", lambda: mock_validator_new).return_value = _c_(561726, _a_(561724, _n_(561723, "MockUploadValidator", lambda: MockUploadValidator), "__new__"), _n_(561725, "MockUploadValidator", lambda: MockUploadValidator))
        _l_(561727)
        _n_(561728, "mock_parse", lambda: mock_parse).return_value = _n_(561729, "mock_csv_details", lambda: mock_csv_details)
        _l_(561730)
        _n_(561731, "mock_validator_new", lambda: mock_validator_new).return_value = _c_(561733, _n_(561732, "MockUploadValidator", lambda: MockUploadValidator))
        _l_(561734)

        string_io = _c_(561736, _n_(561735, "build_some_string_io_woohoo", lambda: build_some_string_io_woohoo))  # this returns a StringIO
        _l_(561737)  # this returns a StringIO
        some_file = _c_(561740, _n_(561738, "get_temp_from_stream", lambda: get_temp_from_stream), _n_(561739, "string_io", lambda: string_io))
        _l_(561741)

        upload_manager = _c_(561745, _n_(561742, "CSVUploadManager", lambda: CSVUploadManager), _n_(561743, "a_model_instance", lambda: a_model_instance), _n_(561744, "some_file", lambda: some_file))
        _l_(561746)
        _c_(561749, _a_(561748, _n_(561747, "upload_manager", lambda: upload_manager), "is_valid")) # this is where it fails and produces that error
        _l_(561750) # this is where it fails and produces that error

        _c_(561755, _a_(561752, _n_(561751, "self", lambda: self), "assertTrue"), _a_(561754, _n_(561753, "mock_parse", lambda: mock_parse), "called"))
        _l_(561756)
        _c_(561761, _a_(561758, _n_(561757, "self", lambda: self), "assertTrue"), _a_(561760, _n_(561759, "mock_validator_new", lambda: mock_validator_new), "called"))
        _l_(561762)
        validator_new_call_args = (_n_(561763, "SomeValidator", lambda: SomeValidator), _a_(561765, _n_(561764, "self", lambda: self), "cash_activity"), _n_(561766, "mock_csv_details", lambda: mock_csv_details))
        _l_(561767)
        _c_(561773, _a_(561769, _n_(561768, "self", lambda: self), "assertEqual"), _a_(561771, _n_(561770, "mock_validator_new", lambda: mock_validator_new), "_mock_call_args_list")[0][0], _n_(561772, "validator_new_call_args", lambda: validator_new_call_args))
        _l_(561774)