import datetime
import os
import smtplib
import pyttsx3
import speech_recognition as sr
import cv2
from requests import get
import wikipedia
import webbrowser
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#speech to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 2
        audio = r.listen(source, timeout=1, phrase_time_limit=2)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")    # User query will be printed.

    except Exception as e:
         #print(e)
        print("Say that again please...")
        return "None"

    return query

#greetings
def wish():

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning")
        speak("Good Morning")

    elif hour>=12 and hour<18:
        print("Good Afternoon")
        speak("Good Afternoon")

    else:
        print("Good Evening")
        speak("Good Evening")

    print("I am Carlo.")
    print("Please tell me how may i help you.")
    speak("I am Carlo. Please tell me how may i help you")


#send email function
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('**********@gmail.com', 'password')
    server.sendmail('**********@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    print("Hello Sir")
    speak("Hello Sir")
    wish()
# infinte loop
    while True:
    #if 1:
        query = takecommand().lower()

        #logic for task!!!!

        if "open notepad" in query:
            print("opening notepad...")
            speak("opening notepad...")
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)

        elif "open chrome" in query:
            print("opening chrome...")
            speak("opening chrome...")
            ypath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(ypath)

        elif "open vs code" in query:
            print("opening vs code...")
            speak("opening vs code...")
            cpath = "C:\\Users\\Arpit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(cpath)

        elif "open command prompt" in query:
            print("opening command prompt...")
            speak("opening command prompt...")
            os.startfile("start cmd")

        elif "open camera" in query:
            print("opening camera...")
            speak("opening camera...")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            print("playing music...")
            speak("playing music...")
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            #rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            print(ip)
            speak(f"Your ip address is {ip}")


        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            print("opening youtube...")
            speak("opening youtube...")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            print("opening google...")
            speak("opening google...")
            speak("Sir what should i search")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open stackoverflow' in query:
            print("opening stackoverflow...")
            speak("opening stackoverflow...")
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")


        elif 'email to Utkarsh' in query:
            try:
                speak("What should I send?")
                content = takecommand().lower()
                to = "**************@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")

        elif "no thanks" in query:
            speak("Thank for using me sir, have a good day.")
            sys.exit()
        print("Sir, do you have any other work?")
        speak("Sir, do you have any other work?")
