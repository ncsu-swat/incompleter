# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module
# see the docs: if you set no timeout the call never times out! A tuple means "max 
# connect time" and "max read time"
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
DEFAULT_REQUESTS_TIMEOUT = (5, 15) # for example
_l_(1543978) # for example

def log_exception(e, verb, url, kwargs):
    _l_(1544013)

    # the reason for making this a separate function will become apparent
    raw_tb = _c_(1543981, _a_(1543980, _n_(1543979, "traceback", lambda: traceback), "extract_stack"))
    _l_(1543982)
    if 'data' in _n_(1543983, "kwargs", lambda: kwargs) and _c_(1543986, _n_(1543984, "len", lambda: len), _n_(1543985, "kwargs", lambda: kwargs)['data']) > 500:
        _l_(1543990)

        _n_(1543987, "kwargs", lambda: kwargs)['data'] = f'{_n_(1543988, "kwargs", lambda: kwargs)["data"][:500]}...'  
        _l_(1543989)  
    msg = f'BaseException raised: {_a_(1543993, _a_(1543992, _n_(1543991, "e", lambda: e), "__class__"), "__module__")}.{_a_(1543996, _a_(1543995, _n_(1543994, "e", lambda: e), "__class__"), "__qualname__")}: {_n_(1543997, "e", lambda: e)}\n' \
        + f'verb {_n_(1543998, "verb", lambda: verb)}, url {_n_(1543999, "url", lambda: url)}, kwargs {_n_(1544000, "kwargs", lambda: kwargs)}\n\n' \
        + 'Stack trace:\n' + _c_(1544006, _a_(1544001, '', 'join'), _c_(1544005, _a_(1544003, _n_(1544002, 'traceback', lambda: traceback), 'format_list'), _n_(1544004, 'raw_tb', lambda: raw_tb)[:-2]))
    _l_(1544007)
    _c_(1544011, _a_(1544009, _n_(1544008, 'logger', lambda: logger), 'error'), _n_(1544010, 'msg', lambda: msg)) 
    _l_(1544012) 

def requests_call(verb, url, **kwargs):
    _l_(1544043)

    response = None
    _l_(1544014)
    exception = None
    _l_(1544015)
    try:
        _l_(1544039)

        if 'timeout' not in _n_(1544016, 'kwargs', lambda: kwargs):
            _l_(1544020)

            _n_(1544017, 'kwargs', lambda: kwargs)['timeout'] = _n_(1544018, 'DEFAULT_REQUESTS_TIMEOUT', lambda: DEFAULT_REQUESTS_TIMEOUT)
            _l_(1544019)
        response = _c_(1544026, _a_(1544022, _n_(1544021, 'requests', lambda: requests), 'request'), _n_(1544023, 'verb', lambda: verb), _n_(1544024, 'url', lambda: url), **_n_(1544025, 'kwargs', lambda: kwargs))
        _l_(1544027)
    except _n_(1544028, 'BaseException', lambda: BaseException) as e:
        _l_(1544038)

        _c_(1544034, _n_(1544029, 'log_exception', lambda: log_exception), _n_(1544030, 'e', lambda: e), _n_(1544031, 'verb', lambda: verb), _n_(1544032, 'url', lambda: url), _n_(1544033, 'kwargs', lambda: kwargs))
        _l_(1544035)
        exception = _n_(1544036, 'e', lambda: e)
        _l_(1544037)
    aux = (_n_(1544040, 'response', lambda: response), _n_(1544041, 'exception', lambda: exception))
    _l_(1544042)
    return aux

search_response, exception = _c_(1544047, _a_(1544045, _n_(1544044, 'utilities', lambda: utilities), 'requests_call'), 'get',
    f'http://localhost:9200/my_index/_search?q={_n_(1544046, "search_string", lambda: search_string)}')
_l_(1544048)

if _n_(1544049, 'search_response', lambda: search_response) == None:
    _l_(1544062)

    # you might check here for (e.g.) a requests.Timeout, tailoring the message
    # accordingly, as the kind of error anyone might be expected to understand
    msg = f'No response searching on |{_n_(1544050, "search_string", lambda: search_string)}|. See log'
    _l_(1544051)
    _c_(1544059, _a_(1544055, _c_(1544054, _a_(1544053, _n_(1544052, 'MainWindow', lambda: MainWindow), 'the')), 'visual_log'), _n_(1544056, 'msg', lambda: msg), log_level=_a_(1544058, _n_(1544057, 'logging', lambda: logging), 'ERROR'))
    _l_(1544060)
    aux = ""
    _l_(1544061)
    return aux
response_json = _c_(1544065, _a_(1544064, _n_(1544063, 'search_response', lambda: search_response), 'json'))
_l_(1544066)
if _a_(1544068, _n_(1544067, 'search_response', lambda: search_response), 'status_code') != 200:
    _l_(1544092)

    msg = f'Bad response searching on |{_n_(1544069, "search_string", lambda: search_string)}|. See log'
    _l_(1544070)
    _c_(1544078, _a_(1544074, _c_(1544073, _a_(1544072, _n_(1544071, 'MainWindow', lambda: MainWindow), 'the')), 'visual_log'), _n_(1544075, 'msg', lambda: msg), log_level=_a_(1544077, _n_(1544076, 'logging', lambda: logging), 'ERROR'))
    _l_(1544079)
    # usually response_json will give full details about the problem
    log_msg = f'search on |{_n_(1544080, "search_string", lambda: search_string)}| bad response\n{_c_(1544084, _a_(1544082, _n_(1544081, "json", lambda: json), "dumps"), _n_(1544083, "response_json", lambda: response_json), indent=4)}'
    _l_(1544085)
    _c_(1544089, _a_(1544087, _n_(1544086, 'logger', lambda: logger), 'error'), _n_(1544088, 'log_msg', lambda: log_msg))
    _l_(1544090)
    aux = ""
    _l_(1544091)
    return aux

# now examine the keys and values in response_json: these may of course 
# indicate an error of some kind even though the response returned OK (status 200)... 

def log_response_error(response_type, call_name, deliverable, verb, url, **kwargs):
    _l_(1544179)

    # NB this function can also be used independently
    if _n_(1544093, 'response_type', lambda: response_type) == 'No':
        _l_(1544168)

        if _c_(1544098, _n_(1544094, 'isinstance', lambda: isinstance), _n_(1544095, 'deliverable', lambda: deliverable), _a_(1544097, _n_(1544096, 'requests', lambda: requests), 'Timeout')):
            _l_(1544109)

            _c_(1544106, _a_(1544102, _c_(1544101, _a_(1544100, _n_(1544099, 'MainWindow', lambda: MainWindow), 'the')), 'visual_log'), f'Time out of {_n_(1544103, "call_name", lambda: call_name)} before response received!', _a_(1544105, _n_(1544104, 'logging', lambda: logging), 'ERROR'))
            _l_(1544107)
            aux = ""    
            _l_(1544108)    
            return aux    
    else:
        if _c_(1544113, _n_(1544110, 'isinstance', lambda: isinstance), _n_(1544111, 'deliverable', lambda: deliverable), _n_(1544112, 'BaseException', lambda: BaseException)):
            _l_(1544167)

            # NB if response.json() raises an exception we end up here
            _c_(1544119, _n_(1544114, 'log_exception', lambda: log_exception), _n_(1544115, 'deliverable', lambda: deliverable), _n_(1544116, 'verb', lambda: verb), _n_(1544117, 'url', lambda: url), _n_(1544118, 'kwargs', lambda: kwargs))
            _l_(1544120)
        else:
            # if we get here no exception has been raised, so no stack trace has yet been logged.  
            # a response has been returned, but is either "Bad" or "Anomalous"
            response_json = _c_(1544123, _a_(1544122, _n_(1544121, 'deliverable', lambda: deliverable), 'json'))
            _l_(1544124)

            raw_tb = _c_(1544127, _a_(1544126, _n_(1544125, 'traceback', lambda: traceback), 'extract_stack'))
            _l_(1544128)
            if 'data' in _n_(1544129, 'kwargs', lambda: kwargs) and _c_(1544132, _n_(1544130, 'len', lambda: len), _n_(1544131, 'kwargs', lambda: kwargs)['data']) > 500:
                _l_(1544136)

                _n_(1544133, 'kwargs', lambda: kwargs)['data'] = f'{_n_(1544134, "kwargs", lambda: kwargs)["data"][:500]}...'
                _l_(1544135)
            added_message = ''     
            _l_(1544137)     
            if _c_(1544140, _n_(1544138, 'hasattr', lambda: hasattr), _n_(1544139, 'deliverable', lambda: deliverable), 'added_message'):
                _l_(1544145)

                added_message = _a_(1544142, _n_(1544141, 'deliverable', lambda: deliverable), 'added_message') + '\n'
                _l_(1544143)
                del deliverable.added_message
                _l_(1544144)
            call_and_response_details = f'{_n_(1544146, "response_type", lambda: response_type)} response\n{_n_(1544147, "added_message", lambda: added_message)}' \
                + f'verb {_n_(1544148, "verb", lambda: verb)}, url {_n_(1544149, "url", lambda: url)}, kwargs {_n_(1544150, "kwargs", lambda: kwargs)}\nresponse:\n{_c_(1544154, _a_(1544152, _n_(1544151, "json", lambda: json), "dumps"), _n_(1544153, "response_json", lambda: response_json), indent=4)}'
            _l_(1544155)
            _c_(1544165, _a_(1544157, _n_(1544156, 'logger', lambda: logger), 'error'), f'{_n_(1544158, "call_and_response_details", lambda: call_and_response_details)}\nStack trace: {_c_(1544164, _a_(1544159, "", "join"), _c_(1544163, _a_(1544161, _n_(1544160, "traceback", lambda: traceback), "format_list"), _n_(1544162, "raw_tb", lambda: raw_tb)[:-1]))}')
            _l_(1544166)
    _c_(1544177, _a_(1544172, _c_(1544171, _a_(1544170, _n_(1544169, 'MainWindow', lambda: MainWindow), 'the')), 'visual_log'), f'{_n_(1544173, "response_type", lambda: response_type)} response {_n_(1544174, "call_name", lambda: call_name)}. See log.', _a_(1544176, _n_(1544175, 'logging', lambda: logging), 'ERROR'))
    _l_(1544178)
def check_keys(req_dict_structure, response_dict_structure, response):
    _l_(1544307)

    # so this function is about checking the keys in the returned json object...
    # NB both structures MUST be dicts
    if not _c_(1544183, _n_(1544180, 'isinstance', lambda: isinstance), _n_(1544181, 'req_dict_structure', lambda: req_dict_structure), _n_(1544182, 'dict', lambda: dict)):
        _l_(1544190)

        _n_(1544184, 'response', lambda: response).added_message = f'req_dict_structure not dict: {_c_(1544187, _n_(1544185, "type", lambda: type), _n_(1544186, "req_dict_structure", lambda: req_dict_structure))}\n'
        _l_(1544188)
        aux = False
        _l_(1544189)
        return aux
    if not _c_(1544194, _n_(1544191, 'isinstance', lambda: isinstance), _n_(1544192, 'response_dict_structure', lambda: response_dict_structure), _n_(1544193, 'dict', lambda: dict)):
        _l_(1544201)

        _n_(1544195, 'response', lambda: response).added_message = f'response_dict_structure not dict: {_c_(1544198, _n_(1544196, "type", lambda: type), _n_(1544197, "response_dict_structure", lambda: response_dict_structure))}\n'
        _l_(1544199)
        aux = False
        _l_(1544200)
        return aux
    for dict_key in _c_(1544204, _a_(1544203, _n_(1544202, 'req_dict_structure', lambda: req_dict_structure), 'keys')):
        _l_(1544305)

        if _n_(1544205, 'dict_key', lambda: dict_key) not in _n_(1544206, 'response_dict_structure', lambda: response_dict_structure):
            _l_(1544211)

            _n_(1544207, 'response', lambda: response).added_message = f'key |{_n_(1544208, "dict_key", lambda: dict_key)}| missing\n'
            _l_(1544209)
            aux = False
            _l_(1544210)
            return aux
        req_value = _n_(1544212, 'req_dict_structure', lambda: req_dict_structure)[_n_(1544213, 'dict_key', lambda: dict_key)]
        _l_(1544214)
        response_value = _n_(1544215, 'response_dict_structure', lambda: response_dict_structure)[_n_(1544216, 'dict_key', lambda: dict_key)]
        _l_(1544217)
        if _c_(1544221, _n_(1544218, 'isinstance', lambda: isinstance), _n_(1544219, 'req_value', lambda: req_value), _n_(1544220, 'dict', lambda: dict)):
            _l_(1544304)

            # if the response at this point is a list apply the req_value dict to each element:
            # failure in just one such element leads to "Anomalous response"... 
            if _c_(1544225, _n_(1544222, 'isinstance', lambda: isinstance), _n_(1544223, 'response_value', lambda: response_value), _n_(1544224, 'list', lambda: list)):
                _l_(1544242)

                for resp_list_element in _n_(1544226, 'response_value', lambda: response_value):
                    _l_(1544234)

                    if not _c_(1544231, _n_(1544227, 'check_keys', lambda: check_keys), _n_(1544228, 'req_value', lambda: req_value), _n_(1544229, 'resp_list_element', lambda: resp_list_element), _n_(1544230, 'response', lambda: response)):
                        _l_(1544233)

                        aux = False
                        _l_(1544232)
                        return aux
            elif not _c_(1544239, _n_(1544235, 'check_keys', lambda: check_keys), _n_(1544236, 'req_value', lambda: req_value), _n_(1544237, 'response_value', lambda: response_value), _n_(1544238, 'response', lambda: response)):
                _l_(1544241)

                aux = False
                _l_(1544240)
                return aux
        elif _c_(1544246, _n_(1544243, 'isinstance', lambda: isinstance), _n_(1544244, 'req_value', lambda: req_value), _n_(1544245, 'list', lambda: list)):
            _l_(1544303)

            if not _c_(1544250, _n_(1544247, 'isinstance', lambda: isinstance), _n_(1544248, 'response_value', lambda: response_value), _n_(1544249, 'list', lambda: list)):
                _l_(1544258)

                _n_(1544251, 'response', lambda: response).added_message = f'key |{_n_(1544252, "dict_key", lambda: dict_key)}| not list: {_c_(1544255, _n_(1544253, "type", lambda: type), _n_(1544254, "response_value", lambda: response_value))}\n'
                _l_(1544256)
                aux = False
                _l_(1544257)
                return aux
            # it is OK for the value to be a list, but these must be strings (keys) or dicts
            for req_list_element, resp_list_element in _c_(1544262, _n_(1544259, 'zip', lambda: zip), _n_(1544260, 'req_value', lambda: req_value), _n_(1544261, 'response_value', lambda: response_value)):
                _l_(1544293)

                if _c_(1544266, _n_(1544263, 'isinstance', lambda: isinstance), _n_(1544264, 'req_list_element', lambda: req_list_element), _n_(1544265, 'dict', lambda: dict)):
                    _l_(1544274)

                    if not _c_(1544271, _n_(1544267, 'check_keys', lambda: check_keys), _n_(1544268, 'req_list_element', lambda: req_list_element), _n_(1544269, 'resp_list_element', lambda: resp_list_element), _n_(1544270, 'response', lambda: response)):
                        _l_(1544273)

                        aux = False
                        _l_(1544272)
                        return aux
                if not _c_(1544278, _n_(1544275, 'isinstance', lambda: isinstance), _n_(1544276, 'req_list_element', lambda: req_list_element), _n_(1544277, 'str', lambda: str)):
                    _l_(1544285)

                    _n_(1544279, 'response', lambda: response).added_message = f'req_list_element not string: {_c_(1544282, _n_(1544280, "type", lambda: type), _n_(1544281, "req_list_element", lambda: req_list_element))}\n'
                    _l_(1544283)
                    aux = False
                    _l_(1544284)
                    return aux
                if _n_(1544286, 'req_list_element', lambda: req_list_element) not in _n_(1544287, 'response_value', lambda: response_value):
                    _l_(1544292)

                    _n_(1544288, 'response', lambda: response).added_message = f'key |{_n_(1544289, "req_list_element", lambda: req_list_element)}| missing from response list\n'
                    _l_(1544290)
                    aux = False
                    _l_(1544291)
                    return aux
        # put None as a dummy value (otherwise something like {'my_key'} will be seen as a set, not a dict 
        elif _n_(1544294, 'req_value', lambda: req_value) != None:
            _l_(1544302)

            _n_(1544295, 'response', lambda: response).added_message = f'required value of key |{_n_(1544296, "dict_key", lambda: dict_key)}| must be None (dummy), dict or list: {_c_(1544299, _n_(1544297, "type", lambda: type), _n_(1544298, "req_value", lambda: req_value))}\n'
            _l_(1544300)
            aux = False
            _l_(1544301)
            return aux
    aux = True
    _l_(1544306)
    return aux

def process_json_requests_call(verb, url, **kwargs):
    _l_(1544415)

    # "call_name" is a mandatory kwarg
    if 'call_name' not in _n_(1544308, 'kwargs', lambda: kwargs):
        _l_(1544312)

        raise _c_(1544310, _n_(1544309, 'Exception', lambda: Exception), 'kwarg "call_name" not supplied!')
        _l_(1544311)
    call_name = _n_(1544313, 'kwargs', lambda: kwargs)['call_name']
    _l_(1544314)
    del kwargs['call_name']
    _l_(1544315)

    required_keys = {}    
    _l_(1544316)    
    if 'required_keys' in _n_(1544317, 'kwargs', lambda: kwargs):
        _l_(1544321)

        required_keys = _n_(1544318, 'kwargs', lambda: kwargs)['required_keys']
        _l_(1544319)
        del kwargs['required_keys']
        _l_(1544320)

    acceptable_statuses = [200]
    _l_(1544322)
    if 'acceptable_statuses' in _n_(1544323, 'kwargs', lambda: kwargs):
        _l_(1544327)

        acceptable_statuses = _n_(1544324, 'kwargs', lambda: kwargs)['acceptable_statuses']
        _l_(1544325)
        del kwargs['acceptable_statuses']
        _l_(1544326)

    exception_handler = _n_(1544328, 'log_response_error', lambda: log_response_error)
    _l_(1544329)
    if 'exception_handler' in _n_(1544330, 'kwargs', lambda: kwargs):
        _l_(1544334)

        exception_handler = _n_(1544331, 'kwargs', lambda: kwargs)['exception_handler']
        _l_(1544332)
        del kwargs['exception_handler']
        _l_(1544333)
    response, exception = _c_(1544339, _n_(1544335, 'requests_call', lambda: requests_call), _n_(1544336, 'verb', lambda: verb), _n_(1544337, 'url', lambda: url), **_n_(1544338, 'kwargs', lambda: kwargs))
    _l_(1544340)

    if _n_(1544341, 'response', lambda: response) == None:
        _l_(1544352)

        _c_(1544348, _n_(1544342, 'exception_handler', lambda: exception_handler), 'No', _n_(1544343, 'call_name', lambda: call_name), _n_(1544344, 'exception', lambda: exception), _n_(1544345, 'verb', lambda: verb), _n_(1544346, 'url', lambda: url), **_n_(1544347, 'kwargs', lambda: kwargs))
        _l_(1544349)
        aux = (False, _n_(1544350, 'exception', lambda: exception))
        _l_(1544351)
        return aux
    try:
        _l_(1544375)

        response_json = _c_(1544355, _a_(1544354, _n_(1544353, 'response', lambda: response), 'json'))
        _l_(1544356)
    except _n_(1544357, 'BaseException', lambda: BaseException) as e:
        _l_(1544374)

        _c_(1544362, _a_(1544359, _n_(1544358, 'logger', lambda: logger), 'error'), f'response.status_code {_a_(1544361, _n_(1544360, "response", lambda: response), "status_code")} but calling json() raised exception')
        _l_(1544363)
        # an exception raised at this point can't truthfully lead to a "No response" message... so say "bad"
        _c_(1544370, _n_(1544364, 'exception_handler', lambda: exception_handler), 'Bad', _n_(1544365, 'call_name', lambda: call_name), _n_(1544366, 'e', lambda: e), _n_(1544367, 'verb', lambda: verb), _n_(1544368, 'url', lambda: url), **_n_(1544369, 'kwargs', lambda: kwargs))
        _l_(1544371)
        aux = (False, _n_(1544372, 'response', lambda: response))
        _l_(1544373)
        return aux
    status_ok = _a_(1544377, _n_(1544376, 'response', lambda: response), 'status_code') in _n_(1544378, 'acceptable_statuses', lambda: acceptable_statuses)
    _l_(1544379)
    if not _n_(1544380, 'status_ok', lambda: status_ok):
        _l_(1544395)

        _n_(1544381, 'response', lambda: response).added_message = f'status code was {_a_(1544383, _n_(1544382, "response", lambda: response), "status_code")}'
        _l_(1544384)
        _c_(1544391, _n_(1544385, 'log_response_error', lambda: log_response_error), 'Bad', _n_(1544386, 'call_name', lambda: call_name), _n_(1544387, 'response', lambda: response), _n_(1544388, 'verb', lambda: verb), _n_(1544389, 'url', lambda: url), **_n_(1544390, 'kwargs', lambda: kwargs))
        _l_(1544392)
        aux = (False, _n_(1544393, 'response', lambda: response))
        _l_(1544394)
        return aux
    check_result = _c_(1544400, _n_(1544396, 'check_keys', lambda: check_keys), _n_(1544397, 'required_keys', lambda: required_keys), _n_(1544398, 'response_json', lambda: response_json), _n_(1544399, 'response', lambda: response))
    _l_(1544401)
    if not _n_(1544402, 'check_result', lambda: check_result):
        _l_(1544411)

        _c_(1544409, _n_(1544403, 'log_response_error', lambda: log_response_error), 'Anomalous', _n_(1544404, 'call_name', lambda: call_name), _n_(1544405, 'response', lambda: response), _n_(1544406, 'verb', lambda: verb), _n_(1544407, 'url', lambda: url), **_n_(1544408, 'kwargs', lambda: kwargs))
        _l_(1544410)
    aux = (_n_(1544412, 'check_result', lambda: check_result), _n_(1544413, 'response', lambda: response))      
    _l_(1544414)      
    return aux      

success, deliverable = _c_(1544421, _a_(1544417, _n_(1544416, 'utilities', lambda: utilities), 'process_json_requests_call'), 'get', 
    f'{_n_(1544418, "ES_URL", lambda: ES_URL)}{_n_(1544419, "INDEX_NAME", lambda: INDEX_NAME)}/_doc/1', 
    call_name=f'checking index {_n_(1544420, "INDEX_NAME", lambda: INDEX_NAME)}',
    required_keys={'_source':{'status_text': None}})
_l_(1544422)
if not _n_(1544423, 'success', lambda: success):
    _l_(1544424)

return False# here, we know the deliverable is a response, not an exception
# we also don't need to check for the keys being present: 
# the generic code has checked that all expected keys are present
index_status = _c_(1544427, _a_(1544426, _n_(1544425, 'deliverable', lambda: deliverable), 'json'))['_source']['status_text']
_l_(1544428)
if _n_(1544429, 'index_status', lambda: index_status) != 'successfully completed':
    _l_(1544451)

    # ... i.e. an example of a 200 response, but an error nonetheless
    msg = f'Error response: ES index {_n_(1544430, "INDEX_NAME", lambda: INDEX_NAME)} does not seem to have been built OK: cannot search'
    _l_(1544431)
    _c_(1544437, _a_(1544435, _c_(1544434, _a_(1544433, _n_(1544432, 'MainWindow', lambda: MainWindow), 'the')), 'visual_log'), _n_(1544436, 'msg', lambda: msg))
    _l_(1544438)
    _c_(1544448, _a_(1544440, _n_(1544439, 'logger', lambda: logger), 'error'), f'index |{_n_(1544441, "INDEX_NAME", lambda: INDEX_NAME)}|: deliverable.json() {_c_(1544447, _a_(1544443, _n_(1544442, "json", lambda: json), "dumps"), _c_(1544446, _a_(1544445, _n_(1544444, "deliverable", lambda: deliverable), "json")), indent=4)}')
    _l_(1544449)
    aux = False
    _l_(1544450)
    return aux

