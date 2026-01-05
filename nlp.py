import random
from apps import open_app, close_app, close_all_apps, close_all_except
from conversation import chat_response

conversation_mode = False

INCOMPLETE = [
    "Tell me the app name.",
    "Which app should I open?",
]

UNKNOWN = [
    "I didn’t get that.",
    "Try saying it differently.",
]

def process(cmd):
    global conversation_mode

    if cmd == "__MISSED__":
        return "I didn’t catch that."

    # MODE CONTROL
    if "start normal conversation" in cmd:
        conversation_mode = True
        return "Okay. I’m here with you."

    if "terminate normal conversation" in cmd:
        conversation_mode = False
        return "Alright. Back to assistant mode."

    # CONVERSATION MODE
    if conversation_mode:
        return chat_response(cmd)

    # COMMAND MODE
    if cmd in ("open", "close"):
        return random.choice(INCOMPLETE)

    if cmd == "close all":
        return close_all_apps()

    if cmd.startswith("close all except"):
        app = cmd.replace("close all except", "").strip()
        return close_all_except(app)

    if cmd.startswith("open"):
        return open_app(cmd.replace("open", "").strip())

    if cmd.startswith("close"):
        return close_app(cmd.replace("close", "").strip())

    if "exit program" in cmd or "terminate program" in cmd:
        return "__EXIT__"

    return random.choice(UNKNOWN)
