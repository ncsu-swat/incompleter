# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69186111/how-to-solve-could-not-import-todo-schema-schema-for-graphene-setting-schema
# declar todo model field
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TodoType(_n_(546182, "DjangoObjectType", lambda: DjangoObjectType)):
    _l_(546186)

    class Meta:
        _l_(546185)

        model = TodoList
        _l_(546183)
        fields = ('id', 'title', 'date', 'text')
        _l_(546184)


# declar user model filed
class UserType(_n_(546187, "DjangoObjectType", lambda: DjangoObjectType)):
    _l_(546190)

    class Meta:
        _l_(546189)

        model = User
        _l_(546188)


# todo list query
class TodoQuery(_a_(546192, _n_(546191, "graphene", lambda: graphene), "ObjectType")):
    _l_(546202)

    todoList = _c_(546194, DjangoListField, _n_(546193, "TodoType", lambda: TodoType))
    _l_(546195)

    def resolve_todoList(root, info):
        _l_(546201)

        aux = _c_(546199, _a_(546198, _a_(546197, _n_(546196, "TodoList", lambda: TodoList), "objects"), "filter"), userId=2)
        _l_(546200)
        return aux


# create todo
class TodoCreate(_a_(546204, _n_(546203, "graphene", lambda: graphene), "Mutation")):
    _l_(546236)

    class Arguments:
        _l_(546211)

        title = _c_(546206, _a_(546205, graphene, "String"), Required=True)
        _l_(546207)
        text = _c_(546209, _a_(546208, graphene, "string"), Required=True)
        _l_(546210)

    todo = _c_(546214, _a_(546212, graphene, "Field"), _n_(546213, "TodoType", lambda: TodoType))
    _l_(546215)

    def mutate(root, info, title, text):
        _l_(546235)

        # userId = info.context.user
        user = _c_(546219, _a_(546218, _a_(546217, _n_(546216, "User", lambda: User), "objects"), "get"), id=2)
        _l_(546220)
        todo = _c_(546225, _n_(546221, "TodoList", lambda: TodoList), userId=_n_(546222, "user", lambda: user), title=_n_(546223, "title", lambda: title), text=_n_(546224, "text", lambda: text))
        _l_(546226)
        _c_(546229, _a_(546228, _n_(546227, "todo", lambda: todo), "save"))
        _l_(546230)
        aux = _c_(546233, _n_(546231, "TodoCreate", lambda: TodoCreate), todo=_n_(546232, "todo", lambda: todo))
        _l_(546234)
        return aux


# todo mutation
class Mutation(_a_(546238, _n_(546237, "graphene", lambda: graphene), "ObjectType")):
    _l_(546243)

    createTodo = _c_(546241, _a_(546240, _n_(546239, "TodoCreate", lambda: TodoCreate), "Field"))
    _l_(546242)