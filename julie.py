import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
#import random


#from google.cloud import speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("good morning")

    elif hour>=12 and hour < 18:
        speak("good afternoon")

    else:
        speak("good evening")

    speak("I am julie mam Please tell me how may I help you?")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source,timeout=1,phrase_time_limit=5) 

    try:
        print("recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said : {query}")

    except Exception as e:
        #print(e)

        print("say that again please..")
        return  "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('arya.saxena230@gmail.com', 'Anya@1234')
    server.sendmail('arya.saxena230@gmail.com', to , content)
    server.close()

if __name__=="__main__":
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if "wikipedia" in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        #elif "play music" in query:
            #music_dir = ("directory location")
            #songs = os.listdir(music_dir)
            #rd = random.choice(songs)

            #if you want only mp3 files to get played then,
            #comment out randomn line 82 and code:
            #for song in songs:
            #if song.endswith('mp3'):
            #os.startfile(os.path.join(music_dir,rd))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'send email to arya' in query:
            try:
                speak("what should I say?")
                content = takeCommand().lower()
                to = "sarya2604@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry my friend I am unable to send this email")

            
        
    