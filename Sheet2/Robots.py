from gasp import *
def lines():
    line_x = 0
    line_y = 0
    for y in range(0,480,10):
        Line((0,y),(640,y),thickness=.01,color='lightgray')
    for x in range(0,640,10):
        Line((x,0),(x,640),thickness=.01,color='lightgray')

def place_player(player_x,player_y):
    Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True)
begin_graphics()            
lines()

player_x= 30
player_y= 30 


while True: 
    player = Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True)
    key = update_when('key_pressed')
    remove_from_screen(player)
    if key == 'Right':
        player_x += 1
    if key == 'Left':
        player_x -= 1
    if key == 'Up':
        player_y += 1
    if key == 'Down': 
        player_y -= 1
    if key == 'q':
        break

update_when('key_pressed')
end_graphics() 
