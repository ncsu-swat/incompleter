# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72119681/attributeerror-could-not-locate-column-in-row-for-column-sa-instance-state-f
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Clientes(_a_(466732, _n_(466731, "db", lambda: db), "Model")):
    _l_(466807)

  
    __tablename__ = "clientes"
    _l_(466733)


    id = _c_(466736, _a_(466734, db, "Column"), _a_(466735, db, "Integer"), primary_key=True)
    _l_(466737)
    nombres = _c_(466741, _a_(466738, db, "Column"), _c_(466740, _a_(466739, db, "String"), 80), nullable=False)
    _l_(466742)
    apellidos = _c_(466746, _a_(466743, db, "Column"), _c_(466745, _a_(466744, db, "String"), 80), nullable=False)
    _l_(466747)
    correo = _c_(466751, _a_(466748, db, "Column"), _c_(466750, _a_(466749, db, "String"), 120), nullable=False)
    _l_(466752)
    empresa = _c_(466756, _a_(466753, db, "Column"), _c_(466755, _a_(466754, db, "String"), 120), nullable=False)
    _l_(466757)
    celular = _c_(466761, _a_(466758, db, "Column"), _c_(466760, _a_(466759, db, "String"), 50), nullable=False)
    _l_(466762)
    mensaje = _c_(466766, _a_(466763, db, "Column"), _c_(466765, _a_(466764, db, "String"), 500), nullable=False)
    _l_(466767)
    checkbox = _c_(466770, _a_(466768, db, "Column"), _a_(466769, db, "Boolean"), nullable=False)
    _l_(466771)
    cotizaciones = _c_(466773, _a_(466772, db, "relationship"), 'Cotizacion', backref='clientes_cotizan', lazy=True)
    _l_(466774)
    solicitudes = _c_(466776, _a_(466775, db, "relationship"), 'Solicitud', backref='sol_client', lazy=True)
    _l_(466777)

    
    

    def __init__(self, nombres, apellidos, correo, empresa, celular, mensaje, checkbox, sol_client):
        _l_(466802)

        
        _n_(466778, "self", lambda: self).nombres = _n_(466779, "nombres", lambda: nombres)
        _l_(466780)
        _n_(466781, "self", lambda: self).apellidos = _n_(466782, "apellidos", lambda: apellidos)
        _l_(466783)
        _n_(466784, "self", lambda: self).correo = _n_(466785, "correo", lambda: correo)
        _l_(466786)
        _n_(466787, "self", lambda: self).empresa = _n_(466788, "empresa", lambda: empresa)
        _l_(466789)
        _n_(466790, "self", lambda: self).celular = _n_(466791, "celular", lambda: celular)
        _l_(466792)
        _n_(466793, "self", lambda: self).mensaje = _n_(466794, "mensaje", lambda: mensaje)
        _l_(466795)
        _n_(466796, "self", lambda: self).checkbox = _n_(466797, "checkbox", lambda: checkbox)
        _l_(466798)
        _n_(466799, "self", lambda: self).sol_client = _n_(466800, "sol_client", lambda: sol_client)
        _l_(466801)
    

    def __repr__(self):
        _l_(466806)

        aux = '<Clientes %r>' % _a_(466804, _n_(466803, "self", lambda: self), "id")
        _l_(466805)
        return aux


class Solicitud(_a_(466809, _n_(466808, "db", lambda: db), "Model")):
    _l_(466844)

    __tablename__ = "solicitud"
    _l_(466810)

    id = _c_(466813, _a_(466811, db, "Column"), _a_(466812, db, "Integer"), primary_key=True)
    _l_(466814)
    
    servicio_campo = _c_(466818, _a_(466815, db, "Column"), _c_(466817, _a_(466816, db, "String"), 120), nullable=False)
    _l_(466819)
    asesore = _c_(466823, _a_(466820, db, "Column"), _c_(466822, _a_(466821, db, "String"), 120), nullable=False)
    _l_(466824)

     # LLAVE FORANEA
    solicitud_cliente = _c_(466829, _a_(466825, db, "Column"), _a_(466826, db, "Integer"), _c_(466828, _a_(466827, db, "ForeignKey"), "clientes.id"), nullable=True)
    _l_(466830)
    solicitudes_cliente = _c_(466832, _a_(466831, db, "relationship"), 'Cotizacion', backref='clientes_solicitan', lazy=True)
    _l_(466833)

    

    def __init__(self, servicio_campo, asesore, sol_client):
        _l_(466843)

       
        _n_(466834, "self", lambda: self).servicio_campo = _n_(466835, "servicio_campo", lambda: servicio_campo)
        _l_(466836)
        _n_(466837, "self", lambda: self).asesore = _n_(466838, "asesore", lambda: asesore)
        _l_(466839)
        _n_(466840, "self", lambda: self).sol_client = _n_(466841, "sol_client", lambda: sol_client)
        _l_(466842)



class Cotizacion(_a_(466846, _n_(466845, "db", lambda: db), "Model")):
    _l_(466889)

    __tablename__ = "cotizacion"
    _l_(466847)

    id = _c_(466850, _a_(466848, db, "Column"), _a_(466849, db, "Integer"), primary_key=True)
    _l_(466851)
   
    numero_horas = _c_(466854, _a_(466852, db, "Column"), _a_(466853, db, "Integer"), nullable=False)
    _l_(466855)
    
    descuento = _c_(466858, _a_(466856, db, "Column"), _a_(466857, db, "Integer"), nullable=False)
    _l_(466859)

    # LLAVE FORANEA
    cliente_id = _c_(466864, _a_(466860, db, "Column"), _a_(466861, db, "Integer"), _c_(466863, _a_(466862, db, "ForeignKey"), "clientes.id"), nullable=True)
    _l_(466865)
    solicitud_id = _c_(466870, _a_(466866, db, "Column"), _a_(466867, db, "Integer"), _c_(466869, _a_(466868, db, "ForeignKey"), "solicitud.id"), nullable=True)
    _l_(466871)
    

    def __init__(self, numero_horas, descuento, clientes_cotizan, clientes_solicitan):
        _l_(466884)

       
        _n_(466872, "self", lambda: self).numero_horas = _n_(466873, "numero_horas", lambda: numero_horas)
        _l_(466874)
        _n_(466875, "self", lambda: self).descuento = _n_(466876, "descuento", lambda: descuento)
        _l_(466877)
        _n_(466878, "self", lambda: self).clientes_cotizan = _n_(466879, "clientes_cotizan", lambda: clientes_cotizan)
        _l_(466880)
        _n_(466881, "self", lambda: self).clientes_solicitan = _n_(466882, "clientes_solicitan", lambda: clientes_solicitan)
        _l_(466883)
      
       

    def __repr__(self):
        _l_(466888)

        aux = '<Cotizacion %r>' % _a_(466886, _n_(466885, "self", lambda: self), "id")
        _l_(466887)
        return aux