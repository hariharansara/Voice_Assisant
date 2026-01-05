import subprocess, json

cmd = [
    "powershell",
    "-Command",
    "Get-StartApps | ConvertTo-Json"
]

result = subprocess.run(cmd, capture_output=True, text=True)
apps_raw = json.loads(result.stdout)

apps = {}

for app in apps_raw:
    name = app["Name"].lower()
    apps[name] = {
        "type": "uwp",
        "appid": app["AppID"]
    }

with open("uwp_apps.json", "w", encoding="utf-8") as f:
    json.dump(apps, f, indent=2)

print("UWP apps extracted")
