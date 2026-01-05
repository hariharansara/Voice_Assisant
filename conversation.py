import subprocess
import json
import time

MODEL = "llama3:latest"

SYSTEM_PROMPT = (
    "You are Catherine, a friendly, intelligent assistant. "
    "Speak naturally and warmly. "
    "Answer in 3–5 sentences unless asked for more. "
    "You know world leaders, history, science, and current events."
)

def _ask_ollama(prompt: str) -> str:
    try:
        process = subprocess.Popen(
            ["ollama", "run", MODEL, "--format", "json"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            encoding="utf-8",
            errors="ignore"
        )

        process.stdin.write(prompt)
        process.stdin.close()

        response_text = ""

        for line in process.stdout:
            if not line.strip():
                continue

            try:
                data = json.loads(line)
            except json.JSONDecodeError:
                continue

            if "response" in data:
                response_text += data["response"]

            if data.get("done") is True:
                break

        process.stdout.close()
        process.wait()

        return response_text.strip()

    except Exception:
        return ""


def chat_response(user_input: str) -> str:
    prompt = (
        f"{SYSTEM_PROMPT}\n"
        f"User: {user_input}\n"
        f"Catherine:"
    )

    
    reply = _ask_ollama(prompt)

    if not reply:
        time.sleep(0.5)
        reply = _ask_ollama(prompt + " Please answer clearly.")

    if not reply:
        return "I know this one — give me a second and ask again."

    if len(reply) > 900:
        reply = reply[:900] + "… want me to continue?"

    return reply
