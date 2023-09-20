import win32api,win32con,time,PIL.ImageGrab,pyautogui,keyboard,math

GRILLE = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
RADAR = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

enemy_state = '000000000000000000'

count_hit = 0

WIN = False

win_count = 0
play_count = 0

just_hit = False

looking_for = 5

POSITIONS_BAS = [
[[802,499],[847,499],[892,499],[937,499],[982,499],[1027,499],[1072,499],[1117,499]],
[[798,538],[845,538],[891,538],[937,538],[983,538],[1029,538],[1075,538],[1121,538]],
[[795,578],[842,578],[889,578],[936,578],[983,578],[1030,578],[1077,578],[1124,578]],
[[791,620],[839,620],[887,620],[935,620],[983,620],[1031,620],[1079,620],[1127,620]],
[[787,662],[837,662],[887,662],[937,662],[987,662],[1037,662],[1087,662],[1137,662]],
[[783,708],[834,708],[885,708],[936,708],[987,708],[1038,708],[1089,708],[1140,708]],
[[778,760],[830,760],[882,760],[934,760],[986,760],[1038,760],[1090,760],[1142,760]],
[[774,811],[827,811],[880,811],[933,811],[986,811],[1039,811],[1092,811],[1145,811]]]

POSITIONS_HAUT = [
[[805,332],[847,332],[890,332],[933,332],[975,332],[1019,332],[1062,332],[1106,332]],
[[801,365],[846,365],[889,365],[934,365],[976,365],[1020,365],[1064,365],[1108,365]],
[[798,400],[842,400],[885,400],[931,400],[977,400],[1021,400],[1066,400],[1111,400]],
[[795,436],[839,436],[887,436],[931,436],[977,436],[1023,436],[1069,436],[1114,436]],
[[790,474],[837,474],[884,474],[931,474],[977,474],[1025,474],[1071,474],[1119,474]],
[[787,513],[834,513],[882,513],[930,513],[978,513],[1027,513],[1074,513],[1123,513]],
[[782,555],[832,555],[880,555],[931,555],[978,555],[1029,555],[1077,555],[1127,555]],
[[779,598],[829,598],[879,598],[929,598],[979,598],[1029,598],[1079,598],[1130,598]]]

TARGET_LIST = [52,25,22,55,73,30,4,47,43,34,11,66,16,61,70,0,7,77,13,36,64,41,2,27,75,50,21,32,45,56,62,53,24,15,10,3,74,57,6,37,72,40,60,51,5,14,67,76,1,12,17,26,42,54,35,46,44,63,31,23,65,71,20,33]
NEXT_TARGET = []

FINAL_POSITION_2 = [['C',1,5,'RL'],['C',1,5,'LR']]
FINAL_POSITION_3 = [['L',8,5,'CRC'],['L',8,5,'CRC']]
FINAL_POSITION_41 = [['L',1,0,'PPRP'],['L',1,0,'PRPP']]
FINAL_POSITION_42 = [['L',4,1,'PPRP'],['L',4,1,'PRPP']]
FINAL_POSITION_5 = [['C',7,0,'OOROO'],['C',7,0,'OOROO']]

screenshot_index = 1

line1 = ''
line2 = ''
line3 = ''
line4 = ''
line5 = ''
line6 = ''
line7 = ''
line8 = ''
column1 = ''
column2 = ''
column3 = ''
column4 = ''
column5 = ''
column6 = ''
column7 = ''
column8 = ''

anchor_offset_x = 0
anchor_offset_y = 0

SHIP2 = [0]
SHIP3 = [0]
SHIP41 = [0]
SHIP42 = [0]
SHIP5 = [0]

H21=False
H22=False

H31=False
H32=False
H33=False

H411=False
H412=False
H413=False
H414=False

H421=False
H422=False
H423=False
H424=False

H51=False
H52=False
H53=False
H54=False
H55=False

is_2_alive = True
is_3_alive = True
is_41_alive = True
is_42_alive = True
is_5_alive = True

just_hit_2 = False
just_hit_3 = False
just_hit_41 = False
just_hit_42 = False
just_hit_5 = False

is_2_damaged = False
is_3_damaged = False
is_41_damaged = False
is_42_damaged = False
is_5_damaged = False

still_time_to_place_ships = True

def prepare_next_game():

    global GRILLE
    global RADAR
    global enemy_state
    global count_hit
    global just_hit
    global looking_for
    global NEXT_TARGET
    global screenshot_index
    global line1
    global line2
    global line3
    global line4
    global line5
    global line6
    global line7
    global line8
    global column1
    global column2
    global column3
    global column4
    global column5
    global column6
    global column7
    global column8
    global anchor_offset_x
    global anchor_offset_y
    global SHIP2
    global SHIP3
    global SHIP41
    global SHIP42
    global SHIP5
    global H21
    global H22
    global H31
    global H32
    global H33
    global H411
    global H412
    global H413
    global H414
    global H421
    global H422
    global H423
    global H424
    global H51
    global H52
    global H53
    global H54
    global H55
    global is_2_alive 
    global is_3_alive 
    global is_41_alive 
    global is_42_alive 
    global is_5_alive 
    global just_hit_2 
    global just_hit_3 
    global just_hit_41 
    global just_hit_42 
    global just_hit_5 
    global is_2_damaged 
    global is_3_damaged 
    global is_41_damaged 
    global is_42_damaged 
    global is_5_damaged 
    global still_time_to_place_ships 
    global WIN

    RILLE = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    RADAR = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

    enemy_state = '000000000000000000'

    count_hit = 0

    just_hit = False

    looking_for = 5

    NEXT_TARGET = []

    screenshot_index = 1
    
    WIN = False

    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    line5 = ''
    line6 = ''
    line7 = ''
    line8 = ''
    column1 = ''
    column2 = ''
    column3 = ''
    column4 = ''
    column5 = ''
    column6 = ''
    column7 = ''
    column8 = ''

    anchor_offset_x = 0
    anchor_offset_y = 0

    SHIP2 = [0]
    SHIP3 = [0]
    SHIP41 = [0]
    SHIP42 = [0]
    SHIP5 = [0]

    H21=False
    H22=False

    H31=False
    H32=False
    H33=False

    H411=False
    H412=False
    H413=False
    H414=False

    H421=False
    H422=False
    H423=False
    H424=False

    H51=False
    H52=False
    H53=False
    H54=False
    H55=False

    is_2_alive = True
    is_3_alive = True
    is_41_alive = True
    is_42_alive = True
    is_5_alive = True

    just_hit_2 = False
    just_hit_3 = False
    just_hit_41 = False
    just_hit_42 = False
    just_hit_5 = False

    is_2_damaged = False
    is_3_damaged = False
    is_41_damaged = False
    is_42_damaged = False
    is_5_damaged = False

    still_time_to_place_ships = True

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
    
def get_column(matrix,index):
    return [row[index] for row in matrix]
    
def matrix_to_string(matrix):
    return ''.join(ele for sub in matrix for ele in sub)
    
def reshuffle():
    click(735,880)
    time.sleep(1)
    
def identify_color(rgb):
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    if green<=210 and green>=190 and blue<20:
        return "R"
    elif red<50 and red+green+blue<300:
        return "V"
    elif red>150 and red < 245 and green>220 and blue>120 and blue<200 :
        return "L"
    elif (red/(green+1))>1.7 and (blue/(green+1))>1.7:
        return "P"
    elif red>green and green>blue and blue<150:
        return "O"
    elif blue>green and green>red and green>100 and blue/(red+1)>1.5:
        return "C"
    else:
        return "?"

def is_empty(ship_index,ship_matrix):

    if still_time_to_place_ships==False: return False

    reference_grid = remove_ship_from_grid(ship_matrix)

    if ship_index==2:
        return reference_grid[5][0]=='V' and reference_grid[6][0]=='V'
    if ship_index==3:
        return reference_grid[7][5]=='V' and reference_grid[7][6]=='V' and reference_grid[7][7]=='V'
    if ship_index==41:
        return reference_grid[0][0]=='V' and reference_grid[0][1]=='V' and reference_grid[0][2]=='V' and reference_grid[0][3]=='V'
    if ship_index==42:
        return reference_grid[3][1]=='V' and reference_grid[3][2]=='V' and reference_grid[3][3]=='V' and reference_grid[3][4]=='V'
    if ship_index==5:
        return reference_grid[0][6]=='V' and reference_grid[1][6]=='V' and reference_grid[2][6]=='V' and reference_grid[3][6]=='V' and reference_grid[4][6]=='V'
    return False
    
def find_ship(ship_index):

    if still_time_to_place_ships==False: return False
    
    if ship_index==2:
        needle1 = 'RL'
        needle2 = 'LR'
    elif ship_index==3:
        needle1 = 'CRC'
        needle2 = 'CRC'
    elif ship_index==41 or ship_index==42:
        needle1 = 'PRPP'
        needle2 = 'PPRP'
    elif ship_index==5:
        needle1 = 'OOROO'
        needle2 = 'OOROO'
    else:
        return False

    if line1.find(needle1)>=0 or line1.find(needle2)>=0:
        if (ship_index!=42):
            if line1.find(needle1)>=0:
                return ['L',1,line1.find(needle1),needle1]
            else:
                return ['L',1,line1.find(needle2),needle2]
        else:
            ship_index=41
    if line2.find(needle1)>=0 or line2.find(needle2)>=0:
        if (ship_index!=42):
            if line2.find(needle1)>=0:
                return ['L',2,line2.find(needle1),needle1]
            else:
                return ['L',2,line2.find(needle2),needle2]
        else:
            ship_index=41
    if line3.find(needle1)>=0 or line3.find(needle2)>=0:
        if (ship_index!=42):
            if line3.find(needle1)>=0:
                return ['L',3,line3.find(needle1),needle1]
            else:
                return ['L',3,line3.find(needle2),needle2]
        else:
            ship_index=41
    if line4.find(needle1)>=0 or line4.find(needle2)>=0:
        if (ship_index!=42):
            if line4.find(needle1)>=0:
                return ['L',4,line4.find(needle1),needle1]
            else:
                return ['L',4,line4.find(needle2),needle2]
        else:
            ship_index=41
    if line5.find(needle1)>=0 or line5.find(needle2)>=0:
        if (ship_index!=42):
            if line5.find(needle1)>=0:
                return ['L',5,line5.find(needle1),needle1]
            else:
                return ['L',5,line5.find(needle2),needle2]
        else:
            ship_index=41
    if line6.find(needle1)>=0 or line6.find(needle2)>=0:
        if (ship_index!=42):
            if line6.find(needle1)>=0:
                return ['L',6,line6.find(needle1),needle1]
            else:
                return ['L',6,line6.find(needle2),needle2]
        else:
            ship_index=41
    if line7.find(needle1)>=0 or line7.find(needle2)>=0:
        if (ship_index!=42):
            if line7.find(needle1)>=0:
                return ['L',7,line7.find(needle1),needle1]
            else:
                return ['L',7,line7.find(needle2),needle2]
        else:
            ship_index=41
    if line8.find(needle1)>=0 or line8.find(needle2)>=0:
        if (ship_index!=42):
            if line8.find(needle1)>=0:
                return ['L',8,line8.find(needle1),needle1]
            else:
                return ['L',8,line8.find(needle2),needle2]
        else:
            ship_index=41
    if column1.find(needle1)>=0 or column1.find(needle2)>=0:
        if (ship_index!=42):
            if column1.find(needle1)>=0:
                return ['C',1,column1.find(needle1),needle1]
            else:
                return ['C',1,column1.find(needle2),needle2]
        else:
            ship_index=41
    if column2.find(needle1)>=0 or column2.find(needle2)>=0:
        if (ship_index!=42):
            if column2.find(needle1)>=0:
                return ['C',2,column2.find(needle1),needle1]
            else:
                return ['C',2,column2.find(needle2),needle2]
        else:
            ship_index=41
    if column3.find(needle1)>=0 or column3.find(needle2)>=0:
        if (ship_index!=42):
            if column3.find(needle1)>=0:
                return ['C',3,column3.find(needle1),needle1]
            else:
                return ['C',3,column3.find(needle2),needle2]
        else:
            ship_index=41
    if column4.find(needle1)>=0 or column4.find(needle2)>=0:
        if (ship_index!=42):
            if column4.find(needle1)>=0:
                return ['C',4,column4.find(needle1),needle1]
            else:
                return ['C',4,column4.find(needle2),needle2]
        else:
            ship_index=41
    if column5.find(needle1)>=0 or column5.find(needle2)>=0:
        if (ship_index!=42):
            if column5.find(needle1)>=0:
                return ['C',5,column5.find(needle1),needle1]
            else:
                return ['C',5,column5.find(needle2),needle2]
        else:
            ship_index=41
    if column6.find(needle1)>=0 or column6.find(needle2)>=0:
        if (ship_index!=42):
            if column6.find(needle1)>=0:
                return ['C',6,column6.find(needle1),needle1]
            else:
                return ['C',6,column6.find(needle2),needle2]
        else:
            ship_index=41
    if column7.find(needle1)>=0 or column7.find(needle2)>=0:
        if (ship_index!=42):
            if column7.find(needle1)>=0:
                return ['C',7,column7.find(needle1),needle1]
            else:
                return ['C',7,column7.find(needle2),needle2]
        else:
            ship_index=41
    if column8.find(needle1)>=0 or column8.find(needle2)>=0:
        if (ship_index!=42):
            if column8.find(needle1)>=0:
                return ['C',8,column8.find(needle1),needle1]
            else:
                return ['C',8,column8.find(needle2),needle2]
        else:
            ship_index=41
    return False

def remove_ship_from_grid(ship_matrix):

    if still_time_to_place_ships==False: return False

    grid = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    
    for row in range(8):
        for column in range(8):
            grid[row][column]=GRILLE[row][column]
    
    ship_length = len(ship_matrix[3])
    if ship_matrix[0]=='L':
        x = ship_matrix[1]-1
        for i in range(ship_length):
            y = ship_matrix[2]+i
            grid[x][y]='V'
    else:
        y = ship_matrix[1]-1
        for i in range(ship_length):
            x = ship_matrix[2]+i
            grid[x][y]='V'
    return grid
    
def rotate_ship(ship_matrix):

    if still_time_to_place_ships==False: return False

    rotula_position = ship_matrix[3].index("R")
    ship_length = len(ship_matrix[3])
    
    reference_grid = remove_ship_from_grid(ship_matrix)
    
    if ship_matrix[0]=='L':
        left_of_rotula = rotula_position
        right_of_rotula = ship_length-left_of_rotula-1
        rotula_x = ship_matrix[1]-1
        rotula_y = ship_matrix[2]+rotula_position
        while(rotula_x+right_of_rotula>7): rotula_x=rotula_x-1
            
        while(rotula_x-left_of_rotula<0): rotula_x=rotula_x+1

        for i in range(1,left_of_rotula+1):
            if reference_grid[rotula_x-i][rotula_y]!='V': 
                print(ship_matrix,' can rotate inside the grid but would obstruct another ship in its upper part')
                return ship_matrix
        for i in range(1,right_of_rotula+1):
            if reference_grid[rotula_x+i][rotula_y]!='V': 
                print(ship_matrix,' can rotate inside the grid but would obstruct another ship in its lower part')    
                return ship_matrix
        print(ship_matrix,' can be rotated freely')
        click(POSITIONS_BAS[ship_matrix[1]-1][ship_matrix[2]+rotula_position][0],POSITIONS_BAS[ship_matrix[1]-1][ship_matrix[2]+rotula_position][1])
        time.sleep(0.1)
        map_redo()
        return ['C',rotula_y+1,rotula_x-left_of_rotula,ship_matrix[3]]
    else:
        above_rotula = rotula_position
        below_rotula = ship_length-above_rotula-1
        rotula_x = ship_matrix[2]+rotula_position
        rotula_y = ship_matrix[1]-1

        while(rotula_y+above_rotula>7): rotula_y=rotula_y-1
            
        while(rotula_y-below_rotula<0): rotula_y=rotula_y+1
        
        for i in range(1,above_rotula+1):
            if reference_grid[rotula_x][rotula_y+i]!='V': 
                print(ship_matrix,' can rotate inside the grid but would obstruct another ship in its right part')
                return ship_matrix
        for i in range(1,below_rotula+1):
            if reference_grid[rotula_x][rotula_y-i]!='V': 
                print(ship_matrix,' can rotate inside the grid but would obstruct another ship in its left part')    
                return ship_matrix
        print(ship_matrix,' can be rotated freely')
        click(POSITIONS_BAS[ship_matrix[2]+rotula_position][ship_matrix[1]-1][0],POSITIONS_BAS[ship_matrix[2]+rotula_position][ship_matrix[1]-1][1])
        time.sleep(0.1)
        map_redo()
        return ['L',rotula_x+1,rotula_y-below_rotula,ship_matrix[3][::-1]]

def force_rotate_ship(ship_matrix):

    if still_time_to_place_ships==False: return False

    global anchor_offset_x
    global anchor_offset_y
    
    anchor_offset_x = 0
    anchor_offset_y = 0

    rotula_position = ship_matrix[3].index("R")
    ship_length = len(ship_matrix[3])
    
    reference_grid = remove_ship_from_grid(ship_matrix)
    
    if ship_matrix[0]=='L':
        left_of_rotula = rotula_position
        right_of_rotula = ship_length-left_of_rotula-1
        rotula_x = ship_matrix[1]-1
        rotula_y = ship_matrix[2]+rotula_position
        while(rotula_x+right_of_rotula>7): rotula_x=rotula_x-1
            
        while(rotula_x-left_of_rotula<0): rotula_x=rotula_x+1

        for i in range(ship_length):
            if reference_grid[rotula_x-left_of_rotula+i][rotula_y]=='V':
                click(POSITIONS_BAS[ship_matrix[1]-1][ship_matrix[2]+rotula_position][0],POSITIONS_BAS[ship_matrix[1]-1][ship_matrix[2]+rotula_position][1])
                time.sleep(0.1)
                anchor_offset_x = i
                return ['C',rotula_y+1,rotula_x-left_of_rotula,ship_matrix[3]]
        print(ship_matrix,' rotation could not be forced')
        return ship_matrix
    else:
        above_rotula = rotula_position
        below_rotula = ship_length-above_rotula-1
        rotula_x = ship_matrix[2]+rotula_position
        rotula_y = ship_matrix[1]-1

        while(rotula_y+above_rotula>7): rotula_y=rotula_y-1
            
        while(rotula_y-below_rotula<0): rotula_y=rotula_y+1
        
        for i in range(ship_length):
            if reference_grid[rotula_x][rotula_y-below_rotula+i]=='V':
                click(POSITIONS_BAS[ship_matrix[2]+rotula_position][ship_matrix[1]-1][0],POSITIONS_BAS[ship_matrix[2]+rotula_position][ship_matrix[1]-1][1])
                time.sleep(0.1)
                anchor_offset_y = i
                return ['L',rotula_x+1,rotula_y-below_rotula,ship_matrix[3][::-1]]
        print(ship_matrix,' rotation could not be forced')
        return ship_matrix

def place_ship(ship_index,allow_rotation,allow_force_translation):

    global SHIP2
    global SHIP3
    global SHIP41
    global SHIP42
    global SHIP5
    
    global GRILLE

    if ship_index==2: SHIP=SHIP2
    if ship_index==3: SHIP=SHIP3
    if ship_index==41: SHIP=SHIP41
    if ship_index==42: SHIP=SHIP42
    if ship_index==5: SHIP=SHIP5
    
    if (SHIP==False):
        print('Ship',ship_index,' could not be identified')
        return False
    
    global anchor_offset_x
    global anchor_offset_y
    
    anchor_offset_x = 0
    anchor_offset_y = 0
    
    if ship_index==2: FINAL_POSITION = FINAL_POSITION_2
    if ship_index==3: FINAL_POSITION = FINAL_POSITION_3
    if ship_index==41: FINAL_POSITION = FINAL_POSITION_41
    if ship_index==42: FINAL_POSITION = FINAL_POSITION_42
    if ship_index==5: FINAL_POSITION = FINAL_POSITION_5
    
    can_be_placed=True
    
    if (SHIP==FINAL_POSITION[0] or SHIP==FINAL_POSITION[1]):
        print('Ship ',ship_index,' is already placed')
        return True
    if (ship_index==2 and SHIP[0]=='L') or (ship_index==3 and SHIP[0]=='C') or (ship_index==41 and SHIP[0]=='C') or (ship_index==42 and SHIP[0]=='C') or (ship_index==5 and SHIP[0]=='L'):
            if allow_rotation:
                print('Ship ',ship_index,' needs to be rotated')
                NEW_SHIP = rotate_ship(SHIP)
                if NEW_SHIP!=SHIP: 
                    SHIP=NEW_SHIP
                    
                    if ship_index==2: SHIP2=SHIP
                    if ship_index==3: SHIP3=SHIP
                    if ship_index==41: SHIP41=SHIP
                    if ship_index==42: SHIP42=SHIP
                    if ship_index==5: SHIP5=SHIP
                    
                    print('Rotated ship is now ',SHIP)
                elif is_empty(ship_index,SHIP):
                    NEW_SHIP = force_rotate_ship(SHIP)
                    if NEW_SHIP!=SHIP: 
                        SHIP=NEW_SHIP
                        
                        if ship_index==2: SHIP2=SHIP
                        if ship_index==3: SHIP3=SHIP
                        if ship_index==41: SHIP41=SHIP
                        if ship_index==42: SHIP42=SHIP
                        if ship_index==5: SHIP5=SHIP
                        
                        print('Ship ',ship_index,' has been forced to ',SHIP,' for immediate translation with anchor offsets (',anchor_offset_x,':',anchor_offset_y,')')
                        can_be_placed=True
                    else:
                        print('Ship ',ship_index,' will need to be rotated later and could not be forced.')
                        can_be_placed = False   
            else:
                can_be_placed=False
                print('Ship ',ship_index,' will need to be rotated later')
    if is_empty(ship_index,SHIP) and can_be_placed:
            if SHIP[0]=='L':
                if SHIP[3]=='RL':
                    depart = POSITIONS_BAS[SHIP[1]-1+anchor_offset_x][SHIP[2]+1+anchor_offset_y]
                else:
                    depart = POSITIONS_BAS[SHIP[1]-1+anchor_offset_x][SHIP[2]+anchor_offset_y]
            else:
                if SHIP[3]=='RL':
                    depart = POSITIONS_BAS[SHIP[2]+1+anchor_offset_x][SHIP[1]-1+anchor_offset_y]
                else:
                    depart = POSITIONS_BAS[SHIP[2]+anchor_offset_x][SHIP[1]-1+anchor_offset_y]
            if FINAL_POSITION[0][0]=='L':
                if SHIP[3]=='RL':
                    arrivee = POSITIONS_BAS[FINAL_POSITION[0][1]-1+anchor_offset_x][FINAL_POSITION[0][2]+1+anchor_offset_y]
                else:
                    arrivee = POSITIONS_BAS[FINAL_POSITION[0][1]-1+anchor_offset_x][FINAL_POSITION[0][2]+anchor_offset_y]
            else:
                if SHIP[3]=='RL':
                    arrivee = POSITIONS_BAS[FINAL_POSITION[0][2]+1+anchor_offset_x][FINAL_POSITION[0][1]-1+anchor_offset_y]
                else:
                    arrivee = POSITIONS_BAS[FINAL_POSITION[0][2]+anchor_offset_x][FINAL_POSITION[0][1]-1+anchor_offset_y]
            print('Ship ',ship_index,' can be translated from ',depart,' to ',arrivee)
            click_and_drag(depart,arrivee)
            map_redo()
            if ship_index==2: SHIP2 = find_ship(2)
            if ship_index==3: SHIP3 = find_ship(3)
            if ship_index==41: SHIP41 = find_ship(41)
            if ship_index==42: SHIP42 = find_ship(42)
            if ship_index==5: SHIP5 = find_ship(5)
            anchor_offset_x = 0
            anchor_offset_y = 0
            return True
    elif allow_force_translation and can_be_placed:
        ship_length = len(SHIP[3])
        rotula_position = SHIP[3].index('R')
        for i in range(ship_length):
            if i==rotula_position: continue
            if SHIP[0]=='L':
                if GRILLE[FINAL_POSITION[0][1]-1][FINAL_POSITION[0][2]+i]=='V':
                    if SHIP[1]-1+0 or SHIP[1]-1>7: return False
                    if SHIP[2]+i<0 or SHIP[2]+i>7: return False
                    depart = POSITIONS_BAS[SHIP[1]-1][SHIP[2]+i]
                    arrivee = POSITIONS_BAS[FINAL_POSITION[0][1]-1][FINAL_POSITION[0][2]+i]
                    print('Ship ',ship_index,' can be force-translated from ',depart,' to ',arrivee,' anchor offset is ',i)
                    click_and_drag(depart,arrivee)
                    map_redo()
                    if ship_index==2: SHIP2 = find_ship(2)
                    if ship_index==3: SHIP3 = find_ship(3)
                    if ship_index==41: SHIP41 = find_ship(41)
                    if ship_index==42: SHIP42 = find_ship(42)
                    if ship_index==5: SHIP5 = find_ship(5)
                    return True
            else:
                if GRILLE[FINAL_POSITION[0][2]+i][FINAL_POSITION[0][1]-1]=='V':
                    if SHIP[1]-1+i<0 or SHIP[1]-1+i>7: return False
                    if SHIP[2]<0 or SHIP[2]>7: return False
                    depart = POSITIONS_BAS[SHIP[1]-1+i][SHIP[2]]
                    arrivee = POSITIONS_BAS[FINAL_POSITION[0][1]-1+i][FINAL_POSITION[0][2]]
                    print('Ship ',ship_index,' can be force-translated from ',depart,' to ',arrivee,' anchor offset is ',i)
                    click_and_drag(depart,arrivee)
                    map_redo()
                    if ship_index==2: SHIP2 = find_ship(2)
                    if ship_index==3: SHIP3 = find_ship(3)
                    if ship_index==41: SHIP41 = find_ship(41)
                    if ship_index==42: SHIP42 = find_ship(42)
                    if ship_index==5: SHIP5 = find_ship(5)
                    return True
        print('Final position for ship ',ship_index,' is not available or the ship needs to be rotated first')
        return False
    
    
def map_grid(pos,pixels):
    
    global still_time_to_place_ships
    
    if pixels[1190,990]!=(249,205,32):
        time.sleep(0.5)
        pixels2 = PIL.ImageGrab.grab().load()
        if pixels2[1190,990]!=(249,205,32):
            still_time_to_place_ships=False
            print('too late to place ships aborting')
            screenshot()
    
    for row in range(8):
        for column in range(8):
            main_marker = identify_color(pixels[pos[row][column][0],pos[row][column][1]])
            if main_marker=='V' or main_marker=='R' or main_marker=='L' or main_marker=='P': 
                GRILLE[row][column]=main_marker
            else:
                for expanse in range(-19,19):
                    marker = identify_color(pixels[pos[row][column][0]+expanse,pos[row][column][1]])
                    if marker=='P':
                        GRILLE[row][column]='P'
                        break
                    if marker=='O':
                        GRILLE[row][column]='O'
                        break
                    if marker=='C':
                        GRILLE[row][column]='C'
                        break
                    marker = identify_color(pixels[pos[row][column][0],pos[row][column][1]+expanse])
                    if marker=='P':
                        GRILLE[row][column]='P'
                        break
                    if marker=='O':
                        GRILLE[row][column]='O'
                        break
                    if marker=='C':
                        GRILLE[row][column]='C'
                        break
                if GRILLE[row][column]==0: GRILLE[row][column]='W'           

def display_grid(source):
    print(source[0])
    print(source[1])
    print(source[2])
    print(source[3])
    print(source[4])
    print(source[5])
    print(source[6])
    print(source[7])
    
def target_span(x,y):

    up = 0
    down = 0
    left = 0
    right = 0

    for i in range(8):
        if x-i-1<0 or RADAR[x-i-1][y]>1: 
            up = i
            break
    for i in range(8):
        if x+i+1>7 or RADAR[x+i+1][y]>1: 
            down = i
            break
    for i in range(8):
        if y-i-1<0 or RADAR[x][y-1-i]>1: 
            left = i
            break
    for i in range(8):
        if y+i+1>7 or RADAR[x][y+1+i]>1: 
            right = i
            break
    
    result = max(up+down+1,left+right+1)
    print('Target_span for ',x,':',y,' is ',result)
    
    return result
    
def radar_analysis():

    global RADAR
    global NEXT_TARGET
    
    NEXT_TARGET = []
    
    up_spots = 0
    down_spots = 0
    left_spots = 0
    right_spots = 0
    
    is_2_done = False
    is_3_done = False
    is_41_done = False
    is_42_done = False
    is_5_done = False

    for row in range(8):
        for column in range(8):
            if RADAR[row][column]>=2 and RADAR[row][column]<=6:
            
                H_zone = False
                V_zone = False
                sure_is_H = False
                sure_is_V = False
                    
                ship_span = RADAR[row][column]
                ship_name = ship_span
                if ship_name==4: ship_name=41
                if ship_span>=5: 
                    if ship_span==5: ship_name=42
                    if ship_span==6: ship_name=5
                    ship_span = ship_span-1
                    
                if (ship_name==2 and is_2_done==False and is_2_alive) or (ship_name==3 and is_3_done==False and is_3_alive) or (ship_name==41 and is_41_done==False and is_41_alive) or (ship_name==42 and is_42_done==False and is_42_alive) or (ship_name==5 and is_5_done==False and is_5_alive):
                    print('RADAR screening for ship',ship_name)
                    
                    if ship_name==2: is_2_done=True
                    if ship_name==3: is_3_done=True
                    if ship_name==41: is_41_done=True
                    if ship_name==42: is_42_done=True
                    if ship_name==5: is_5_done=True
                    
                    for i in range(ship_span):
                        offset = i+1
                        if row-offset>=0 and RADAR[row-offset][column]==RADAR[row][column]: sure_is_V = True
                        if row-offset<0 or (RADAR[row-offset][column]!=0 and RADAR[row-offset][column]!=RADAR[row][column] and RADAR[row-offset][column]!=1): break
                    up_spots = offset-1
                    for i in range(ship_span):
                        offset = i+1
                        if row+offset<=7 and RADAR[row+offset][column]==RADAR[row][column]: sure_is_V = True
                        if row+offset>7 or (RADAR[row+offset][column]!=0 and RADAR[row+offset][column]!=RADAR[row][column] and RADAR[row+offset][column]!=1): break
                    down_spots = offset-1
                    
                    for i in range(ship_span):
                        offset = i+1
                        if column-offset>=0 and RADAR[row][column-offset]==RADAR[row][column]: sure_is_H = True
                        if column-offset<0 or (RADAR[row][column-offset]!=0 and RADAR[row][column-offset]!=RADAR[row][column] and RADAR[row][column-offset]!=1): break
                    left_spots = offset-1
                    for i in range(ship_span):
                        offset = i+1
                        if column+offset<=7 and RADAR[row][column+offset]==RADAR[row][column]: sure_is_H = True
                        if column+offset>7 or (RADAR[row][column+offset]!=0 and RADAR[row][column+offset]!=RADAR[row][column] and RADAR[row][column+offset]!=1): break
                    right_spots = offset-1
                    if down_spots+up_spots+1>=ship_span: V_zone = True    
                    if left_spots+right_spots+1>=ship_span: H_zone = True
                    
                    if V_zone and sure_is_H==False:
                        print('Ship',ship_name,'can be placed vertically (U',up_spots,':D',down_spots,')')
                        for i in range(up_spots):
                            if RADAR[row-i-1][column]==0: NEXT_TARGET.append(10*(row-i-1)+column)
                        for i in range(down_spots):
                            if RADAR[row+i+1][column]==0: NEXT_TARGET.append(10*(row+i+1)+column)
                    if H_zone and sure_is_V==False:
                        print('Ship',ship_name,'can be placed horizontally (L',left_spots,':R',right_spots,')')
                        for i in range(left_spots):
                            if RADAR[row][column-i-1]==0: NEXT_TARGET.append(10*(row)+column-i-1)
                        for i in range(right_spots):
                             if RADAR[row][column+i+1]==0: NEXT_TARGET.append(10*(row)+column+i+1)
                             
    if len(NEXT_TARGET)==0 and (is_2_damaged or is_3_damaged or is_41_damaged or is_42_damaged or is_5_damaged):
        for row in range(8):
            for column in range(8):
                if RADAR[row][column]==1:
                    if row>0 and RADAR[row-1][column]==0:
                        NEXT_TARGET.append(10*(row-1)+column)
                        break
                    if row<7 and RADAR[row+1][column]==0:
                        NEXT_TARGET.append(10*(row+1)+column)
                        break
                    if column>0 and RADAR[row][column-1]==0:
                        NEXT_TARGET.append(10*(row)+column-1)
                        break
                    if column<7 and RADAR[row][column+1]==0:
                        NEXT_TARGET.append(10*(row)+column+1)
                        break
                    

def get_enemy_state(x,y,salve,pixels):

    global looking_for

    global enemy_state
    global count_hit
    global RADAR
    
    global H21
    global H22
    
    global H31
    global H32
    global H33
    
    global H411
    global H412
    global H413
    global H414
    
    global H421
    global H422
    global H423
    global H424
    
    global H51
    global H52
    global H53
    global H54
    global H55
    
    global is_2_alive
    global is_3_alive
    global is_41_alive
    global is_42_alive
    global is_5_alive
    
    global just_hit_2
    global just_hit_3
    global just_hit_41
    global just_hit_42
    global just_hit_5
    
    global is_2_damaged
    global is_3_damaged
    global is_41_damaged
    global is_42_damaged
    global is_5_damaged
    
    just_hit_2 = False
    just_hit_3 = False
    just_hit_41 = False
    just_hit_42 = False
    just_hit_5 = False
    
    global just_hit
    
    just_hit=False
    
    H21 = pixels[1130,105][1]<pixels[1130,105][0]
    H22 = pixels[1140,105][1]<pixels[1140,105][0]
    
    H31 = pixels[1157,105][1]<pixels[1157,105][0]
    H32 = pixels[1166,105][1]<pixels[1166,105][0]
    H33 = pixels[1176,105][1]<pixels[1176,105][0]
    
    H411 = pixels[1194,105][1]<pixels[1194,105][0]
    H412 = pixels[1203,105][1]<pixels[1203,105][0]
    H413 = pixels[1213,105][1]<pixels[1213,105][0]
    H414 = pixels[1222,105][1]<pixels[1222,105][0]
    
    H421 = pixels[1194,117][1]<pixels[1194,117][0]
    H422 = pixels[1204,117][1]<pixels[1204,117][0]
    H423 = pixels[1213,117][1]<pixels[1213,117][0]
    H424 = pixels[1222,117][1]<pixels[1222,117][0]
    
    H51 = pixels[1140,117][1]<pixels[1140,117][0]
    H52 = pixels[1148,117][1]<pixels[1148,117][0]
    H53 = pixels[1158,117][1]<pixels[1158,117][0]
    H54 = pixels[1167,117][1]<pixels[1167,117][0]
    H55 = pixels[1176,117][1]<pixels[1176,117][0]
    
    if (H51 and H52 and H53 and H54 and H55): 
        print('Enemy ship 5 is down')
        is_5_alive = False
        is_5_damaged = False
    if (H421 and H422 and H423 and H424): 
        print('Enemy ship 42 is down')
        is_42_alive = False
        is_42_damaged = False
    if (H411 and H412 and H413 and H414): 
        print('Enemy ship 41 is down')
        is_41_alive = False
        is_41_damaged = False
    if (H31 and H32 and H33): 
        print('Enemy ship 3 is down')
        is_3_alive = False
        is_3_damaged = False
    if (H21 and H22): 
        print('Enemy ship 2 is down')
        is_2_alive = False
        is_2_damaged = False
        
    if looking_for==5 and is_5_alive==False: looking_for=4
    if looking_for==4 and is_41_alive==False and is_42_alive==False: looking_for=3
    if looking_for==3 and is_3_alive==False: looking_for=2
    
    print('Looking for ship with a span of ',looking_for)
    
    new_enemy_state = str(int(H21))+str(int(H22))+str(int(H31))+str(int(H32))+str(int(H33))+str(int(H411))+str(int(H412))+str(int(H413))+str(int(H414))+str(int(H421))+str(int(H422))+str(int(H423))+str(int(H424))+str(int(H51))+str(int(H52))+str(int(H53))+str(int(H54))+str(int(H55))
    
    new_count_hit = int(H21)+int(H22)+int(H31)+int(H32)+int(H33)+int(H411)+int(H412)+int(H413)+int(H414)+int(H421)+int(H422)+int(H423)+int(H424)+int(H51)+int(H52)+int(H53)+int(H54)+int(H55)
    
    if new_count_hit==18:
        print('WIN!!')
        WIN = True
        return True
    
    target_id = 0
    
    if new_count_hit!=count_hit:
        for i in range(18):
            if new_enemy_state[i]!=enemy_state[i]:
                if i<2:
                    print('Just hit enemy ship 2')
                    target_id = 2
                    just_hit_2 = True
                    is_2_damaged = True
                elif i<5:
                    print('Just hit enemy ship 3')
                    target_id = 3
                    just_hit_3 = True
                    is_3_damaged = True
                elif i<9:
                    print('Just hit enemy ship 41')
                    target_id = 4
                    just_hit_41 = True
                    is_41_damaged = True
                elif i<13:
                    print('Just hit enemy ship 42')
                    target_id = 5
                    just_hit_42 = True
                    is_42_damaged = True
                else:
                    print('Just hit enemy ship 5')
                    target_id = 6
                    just_hit_5 = True
                    is_42_damaged = True
    
    if int(just_hit_2)+int(just_hit_3)+int(just_hit_41)+int(just_hit_42)+int(just_hit_5)>1:
        multiple_target = True
        target_id=1
    else:
        multiple_target = False
        
    enemy_state = new_enemy_state
    
    count_hit = new_count_hit
    
    print(enemy_state)
    
    new_pixels = PIL.ImageGrab.grab().load()
    
    color_map = pixels[POSITIONS_HAUT[x][y][0],POSITIONS_HAUT[x][y][1]]
    color_map_1 = pixels[POSITIONS_HAUT[x][y][0]-2,POSITIONS_HAUT[x][y][1]]
    color_map_2 = pixels[POSITIONS_HAUT[x][y][0]+2,POSITIONS_HAUT[x][y][1]]
    new_color_map = new_pixels[POSITIONS_HAUT[x][y][0],POSITIONS_HAUT[x][y][1]]
    new_color_map_1 = new_pixels[POSITIONS_HAUT[x][y][0]-2,POSITIONS_HAUT[x][y][1]]
    new_color_map_2 = new_pixels[POSITIONS_HAUT[x][y][0]+2,POSITIONS_HAUT[x][y][1]]
    
    if RADAR[x][y]==0 or (RADAR[x][y]==1 and target_id>1):
        RADAR[x][y]=target_id*int(((color_map[0]>50) or (color_map_1[0]>50) or (color_map_2[0]>50)) and ((new_color_map[0]>50) or (new_color_map_1[0]>50) or (new_color_map_2[0]>50)))
        if RADAR[x][y]==0: RADAR[x][y]=9
        print('M:',x,':',y,' > ',color_map)
    if salve:
        if x>0: 
            color_map = pixels[POSITIONS_HAUT[x-1][y][0],POSITIONS_HAUT[x-1][y][1]]
            color_map_1 = pixels[POSITIONS_HAUT[x-1][y][0]-2,POSITIONS_HAUT[x-1][y][1]]
            color_map_2 = pixels[POSITIONS_HAUT[x-1][y][0]+2,POSITIONS_HAUT[x-1][y][1]]
            new_color_map = new_pixels[POSITIONS_HAUT[x-1][y][0],POSITIONS_HAUT[x-1][y][1]]
            new_color_map_1 = new_pixels[POSITIONS_HAUT[x-1][y][0]-2,POSITIONS_HAUT[x-1][y][1]]
            new_color_map_2 = new_pixels[POSITIONS_HAUT[x-1][y][0]+2,POSITIONS_HAUT[x-1][y][1]]
            if RADAR[x-1][y]==0 or (RADAR[x-1][y]==1 and target_id>1):
                RADAR[x-1][y]=target_id*int(((color_map[0]>50) or (color_map_1[0]>50) or (color_map_2[0]>50)) and ((new_color_map[0]>50) or (new_color_map_1[0]>50) or (new_color_map_2[0]>50)))
                if RADAR[x-1][y]==0: RADAR[x-1][y]=9
                print('S1:',x-1,':',y,' > ',color_map)
        if x<7: 
            color_map = pixels[POSITIONS_HAUT[x+1][y][0],POSITIONS_HAUT[x+1][y][1]]
            color_map_1 = pixels[POSITIONS_HAUT[x+1][y][0]-2,POSITIONS_HAUT[x+1][y][1]]
            color_map_2 = pixels[POSITIONS_HAUT[x+1][y][0]+2,POSITIONS_HAUT[x+1][y][1]]
            new_color_map = new_pixels[POSITIONS_HAUT[x+1][y][0],POSITIONS_HAUT[x+1][y][1]]
            new_color_map_1 = new_pixels[POSITIONS_HAUT[x+1][y][0]-2,POSITIONS_HAUT[x+1][y][1]]
            new_color_map_2 = new_pixels[POSITIONS_HAUT[x+1][y][0]+2,POSITIONS_HAUT[x+1][y][1]]
            if RADAR[x+1][y]==0 or (RADAR[x+1][y]==1 and target_id>1):
                RADAR[x+1][y]=target_id*int(((color_map[0]>50) or (color_map_1[0]>50) or (color_map_2[0]>50)) and ((new_color_map[0]>50) or (new_color_map_1[0]>50) or (new_color_map_2[0]>50)))
                if RADAR[x+1][y]==0: RADAR[x+1][y]=9
                print('S2:',x+1,':',y,' > ',color_map)
        if y>0: 
            color_map = pixels[POSITIONS_HAUT[x][y-1][0],POSITIONS_HAUT[x][y-1][1]]
            color_map_1 = pixels[POSITIONS_HAUT[x][y-1][0]-2,POSITIONS_HAUT[x][y-1][1]]
            color_map_2 = pixels[POSITIONS_HAUT[x][y-1][0]+2,POSITIONS_HAUT[x][y-1][1]]
            new_color_map = new_pixels[POSITIONS_HAUT[x][y-1][0],POSITIONS_HAUT[x][y-1][1]]
            new_color_map_1 = new_pixels[POSITIONS_HAUT[x][y-1][0]-2,POSITIONS_HAUT[x][y-1][1]]
            new_color_map_2 = new_pixels[POSITIONS_HAUT[x][y-1][0]+2,POSITIONS_HAUT[x][y-1][1]]
            if RADAR[x][y-1]==0 or (RADAR[x][y-1]==1 and target_id>1):
                RADAR[x][y-1]=target_id*int(((color_map[0]>50) or (color_map_1[0]>50) or (color_map_2[0]>50)) and ((new_color_map[0]>50) or (new_color_map_1[0]>50) or (new_color_map_2[0]>50)))
                if RADAR[x][y-1]==0: RADAR[x][y-1]=9
                print('S3:',x,':',y-1,' > ',color_map)
        if y<7: 
            color_map = pixels[POSITIONS_HAUT[x][y+1][0],POSITIONS_HAUT[x][y+1][1]]
            color_map_1 = pixels[POSITIONS_HAUT[x][y+1][0]-2,POSITIONS_HAUT[x][y+1][1]]
            color_map_2 = pixels[POSITIONS_HAUT[x][y+1][0]+2,POSITIONS_HAUT[x][y+1][1]]
            new_color_map = new_pixels[POSITIONS_HAUT[x][y+1][0],POSITIONS_HAUT[x][y+1][1]]
            new_color_map_1 = new_pixels[POSITIONS_HAUT[x][y+1][0]-2,POSITIONS_HAUT[x][y+1][1]]
            new_color_map_2 = new_pixels[POSITIONS_HAUT[x][y+1][0]+2,POSITIONS_HAUT[x][y+1][1]]
            if RADAR[x][y+1]==0 or (RADAR[x][y+1]==1 and target_id>1):
                RADAR[x][y+1]=target_id*int(((color_map[0]>50) or (color_map_1[0]>50) or (color_map_2[0]>50)) and ((new_color_map[0]>50) or (new_color_map_1[0]>50) or (new_color_map_2[0]>50)))
                if RADAR[x][y+1]==0: RADAR[x][y+1]=9
                print('S4:',x,':',y+1,' > ',color_map)

def map_redo():

    global GRILLE
    GRILLE = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    
    global line1
    global line2
    global line3
    global line4
    global line5
    global line6
    global line7
    global line8
    global column1
    global column2
    global column3
    global column4
    global column5
    global column6
    global column7
    global column8
    
    map_grid(POSITIONS_BAS,PIL.ImageGrab.grab().load())
    
    line1 = matrix_to_string(GRILLE[0])
    line2 = matrix_to_string(GRILLE[1])
    line3 = matrix_to_string(GRILLE[2])
    line4 = matrix_to_string(GRILLE[3])
    line5 = matrix_to_string(GRILLE[4])
    line6 = matrix_to_string(GRILLE[5])
    line7 = matrix_to_string(GRILLE[6])
    line8 = matrix_to_string(GRILLE[7])
    column1 = matrix_to_string(get_column(GRILLE,0))
    column2 = matrix_to_string(get_column(GRILLE,1))
    column3 = matrix_to_string(get_column(GRILLE,2))
    column4 = matrix_to_string(get_column(GRILLE,3))
    column5 = matrix_to_string(get_column(GRILLE,4))
    column6 = matrix_to_string(get_column(GRILLE,5))
    column7 = matrix_to_string(get_column(GRILLE,6))
    column8 = matrix_to_string(get_column(GRILLE,7))

def retry():
    reshuffle()
    map_redo()
    display_grid(GRILLE)
    
def fire():
    click(960,800)
    
def identify_all_ships():

    if still_time_to_place_ships==False: 
        print('aborting because no time to place ships')
        return False

    global SHIP2
    global SHIP3
    global SHIP41
    global SHIP42
    global SHIP5

    SHIP5 = find_ship(5)
    if (SHIP5==False): return False
    GRILLE = remove_ship_from_grid(SHIP5)
    SHIP41 = find_ship(41)
    if (SHIP41==False): return False
    GRILLE = remove_ship_from_grid(SHIP41)
    SHIP42 = find_ship(42)
    if (SHIP42==False): return False
    GRILLE = remove_ship_from_grid(SHIP42)
    SHIP3 = find_ship(3)
    if (SHIP3==False): return False
    GRILLE = remove_ship_from_grid(SHIP3)
    SHIP2 = find_ship(2)
    if (SHIP2==False): return False
    
    map_redo()
    
    return True
    
def try_to_place_all_ships():

    reshuffle();
    click(1110,970);
    return True;
    
    screenshot()
    
    retry_find = 0

    map_redo()
    if still_time_to_place_ships==False: return False
    display_grid(GRILLE)
    while identify_all_ships()==False and still_time_to_place_ships==True:
        retry_find=retry_find+1
        if keyboard.is_pressed("q"):
            keyboard.release("q")
            raise SystemExit
        print('Could not find all ships, retrying')
        if retry_find<=10:
            retry()
        else:
            print('Too many retries finding ships, exiting')
            click(1110,970)
            return False

    test1=place_ship(2,False,False)
    test2=place_ship(3,False,False)
    test3=place_ship(41,False,False)
    test4=place_ship(42,False,False)
    test5=place_ship(5,False,False)

    if (test1 and test2 and test3 and test4 and test5): 
        click(1110,970)
        return True

    display_grid(GRILLE)
    
    screenshot()
    
    if keyboard.is_pressed("q"):
        keyboard.release("q")
        raise SystemExit

    test1=place_ship(2,True,False)
    test1=place_ship(3,True,False)
    test1=place_ship(41,True,False)
    test1=place_ship(42,True,False)
    test1=place_ship(5,True,False)
    
    if (test1 and test2 and test3 and test4 and test5): 
        click(1110,970)
        return True

    display_grid(GRILLE)
    
    screenshot()
    
    if keyboard.is_pressed("q"):
        keyboard.release("q")
        raise SystemExit

    test1=place_ship(2,True,False)
    test1=place_ship(3,True,False)
    test1=place_ship(41,True,False)
    test1=place_ship(42,True,False)
    test1=place_ship(5,True,False)
    
    if (test1 and test2 and test3 and test4 and test5): 
        click(1110,970)
        return True
    
    screenshot()
    
    if keyboard.is_pressed("q"):
        keyboard.release("q")
        raise SystemExit

    display_grid(GRILLE)

    if (place_ship(2,True,True) and place_ship(3,True,True) and place_ship(41,True,True) and place_ship(42,True,True) and place_ship(5,True,True)):
        click(1110,970)
        print('YOUHOU')
        return True
    else:
        print('Could not place all ships')
        return False
        
def core():
    count_strike = 0
    global win_count
    
    retry_place = 0
    while try_to_place_all_ships()==False and still_time_to_place_ships==True:

        if keyboard.is_pressed("q"):
            keyboard.release("q")
            raise SystemExit
            
        retry_place = retry_place+1
        if retry_place>10:
            print('Too many retries placing ships, exiting')
            break
        print('Retrying completely')
    if still_time_to_place_ships==False:
        print('Too late to place ships')
    print('Waiting for my turn')
    count_strike = 0
    while True:
        print('Count strike is ',count_strike)
        if keyboard.is_pressed("q"):
            keyboard.release("q")
            raise SystemExit
        
        pixels = PIL.ImageGrab.grab().load() 
        if pixels[1150,950]==(255,215,28) or pixels[1150,950]==(255,216,28):
            print('LOST :(')
            return False
        
        if pixels[960,800]==(103,6,0):
            time.sleep(0.5)
            
            radar_analysis()
            if len(NEXT_TARGET)==0:
                target_x = (TARGET_LIST[count_strike]//10);
                target_y = (TARGET_LIST[count_strike]%10);
                while RADAR[target_x][target_y]!=0 or target_span(target_x,target_y)<looking_for:
                    count_strike=count_strike+1
                    print('count strike is now', count_strike)
                    if count_strike>63: 
                        print('count strike > 63 aborting')
                        return False
                    target_x = (TARGET_LIST[count_strike]//10);
                    target_y = (TARGET_LIST[count_strike]%10);
            else:
                target_x = (NEXT_TARGET[0]//10);
                target_y = (NEXT_TARGET[0]%10);
            
            click(POSITIONS_HAUT[target_x][target_y][0],POSITIONS_HAUT[target_x][target_y][1])
            time.sleep(0.2)
            print('Firing on : ',target_x,':',target_y)
            fire()
            time.sleep(1)
            pixels1 = PIL.ImageGrab.grab().load()
            time.sleep(0.005)
            pixels2 = PIL.ImageGrab.grab().load()
            salve = False
            
            if (target_y>0): 
                salve_px = pixels1[POSITIONS_HAUT[target_x][target_y-1][0],POSITIONS_HAUT[target_x][target_y-1][1]]
            else: 
                salve_px = pixels2[POSITIONS_HAUT[target_x][target_y+1][0],POSITIONS_HAUT[target_x][target_y+1][1]]
                
            if salve_px[0]>240 and salve_px[1]>240 and salve_px[2]>150:
                print("SALVE : ",salve_px)
                time.sleep(1.3)
                salve = True
            else:
                print("PAS DE SALVE : ",salve_px)
                time.sleep(1.2)                

            if len(NEXT_TARGET)==0: count_strike=count_strike+1
            
            screenshot()
            
            pixels = PIL.ImageGrab.grab().load()
            
            get_enemy_state(target_x,target_y,salve,pixels)
            if WIN:
                win_count = win_count+1
                if play_count>1:
                    print('WIN RATIO : ',win_count,'/',play_count)
                return True
            display_grid(RADAR)
            
            time.sleep(1)    
            
            if count_strike>len(TARGET_LIST)-1: 
                print('count_strike>len(target_list-1)')
                raise SystemExit

while True:
    print("I'm in a loop")
    if keyboard.is_pressed("q"):
        keyboard.release("q")
        raise SystemExit
    pixels = PIL.ImageGrab.grab().load()
    if around_color(pixels[877,800],(255,221,28),2):
        click(877,800)
        time.sleep(0.25)
        print('Starting Game')
    if around_color(pixels[1015,960],(249,211,32),2):
        click(1015,960)
        time.sleep(0.25)
        print('Taking Loots')
        prepare_next_game()
    if around_color(pixels[1150,950],(255,216,28),2):
        click(1150,950)
        prepare_next_game()
        print('Restarting Game')
    if around_color(pixels[1180,980],(249,209,32),2):
        print('Starting Core')
        time.sleep(0.25)
        play_count=play_count+1
        core()