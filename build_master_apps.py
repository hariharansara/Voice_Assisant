import json

files = ["exe_apps.json", "lnk_apps.json", "uwp_apps.json"]
master = {}

for f in files:
    try:
        with open(f, "r", encoding="utf-8") as file:
            data = json.load(file)
            master.update(data)
    except:
        pass

with open("master_apps.json", "w", encoding="utf-8") as f:
    json.dump(master, f, indent=2)

print("MASTER app database created")
