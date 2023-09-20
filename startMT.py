import win32api, win32con, time, PIL.ImageGrab,pyautogui,keyboard

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def around_color(color,match,tolerance):
    if abs(color[0]-match[0])>tolerance: return False
    if abs(color[1]-match[1])>tolerance: return False
    if abs(color[2]-match[2])>tolerance: return False
    return True

while True:
    if keyboard.is_pressed("q"):
        keyboard.release("q")
        time.sleep(0.5)
        break
    px = PIL.ImageGrab.grab().load()
    color_1 = px[730, 240]
    if around_color(color_1,(199,59,190),2):
        click(730,240)
        break