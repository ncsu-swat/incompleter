# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60123122/typeerror-get-got-an-unexpected-keyword-argument-project-id-in-flask-applica
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import request
    _l_(698417)

except ImportError:
    pass
try:
    from flask_restful import Resource
    _l_(698419)

except ImportError:
    pass
try:
    from  Model import db, Project, ProjectSchema
    _l_(698421)

except ImportError:
    pass

projects_schema = _c_(698423, _n_(698422, "ProjectSchema", lambda: ProjectSchema), many=True)
_l_(698424)
project_schema = _c_(698426, _n_(698425, "ProjectSchema", lambda: ProjectSchema))
_l_(698427)

"""
Get project by id
"""
def get_by_id(project_id):
    _l_(698444)

    project = _c_(698434, _a_(698433, _c_(698432, _a_(698430, _a_(698429, _n_(698428, "Project", lambda: Project), "query"), "filter_by"), id=_n_(698431, "project_id", lambda: project_id)), "first"))
    _l_(698435)
    project = _a_(698440, _c_(698439, _a_(698437, _n_(698436, "projects_schema", lambda: projects_schema), "dump"), _n_(698438, "project", lambda: project)), "data")
    _l_(698441)
    aux = {'status': 'success', 'data': _n_(698442, "project", lambda: project)}, 200
    _l_(698443)
    return aux