# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55058939/typeerror-create-got-multiple-values-for-keyword-argument-user
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from rest_framework import serializers
    _l_(695593)

except ImportError:
    pass
try:
    from .models import Project, Module, Technology, Requirement
    _l_(695595)

except ImportError:
    pass
try:
    from tags.models import Tag
    _l_(695597)

except ImportError:
    pass
try:
    from accounts.models import User
    _l_(695599)

except ImportError:
    pass


class TagSerializer(_a_(695601, _n_(695600, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(695606)

    """Serializer for Project Tags"""

    class Meta:
        _l_(695605)

        model = _n_(695602, "Tag", lambda: Tag)
        _l_(695603)
        fields = ('title',)
        _l_(695604)


class RequirementSerializer(_a_(695608, _n_(695607, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(695613)

    """Serializer for Project requirements"""

    class Meta:
        _l_(695612)

        model = _n_(695609, "Requirement", lambda: Requirement)
        _l_(695610)
        fields = ('name',)
        _l_(695611)


class TechnologySerializer(_a_(695615, _n_(695614, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(695620)

    """Serializer for Project technologies"""

    class Meta:
        _l_(695619)

        model = _n_(695616, "Technology", lambda: Technology)
        _l_(695617)
        fields = ('name',)
        _l_(695618)


class ModuleSerializer(_a_(695622, _n_(695621, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(695630)

    """Serializer for Project Modules"""
    _c_(695624, _n_(695623, "print", lambda: print), "MODULES SERIALIZER")
    _l_(695625)

    class Meta:
        _l_(695629)

        model = _n_(695626, "Module", lambda: Module)
        _l_(695627)
        fields = ('name',)
        _l_(695628)


class ProjectSerializer(_a_(695632, _n_(695631, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(695719)

    """Serializer for Project"""
    modules = _c_(695634, _n_(695633, "ModuleSerializer", lambda: ModuleSerializer), many=True)
    _l_(695635)
    technologies = _c_(695637, _n_(695636, "TechnologySerializer", lambda: TechnologySerializer), many=True)
    _l_(695638)
    requirements = _c_(695640, _n_(695639, "RequirementSerializer", lambda: RequirementSerializer), many=True)
    _l_(695641)
    tags = _c_(695643, _n_(695642, "TagSerializer", lambda: TagSerializer), many=True)
    _l_(695644)

    class Meta:
        _l_(695648)

        model = _n_(695645, "Project", lambda: Project)
        _l_(695646)
        fields = [
            'id',
            'slug',
            'user',
            'title',
            'description',
            'price',
            'ratings',
            'modules',
            'technologies',
            'requirements',
            'tags'
            ]
        _l_(695647)

    def create(self, validated_data):
        _l_(695718)

        user = _n_(695649, "validated_data", lambda: validated_data)['user']
        _l_(695650)
        modules = _c_(695653, _a_(695652, _n_(695651, "validated_data", lambda: validated_data), "pop"), 'modules')
        _l_(695654)
        technologies = _c_(695657, _a_(695656, _n_(695655, "validated_data", lambda: validated_data), "pop"), 'technologies')
        _l_(695658)
        requirements = _c_(695661, _a_(695660, _n_(695659, "validated_data", lambda: validated_data), "pop"), 'requirements')
        _l_(695662)
        tags = _c_(695665, _a_(695664, _n_(695663, "validated_data", lambda: validated_data), "pop"), 'tags')
        _l_(695666)
        user_key = _c_(695671, _a_(695669, _a_(695668, _n_(695667, "User", lambda: User), "objects"), "filter"), id__iexact=_n_(695670, "user", lambda: user))
        _l_(695672)
        project = _c_(695678, _a_(695675, _a_(695674, _n_(695673, "Project", lambda: Project), "objects"), "create"), **_n_(695676, "validated_data", lambda: validated_data), user=_n_(695677, "user_key", lambda: user_key))
        _l_(695679)
        for module in _n_(695680, "modules", lambda: modules):
            _l_(695688)

            _c_(695686, _a_(695683, _a_(695682, _n_(695681, "Module", lambda: Module), "objects"), "create"), **_n_(695684, "module", lambda: module), project=_n_(695685, "project", lambda: project))
            _l_(695687)
        for technology in _n_(695689, "technologies", lambda: technologies):
            _l_(695697)

            _c_(695695, _a_(695692, _a_(695691, _n_(695690, "Technology", lambda: Technology), "objects"), "create"), **_n_(695693, "technology", lambda: technology), project=_n_(695694, "project", lambda: project))
            _l_(695696)
        for requirement in _n_(695698, "requirements", lambda: requirements):
            _l_(695706)

            _c_(695704, _a_(695701, _a_(695700, _n_(695699, "Requirement", lambda: Requirement), "objects"), "create"), **_n_(695702, "requirement", lambda: requirement), project=_n_(695703, "project", lambda: project))
            _l_(695705)
        for tag in _n_(695707, "tags", lambda: tags):
            _l_(695715)

            _c_(695713, _a_(695710, _a_(695709, _n_(695708, "Tag", lambda: Tag), "objects"), "create"), **_n_(695711, "tag", lambda: tag), project=_n_(695712, "project", lambda: project))
            _l_(695714)
        aux = _n_(695716, "project", lambda: project)
        _l_(695717)

        return aux