import pyttsx3
import os
import speech_recognition as sr
import webbrowser
import subprocess
import datetime
import smtplib

#defining the engine
engine=pyttsx3.init() 
voices=engine.getProperty('voices')

#voice ids
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice',voice_id)
engine.setProperty('rate', 180)
engine.runAndWait()


#speech funtion
def speak(text):
    engine.say(text)
    engine.runAndWait()
       
def command():
        r=sr.Recognizer()
        with sr.Microphone() as source:
           print("listening...")
           audio = r.listen(source)
        
        try:
            query=r.recognize_google(audio, language= 'en-in')
            
        except Exception as e:
            speak("Can you say that again? Please")
            query=None
        return query
            
""" def setup():
    speak("What would you like me to call you?")
    mastername = 
    return mastername 
 """
MASTER = "Shaan"



def Wakeup():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Goodmorning" + MASTER)
        
    elif hour>=12 and hour<15:
        speak("Good Afternoon" + MASTER)
        
    else:
        speak("Good Evening" + MASTER)

#ADDITIONAL STUFF
#system programs to open - enter your online url links and application path.
url={}

url_youtube='https://www.youtube.com/'
url_netflix='https://www.netflix.com/browse'
url_whatsapp='https://web.whatsapp.com/' #build dictionary to store


if __name__ ==  "__main__":
    
    Wakeup()
    while True:
        query=command().lower()
        if 'tell me about' in query.lower():
            query=query.replace("tell me about", "")
            results=wikipedia.summary(query, sentences = 2)
            speak(results)
        elif 'open youtube' in query.lower():
            webbrowser.open_new(url_youtube)
    
        
    


    
    
    

    