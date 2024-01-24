# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76009794/why-when-i-run-this-code-return-attributeerror-nonetype-object-has-no-attrib
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(602700)

except ImportError:
    pass
try:
    import numpy as np
    _l_(602702)

except ImportError:
    pass
try:
    import sys
    _l_(602704)

except ImportError:
    pass
try:
    import os
    _l_(602706)

except ImportError:
    pass
path = r'C:/Users/' +  _c_(602709, _a_(602708, _n_(602707, "os", lambda: os), "getlogin"))  +'/OneDrive - Falabella/Documentos - Desarrollo Logistico/Proyectos Desarrollo Interno/Proyectos Internos'
_l_(602710)
_c_(602715, _a_(602713, _a_(602712, _n_(602711, "sys", lambda: sys), "path"), "insert"), 0, _n_(602714, "path", lambda: path))
_l_(602716)
try:
    import PyPDF2
    _l_(602718)

except ImportError:
    pass
try:
    import tabula
    _l_(602720)

except ImportError:
    pass
try:
    import re
    _l_(602722)

except ImportError:
    pass
try:
    from openpyxl import Workbook
    _l_(602724)

except ImportError:
    pass
try:
    from openpyxl.utils.dataframe import dataframe_to_rows
    _l_(602726)

except ImportError:
    pass
try:
    import pdfplumber
    _l_(602728)

except ImportError:
    pass
#import EjecutarQuery as EQ 
#from datetime import datetime
#from datetime import timedelta
#import ToolsBI

#%%
#Leemos archivo excel de Base
path = r'C:/Users/'+  _c_(602731, _a_(602730, _n_(602729, "os", lambda: os), "getlogin"))  +'/OneDrive - Falabella/Documentos - Desarrollo Logistico/Proyectos Desarrollo Interno/Proyectos Internos/Confimación y Facturación Apple/Base proveedor/Base-prueba.xlsx'
_l_(602732)
detalle_base = _c_(602736, _a_(602734, _n_(602733, "pd", lambda: pd), "read_excel"), _n_(602735, "path", lambda: path), sheet_name="Base")
_l_(602737)
detalle_base = _c_(602740, _a_(602739, _n_(602738, "detalle_base", lambda: detalle_base), "reindex"), columns = ['Factura', 'New OC', 'PRODUCTO', 'NOMBRE', 'Units', 'CAJAS', 'SKU Falabella', 'Costo Unitario', 'Monto total', 'Diferencia Informada', 'Comentarios'])
_l_(602741)

def extract_pdf_data(file_names):
    _l_(602797)

    all_data = []
    _l_(602742)
    for file_name in _n_(602743, "file_names", lambda: file_names):
        _l_(602794)

        with _c_(602747, _a_(602745, _n_(602744, "pdfplumber", lambda: pdfplumber), "open"), _n_(602746, "file_name", lambda: file_name)) as pdf:
            _l_(602793)

            page = _a_(602749, _n_(602748, "pdf", lambda: pdf), "pages")[0]
            _l_(602750)
            text = _c_(602753, _a_(602752, _n_(602751, "page", lambda: page), "extract_text"))
            _l_(602754)
            numero_factura = _c_(602760, _a_(602759, _c_(602758, _a_(602756, _n_(602755, "re", lambda: re), "search"), r'N°\s*(d\+)', _n_(602757, "text", lambda: text)), "group"), 1)
            _l_(602761)
            cantidad = _c_(602767, _a_(602766, _c_(602765, _a_(602763, _n_(602762, "re", lambda: re), "search"), r'Cant.\s*(d\+)', _n_(602764, "text", lambda: text)), "group"), 1)
            _l_(602768)
            costo_unitario_fact = _c_(602774, _a_(602773, _c_(602772, _a_(602770, _n_(602769, "re", lambda: re), "search"), r'Valor unitario\s*(d\+)', _n_(602771, "text", lambda: text)), "group"), 1)
            _l_(602775)
            valor_total_fact = _c_(602781, _a_(602780, _c_(602779, _a_(602777, _n_(602776, "re", lambda: re), "search"), r'Valor\s*(d\+)', _n_(602778, "text", lambda: text)), "group"), 1)
            _l_(602782)
            data = [_n_(602783, "numero_factura", lambda: numero_factura), _n_(602784, "cantidad", lambda: cantidad), _n_(602785, "costo_unitario_fact", lambda: costo_unitario_fact), _n_(602786, "valor_total_fact", lambda: valor_total_fact)]
            _l_(602787)
            _c_(602791, _a_(602789, _n_(602788, "all_data", lambda: all_data), "append"), _n_(602790, "data", lambda: data))
            _l_(602792)
    aux = _n_(602795, "all_data", lambda: all_data)
    _l_(602796)
    return aux

def convert_pdfs_to_excel(directory, excel_file_name, excel_path):
    _l_(602830)

    file_names = [_c_(602803, _a_(602800, _a_(602799, _n_(602798, "os", lambda: os), "path"), "join"), _n_(602801, "directory", lambda: directory), _n_(602802, "f", lambda: f)) for f in _c_(602807, _a_(602805, _n_(602804, "os", lambda: os), "listdir"), _n_(602806, "directory", lambda: directory)) if _c_(602810, _a_(602809, _n_(602808, "f", lambda: f), "endswith"), '.pdf')]
    _l_(602811)
    all_data = _c_(602814, _n_(602812, "extract_pdf_data", lambda: extract_pdf_data), _n_(602813, "file_names", lambda: file_names))
    _l_(602815)
    flat_data = [_n_(602816, "item", lambda: item) for sublist in _n_(602817, "all_data", lambda: all_data) for item in _n_(602818, "sublist", lambda: sublist)]
    _l_(602819)
    df = _c_(602823, _a_(602821, _n_(602820, "pd", lambda: pd), "DataFrame"), _n_(602822, "flat_data", lambda: flat_data), columns=['Numero Factura', 'Cantidad', 'Costo Unitario', 'Valor Total'])
    _l_(602824)
    _c_(602828, _a_(602826, _n_(602825, "df", lambda: df), "to_excel"), _n_(602827, "excel_file_name", lambda: excel_file_name), index=False)
    _l_(602829)
_c_(602838, _n_(602831, "convert_pdfs_to_excel", lambda: convert_pdfs_to_excel), r'C:/Users/'+ _c_(602834, _a_(602833, _n_(602832, "os", lambda: os), "getlogin")) +'/OneDrive - Falabella/Documentos - Desarrollo Logistico/Proyectos Desarrollo Interno/Proyectos Internos/Confimación y Facturación Apple/Facturas Apple', 'datos.xlsx', 'C:/Users/'+ _c_(602837, _a_(602836, _n_(602835, "os", lambda: os), "getlogin")) +'/OneDrive - Falabella/Documentos - Desarrollo Logistico/Proyectos Desarrollo Interno/Proyectos Internos/Confimación y Facturación Apple')
_l_(602839)