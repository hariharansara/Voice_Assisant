import json

INPUT = "installed_apps_paths.txt"
OUT = "exe_apps.json"

apps = {}

with open(INPUT, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        if " : " in line:
            exe, path = line.strip().split(" : ", 1)
            apps[exe.replace(".exe","").lower()] = {
                "type": "exe",
                "path": path
            }

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(apps, f, indent=2)

print("EXE apps extracted")
