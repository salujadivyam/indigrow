
import pyttsx3
import time
engine = pyttsx3.init()
voices = engine.getProperty('voices')

for idx, voice in enumerate(voices):
    print(f"{idx}: {voice.name} - {voice.languages}")
def speak(text, lang="en"):
    if lang == "hi":
        engine.setProperty('voice', voices[1].id)  
    else:
        engine.setProperty('voice', voices[0].id)
    
    engine.say(text)
    engine.runAndWait()
temp = "30°C"
rain= "40%"
irrigation_method = "Drip Irrigation"
fertilizer = "Urea"
yield_est = "2.5"
text_en = f"Good Day, the weather today will be partly cloudy, the temperature is expected to be around {temp} with a {rain} chance of rain. The best method for irrigation as per your details is {irrigation_method}, the best fertilizer that can be used for your crop is {fertilizer}, and the estimated yield from your crop would come out to be {yield_est} Tons."


time.sleep(2) 
text_hi = f"शुभ दिन, आज मौसम आंशिक रूप से बादल रहेगा, तापमान {temp} के आसपास रहने की उम्मीद है और बारिश की संभावना {rain} है। आपके विवरण के अनुसार सिंचाई के लिए सबसे अच्छी विधि {irrigation_method} है, आपकी फसल के लिए इस्तेमाल किया जा सकने वाला सबसे अच्छा उर्वरक {fertilizer} है, और आपकी फसल से अनुमानित उपज {yield_est} टन निकलेगी।"
