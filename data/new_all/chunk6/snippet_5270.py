# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74596527/nameerror-name-alltodos-is-not-defined-unboundlocalerror-local-variable-a
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask, render_template ,request
    _l_(365113)

except ImportError:
    pass
try:
    from flask_sqlalchemy import SQLAlchemy
    _l_(365115)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(365117)

except ImportError:
    pass


app = _c_(365120, _n_(365118, "Flask", lambda: Flask), _n_(365119, "__name__", lambda: __name__))
_l_(365121)
_a_(365123, _n_(365122, "app", lambda: app), "config")['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
_l_(365124)
db = _c_(365127, _n_(365125, "SQLAlchemy", lambda: SQLAlchemy), _n_(365126, "app", lambda: app))
_l_(365128)


class Todo(_a_(365130, _n_(365129, "db", lambda: db), "Model")):
    _l_(365166)

    SNumber = _c_(365135, _a_(365132, _n_(365131, "db", lambda: db), "Column"), _a_(365134, _n_(365133, "db", lambda: db), "Integer"),primary_key=True)
    _l_(365136)
    title = _c_(365142, _a_(365138, _n_(365137, "db", lambda: db), "Column"), _c_(365141, _a_(365140, _n_(365139, "db", lambda: db), "String"), 200),nullable=False)
    _l_(365143)
    desc = _c_(365149, _a_(365145, _n_(365144, "db", lambda: db), "Column"), _c_(365148, _a_(365147, _n_(365146, "db", lambda: db), "String"), 500),nullable=False)
    _l_(365150)
    data_created = _c_(365157, _a_(365152, _n_(365151, "db", lambda: db), "Column"), _a_(365154, _n_(365153, "db", lambda: db), "DateTime"), default = _a_(365156, _n_(365155, "datetime", lambda: datetime), "utcnow"))
    _l_(365158)

    def __repr__(self) -> _n_(365159, "str", lambda: str):
        _l_(365165)

        aux = f"{_a_(365161, _n_(365160, 'self', lambda: self), 'SNumber')} - {_a_(365163, _n_(365162, 'self', lambda: self), 'title')}"
        _l_(365164)
        return aux


@_c_(365169, _a_(365168, _n_(365167, "app", lambda: app), "route"), '/' , methods=['GET','POST'])
def hello_world():
    _l_(365204)

    if _a_(365171, _n_(365170, "request", lambda: request), "method") == 'POST':
        _l_(365199)

        title = _a_(365173, _n_(365172, "request", lambda: request), "form")['title']
        _l_(365174)
        desc = _a_(365176, _n_(365175, "request", lambda: request), "form")['desc']
        _l_(365177)
        todo = _c_(365181, _n_(365178, "Todo", lambda: Todo), title = _n_(365179, "title", lambda: title), desc = _n_(365180, "desc", lambda: desc))
        _l_(365182)
        _c_(365187, _a_(365185, _a_(365184, _n_(365183, "db", lambda: db), "session"), "add"), _n_(365186, "todo", lambda: todo))
        _l_(365188)
        _c_(365192, _a_(365191, _a_(365190, _n_(365189, "db", lambda: db), "session"), "commit"))
        _l_(365193)
        
        allTodos = _c_(365197, _a_(365196, _a_(365195, _n_(365194, "Todo", lambda: Todo), "query"), "all"))
        _l_(365198)
    aux = _c_(365202, _n_(365200, "render_template", lambda: render_template), 'index.html',allTodo=_n_(365201, "allTodos", lambda: allTodos))
    _l_(365203)
    return aux

@_c_(365207, _a_(365206, _n_(365205, "app", lambda: app), "route"), '/show')
def products():
    _l_(365209)

    aux = "this is a product page"    
    _l_(365208)    
    #allTodo = Todo.query.all()
    #print(allTodo)
    return aux    

if _n_(365210, "__name__", lambda: __name__) == "__main__":
    _l_(365215)

    _c_(365213, _a_(365212, _n_(365211, "app", lambda: app), "run"), debug=True)
    _l_(365214)