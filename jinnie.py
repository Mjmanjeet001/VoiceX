import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning everyone")
    elif hour>=12 and hour<=18:
        speak("good afternoon everyone")
    else:
        speak("good evening everyone")
    speak("I am VoiceX . I am your friend "
          "Please tell me how can I help you"  
          )

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("listening to you.......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing your voice.....")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"Aaka said :{query}\n")

    except Exception as e :
        print("Aaka say that again please.......")
        return "none"
    return query

def sendEmail (to,content) :
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.ehlo()
    server.starttls()
    server.login('mjmanjeet001@gmail.com' , 'Manjeet@123')
    server.sendmail('mjmanjeet001@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia....')
            query = query.replace("wikipedia"," ")
            results = wikipedia.summary(query,sentences=3)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'open notepad' in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'tell the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Aaka, the time is{strTime}")

        elif 'open channel apna college ' in query:
            webbrowser.open("https://www.youtube.com/@ApnaCollegeOfficial")

        elif 'open Leetcode' in query:
            webbrowser.open("https://leetcode.com/")

        elif 'tell me about manas' in query:
            speak("manas is a gymmer but also a patla boy")

        elif 'tell me about harsh' in query:
            speak("harsh is most chutia person of third floor and farzi and sasta canadian")

        elif 'tell me about sumit' in query:
            speak("sumit is tall and good looking and as gorgeous as Mia Khalifa")

        elif 'tell me about arun' in query:
            speak("arun is a good guy and also a chutiya")

        elif 'tell me about kittu' in query:
            speak("kittu is a heavy person and look like a bouncer")

        elif 'tell me about satyam' in query:
            speak("satyam is a porn lover and looks like a bouncer")

        elif 'send email to sumit' in query:
            try:
                speak("what should I send in the mail")
                content = takecommand()
                to = "sumitpatel88922@gmail.com"
                sendEmail(to, content)
                speak("email has been send to sumit")
            except Exception as e:
                print(e)
                speak('sorry manjeet , I am not able to send the email as you need to enter password and email')
