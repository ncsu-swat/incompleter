# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59848259/typeerror-int-object-is-not-iterable-serializer-django-serializer-for-one-to
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class SectorSerializer(_a_(421644, _n_(421643, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(421648)


    class Meta:
        _l_(421647)

        model = Sector
        _l_(421645)
        fields = '__all__'
        _l_(421646)


class TrailCompanySerializer(_a_(421650, _n_(421649, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(421657)

    sectors = _c_(421652, _n_(421651, "SectorSerializer", lambda: SectorSerializer), source="sector_id", many=True)
    _l_(421653)

    class Meta:
        _l_(421656)

        model = TrailCompany
        _l_(421654)
        fields = '__all__'
        _l_(421655)


class TrailSerializer(_a_(421659, _n_(421658, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(421666)

    companies = _c_(421661, _n_(421660, "TrailCompanySerializer", lambda: TrailCompanySerializer), source="company_id", many=True)
    _l_(421662)

    class Meta:
        _l_(421665)

        model = Trail
        _l_(421663)
        fields = '__all__'
        _l_(421664)