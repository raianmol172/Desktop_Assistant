import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import webbrowser
import pywhatkit
import sys
import smtplib
import subprocess
import wolframalpha


emails_dict = {'Boss': 'raianmol172@gmail.com',
               'Assistant': 'dummymail@gmail.com',
               'coco': 'abc2002@gmail.com',
               'sam': 'samdummy@gmail.com'
               }

print(" I am your Personal Assistant Alexa")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_Me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak('Good Morning !')

    elif 12 <= hour < 18:
        speak('Good Afternoon !')

    else:
        speak('Good Evening !')
    speak("I am Alexa, how may I help you")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
        print('Recognizing...')

    except Exception as e:
        speak("sorry I could not hear your voice")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('askankit123@gmail.com', 'type your password here')
    server.sendmail('askankit123@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wish_Me()
    while True:
        query = take_command().lower()
        if 'Alexa' in query:
            query = query.replace('Alexa', '')
            print(query)

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=1)
            speak('According to wikipedia..')
            print(results)
            speak(results)

        elif 'time' in query:
            times = datetime.datetime.now().strftime("%I:%M %p")
            print(f"the time is: {times}\n")
            speak(times)

        elif 'open google' in query:
            webbrowser.open("http://www.google.com")
            speak("google is open now")

        elif 'open chrome' in query:
            webbrowser.open("http://www.chrome.com")
            speak("chrome is open now")

        elif 'open github' in query:
            webbrowser.open("http://www.github.com")
            speak("github is open now")

        elif 'play' in query:
            song = query.replace('play', '')
            print(f"playing {song} on youtube")
            speak(f"playing {song} on youtube")
            pywhatkit.playonyt(song)

        elif 'search' in query:
            search = query.replace('search', '')
            speak(f"searching {search} on google")
            pywhatkit.search(search)

        elif 'what you can do' in query:
            speak('''I am a desktop assistant who can perform smaller task like play a song present in your directory,
              logging off your pc, searching things on wikipedia, sending an email, 
            playing a song on youtube, open chrome or stackoverflow or even chrome and much more ''')

        elif "who created you" in query:
            speak("I was built by Anmol RAI")
            print("I was built by Anmol RAI")

        elif "open stackoverflow" in query:
            webbrowser.open("https://stackoverflow.com")
            speak("Here is stackoverflow")

        elif 'open workbench' in query:
            path = "C:\Program Files\MySQL\MySQL Workbench 8.0\MySQLWorkbench.exe"
            os.startfile(path)

        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India')

        elif 'exit' in query:
            print("I am leaving now.")
            speak("I am leaving now...")
            sys.exit()

        elif 'open notepad' in query:
            try:
                os.startfile('notepad.exe')
            except Exception as e:
                str(e)

        elif 'send email to ' in query:
            try:
                speak("What should I say? ")
                content = take_command()
                if 'send email to boss' in query:
                    to = emails_dict['Boss']
                elif 'send email to assistant' in query:
                    to = emails_dict['Assistant']
                elif 'send email to coco' in query:
                    to = emails_dict['coco']
                elif 'send email to sam' in query:
                    to = emails_dict['sam']
                sendEmail(to, content)
                speak("email has been sent!")

            except Exception as e:
                print(e)
                speak("sorry, I could not able to send this email")

        elif 'question' in query:
            speak('what is your question')
            question = take_command()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            print(answer)
            speak(answer)

        elif 'music' in query:
            music_dir = "G:\songs1"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "log off" in query:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
            break