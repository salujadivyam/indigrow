
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')

for idx, voice in enumerate(voices):
    print(f"{idx}: {voice.name} - {voice.languages}")
def speak(text_en,text_hi):
        engine.setProperty('voice', voices[1].id)  
        engine.say(text_en)
        engine.runAndWait()
        engine.setProperty('voice', voices[2].id)  
        engine.say(text_hi)
        engine.runAndWait()
