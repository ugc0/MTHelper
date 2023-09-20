import win32api,win32con,time,PIL.ImageGrab,pyautogui,keyboard,math

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def around_color(color,match,tolerance):
    if abs(color[0]-match[0])>tolerance: return False
    if abs(color[1]-match[1])>tolerance: return False
    if abs(color[2]-match[2])>tolerance: return False
    return True

accelerated = False

while True:
    if keyboard.is_pressed("q"):
        keyboard.release("q")
        raise SystemExit
    pixels = PIL.ImageGrab.grab().load()
    if around_color(pixels[890,730],(255,215,28),2):
        click(1015,615)
        click(890,730)
        time.sleep(1)
    if around_color(pixels[940,970],(176,126,251),2):
        click(1170,805)
        accelerated = False
        time.sleep(1)
    if around_color(pixels[940,970],(12,67,124),2) and accelerated==False:
        click(1200,1000)
        accelerated = True
        start_time = time.time()
        time.sleep(1)
    if (accelerated and time.time()-start_time>30):
        click(1120,990)
        accelerated = False
        time.sleep(1)
    if around_color(pixels[890,830],(249,205,32),2):
        click(890,830)
        time.sleep(1)
    if around_color(pixels[890,940],(255,219,28),2):
        click(890,940)
        time.sleep(1)
    if around_color(pixels[990,950],(255,215,28),2):
        click(990,950)
        time.sleep(1)
        