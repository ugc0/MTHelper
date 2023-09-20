import win32api, win32con, time, PIL.ImageGrab,pyautogui,keyboard,math,random

def screenshot():
    global screenshot_index
    
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'C:\Users\Ugo\Desktop\Screenshots Bataille Navale\Run\screenshot_'+str(screenshot_index)+'.png')
    
    print('Screenshot',screenshot_index)
    
    screenshot_index=screenshot_index+1
    
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    
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
    
print(random.randrange(1, 50))
print(random.randrange(1, 50))
print(random.randrange(1, 50))
print(random.randrange(1, 50))
print(random.randrange(1, 50))

print(random.randrange(1, 12))
print(random.randrange(1, 12))
