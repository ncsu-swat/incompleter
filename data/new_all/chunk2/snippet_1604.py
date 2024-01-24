# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72119681/attributeerror-could-not-locate-column-in-row-for-column-sa-instance-state-f
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(431812, _a_(431811, _n_(431810, "app", lambda: app), "route"), '/cotizaciones/crear/<int:id>', methods=("GET", "POST"))

@_n_(431813, "login_required", lambda: login_required)

def crearcotizacion(id):
    _l_(431914)

    
    
    datos_clientes = _c_(431841, _a_(431840, _c_(431839, _a_(431837, _c_(431836, _a_(431834, _c_(431833, _a_(431816, _a_(431815, _n_(431814, "db", lambda: db), "session"), "query"), _a_(431818, _n_(431817, "Clientes", lambda: Clientes), "id"), _a_(431820, _n_(431819, "Clientes", lambda: Clientes), "nombres"), _a_(431822, _n_(431821, "Clientes", lambda: Clientes), "apellidos"), _a_(431824, _n_(431823, "Clientes", lambda: Clientes), "empresa"), _a_(431826, _n_(431825, "Clientes", lambda: Clientes), "correo"), _a_(431828, _n_(431827, "Solicitud", lambda: Solicitud), "id"), _a_(431830, _n_(431829, "Solicitud", lambda: Solicitud), "servicio_campo"), _a_(431832, _n_(431831, "Solicitud", lambda: Solicitud), "asesore")), "join"), _n_(431835, "Solicitud", lambda: Solicitud)), "filter_by"), id=_n_(431838, "id", lambda: id)), "one"))
    _l_(431842)
    
    datos_solicitud = _c_(431853, _a_(431852, _c_(431851, _a_(431848, _c_(431847, _a_(431845, _a_(431844, _n_(431843, "db", lambda: db), "session"), "query"), _n_(431846, "Solicitud", lambda: Solicitud)), "filter_by"), id=_a_(431850, _n_(431849, "Solicitud", lambda: Solicitud), "id")), "first"))
    _l_(431854)
    
    form = _c_(431858, _n_(431855, "creacion_Cotizacion", lambda: creacion_Cotizacion), _a_(431857, _n_(431856, "request", lambda: request), "form"))
    _l_(431859)

    if _a_(431861, _n_(431860, "current_user", lambda: current_user), "role") == True:
        _l_(431900)

        
        if _a_(431863, _n_(431862, "request", lambda: request), "method") == 'POST':
            _l_(431896)


            cotizan = _c_(431873, _n_(431864, "Cotizacion", lambda: Cotizacion), numero_horas=_a_(431867, _a_(431866, _n_(431865, "form", lambda: form), "numero_horas"), "data"),
            descuento=_a_(431870, _a_(431869, _n_(431868, "form", lambda: form), "descuento"), "data"),
            clientes_cotizan = _n_(431871, "datos_clientes", lambda: datos_clientes),
            clientes_solicitan= _n_(431872, "datos_solicitud", lambda: datos_solicitud)
            
            )
            _l_(431874)
            
            _c_(431879, _a_(431877, _a_(431876, _n_(431875, "db", lambda: db), "session"), "add"), _n_(431878, "cotizan", lambda: cotizan))
            _l_(431880)
            _c_(431884, _a_(431883, _a_(431882, _n_(431881, "db", lambda: db), "session"), "commit"))
            _l_(431885)
            _c_(431887, _n_(431886, "flash", lambda: flash), 'La cotización ha sido creado exitosamente', 'success')
            _l_(431888)
            aux = _c_(431894, _n_(431889, "render_template", lambda: render_template), 'crearcotizacion.html', form=_n_(431890, "form", lambda: form), id=_n_(431891, "id", lambda: id), datos_solicitud=_n_(431892, "datos_solicitud", lambda: datos_solicitud), datos_clientes=_n_(431893, "datos_clientes", lambda: datos_clientes))
            _l_(431895)
            return aux
    else:
        _c_(431898, _n_(431897, "abort", lambda: abort), 401)
        _l_(431899)
    aux = _c_(431912, _n_(431901, "render_template", lambda: render_template), 'crearcotizacion.html', nombres=_a_(431903, _n_(431902, "current_user", lambda: current_user), "nombres"), correo=_a_(431905, _n_(431904, "current_user", lambda: current_user), "correo"), role=_a_(431907, _n_(431906, "current_user", lambda: current_user), "role"), id=_n_(431908, "id", lambda: id), form=_n_(431909, "form", lambda: form), datos_solicitud=_n_(431910, "datos_solicitud", lambda: datos_solicitud), datos_clientes=_n_(431911, "datos_clientes", lambda: datos_clientes))
    _l_(431913)

    return aux