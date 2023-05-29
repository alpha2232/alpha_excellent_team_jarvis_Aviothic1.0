import pyttsx3
import speech_recognition
import datetime
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")

    else:

        speak("good evening")

    speak("i am jarvis sir how may i can help you")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone(1) as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Reconizing..")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-pasword')
    server.sendmail('yourEmail@gmail.com',to,content)
    server.close()
wishMe()
while True:
    query=takeCommand().lower()
    if 'wikipedia' in query:
        speak(" searching wikipedia..")
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=2)
        speak("according to wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'open stackoverflow' in query:
        webbrowser.Open("stackoverflow.com")
    elif 'play music' in query:
        music_dir='D:\\Non Critical\\songs\\favourite songs2'
        songs=os.listdir(music_dir)
        print(songs)
        os.startflie(os.path.join(music_dir,songs[0]))
    elif 'the time' in query:
        strTime=datetime.datetime.now().strftime(("%H%M%S"))
        speak(f"sir the time is{strTime}")
    elif 'email to anurag' in query:
        try:
            speak("what should i say")
            content=takeCommand()
            to="anuragyourEmail@gmail.com"
            sendEmail(to,content)
            speak("email has been sent!")
        except Exception as e:
            print(e)
            speak("sorry my friend anurag bhi.I am not able to send the mail")


