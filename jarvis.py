import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import random
import os
import smtplib



'''
    sapi5 is microsoft speach api
'''
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id) 
engine.setProperty('voice', voices[1].id)


#////////////////////////// SPEAK /////////////////////////////
def speak(audio):
    '''
    Speakes what ever the strings is give to it
    '''
    engine.say(audio)
    engine.runAndWait()
#////////////////////////// WISH ME /////////////////////////////
def wishMe():
    '''
    Whises the user
    '''
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning")
    elif hour >=12 and hour <= 17:
        speak("Good Afternoon")
    else :
        speak("Good Evening")
    
    speak("I am jarvis, How may i help you sir")


#////////////////////////// TAKE COMMAND /////////////////////////////
def takeCommand():
    '''
    it takes microphone input and convert to string .
    '''
    r=sr.Recognizer()
    # mic= sr.Microphone(device_index=0)
    with sr.Microphone() as source:
        print("\nListening........")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=3)
        print(".....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("\nRecognizing......\n")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said :{query}\n") 
    
    except Exception as e:
        # print(e)
        print("Say that again Please")
        return "None"   
    
    return query


def sendmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('kjcoemr522@gmail.com','kjcollege522')
    server.sendmail('kjcoemr522@gmail.com',to , content)
    server.close()




if __name__ == "__main__":
    # speak("Hello quresh lakdawala")
    wishMe()
    while True:
        query = takeCommand().lower()
        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching in wikipedia...')
            print(query)
            query = query.replace("wikipedia", " ")
            print(query)
            result = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(result)
            speak(result)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open website' in query:
            speak('sir plz tell me the website name')
            website = takeCommand().lower()
            webbrowser.open(""+website+".com")

        elif 'play music' in query:
            music_dir = 'D:\\Desktop\\music'
            songs = os.listdir(music_dir)
            print(songs)
            print(len(songs))
            a=random.randint(0,len(songs)-1)
            print(a)
            os.startfile(os.path.join(music_dir,songs[a]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir The time is {strTime}")
        
        elif 'open visual studio' in query:
            code_path='"C:\\Users\\IAQMH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            os.startfile(code_path)
        
        elif 'send mail' in query:
            try:
                speak('what should i say')
                content = takeCommand()
                to = 'lquresh52@gmail.com'
                sendmail(to,content)
                speak('Enail sent')
            except Exception as e:
                print(e)
                speak('sorry sir Could not send mail')


        elif query=='exit':
            break