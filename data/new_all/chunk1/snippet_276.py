# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67764955/init-takes-1-positional-argument-but-2-were-given-type-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render, redirect, get_object_or_404
    _l_(415202)

except ImportError:
    pass
try:
    from django.http import HttpResponse
    _l_(415204)

except ImportError:
    pass
try:
    from .forms import AvonleaForm
    _l_(415206)

except ImportError:
    pass
try:
    from .models import AvonleaClass
    _l_(415208)

except ImportError:
    pass
try:
    from django.contrib import messages
    _l_(415210)

except ImportError:
    pass
try:
    from django.views import View
    _l_(415212)

except ImportError:
    pass


#Operational

def home(request):
    _l_(415217)

    aux = _c_(415215, _n_(415213, "render", lambda: render), _n_(415214, "request", lambda: request), 'meter_readings/home.html' )
    _l_(415216)
    return aux


# Complexes

#AVONLEA
#
#
#

class AvonleaView( _n_(415218, "View", lambda: View)):
    _l_(415304)


    def get(self,request):
        _l_(415262)

        created_nums= _c_(415224, _a_(415223, _c_(415222, _a_(415221, _a_(415220, _n_(415219, "AvonleaClass", lambda: AvonleaClass), "objects"), "all")), "values"), 'unitNumber')
        _l_(415225)

        Aprev = _c_(415231, _a_(415230, _c_(415229, _a_(415228, _a_(415227, _n_(415226, "AvonleaClass", lambda: AvonleaClass), "objects"), "all")), "order_by"), '-unitDateEntered')
        _l_(415232)
        previousReading = _a_(415234, _n_(415233, "Aprev", lambda: Aprev)[1], "newReading")
        _l_(415235)
        # created_nums= AvonleaClass.objects.all()
        _c_(415239, _n_(415236, "print", lambda: print), _n_(415237, "created_nums", lambda: created_nums) , _n_(415238, "previousReading", lambda: previousReading))
        _l_(415240)

        created_nums =[_c_(415243, _n_(415241, "int", lambda: int), _n_(415242, "i", lambda: i)['unitNumber']) for i in _n_(415244, "created_nums", lambda: created_nums)]
        _l_(415245)
        _c_(415249, _n_(415246, "print", lambda: print), _n_(415247, "created_nums", lambda: created_nums) , _n_(415248, "previousReading", lambda: previousReading))
        _l_(415250)

        form = _c_(415252, _n_(415251, "AvonleaForm", lambda: AvonleaForm))
        _l_(415253)
        aux = _c_(415260, _n_(415254, "render", lambda: render), _n_(415255, "request", lambda: request),"meter_readings/avonlea.html",{'form':_n_(415256, "form", lambda: form) , 'created_nums':_n_(415257, "created_nums", lambda: created_nums) , 'name':_n_(415258, "name", lambda: name), 'previousReading' : _n_(415259, "previousReading", lambda: previousReading) })
        _l_(415261)
        return aux

    def post(self,request):
        _l_(415303)

        created_nums= _c_(415268, _a_(415267, _c_(415266, _a_(415265, _a_(415264, _n_(415263, "AvonleaClass", lambda: AvonleaClass), "objects"), "all")), "values_list"), 'unitNumber')
        _l_(415269)
        _c_(415272, _n_(415270, "print", lambda: print), _n_(415271, "created_nums", lambda: created_nums))
        _l_(415273)
        form = _c_(415277, _n_(415274, "AvonleaForm", lambda: AvonleaForm), _a_(415276, _n_(415275, "request", lambda: request), "POST"))
        _l_(415278)
        if _c_(415281, _a_(415280, _n_(415279, "form", lambda: form), "is_valid")):
            _l_(415302)

            _c_(415284, _a_(415283, _n_(415282, "form", lambda: form), "save"))
            _l_(415285)
            aux = _c_(415288, _n_(415286, "redirect", lambda: redirect), 'unt-url' , _n_(415287, "name", lambda: name) )
            _l_(415289)
            return aux
            _c_(415293, _a_(415291, _n_(415290, "messages", lambda: messages), "success"), _n_(415292, "request", lambda: request) , 'creates successfully ')
            _l_(415294)
        else:
            aux = _c_(415300, _n_(415295, "render", lambda: render), _n_(415296, "request", lambda: request), 'meter_readings/avonlea.html', {'form': _n_(415297, "form", lambda: form) ,  _n_(415298, "created_nums", lambda: created_nums):_n_(415299, "created_nums", lambda: created_nums) })
            _l_(415301)
            return aux

def currentavonleas(request):
    _l_(415315)

    avonleas = _c_(415308, _a_(415307, _a_(415306, _n_(415305, "AvonleaClass", lambda: AvonleaClass), "objects"), "all"))
    _l_(415309)
    aux = _c_(415313, _n_(415310, "render", lambda: render), _n_(415311, "request", lambda: request), 'meter_readings/currentavonleas.html', {'avonleas':_n_(415312, "avonleas", lambda: avonleas)})
    _l_(415314)
    return aux

def viewavonlea(request,  avonleas_pk):
    _l_(415356)

    avonlea = _c_(415319, _n_(415316, "get_object_or_404", lambda: get_object_or_404), _n_(415317, "AvonleaClass", lambda: AvonleaClass), pk=_n_(415318, "avonleas_pk", lambda: avonleas_pk))
    _l_(415320)
    if _a_(415322, _n_(415321, "request", lambda: request), "method") == 'GET':
        _l_(415355)

        form = _c_(415325, _n_(415323, "AvonleaForm", lambda: AvonleaForm), instance=_n_(415324, "avonlea", lambda: avonlea))
        _l_(415326)
        aux = _c_(415331, _n_(415327, "render", lambda: render), _n_(415328, "request", lambda: request), 'meter_readings/viewavonleas.html', {'avonlea': _n_(415329, "avonlea", lambda: avonlea), 'form':_n_(415330, "form", lambda: form)})
        _l_(415332)
        return aux
    else:
        try:
            _l_(415354)

            form =  _c_(415337, _n_(415333, "AvonleaForm", lambda: AvonleaForm), _a_(415335, _n_(415334, "request", lambda: request), "POST"), instance=_n_(415336, "avonlea", lambda: avonlea))
            _l_(415338)
            _c_(415341, _a_(415340, _n_(415339, "form", lambda: form), "save"))
            _l_(415342)
            aux = _c_(415344, _n_(415343, "redirect", lambda: redirect), 'Avonlea')
            _l_(415345)
            return aux
        except _n_(415346, "ValueError", lambda: ValueError):
            _l_(415353)

            aux = _c_(415351, _n_(415347, "render", lambda: render), _n_(415348, "request", lambda: request), 'meter_readings/viewavonleas.html', {'avonlea': _n_(415349, "avonlea", lambda: avonlea), 'form':_n_(415350, "form", lambda: form), 'error':'Bad info'})
            _l_(415352)
            return aux

def deleteavonlea(request, avonleas_pk):
    _l_(415372)

    avonlea = _c_(415360, _n_(415357, "get_object_or_404", lambda: get_object_or_404), _n_(415358, "AvonleaClass", lambda: AvonleaClass), pk=_n_(415359, "avonleas_pk", lambda: avonleas_pk))
    _l_(415361)
    if _a_(415363, _n_(415362, "request", lambda: request), "method") == 'POST':
        _l_(415371)

        _c_(415366, _a_(415365, _n_(415364, "avonlea", lambda: avonlea), "delete"))
        _l_(415367)
        aux = _c_(415369, _n_(415368, "redirect", lambda: redirect), 'Avonlea')
        _l_(415370)
        return aux
try:
    import csv
    _l_(415374)

except ImportError:
    pass
def Avonleacsv(request):
    _l_(415406)

    data =_c_(415378, _a_(415377, _a_(415376, _n_(415375, "AvonleaClass", lambda: AvonleaClass), "objects"), "all"))
    _l_(415379)
    response = _c_(415381, _n_(415380, "HttpResponse", lambda: HttpResponse), content_type='text/csv')
    _l_(415382)
    _n_(415383, "response", lambda: response)['Content-Disposition'] = 'attachment; filename="saved_file.csv"'
    _l_(415384)
    writer = _c_(415388, _a_(415386, _n_(415385, "csv", lambda: csv), "writer"), _n_(415387, "response", lambda: response))
    _l_(415389)
    _c_(415392, _a_(415391, _n_(415390, "writer", lambda: writer), "writerow"), ['Unit', 'Number of Units'
                     ])
    _l_(415393)
    for avonleaclass in _n_(415394, "data", lambda: data):
        _l_(415403)

        _c_(415401, _a_(415396, _n_(415395, "writer", lambda: writer), "writerow"), [
                        _a_(415398, _n_(415397, "avonleaclass", lambda: avonleaclass), "unitNumber"),
                        _a_(415400, _n_(415399, "avonleaclass", lambda: avonleaclass), "newReading"),
                         ])
        _l_(415402)
    aux = _n_(415404, "response", lambda: response)
    _l_(415405)
    return aux