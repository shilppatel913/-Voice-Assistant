import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import webbrowser
import smtplib
engine = pyttsx3.init('sapi5')
engine.setProperty('rate',140)
voices=engine.getProperty('voices')
#two voices are available male and female
print(voices[0].id,voices[1].id)
print(voices[1].id)
voice_id="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voices',voice_id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour) #getting only the hour 
    if(hour>0 and hour<12):
        speak("good morning")
    elif(hour>12 and hour<18):
        speak("good afternoon")
    else:
        speak("good evening")
    speak("Shilp,how may i help you")

#function to create what you said into a string 
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold=1
        audio=r.listen(source) #source is voice from microphone
    try:
        print("recognizing...")
        query=r.recognize_google(audio,language="en-US") #converting into string
        print(f"User said {query}")
    except Exception as e:
        print(e)
        print("Say that again please")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your-email','your-password') #enter your gmail id and the corresponding password
    server.sendmail('your-email',to,content) 
    server.close()


if __name__ == '__main__':
    wishMe()
    query=takeCommand()
    if 'wikipedia' in query:
        speak("Searching wikipedia...")
        query=query.replace('wikipedia','') 
        results=wikipedia.summary(query,sentences=2)
        speak(results)
    
    elif 'open youtube' in query:
        webbrowser.open('youtube.com')
    elif 'open facebook' in query:
        webbrowser.open('facebook.com')
        
    elif 'play music' in query:
        music_path='D:\\songs'
        songs=os.listdir(music_path)
        os.startfile(os.path.join(music_path,songs[0]))

    elif 'open vscode' in query:
        code_path="C:\\Users\\Shilp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(code_path)

    elif 'send email' in query:
        try:
            to=""
            speak('To whom sir?')
            name=takeCommand()
            file=open("emailfile.txt","r")
            lines=file.readlines()
            for line in lines:
                if name in line:
                    to=line
                    break        
            content=takeCommand()
            sendEmail(to,content)
            speak('Email has been sent')
        except Exception as e:
            print(e)
            speak('Sorry could not send email')
    
    

