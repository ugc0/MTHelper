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
    
def click_and_drag(A,B):
    time.sleep(0.2)
    win32api.SetCursorPos((A[0],A[1]))
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,A[0],A[1],0,0)
    time.sleep(0.1)
    win32api.SetCursorPos((B[0],B[1]))
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,B[0],B[1],0,0)
    time.sleep(0.1)

while True:
    if keyboard.is_pressed("q"):
        keyboard.release("q")
        raise SystemExit
    pixels = PIL.ImageGrab.grab().load()
    if around_color(pixels[1040,990],(249,207,32),2):
        click(1040,990) 
        time.sleep(1)
    elif around_color(pixels[730,965],(255,255,255),20) or around_color(pixels[730,965],(127,127,127),20) or around_color(pixels[730,965],(150,150,150),20):
        click(730,965)
        click(734,887)
        click(824,983)
        click(900,984)
        click(982,977)
        click_and_drag([736,805],[935,269])
        time.sleep(0.5)
    else:
        click(960,950)
        time.sleep(1)
        