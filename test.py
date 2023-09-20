import win32api, win32con, time, PIL.ImageGrab,pyautogui,keyboard

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

def around_color(color,match,tolerance):
    if abs(color[0]-match[0])>tolerance: return False
    if abs(color[1]-match[1])>tolerance: return False
    if abs(color[2]-match[2])>tolerance: return False
    return True

timer = 0;

while True:
    if keyboard.is_pressed("q"):
        keyboard.release("q")
        time.sleep(0.5)
        break
        
    px = PIL.ImageGrab.grab().load()
        
    color_1 = px[880, 835]
    color_2 = px[990, 970]
    if color_1 == (255,221,28) or color_1 == (255,220,28) or color_1 == (255,219,28):
        click(880,835)
        timer = 0
        time.sleep(8)
    elif color_2 == (28,181,255) or color_2 == (255,215,28) or color_2 == (24,187,255) or color_2 == (249,207,32):
        click(990,970)
        timer = 0
    else:
        click(730,880)
        click(730,980)
        click(816,980)
        click(905,980)
        click(979,980)
        click_and_drag([736,805],[935,269])
        
        #click_and_drag((700,150),(1200,150))
        
        if px[875,79]!=(237,66,4):
            click(987,450)
        if px[875,79]!=(237,66,4):
            click(980,450)
        if px[875,79]!=(237,66,4):
            click(987,450)
        if px[875,79]!=(237,66,4):
            click(980,450)
        if px[875,79]!=(237,66,4):
            time.sleep(1)
    timer = timer+1
