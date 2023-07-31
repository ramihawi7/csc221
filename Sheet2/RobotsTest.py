
from gasp import * # As usual
import random
 
 
class Player:
    pass
 
 
class Robot:
    pass
 
 
def place_player():
    global player

    player = Player()

    player.x = random.randint(0, 63)
    player.y = random.randint(0, 47)


def safely_place_player():
    global player

    place_player()

    while collided(player, robots):
        place_player()

    player.shape = Circle(
    (   10 * player.x + 5, 10 * player.y + 5), 5, filled=True
    )


def place_robots():
    global robots

    robots = []

    while len(robots) < numbots:
        robot = Robot()
        robot.x = random.randint(0, 63)
        robot.y = random.randint(0, 47)
        robot.junk = False
        robot.shape = Box((10 * robot.x, 10 * robot.y), 10, 10)
        robots.append(robot)



def move_player():
    global player
 
    key = update_when("key_pressed")

    while key == "h":
        remove_from_screen(player.shape)
        safely_place_player()
        key = update_when("key_pressed")
 
    if key == "b":
        if player.x > 0:
            player.x −= 1
        if player.y > 0:
            player.y −= 1
    elif key == "n" and player.y > 0:
        player.y −= 1
    elif key == "m":
        if player.x < 63:
            player.x += 1
        if player.y > 0:
            player.y −= 1
    elif key == "g" and player.x > 0:
        player.x −= 1
    elif key == "j" and player.x < 63:
        player.x += 1
    elif key == "t":
        if player.x > 0:
            player.x −= 1
        if player.y < 47:
            player.y += 1
    elif key == "y" and player.y < 47:
        player.y += 1
    elif key == "u":
        if player.x < 63:
            player.x += 1
        if player.y < 47:
            player.y += 1

    move_to(player.shape, (10 * player.x + 5, 10 * player.y + 5))
 88
 89
 90 def move_robots():
 91 global robots
 92
 93 for robot in robots:
 94 if not robot.junk:
 95 if robot.x > player.x:
 96 robot.x −= 1
 97 elif robot.x < player.x:
 98 robot.x += 1
 99
 100 if robot.y > player.y:
 101 robot.y −= 1
 102 elif robot.y < player.y:
 103 robot.y += 1
 104
 105 move_to(robot.shape, (10 * robot.x, 10 * robot.y))
 106
 107
 108 def collided(thing1, list_of_things):
 109 for thing2 in list_of_things:
 110 if thing1.x == thing2.x and thing1.y == thing2.y:
 111 return True
 112 return False
 113
 114
 115
robots.py[+] Page 3
 116 def robot_crashed(the_bot):
 117 for a_bot in robots:
 118 if a_bot == the_bot:
 119 return False
 120 if a_bot.x == the_bot.x and a_bot.y == the_bot.y:
 121 return a_bot
 122 return False
 123
 124
 125 def check_collisions():
 126 global finished, robots
 127
 128 # Handle player crashes into robot
 129 if collided(player, robots):
 130 finished = True
 131 Text("You've been caught!", (320, 240), size=22)
 132 sleep(3)
 133 return
 134
 135 # Handle robots crashing into each other
 136 surviving_robots = []
 137
 138 for robot in robots:
 139 if collided(robot, junk):
 140 continue
 141
 142 zombie = robot_crashed(robot)
 143
 144 if not zombie:
 145 surviving_robots.append(robot)
 146 else:
 147 remove_from_screen(zombie.shape)
 148 zombie.junk = True
 149 zombie.shape = Box(
 150 (10 * zombie.x, 10 * zombie.y), 10, 10, filled=True
 151 )
 152 junk.append(zombie)
 153
 154 robots = []
 155
 156 for robot in surviving_robots:
 157 if not collided(robot, junk):
 158 robots.append(robot)
 159
 160 if not robots:
 161 finished = True
 162 Text("You win!", (160, 240), size=24)
 163 sleep(3)
 164 return
 165
 166
 167 begin_graphics() # So that you can draw things
 168
 169 finished = False
 170 numbots = 4
 171 junk = []
 172
 173 place_robots()
 174 safely_place_player()
 175
 176 while not finished:
 177 move_player()
 178 move_robots()
 179 check_collisions()
 180
 181 end_graphics() # Finished!