import pyautogui
import win32gui
import time

# Set the coordinates of the area where mouse movements will be recorded
pos_x1 = 3136
pos_y1 = 333
pos_x2 = 3186
pos_y2 = 168

window_name = "Rocket League (64-bit, DX11, Cooked)"

toggle_key = "f2"

pause_key = "f3"

# Set the interval between recorded mouse events
interval = 0.01

# Initialize variables
toggle = False
pause = False
recorded_events = []

#get the handle of the window by its name
def get_window_handle(window_name):
    handle = win32gui.FindWindow(None, window_name)
    if handle == 0:
        print("Window not found!")
        return None
    else:
        return handle

#record mouse events within the designated area
def record_mouse_events():
    print("Recording mouse events. Press {} to stop recording...".format(toggle_key))
    while not toggle:
        pos = pyautogui.position()
        if pos_x1 <= pos[0] <= pos_x2 and pos_y1 <= pos[1] <= pos_y2:
            recorded_events.append((pos[0], pos[1], pyautogui.mouseDown(button='left')))
        time.sleep(interval)

#send the recorded mouse events to the designated window
def send_recorded_events():
    print("Sending mouse events to window '{}'...".format(window_name))
    handle = get_window_handle(window_name)
    if handle:
        win32gui.SetForegroundWindow(handle)
        while True:
            if not pause:
                for event in recorded_events:
                    pyautogui.moveTo(event[0], event[1])
                    pyautogui.mouseDown(button='left')
                    time.sleep(interval)
            time.sleep(0.1)

def toggle_script():
    global toggle
    toggle = not toggle
    if toggle:
        send_recorded_events()

def pause_script():
    global pause
    pause = not pause

# Register hotkeys
import keyboard
keyboard.add_hotkey(toggle_key, toggle_script)
keyboard.add_hotkey(pause_key, pause_script)

record_mouse_events()
