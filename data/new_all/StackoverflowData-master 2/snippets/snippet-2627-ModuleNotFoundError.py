#Source: https://stackoverflow.com/questions/68352395/attributeerror-super-object-has-no-attribute-getattr-in-python-and-kivy
from kivy.lang import Builder
from kivymd.app import MDApp  
import mysql.connector as ms
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen


acc = NumericProperty("")
pw = StringProperty("")

class safarApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'
        return
        
    def Login(self):
            self.acc = self.root.ids.acc_num.text
            
            self.pw = self.root.ids.password.text
            
            host = ms.connect(
              host="localhost",
              user="root",
              password="bhawarth20",
              database="safar"
              )
              
            cur = host.cursor(buffered = True)
            
            
            
            cur.execute("Select * from data where Account_Number = %s and Password = %s collate utf8mb4_bin", (self.acc, self.pw))
            data="error" #initially just assign the value
            
            for i in cur:
                data=i #if cursor has no data then loop will not run and value of data will be 'error'
                if data== "error":
                    print("User Does not exist")
                else:
                    print("User exist")

class LoginScreen(Screen):
    pass
    
    
class SignUpScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(LoginScreen(name= "login"))
sm.add_widget(SignUpScreen(name= "signup"))



                    
                    
if __name__ == '__main__':
    safarApp().run()