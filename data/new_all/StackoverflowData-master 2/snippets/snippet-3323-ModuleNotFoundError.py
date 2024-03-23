#Source: https://stackoverflow.com/questions/75050989/python-pyqt5-attributeerror-type-object-qwidget-has-no-attribute-radiobutton
import time
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QColor
import requests
from random import randint as r
from datetime import datetime

class settings(QWidget):
    global stngs
    def __init__(self):
        super(settings, self).__init__()
        uic.loadUi("SettingsUI.ui", self)
        self.show()
        self.radioButton.clicked.connect(self.check)
        self.radioButton_2.clicked.connect(self.check)
        self.pushButton_2.clicked.connect(self.gotomain)
        self.fontsizeslider.valueChanged.connect(self.lcdNumber.display)

    def gotomain(self):
        global stngs
        global mn
        stngs = 0
        mn = 1
        self.close()
    
    def check(self):
        global white
        global black
        try:
            black
        except Exception:
            white = 1
            black = 0
        if black == 1:
            self.radioButton_2.nextCheckState()
        if self.radioButton.isChecked():
            white = 1
            black = 0
            return ("white")
        elif self.radioButton_2.isChecked():
            black = 1
            white = 0
            return ("black")

class MyGUI(QMainWindow):

    def __init__(self):
        global black
        global white
        global stngs
        stngs = 0
        super(MyGUI, self).__init__()
        uic.loadUi("ChatbotUI.ui", self)
        self.show()

        self.pushButton.clicked.connect(self.pressenter)
        self.actionClose.triggered.connect(exit)
        self.actionSettings1.triggered.connect(self.gotosettings)
            
    def gotosettings(self):
        global stngs
        stngs = 1
        self.close()

    def checkcolour():
        check = settings.check(settings)
        if check == "white":
            white()
        elif check == "black":
            black()
        else:
            raise ("Something wrong with background colour changing algorithm")

    checkcolour()

    def black(self):
        self.setStyleSheet("background-color: black;")
        self.pushButton.setStyleSheet("background-color : white;")
        self.lineEdit.setStyleSheet("color: white;")
        self.menubar.setStyleSheet("color: white;")
        self.textBrowser.setTextColor(QColor(255, 255, 255))
    def white(self):
        self.setStyleSheet("background-color: white;")
        self.pushButton.setStyleSheet("background-color : white;")
        self.lineEdit.setStyleSheet("color: black;")
        self.menubar.setStyleSheet("color: black;")
        self.textBrowser.setTextColor(QColor(0, 0, 0))

    def pressenter(self):
        userinput = self.lineEdit.text()
        response = self.get_response(userinput)
        self.textBrowser.setText(response)

    def get_response(self, userinput):
        global ait_ball_ans
        ait_ball_ans = [
            "Yes",
            "No",
            "Question unclear, ask later",
            "Maybe",
            "Obviously not",
            "Of course"
        ]

        #getting ip adress of user
        def get_ip():
            response = requests.get('https://api64.ipify.org?format=json').json()
            return response["ip"]

        #getting location info of user
        ip_address = get_ip()
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
            
        #weather api key and location info
        api_key = '14aaded169c4d6e2a5a2547d126b3f70'
        city = response.get("city") + ", " + response.get("country_code")
        qsi = userinput
        qs = qsi.lower().split()
        length = len(qs)

        if "what" in qs and ("name" in qs or "name?" in qs) and ("your" in qs or "ur" in qs) and (length == 3 or length == 4):
            print("My name is chatbot, and I am a language model trained by Zayan Arshad.")
            text = "My name is chatbot, and I am a language model trained by Zayan Arshad."
        elif ("chatbot" in qs or "chatbot?" in qs) and ("you" in qs and "are" in qs):
            print("Yes, my name is chatbot, a language model trained by Zayan Arshad.")
            text = "Yes, my name is chatbot, a language model trained by Zayan Arshad."
        elif "is" in qs and length == 4 and "chatbot" not in qs and "name" in qs:
            print("My name is chatbot, and I am a language model trained by Zayan Arshad.")
            text = "My name is chatbot, and I am a language model trained by Zayan Arshad."
        elif "should" and "you" and "what" and "call" in qs:
            print("My name is chatbot, and I am a language model trained by Zayan Arshad.")
            text = "My name is chatbot, and I am a language model trained by Zayan Arshad."
        elif ("hello" in qs or "hi" in qs) or ("good" and "evening") in qs or ("good" and "morning") in qs or ("good" and "afternoon") in qs:
            print("Hello! Is there any way I can help you?")
            text = "Hello! Is there any way I can help you?"
        elif ("weather" in qs or "weather?" in qs) and ("what" in qs or "pls" in qs or "tell" in qs or "what's" in qs or "whats" in qs):
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
            response = requests.get(url)
            data = response.json()
            conditions = data['weather'][0]['main']
            temperature = data['main']['temp']
            temperature_celsius = temperature - 273.15
            print("The weather condition is " + conditions + " and the temprature is " + str(temperature_celsius) + " in celcius.")
            text = "The weather condition is " + conditions + " and the temprature is " + str(temperature_celsius) + " in celcius."
        elif ("time" in qs or "time?" in qs) and ("what" in qs or "pls" in qs or "tell" in qs or "what's" in qs or "whats" in qs):
            print("The time is " + str(datetime.now().time()))
            text = "The time is " + str(datetime.now().time())
        elif ("give" in qs or "tell" in qs) and ("joke" in qs or "joke!" in qs):
            response = requests.get("https://sv443.net/jokeapi/v2/joke/Any")
            data = response.json()
            if 'setup' in data:
                setup = data['setup']
                delivery = data['delivery']
                print(setup + "\n" + delivery)
                text = setup + "\n" + delivery
            else:
                joke = data['joke']
                print(joke) 
        elif ("give" in qs or "tell" in qs) and "fact" in qs:
            response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
            data = response.json()
            fact = data['text']
            print("Your random fact is:\n" + fact)
            text = "Your random fact is:\n" + fact
        elif ("8" in qs or "eight" in qs) and ("ball" in qs or "ball," in qs):
            ans_num = r(1, 5)
            ans = ait_ball_ans[ans_num]
            print(ans)
            text = ans
        else:
            print("I'm sorry, but I am not advanced enough to answer your question or statement, a child has made me and my creator is a beginner to python and he has somehow made me. Feel free to ask me anything else or tell me something.")
            text = "I'm sorry, but I am not advanced enough to answer your question or statement, a child has made me and my creator is a beginner to python and he has somehow made me. Feel free to ask me anything else or tell me something."  
        return text

        
def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()

    if stngs == 1:
        settingsfunc()

def settingsfunc():
    time.sleep(1)
    app = QApplication([])
    settingswindow = settings()
    app.exec_()

    if mn == 1:
        main()

if __name__ == '__main__':
    main()