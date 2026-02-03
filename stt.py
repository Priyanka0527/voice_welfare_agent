
import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("🎤 Speak now...")
            audio = r.listen(source, timeout=5)
        return r.recognize_google(audio, language="or-IN")
    except:
        return input("Enter input (fallback): ")
