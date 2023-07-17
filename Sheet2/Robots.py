from gasp import *          
def lines():
    for y in range(0,480,10):
        Line((0,y),(640,y),thickness=.01,color='lightgray')
    for x in range(0,640,10):
        Line((x,0),(x,640),thickness=.01,color='lightgray')
begin_graphics()            
lines()


finished = False
def place_player(player_x,player_y):
    Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True)

def move_player():
    #hello
place_player(30,30)

while not finished:
    move_player()

update_when('key_pressed')
end_graphics() 
