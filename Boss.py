import win32api, win32con, time, PIL.ImageGrab,pyautogui,keyboard

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

timer = 0;

while True:
    if keyboard.is_pressed("q"):
        keyboard.release("q")
        time.sleep(0.5)
        break
    px = PIL.ImageGrab.grab().load()
    if px[1160,960]==(249,211,22):
        click(1160,960)
        time.sleep(2)
    else:
        click(730,885)
        click(730,980)
        click(816,980)
        click(905,980)
        click(979,980)
        
        click(961,250)
        
        time.sleep(1)
