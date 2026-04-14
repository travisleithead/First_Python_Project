import time

print("Welcome to BOXED\n" +

"\n" + "\n" +

"use WASD for movement\n" +

"\n" + "\n")


game = True

level = 1

#starting point
char_pos = 1

#map1 global variables
var1 = " "
var2 = " "
var3 = " "
var4 = " "
var5 = " "
var6 = " "
var7 = " "
var8 = " "
var9 = " "

#map2 global variables
var2_1 = " "
var2_2 = " "
var2_3 = " "
var2_4 = " "
var2_5 = " "
var2_6 = "*"
var2_7 = " "
var2_8 = " "
var2_9 = " "



    ###     ###          ###       ########
   #####   #####        #####      ##     ##
  ##   ## ##   ##      ##   ##     ##      ##
  ##   ## ##   ##      ##   ##     ##     ##
 ##      #      ##    #########    ########
 ##             ##   ##       ##   ##
 ##             ##   ##       ##   ##

#################################################################

def draw_map():

#sets traversable grid to blank
   
    if level == 1:

        print("Lv1")

        print(
        "+ - - - +\n" + 
        "|" + " " + var1 + " " + var2 + " " + var3 + " " + "|\n" + 
        "|" + " " + var4 + " " + var5 + " " + var6 + " " + "|\n" + 
        "|" + " " + var7 + "[" + var8 + "]" + var9 + " " + "|\n" + 
        "+ - - - +"
        )
        print("you moved!\n")

    elif level == 2:

        print("Lv2")
        print(
        "+ - - - +\n" + 
        "|" + " " + var2_1 + "[" + var2_2 + "]" + var2_3 + " " + "|\n" + 
        "|" + " " + var2_4 + " " + var2_5 + "  " + var2_6 + "|\n" + 
        "|" + " " + var2_7 + " " + var2_8 + " " + var2_9 + " " + "|\n" + 
        "+ - - - +"
        )
        print("you moved!\n")


def is_level_active():

#map1 global variables
    global var1
    global var2
    global var3
    global var4
    global var5
    global var6
    global var7
    global var8
    global var9

#map2 global variables
    global var2_1
    global var2_2
    global var2_3
    global var2_4
    global var2_5
    global var2_6
    global var2_7
    global var2_8
    global var2_9

#checks for player position, and assigns position based on that data

#map1 update statements

    var1 = " "
    var2 = " "
    var3 = " "
    var4 = " "
    var5 = " "
    var6 = " "
    var7 = " "
    var8 = " "
    var9 = " "

    if char_pos == 1:
        var1 = "\b"

    if char_pos == 2:
        var2 = "\b"

    if char_pos == 3:
        var3 = "\b"

    if char_pos == 4:
        var4 = "\b"

    if char_pos == 5:
        var5 = "\b"

    if char_pos == 6:
        var6 = "\b"

    if char_pos == 7:
        var7 = "\b"

    if char_pos == 8:
        var8 = "\b"

    if char_pos == 9:
        var9 = "\b"


#map2 update statements
    var2_1 = " "
    var2_2 = " "
    var2_3 = " "
    var2_4 = " "
    var2_5 = " "
    var2_6 = "*"
    var2_7 = " "
    var2_8 = " "
    var2_9 = " "

    if char_pos == 1:
        var2_1 = "\b"

    if char_pos == 2:
        var2_2 = "\b"

    if char_pos == 3:
        var2_3 = "\b"

    if char_pos == 4:
        var2_4 = "\b"

    if char_pos == 5:
        var2_5 = "\b"

    if char_pos == 6:
        var2_6 = "\b"

    if char_pos == 7:
        var2_7 = "\b"

    if char_pos == 8:
        var2_8 = "\b"

    if char_pos == 9:
        var2_9 = "\b"

    if level == 1:
        return char_pos != 8
    elif level == 2:
        return char_pos != 6

def change_level():
    global level
    global game
    global char_pos

    if level == 2:
        is_level_active()
        draw_map()
        return False

    is_level_active()
    draw_map()
    level = 2
    game = True
    char_pos = 2
    is_level_active()
    #draw_map()
    return True




"""
for char_pos in range (1, 9):
    if level == 1:
        print(char_pos)
        char_pos = int(input())
        print("Lv1")
        draw_map()
    
        if char_pos == 8:
            print("you expanded the map!\n")
            level = 2
        else:
            print("you moved!")
    


if level == 2:
    char_pos = 2
    print("")
    print("entering Lv2")
    draw_map2()


for char_pos in range (1, 9):
    char_pos = int(input())
    print("Lv2")
    draw_map2()
    
    print("you moved!")
    break
"""

is_level_active()
while game:
    draw_map()
    char_pos = int(input())
    game = is_level_active()
    if game == False:
        game = change_level()