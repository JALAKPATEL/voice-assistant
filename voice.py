import pyttsx3 # for convert text to speech
import speech_recognition as sr
import webbrowser 
import datetime
import pyjokes
import os
import time

recognizer=sr.Recognizer()
# speech to text
def sptext():
    while True:
          
        with sr.Microphone() as source:
                print("Listening...")
                #  remove noice
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)  # listen audio
                try:
                        print("recognizing ...")
                        data = recognizer.recognize_google(audio)
                        print(data)
                        return data
                except sr.UnknownValueError:
                        print("not understand") 
        # sptext()            
# text to speech
def speechtx(x):
     engin = pyttsx3.init()
     voices = engin.getProperty('voices')
     engin.setProperty('voice',voices[0].id) # for 0 male , 1 female
     rate = engin.getProperty('rate')
     engin.setProperty('rate',150) # for speed
     engin.say(x)
     engin.runAndWait()
#   speechtx("hello welcome to the world")      

if __name__ ==  '__main__':
      if "hey bro" in  sptext().lower(): # first speak name of assistant
        while True:
                data1=sptext().lower()
                if "your name" in data1:
                        name = "my name is DELL G3"
                        speechtx(name)
                elif 'time' in data1:
                        time = datetime.datetime.now().strftime("%I%M%p")
                        speechtx(time)
                elif 'youtube' in data1:
                        webbrowser.open("https://www.youtube.com/") 
                elif 'chatgpt' in data1:
                        webbrowser.open("https://chatgpt.com/")
                elif 'whatsapp' in data1:
                        webbrowser.open("https://web.whatsapp.com/")        
                elif 'joke' in data1:
                        joke_1 = pyjokes.get_joke(language="en" ,category="neutral")
                        print(joke_1)
                        speechtx(joke_1)
                elif 'play song' in data1:
                        add = "E:\Music"
                        listsong = os.listdir(add)
                        print(listsong)
                        os.startfile(os.path.join(add,listsong[0]))
                elif "exit" in data1:
                    speechtx("thank you")
                    break

                time.sleep(2)

                
      else:  
        print("wrong name")

