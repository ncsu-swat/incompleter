# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65586172/sqlalchemy-object-throwing-attribute-error-for-sa-instance-state-in-pytest
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TestConfig(_n_(575446, "Config", lambda: Config)):
    _l_(575451)

    TESTING = True                                                                                                                                          
    _l_(575447)                                                                                                                                          
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'                                                                                                           
    _l_(575448)                                                                                                           
    WTF_CSRF_ENABLED = False                                                                                                                                
    _l_(575449)                                                                                                                                
    BCRYPT_LOG_ROUNDS = 4                                                                                                                                   
    _l_(575450)                                                                                                                                   
def fill_database():
    _l_(575473)

    s0 = _c_(575453, _n_(575452, "Source", lambda: Source), title='Catalist')                                                                                                                           
    _l_(575454)                                                                                                                           
    s1 = _c_(575456, _n_(575455, "Source", lambda: Source), title='L2')                                                                                                                                 
    _l_(575457)                                                                                                                                 
    sources = [_n_(575458, "s0", lambda: s0), _n_(575459, "s1", lambda: s1)]                                                                                                                                      
    _l_(575460)                                                                                                                                      
    l0 = _c_(575462, _n_(575461, "Voterlist", lambda: Voterlist), description='Test List 0')                                                                                                               
    _l_(575463)                                                                                                               
    l1 = _c_(575465, _n_(575464, "Voterlist", lambda: Voterlist), description='Test List 1')                                                                                                               
    _l_(575466)                                                                                                               
    lists = [_n_(575467, "l0", lambda: l0), _n_(575468, "l1", lambda: l1)]                                                                                                                                        
    _l_(575469)                                                                                                                                        
    aux = _n_(575470, "lists", lambda: lists), _n_(575471, "sources", lambda: sources)                                                                                                                                   
    _l_(575472)                                                                                                                                   
    return aux                                                                                                                                   
@_c_(575476, _a_(575475, _n_(575474, "pytest", lambda: pytest), "fixture"), scope='class')                                                                                                                              
def test_client():
    _l_(575539)

    flask_app = _c_(575479, _n_(575477, "create_app", lambda: create_app), _n_(575478, "TestConfig", lambda: TestConfig))                                                                                                                      
    _l_(575480)                                                                                                                      
    with _c_(575483, _a_(575482, _n_(575481, "flask_app", lambda: flask_app), "test_client")) as client:
        _l_(575534)

        app_context = _c_(575486, _a_(575485, _n_(575484, "flask_app", lambda: flask_app), "test_request_context"))                                                                                                      
        _l_(575487)                                                                                                      
        _c_(575490, _a_(575489, _n_(575488, "app_context", lambda: app_context), "push"))                                                                                                                                  
        _l_(575491)                                                                                                                                  
        _c_(575494, _a_(575493, _n_(575492, "db", lambda: db), "create_all"))                                                                                                                                     
        _l_(575495)                                                                                                                                     
        lists, sources = _c_(575497, _n_(575496, "fill_database", lambda: fill_database))                                                                                                                    
        _l_(575498)                                                                                                                    
        for s in _n_(575499, "sources", lambda: sources):
            _l_(575511)

            _c_(575504, _a_(575502, _a_(575501, _n_(575500, "db", lambda: db), "session"), "add"), _n_(575503, "s", lambda: s))                                                                                                                               
            _l_(575505)                                                                                                                               
            _c_(575509, _a_(575508, _a_(575507, _n_(575506, "db", lambda: db), "session"), "commit"))                                                                                                                             
            _l_(575510)                                                                                                                             
        for l in _n_(575512, "lists", lambda: lists):
            _l_(575527)

            _c_(575517, _a_(575515, _a_(575514, _n_(575513, "db", lambda: db), "session"), "add"), _n_(575516, "l", lambda: l))                                                                                                                        
            _l_(575518)                                                                                                                        
            _c_(575522, _a_(575521, _a_(575520, _n_(575519, "db", lambda: db), "session"), "commit"))                                                                                                                             
            _l_(575523)                                                                                                                             
            _c_(575525, _n_(575524, "sleep", lambda: sleep), 1)                                                                                                                                        
            _l_(575526)                                                                                                                                        
        yield _n_(575528, "client", lambda: client)                                                                                                                                        
        _l_(575529)                                                                                                                                        
        _c_(575532, _a_(575531, _n_(575530, "db", lambda: db), "drop_all"))                                                                                                                                       
        _l_(575533)                                                                                                                                       
    _c_(575537, _a_(575536, _n_(575535, "app_context", lambda: app_context), "pop")) 
    _l_(575538) 