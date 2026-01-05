import pyautogui

def mouse_action(cmd):
    if "left click" in cmd:
        pyautogui.click()
        return "Left click done."

    if "right click" in cmd:
        pyautogui.click(button="right")
        return "Right click done."

    if "double click" in cmd:
        pyautogui.doubleClick()
        return "Double click done."

    if "move mouse" in cmd:
        pyautogui.moveRel(200, 100, duration=0.4)
        return "Mouse moved."

    return None

def keyboard_action(cmd):
    if "copy" in cmd:
        pyautogui.hotkey("ctrl", "c")
        return "Copied."

    if "paste" in cmd:
        pyautogui.hotkey("ctrl", "v")
        return "Pasted."

    if "cut" in cmd:
        pyautogui.hotkey("ctrl", "x")
        return "Cut."

    if "select all" in cmd:
        pyautogui.hotkey("ctrl", "a")
        return "Selected all."

    if "undo" in cmd:
        pyautogui.hotkey("ctrl", "z")
        return "Undo."

    if "redo" in cmd:
        pyautogui.hotkey("ctrl", "y")
        return "Redo."

    return None
