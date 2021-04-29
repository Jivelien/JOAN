import speech_recognition as sr
import webbrowser
from gtts import gTTS
from playsound import playsound

r = sr.Recognizer();

def listening():
    with sr.Microphone() as source:
        print("DEBUG: Begin of listinning")
        audio_text = r.listen(source, timeout = 5)
        print("DEBUG: end of listinning")
        try:
            text = r.recognize_google(audio_text, language = "fr-FR").replace("Johan", "JOAN")
            print("You said: "+ text)
        except:
            pass
    return text

def speak(text):
    print("Joan: "+text)
    gTTS(text=text,lang="fr",slow=False).save('samp.mp3')
    playsound('samp.mp3')
    
def JOAN():
    print('DEBUG: calibration of ambient noise')
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        
    input = listening()
    if "JOAN" in input:
        speak("que puis-je pour vous?")
        order = listening()
        if "info" in order:
            speak("je mets les infos")
            strURL = "https://www.youtube.com/watch?v=wwNZKfBLAsc"
            webbrowser.open(strURL, new=2)
        else: 
            print("Joan: je n'ai pas compris votre demande")