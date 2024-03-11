#Source: https://stackoverflow.com/questions/77323400/error-kivy-attributeerror-final-object-has-no-attribute-ganar-juego
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivymd.app import MDApp


class Final(Popup):

    def __init__(self, **kwargs):
        super().__init__()
        self.ganar_juego = kwargs["ganador"]
        print(self.ganar_juego)
        
    def on_kv_post(self, base_widget):
        #Selecciono si ha ganado o no
        self.ids.ganar.text = str(self.ganar_juego)