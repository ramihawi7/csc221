from gasp import *
import time
from random import randint
def loose():
    time.sleep(1)
    clear_screen()
    Text("You Lost :'c",(320, 270), size=40)
    key_text = Text("Press esc to stop playing", (320, 100), size=12)
    en = update_when('key_pressed')
    clear_screen()
    if en == "Escape":
        return True
    return False
def teleport():
    global player_x
    global player_y
    while True:
        new_x = randint(1, 63)
        new_y = randint(1, 47)
        
        if new_x != robot_x and new_y != robot_y:
            player_x = new_x
            player_y = new_y
            break
 
def rob(i):
    global robot
    global game
    global player_x
    global player_y 
    global robot_x
    global robot_y
    
    if i % 2 == 0:    
        x = randint(2, 62)
        y = randint(2,47)
        while x > player_x-10 and x < player_x+10:
            x = randint(2, 47)
        while y > player_y-10 and y < player_y+10:
            y = randint(2, 63)
        robot_x.append(x)
        robot_y.append(y)
        
    for ra in range(len(robot_x)-1): 
        robot.append(Circle((10 * robot_x[ra] + 5, 10 * robot_y[ra] + 5), 5, filled=True, color="Red"))
        if player_x > robot_x[ra]:
            robot_x[ra] += 1
        elif player_x < robot_x[ra]:
            robot_x[ra] -= 1
        if player_y > robot_y[ra]:
            robot_y[ra] += 1
        elif player_y < robot_y[ra]:
            robot_y[ra] -= 1
junk_x=[]
junk_y=[]
junk=[]

junk = Box(10 * junk_x,10 *  junk_y, 10,10,color = color.GREEN)
junk.append(junk)
def py():
    global player_x
    global player_y 
    global robot_x
    global robot_y
    global robot
    
    player = Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True)
    key = update_when('key_pressed')
    for ra in robot:
        remove_from_screen(ra)
    Text(key,(320, 100), size=12)
    if key == 'KP_Right 'or key == 'd':
        player_x += 1
    elif key == 'KP_Left 'or key == 'a':
        player_x -= 1
    elif key == 'KP_Up'or key == 'w':
        player_y += 1
    elif key == 'KP_Down'or key == 'x':
        player_y -= 1
    elif key == 'KP_Prior' or key == 'e':
        player_x += 1 
        player_y += 1
    elif key == 'KP_Home' or key == 'q':
        player_x -= 1 
        player_y += 1 
    elif key == 'KP_End' or key == 'z':
        player_x -= 1
        player_y -= 1 
    elif key == 'KP_Next' or key == 'c': 
        player_x += 1 
        player_y -= 1
    elif key == 't':
        teleport()
    if player_x == 63:
        player_x = 1
    if player_y == 47:
        player_y = 1
    if player_x == 0:
        player_x = 63
    if player_y == 0:
        player_y = 47

    remove_from_screen(player)
    return
def lines():
    line_x = 0
    line_y = 0
    for y in range(0,480,10):
        Line((0,y),(640,y),thickness=.01,color='lightgray')
    for x in range(0,640,10):
        Line((x,0),(x,640),thickness=.01,color='lightgray')

def start_screen():
    key_text = Text("ROBOTS!!!", (320, 270), size=48)
    key_text = Text("Press any key to start", (320, 100), size=12)
    update_when('key_pressed')
    clear_screen()

def GGame(i):
    start_screen()
    lines()
    global game
    global player_x 
    global player_y 
    global robot_x
    global robot_y
    global robot
    robot_x = []
    robot_y = []
    robot = []
    game = True
    player_x = randint(2,63)
    player_y = randint(2,47)
    x = randint(2, 62)
    y = randint(2, 47)
    while x > player_x-10 and x < player_x+10:
        x = randint(2, 47)
    while y > player_y-10 and y < player_x+10:
        y = randint(2, 63)
    robot_x.append(x)
    robot_y.append(y)
    while game:
        i += 1
        for mm in range(len(robot_x)):
            if player_x == robot_x[mm] and player_y == robot_y[mm]:
                game = False
        py()
        rob(i)

    lost = loose()
    if not lost:
        GGame(i)


begin_graphics(title = "Robots")
i = 0
GGame(i)
end_graphics()
