import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty("rate", 170)

voices = engine.getProperty("voices")
for v in voices:
    if "female" in v.name.lower() or "zira" in v.name.lower():
        engine.setProperty("voice", v.id)
        break


def speak(text):
    print(f"Catherine: {text}")
    engine.say(text)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        print("\n🎧 Catherine is listening...")
        r.pause_threshold = 1.2
        audio = r.listen(mic)

    try:
        said = r.recognize_google(audio).lower()
        print("You said:", said)
        return said
    except:
        return "__MISSED__"
