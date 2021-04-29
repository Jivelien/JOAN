import speech_recognition as sr
import webbrowser

r = sr.Recognizer();
r.adjust_for_ambient_noise(source, duration=5)

def listening():
    with sr.Microphone() as source:
        print("DEBUG: Begin of listinning")
        audio_text = r.listen(source)
        print("DEBUG: end of listinning")
        try:
            text = r.recognize_google(audio_text, language = "fr-FR").replace("Johan", "JOAN")
            print("You said: "+ input)
        except:
            pass
    return text

def JOAN():
    input = listening()
    if "JOAN" in input:
        print("Joan: que puis-je pour vous?")
        order = listening()
        if order == "mets les infos":
            print("Joan: je mets les infos")
            strURL = "https://www.youtube.com/watch?v=wwNZKfBLAsc"
            webbrowser.open(strURL, new=2)
        else: 
            print("Joan: je n'ai pas compris votre demande")