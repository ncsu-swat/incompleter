# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71928720/attributeerror-imagecard-object-has-no-attribute-source
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivymd.uix.dialog import MDDialog
    _l_(588268)

except ImportError:
    pass
try:
    from kivymd.uix.button import MDFlatButton
    _l_(588270)

except ImportError:
    pass
try:
    from kivy.properties import ListProperty
    _l_(588272)

except ImportError:
    pass
try:
    from kivy.properties import StringProperty
    _l_(588274)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import Screen
    _l_(588276)

except ImportError:
    pass
try:
    from kivymd.uix.card import MDCard
    _l_(588278)

except ImportError:
    pass
try:
    from kivy.uix.boxlayout import BoxLayout
    _l_(588280)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(588282)

except ImportError:
    pass
try:
    from config import config
    _l_(588284)

except ImportError:
    pass
try:
    import pyrebase
    _l_(588286)

except ImportError:
    pass


_c_(588289, _a_(588288, _n_(588287, "Builder", lambda: Builder), "load_string"), """
<ImageCard@MDCard>
    id: ec

    size_hint: ('180dp', None)
    ripple_behavior: True
    image:''
    text:''

    orientation:'vertical'

    FitImage:
        pos_hint: {'center_x': .5, 'center_y': .25} 
        source: './images/user.png' # root.source
        size_hint: None, None
        width: dp(150) 
        height: dp(150) 
        #radius: [99, 99, 99, 99]

    MDBoxLayout:
        orientation:'horizontal'
        MDLabel:
            text:root.text
            halign:"center"
            #bold: True

    MDFlatButton:
        text: "New Screen Here"
        increment_width: "164dp"

        on_release: root.show_confirmation_dialog()

<ScreenRecycleView>:
    name: 'recycle_view' 

    FloatLayout:

        MDTextField:
            id: pesquisa

            helper_text: "Escreva um trecho da pesquisa e clique em pesquisar."
            helper_text_mode: "on_focus"
            size_hint: .99, None
            halign: 'center' 
            multiline: False 


            hint_text: 'Digite o que procura'
            text_validate_unfocus: False
            pos_hint: {'center_x': 0.42, 'center_y': 0.84}
            padding: dp(15)        
            #size_hint_x: .75
            #on_text: root.on_kv_post(self, self.text)

        MDIconButton:
            icon: "magnify"
            pos_hint: {"center_x": .95, "center_y": 0.84}
            on_release: root.on_kv_post(self, pesquisa.text)            
        

        #:import get_color_from_hex kivy.utils.get_color_from_hex        
        MDBoxLayout:
            
            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
            RecycleView:
                data: root.image_data
                viewclass: "ImageCard"
                RecycleGridLayout:
                    cols: 2
                    default_size: dp(155), dp(200)
     
                    padding: dp(5) # Determina o espaçamento entre um widget e outro pelos lados               
                    spacing: dp(5) # Determina o espaçamento entre um widget e outro de cima para baixo
                    default_size_hint: 1, None ##### Define a largura do widget sempre próximo as bordas
                    size_hint_y: None ##### Associado a default_size_hint
                    height: self.minimum_height
                    #ripple_behavior: True""")    
_l_(588290)    

class Content(_n_(588291, "BoxLayout", lambda: BoxLayout)):
    _l_(588293)

    pass
    _l_(588292)

class ImageCard(_n_(588294, "MDCard", lambda: MDCard)):
    _l_(588327)

    dialog = None
    _l_(588295)
    text = _c_(588297, _n_(588296, "StringProperty", lambda: StringProperty))
    _l_(588298)
    source = _c_(588300, _n_(588299, "StringProperty", lambda: StringProperty))
    _l_(588301)

    def show_confirmation_dialog(self):
        _l_(588326)

        if not _a_(588303, _n_(588302, "self", lambda: self), "dialog"):
            _l_(588320)

            _n_(588304, "self", lambda: self).dialog = _c_(588318, _n_(588305, "MDDialog", lambda: MDDialog), type="custom",
                content_cls=_c_(588307, _n_(588306, "Content", lambda: Content)),
                buttons=[
                    _c_(588312, _n_(588308, "MDFlatButton", lambda: MDFlatButton), text="CANCEL",
                        theme_text_color="Custom",
                        text_color=_a_(588311, _a_(588310, _n_(588309, "self", lambda: self), "theme_cls"), "primary_color"),
                    ),
                    _c_(588317, _n_(588313, "MDFlatButton", lambda: MDFlatButton), text="OK",
                        theme_text_color="Custom",
                        text_color=_a_(588316, _a_(588315, _n_(588314, "self", lambda: self), "theme_cls"), "primary_color"),
                    ),
                ],
            )
            _l_(588319)
        _c_(588324, _a_(588323, _a_(588322, _n_(588321, "self", lambda: self), "dialog"), "open"))
        _l_(588325)

class ScreenRecycleView(_n_(588328, "Screen", lambda: Screen)):
    _l_(588390)

    image_data = _c_(588330, _n_(588329, "ListProperty", lambda: ListProperty))
    _l_(588331)

    def on_kv_post(self, base_widget, text="", search=False):
        _l_(588389)

        
        # Inicializando o banco de dados.
        _n_(588332, "self", lambda: self).firebase = _c_(588336, _a_(588334, _n_(588333, "pyrebase", lambda: pyrebase), "initialize_app"), _n_(588335, "config", lambda: config))
        _l_(588337)
        _n_(588338, "self", lambda: self).db = _c_(588342, _a_(588341, _a_(588340, _n_(588339, "self", lambda: self), "firebase"), "database"))
        _l_(588343)

        _n_(588344, "self", lambda: self).produtos = _c_(588350, _a_(588349, _c_(588348, _a_(588347, _a_(588346, _n_(588345, "self", lambda: self), "db"), "child"), "Produtos"), "get"), token='**************************************')
        _l_(588351)
        
        #self.ids.rv3.data = []
        _n_(588352, "self", lambda: self).image_data = []
        _l_(588353)
        
        for produto in _c_(588357, _a_(588356, _a_(588355, _n_(588354, "self", lambda: self), "produtos"), "each")):
            _l_(588388)

            if _c_(588360, _a_(588359, _n_(588358, "text", lambda: text), "upper")) in _c_(588363, _a_(588362, _n_(588361, "produto", lambda: produto), "val"))['nmproduto']:
                _l_(588387)

                if _c_(588366, _a_(588365, _n_(588364, "produto", lambda: produto), "val"))['url'] != 'SemUrl':
                    _l_(588386)

                    _c_(588376, _a_(588369, _a_(588368, _n_(588367, "self", lambda: self), "image_data"), "append"), {"source": _c_(588372, _a_(588371, _n_(588370, "produto", lambda: produto), "val"))['url'],
                        "text": _c_(588375, _a_(588374, _n_(588373, "produto", lambda: produto), "val"))['nmproduto']
                        }
                    )
                    _l_(588377)
                else:
                    _c_(588384, _a_(588380, _a_(588379, _n_(588378, "self", lambda: self), "image_data"), "append"), {"source": './images/sem_imagem.png',
                        "text": _c_(588383, _a_(588382, _n_(588381, "produto", lambda: produto), "val"))['nmproduto']
                        }
                    ) 
                    _l_(588385) 