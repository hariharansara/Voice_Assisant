import os
import psutil
import subprocess
import webbrowser

PROTECTED = ["python", "code", "powershell"]

SYSTEM_APPS = {
    "calculator": "calc.exe",
    "notepad": "notepad.exe",
    "paint": "mspaint.exe",
    "explorer": "explorer.exe",
}

ALIASES = {
    "google": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "microsoft edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "power bi": r"C:\Program Files\Microsoft Power BI Desktop\bin\PBIDesktop.exe",
    "brave": r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
}


def open_app(name):
    if name in SYSTEM_APPS:
        subprocess.Popen(SYSTEM_APPS[name], shell=True)
        return f"Opening {name}"

    if name in ALIASES and os.path.exists(ALIASES[name]):
        os.startfile(ALIASES[name])
        return f"Opening {name} application"

    webbrowser.open(f"https://{name}.com")
    return f"I couldn’t find the app. Opening {name} website instead."


def close_app(name):
    for p in psutil.process_iter(['name']):
        try:
            pname = p.info['name'].lower()
            if name in pname and not any(x in pname for x in PROTECTED):
                p.kill()
                return f"Closed {name}"
        except:
            pass
    return f"{name} cannot be closed or is not running."


def close_all_apps():
    for p in psutil.process_iter(['name']):
        try:
            pname = p.info['name'].lower()
            if not any(x in pname for x in PROTECTED):
                p.kill()
        except:
            pass
    return "All apps closed except my essentials."


def close_all_except(app):
    for p in psutil.process_iter(['name']):
        try:
            pname = p.info['name'].lower()
            if app not in pname and not any(x in pname for x in PROTECTED):
                p.kill()
        except:
            pass
    return f"Closed everything except {app}"
