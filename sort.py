import os

INPUT_FILE = "installed_apps_paths.txt"
OUTPUT_FILE = "installed_apps_sorted.txt"

def sort_apps():
    if not os.path.exists(INPUT_FILE):
        print("installed_apps_paths.txt not found")
        return

    entries = []

    with open(INPUT_FILE, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line or " : " not in line:
                continue

            app, path = line.split(" : ", 1)
            entries.append((app.lower(), app, path))

    # sort alphabetically by app name (case-insensitive)
    entries.sort(key=lambda x: x[0])

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for _, app, path in entries:
            f.write(f"{app} : {path}\n")

    print("✔ Applications sorted alphabetically")
    print(f"✔ Output written to: {OUTPUT_FILE}")

if __name__ == "__main__":
    sort_apps()
