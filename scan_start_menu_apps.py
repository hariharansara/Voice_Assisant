import os, json, winshell

START_MENU_DIRS = [
    os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs"),
    os.path.expandvars(r"%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs"),
]

apps = {}

for base in START_MENU_DIRS:
    for root, _, files in os.walk(base):
        for file in files:
            if file.lower().endswith(".lnk"):
                try:
                    p = os.path.join(root, file)
                    sc = winshell.shortcut(p)
                    if sc.path:
                        name = file.replace(".lnk","").lower()
                        apps[name] = {
                            "type": "lnk",
                            "path": p
                        }
                except:
                    pass

with open("lnk_apps.json", "w", encoding="utf-8") as f:
    json.dump(apps, f, indent=2)

print("Start menu apps extracted")
