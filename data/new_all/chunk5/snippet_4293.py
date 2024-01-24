# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60123122/typeerror-get-got-an-unexpected-keyword-argument-project-id-in-flask-applica
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import request
    _l_(704159)

except ImportError:
    pass
try:
    from flask_restful import Resource
    _l_(704161)

except ImportError:
    pass
try:
    from  Model import db, Project, ProjectSchema
    _l_(704163)

except ImportError:
    pass

projects_schema = _c_(704165, _n_(704164, "ProjectSchema", lambda: ProjectSchema), many=True)
_l_(704166)
project_schema = _c_(704168, _n_(704167, "ProjectSchema", lambda: ProjectSchema))
_l_(704169)

"""
Get project by id
"""
def get_by_id(project_id):
    _l_(704186)

    project = _c_(704176, _a_(704175, _c_(704174, _a_(704172, _a_(704171, _n_(704170, "Project", lambda: Project), "query"), "filter_by"), id=_n_(704173, "project_id", lambda: project_id)), "first"))
    _l_(704177)
    project = _a_(704182, _c_(704181, _a_(704179, _n_(704178, "projects_schema", lambda: projects_schema), "dump"), _n_(704180, "project", lambda: project)), "data")
    _l_(704183)
    aux = {'status': 'success', 'data': _n_(704184, "project", lambda: project)}, 200
    _l_(704185)
    return aux