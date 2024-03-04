#Source: https://stackoverflow.com/questions/74895052/python-attributeerror-module-core-has-no-attribute-children
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineAvatarIconListItem, IconLeftWidget
from application.database.vaccination_calendar import get_children

Builder.load_file("layouts/children.kv")

class Children(Screen):
    pass