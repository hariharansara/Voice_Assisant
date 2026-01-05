import os

APPS_FILE = "installed_apps_paths.txt"

def normalize(text: str) -> str:
    """Lowercase, remove spaces and .exe"""
    return text.lower().replace(" ", "").replace(".exe", "")

def find_app_path(app_name: str):
    app_name_raw = app_name.lower().strip()
    app_name_norm = normalize(app_name_raw)

    if not os.path.exists(APPS_FILE):
        print("installed_apps_paths.txt not found.")
        return

    strong_matches = []
    weak_matches = []

    with open(APPS_FILE, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            line = line.strip()
            if " : " not in line:
                continue

            exe, path = line.split(" : ", 1)

            exe_raw = exe.lower().replace(".exe", "")
            exe_norm = normalize(exe)

            # 1️⃣ Strong match: direct or normalized substring
            if (
                app_name_raw in exe_raw
                or app_name_norm in exe_norm
            ):
                strong_matches.append((exe, path))
                continue

            # 2️⃣ Weak match: character containment (mic → microsoft)
            if all(ch in exe_norm for ch in app_name_norm):
                weak_matches.append((exe, path))

    if strong_matches:
        print("\nStrong matches found:\n")
        for exe, path in strong_matches:
            print(f"{exe} : {path}")
        return

    if weak_matches:
        print("\nNear matches found:\n")
        for exe, path in weak_matches:
            print(f"{exe} : {path}")
        return

    print(f"No application found for '{app_name}'")

if __name__ == "__main__":
    name = input("Enter application name: ")
    find_app_path(name)
