#Source: https://stackoverflow.com/questions/74895052/python-attributeerror-module-core-has-no-attribute-children
from kivymd.app import MDApp

from core.screen_manager import WindowManager


class VaccinationCalendarApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        return WindowManager()


if __name__ == "__main__":
    VaccinationCalendarApp().run()