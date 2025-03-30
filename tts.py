import msvcrt
import os
import sys
from gtts import gTTS
from pygame import mixer

text_en=f"Good Day, the weather today will be {weather}, the temperature is expected to be around {temp} with {chances} chance of rain. The best method for irrigation as per your details is {irrigation_method}, the best fertilizer that can be used for your crop is {fert}, and the estimated yield from your crop would come out to be {yieldd} Tons"

language='en'
myobj=gTTS(text=text_en,lang=language,slow=False)
myobj.save("TTSenglish.mp3")
mixer.init()
mixer.music.load("TTSenglish.mp3")
mixer.music.play()
text_en=f"शुभ दिन, आज मौसम {weather} रहेगा, तापमान {temp} के आसपास रहने की उम्मीद है और बारिश की संभावना {chances} है। आपके विवरण के अनुसार सिंचाई के लिए सबसे अच्छी विधि {irrigation_method} है, आपकी फसल के लिए इस्तेमाल किया जा सकने वाला सबसे अच्छा उर्वरक {fert} है, और आपकी फसल से अनुमानित उपज {yieldd} टन निकलेगी"
language='hi'
myobj=gTTS(text=text_en,lang=language,slow=False)
myobj.save("TTShindi.mp3")
mixer.init()
mixer.music.play()