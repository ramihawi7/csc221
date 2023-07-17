from gasp import *          

begin_graphics()            
for y in range(0,480,10):
    Line((0,y),(640,y),thickness=.01,color='lightgray')
for x in range(0,640,10):
    Line((x,0),(x,640),thickness=.01,color='lightgray')


finished = False
def place_player():
    print("Here I am!")

def move_player():
    print("I'm moving...")
place_player()

while not finished:
    move_player()

update_when('key_pressed')
end_graphics() 
