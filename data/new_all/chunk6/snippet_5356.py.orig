#Source: https://stackoverflow.com/questions/62407341/attributeerror-nonetype-object-has-no-attribute-lower-python3
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import jdatetime
import persian

Boss = 'Mohamaad'
print('Hello sir %s' % Boss)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak('Hello sir %s' % Boss)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.record(source,duration=2)
        speak('I am Listening sir')
        print("Listening ....")
        audio = r.listen(source)

    try :
         print("Recognizing...")
         query = r.recognize_google(audio, Language ='en-us')
         print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please")
        speak('Say that again please')
        query=None

    return query

wishMe()
query = takeCommand()



#Logic for executing tasks as per the query
if 'wikipedia' in query.lower():
    speak('searching in wikipedia....')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences =2)
    print(results)
    speak(results)

elif 'open youtube' in query.lower():
    url = 'youtube.com'
    chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
elif 'open Google' in query.lower():
    url = 'Google.com'
    chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application/chrome.exe %'
    webbrowser.get(chrome_path).open(url)
elif 'open github' in query.lower():
    url = 'github.com'
    chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application/chrome.exe %'
    webbrowser.get(chrome_path).open(url)
elif 'Play music' in query.lower():
    songs_dir = "C:\\Users\\mohmmad\\Downloads\\Music"
    songs = os.listdir(songs_dir)
    speak(songs)
    os.startfile(os.path.join(songs_dir,songs[0]))

elif 'time' in query():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{Boss} the time is {strTime}")