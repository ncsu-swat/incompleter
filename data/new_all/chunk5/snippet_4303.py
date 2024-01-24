# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60123122/typeerror-get-got-an-unexpected-keyword-argument-project-id-in-flask-applica
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import request
    _l_(649918)

except ImportError:
    pass
try:
    from flask_restful import Resource
    _l_(649920)

except ImportError:
    pass
try:
    from  Model import db, Project, ProjectSchema
    _l_(649922)

except ImportError:
    pass

projects_schema = _c_(649924, _n_(649923, "ProjectSchema", lambda: ProjectSchema), many=True)
_l_(649925)
project_schema = _c_(649927, _n_(649926, "ProjectSchema", lambda: ProjectSchema))
_l_(649928)

"""
Get project by id
"""
def get_by_id(project_id):
    _l_(649945)

    project = _c_(649935, _a_(649934, _c_(649933, _a_(649931, _a_(649930, _n_(649929, "Project", lambda: Project), "query"), "filter_by"), id=_n_(649932, "project_id", lambda: project_id)), "first"))
    _l_(649936)
    project = _a_(649941, _c_(649940, _a_(649938, _n_(649937, "projects_schema", lambda: projects_schema), "dump"), _n_(649939, "project", lambda: project)), "data")
    _l_(649942)
    aux = {'status': 'success', 'data': _n_(649943, "project", lambda: project)}, 200
    _l_(649944)
    return aux