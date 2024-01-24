# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49259443/im-overlooking-something-typeerror-create-got-unexpected-keyword-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class ProjectManager(_a_(695112, _n_(695111, "models", lambda: models), "Manager")):
    _l_(695132)

    """"""
    def create(self, owner, project_name):
        _l_(695131)

        project = _c_(695117, _a_(695114, _n_(695113, "super", lambda: super)(), "create"), owner=_n_(695115, "owner", lambda: owner), project_name=_n_(695116, "project_name", lambda: project_name))
        _l_(695118)
        _c_(695121, _a_(695120, _n_(695119, "project", lambda: project), "save"))
        _l_(695122)

        _c_(695127, _a_(695125, _a_(695124, _n_(695123, "System", lambda: System), "objects"), "create"), project=_n_(695126, "project", lambda: project), system_name="System initial name")
        _l_(695128)
        aux = _n_(695129, "project", lambda: project)
        _l_(695130)

        return aux

class Project(_a_(695134, _n_(695133, "models", lambda: models), "Model")):
    _l_(695145)

    objects = _c_(695136, _n_(695135, "ProjectManager", lambda: ProjectManager))
    _l_(695137)

    owner           = _c_(695140, _a_(695138, models, "ForeignKey"), 'auth.User', related_name='projects', on_delete=_a_(695139, models, "CASCADE"))
    _l_(695141)
    project_name    = _c_(695143, _a_(695142, models, "CharField"), max_length=200)
    _l_(695144)