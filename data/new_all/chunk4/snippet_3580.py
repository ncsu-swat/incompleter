# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71928720/attributeerror-imagecard-object-has-no-attribute-source
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivymd.uix.dialog import MDDialog
    _l_(587512)

except ImportError:
    pass
try:
    from kivymd.uix.button import MDFlatButton
    _l_(587514)

except ImportError:
    pass
try:
    from kivy.properties import ListProperty
    _l_(587516)

except ImportError:
    pass
try:
    from kivy.properties import StringProperty
    _l_(587518)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import Screen
    _l_(587520)

except ImportError:
    pass
try:
    from kivymd.uix.card import MDCard
    _l_(587522)

except ImportError:
    pass
try:
    from kivy.uix.boxlayout import BoxLayout
    _l_(587524)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(587526)

except ImportError:
    pass
try:
    from config import config
    _l_(587528)

except ImportError:
    pass
try:
    import pyrebase
    _l_(587530)

except ImportError:
    pass


_c_(587533, _a_(587532, _n_(587531, "Builder", lambda: Builder), "load_string"), """
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
_l_(587534)    

class Content(_n_(587535, "BoxLayout", lambda: BoxLayout)):
    _l_(587537)

    pass
    _l_(587536)

class ImageCard(_n_(587538, "MDCard", lambda: MDCard)):
    _l_(587571)

    dialog = None
    _l_(587539)
    text = _c_(587541, _n_(587540, "StringProperty", lambda: StringProperty))
    _l_(587542)
    source = _c_(587544, _n_(587543, "StringProperty", lambda: StringProperty))
    _l_(587545)

    def show_confirmation_dialog(self):
        _l_(587570)

        if not _a_(587547, _n_(587546, "self", lambda: self), "dialog"):
            _l_(587564)

            _n_(587548, "self", lambda: self).dialog = _c_(587562, _n_(587549, "MDDialog", lambda: MDDialog), type="custom",
                content_cls=_c_(587551, _n_(587550, "Content", lambda: Content)),
                buttons=[
                    _c_(587556, _n_(587552, "MDFlatButton", lambda: MDFlatButton), text="CANCEL",
                        theme_text_color="Custom",
                        text_color=_a_(587555, _a_(587554, _n_(587553, "self", lambda: self), "theme_cls"), "primary_color"),
                    ),
                    _c_(587561, _n_(587557, "MDFlatButton", lambda: MDFlatButton), text="OK",
                        theme_text_color="Custom",
                        text_color=_a_(587560, _a_(587559, _n_(587558, "self", lambda: self), "theme_cls"), "primary_color"),
                    ),
                ],
            )
            _l_(587563)
        _c_(587568, _a_(587567, _a_(587566, _n_(587565, "self", lambda: self), "dialog"), "open"))
        _l_(587569)

class ScreenRecycleView(_n_(587572, "Screen", lambda: Screen)):
    _l_(587634)

    image_data = _c_(587574, _n_(587573, "ListProperty", lambda: ListProperty))
    _l_(587575)

    def on_kv_post(self, base_widget, text="", search=False):
        _l_(587633)

        
        # Inicializando o banco de dados.
        _n_(587576, "self", lambda: self).firebase = _c_(587580, _a_(587578, _n_(587577, "pyrebase", lambda: pyrebase), "initialize_app"), _n_(587579, "config", lambda: config))
        _l_(587581)
        _n_(587582, "self", lambda: self).db = _c_(587586, _a_(587585, _a_(587584, _n_(587583, "self", lambda: self), "firebase"), "database"))
        _l_(587587)

        _n_(587588, "self", lambda: self).produtos = _c_(587594, _a_(587593, _c_(587592, _a_(587591, _a_(587590, _n_(587589, "self", lambda: self), "db"), "child"), "Produtos"), "get"), token='**************************************')
        _l_(587595)
        
        #self.ids.rv3.data = []
        _n_(587596, "self", lambda: self).image_data = []
        _l_(587597)
        
        for produto in _c_(587601, _a_(587600, _a_(587599, _n_(587598, "self", lambda: self), "produtos"), "each")):
            _l_(587632)

            if _c_(587604, _a_(587603, _n_(587602, "text", lambda: text), "upper")) in _c_(587607, _a_(587606, _n_(587605, "produto", lambda: produto), "val"))['nmproduto']:
                _l_(587631)

                if _c_(587610, _a_(587609, _n_(587608, "produto", lambda: produto), "val"))['url'] != 'SemUrl':
                    _l_(587630)

                    _c_(587620, _a_(587613, _a_(587612, _n_(587611, "self", lambda: self), "image_data"), "append"), {"source": _c_(587616, _a_(587615, _n_(587614, "produto", lambda: produto), "val"))['url'],
                        "text": _c_(587619, _a_(587618, _n_(587617, "produto", lambda: produto), "val"))['nmproduto']
                        }
                    )
                    _l_(587621)
                else:
                    _c_(587628, _a_(587624, _a_(587623, _n_(587622, "self", lambda: self), "image_data"), "append"), {"source": './images/sem_imagem.png',
                        "text": _c_(587627, _a_(587626, _n_(587625, "produto", lambda: produto), "val"))['nmproduto']
                        }
                    ) 
                    _l_(587629) 