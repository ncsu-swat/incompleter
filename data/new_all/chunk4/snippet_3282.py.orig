#Source: https://stackoverflow.com/questions/76207404/kivy-python3-attributeerror-super-object-has-no-attribute-getattr
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
class Datatable(MDDataTable):
    column_data = [('col1',dp(30)),('col2',dp(30)),('col3',dp(30)),]
    row_data = [('data1'),('data2'),('data3')]
class app(MDApp):
    def build(self):
        return Builder.load_file('lab.kv')
app().run() 