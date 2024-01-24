# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43055952/typeerror-modelbase-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.http import HttpResponse, JsonResponse
    _l_(424167)

except ImportError:
    pass
try:
    from django.views.decorators.csrf import csrf_exempt
    _l_(424169)

except ImportError:
    pass
try:
    from rest_framework.renderers import JSONRenderer
    _l_(424171)

except ImportError:
    pass
try:
    from rest_framework.parsers import JSONParser
    _l_(424173)

except ImportError:
    pass
try:
    from offense_api.models import Episode, Season, Character
    _l_(424175)

except ImportError:
    pass
try:
    from offense_api.serializers import EpisodeSerializer, SeasonSerializer, CharacterSerializer
    _l_(424177)

except ImportError:
    pass


@_n_(424178, "csrf_exempt", lambda: csrf_exempt)
def season_list(request):
    _l_(424227)

    """
    List all seasons, or create a new one.
    :param request: 
    :return: 
    """
    if _a_(424180, _n_(424179, "request", lambda: request), "method") == 'GET':
        _l_(424226)

        seasons = _c_(424184, _a_(424183, _a_(424182, _n_(424181, "Season", lambda: Season), "objects"), "all"))
        _l_(424185)
        serializer = _c_(424188, _n_(424186, "SeasonSerializer", lambda: SeasonSerializer), _n_(424187, "seasons", lambda: seasons), many=True)
        _l_(424189)
        aux = _c_(424193, _n_(424190, "JsonResponse", lambda: JsonResponse), _a_(424192, _n_(424191, "serializer", lambda: serializer), "data"), safe=False)
        _l_(424194)
        return aux

    elif _a_(424196, _n_(424195, "request", lambda: request), "method") == 'POST':
        _l_(424225)

        data = _c_(424201, _a_(424199, _c_(424198, _n_(424197, "JSONParser", lambda: JSONParser)), "parse"), _n_(424200, "request", lambda: request))
        _l_(424202)
        serializer = _c_(424205, _n_(424203, "SeasonSerializer", lambda: SeasonSerializer), data=_n_(424204, "data", lambda: data))
        _l_(424206)
        if _c_(424209, _a_(424208, _n_(424207, "serializer", lambda: serializer), "is_valid")):
            _l_(424219)

            _c_(424212, _a_(424211, _n_(424210, "serializer", lambda: serializer), "save"))
            _l_(424213)
            aux = _c_(424217, _n_(424214, "JsonResponse", lambda: JsonResponse), _a_(424216, _n_(424215, "serializer", lambda: serializer), "data"), status=201)
            _l_(424218)
            return aux
        aux = _c_(424223, _n_(424220, "JsonResponse", lambda: JsonResponse), _a_(424222, _n_(424221, "serializer", lambda: serializer), "errors"), status=400)
        _l_(424224)
        return aux


@_n_(424228, "csrf_exempt", lambda: csrf_exempt)
def season_detail(request, pk):
    _l_(424296)

    """
    Retrieve, update, or delete a season.
    :param request: 
    :param pk: 
    :return: 
    """
    try:
        _l_(424241)

        season = _c_(424233, _a_(424231, _a_(424230, _n_(424229, "Season", lambda: Season), "objects"), "get"), pk=_n_(424232, "pk", lambda: pk))
        _l_(424234)
    except _a_(424236, _n_(424235, "Season", lambda: Season), "DoesNotExist"):
        _l_(424240)

        aux = _c_(424238, _n_(424237, "HttpResponse", lambda: HttpResponse), status=404)
        _l_(424239)
        return aux

    if _a_(424243, _n_(424242, "request", lambda: request), "method") == 'GET':
        _l_(424295)

        serializer = _c_(424246, _n_(424244, "SeasonSerializer", lambda: SeasonSerializer), _n_(424245, "season", lambda: season))
        _l_(424247)
        aux = _c_(424251, _n_(424248, "JsonResponse", lambda: JsonResponse), _a_(424250, _n_(424249, "serializer", lambda: serializer), "data"))
        _l_(424252)
        return aux

    elif _a_(424254, _n_(424253, "request", lambda: request), "method") == 'PUT':
        _l_(424294)

        data = _c_(424259, _a_(424257, _c_(424256, _n_(424255, "JSONParser", lambda: JSONParser)), "parse"), _n_(424258, "request", lambda: request))
        _l_(424260)
        serializer = _c_(424264, _n_(424261, "SeasonSerializer", lambda: SeasonSerializer), _n_(424262, "season", lambda: season), data=_n_(424263, "data", lambda: data))
        _l_(424265)
        if _c_(424268, _a_(424267, _n_(424266, "serializer", lambda: serializer), "is_valid")):
            _l_(424278)

            _c_(424271, _a_(424270, _n_(424269, "serializer", lambda: serializer), "save"))
            _l_(424272)
            aux = _c_(424276, _n_(424273, "JsonResponse", lambda: JsonResponse), _a_(424275, _n_(424274, "serializer", lambda: serializer), "data"))
            _l_(424277)
            return aux
        aux = _c_(424282, _n_(424279, "JsonResponse", lambda: JsonResponse), _a_(424281, _n_(424280, "serializer", lambda: serializer), "errors"), status=400)
        _l_(424283)
        return aux

    elif _a_(424285, _n_(424284, "request", lambda: request), "method") == 'DELETE':
        _l_(424293)

        _c_(424288, _a_(424287, _n_(424286, "season", lambda: season), "delete"))
        _l_(424289)
        aux = _c_(424291, _n_(424290, "HttpResponse", lambda: HttpResponse), status=204)
        _l_(424292)
        return aux


@_n_(424297, "csrf_exempt", lambda: csrf_exempt)
def character_list(request):
    _l_(424346)

    """
        List all characters, or create a new one.
        :param request: 
        :return: 
        """
    if _a_(424299, _n_(424298, "request", lambda: request), "method") == 'GET':
        _l_(424345)

        characters = _c_(424303, _a_(424302, _a_(424301, _n_(424300, "Character", lambda: Character), "objects"), "all"))
        _l_(424304)
        serializer = _c_(424307, _n_(424305, "CharacterSerializer", lambda: CharacterSerializer), _n_(424306, "Character", lambda: Character), many=True)
        _l_(424308)
        aux = _c_(424312, _n_(424309, "JsonResponse", lambda: JsonResponse), _a_(424311, _n_(424310, "serializer", lambda: serializer), "data"), safe=False)
        _l_(424313)
        return aux

    elif _a_(424315, _n_(424314, "request", lambda: request), "method") == 'POST':
        _l_(424344)

        data = _c_(424320, _a_(424318, _c_(424317, _n_(424316, "JSONParser", lambda: JSONParser)), "parse"), _n_(424319, "request", lambda: request))
        _l_(424321)
        serializer = _c_(424324, _n_(424322, "CharacterSerializer", lambda: CharacterSerializer), data=_n_(424323, "data", lambda: data))
        _l_(424325)
        if _c_(424328, _a_(424327, _n_(424326, "serializer", lambda: serializer), "is_valid")):
            _l_(424338)

            _c_(424331, _a_(424330, _n_(424329, "serializer", lambda: serializer), "save"))
            _l_(424332)
            aux = _c_(424336, _n_(424333, "JsonResponse", lambda: JsonResponse), _a_(424335, _n_(424334, "serializer", lambda: serializer), "data"), status=201)
            _l_(424337)
            return aux
        aux = _c_(424342, _n_(424339, "JsonResponse", lambda: JsonResponse), _a_(424341, _n_(424340, "serializer", lambda: serializer), "errors"), status=400)
        _l_(424343)
        return aux