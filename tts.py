from gtts import gTTS
import playsound
import os

def speak(text):
    print("\nAI:", text)

    # ONLINE Odia voice only
    tts = gTTS(text=text, lang="hi")
    tts.save("voice.mp3")
    playsound.playsound("voice.mp3")
    os.remove("voice.mp3")
