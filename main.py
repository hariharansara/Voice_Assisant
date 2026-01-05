from voice import listen, speak
from nlp import process
import random

GREETINGS = [
    "Hey! I’m Catherine. How can I help?",
    "Hi! Catherine here.",
]

MISSED = [
    "Could you repeat that?",
    "Say that again for me.",
]

speak(random.choice(GREETINGS))

while True:
    command = listen()

    if command in ("__MISSED__", ""):
        speak(random.choice(MISSED))
        continue

    response = process(command)

    if response == "__EXIT__":
        speak("Okay. Shutting down. Talk soon.")
        break

    speak(response)
