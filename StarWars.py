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

pixels = PIL.ImageGrab.grab().load()
if around_color(pixels[1175,835],(24,187,255),2):
    click(800,840)
    time.sleep(1)
    click(715,330)
    time.sleep(1)
    click(970,480)
    time.sleep(2)
    click(730,980)
    time.sleep(1)
    click(1090,990)
    time.sleep(1)
    click(1100,280)
    time.sleep(1)
    click(980,90)
    time.sleep(1)

while True:
    if keyboard.is_pressed("q"):
        keyboard.release("q")
        raise SystemExit
    pixels = PIL.ImageGrab.grab().load()
    if around_color(pixels[1090,780],(249,207,32),2) or around_color(pixels[1090,780],(187,155,24),2):
        click(1090,780)
        time.sleep(1)
        click(1030,430)
    if around_color(pixels[1080,950],(24,187,255),2):
        click(1080,950)
        time.sleep(1)
        click(1080,950)
        