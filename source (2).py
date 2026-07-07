


#           The underground mapping tool (UMT)


#       diagram for room vars.

#   VISIBLE ATRIBUTES

#   0 = corner, "+"
#   1 = horizontal wall, " -"
#   3 = vertical wall, "|"
#   4 = traversable space, " "
#   8 = treasure, "*"

#   INVISIBLE ATRIBUTES

#   2 = corner 
#   5 = horizontal wall
#   6 = verical wall
#   7 = traversable space
#   9 = treasure, "*"

#   DOOR TYPES "[ ]" (VISABLE)

#   10 = w, up
#   20 = s, down
#   30 = a, left
#   40 = d, right

#   DOOR TYPES "[ ]" (INVISABLE)

#   -10 = w, up
#   -20 = s, down
#   -30 = a, left
#   -40 = d, right

#       diagram for invintory vars.

#   VISIBLE ATRIBUTES

#   0 = corner, "+"
#   1 = horizontal wall, " -"
#   3 = vertical wall, "|"
#   4 = traversable space, " "

#   INVISIBLE ATRIBUTES

#   2 = corner 
#   5 = horizontal wall
#   6 = verical wall

#   GLOBAL VARIABLES

char_row = 7

char_column = 7

game = True

scene_type = 1

controller_type = 1

#   GLOBAL VARIABLES FOR INVENTORY

inventory = True

# [TL] I noticed that you have TWO "sources of truth" for your inventory.
#      The first are these sets of global variables slotX and slotX_select
#      which are the globals you are changing in the inventory controller.
#      The second are down in another global variable that you called
#      "invintory" (not to be confused with "inventory" ;-)
#      To get the inventory system working, you'll need to pick one of these
#      two "sources of truth" to be the actual source of truth. My recommendation
#      is to use the array "invintory" vs the sets of globals.

slot1 = 4

slot2 = 4

slot3 = 4

slot4 = 4

slot5 = 4

slot6 = 4

slot7 = 4

slot8 = 4

slot9 = 4




#   GLOBAL VARIABLES FOR INVENTORY SELECTORS

slot1_select = 1

slot2_select = 1

slot3_select = 1

slot4_select = 1

slot5_select = 1

slot6_select = 1

slot7_select = 1

slot8_select = 1

slot9_select = 1


#draw functon assums world has no errors
#somebodys elses resposibily to ensure character is in a legal position

#FUNCTIONS

def is_wall(row, column):
    if not is_in_world(row, column):
        return True
    if room_parts[row][column] in(0, 1, 2, 3, 5, 6):
        return True
    return False



def is_corner(row, column):
    if not is_in_world(row, column):
        return False
    if room_parts[row][column] in(0, 2):
        return True
    return False


def is_in_world(row, column):
    if row >= len(room_parts):
        return False
    if row < 0:
        return False
    #assums that all rows are the same size
    if column >= len(room_parts[0]):
        return False
    if column < 0:
        return False
    return True



def draw():
    if scene_type == 0:
        draw_room_parts()
    if scene_type == 1:
        draw_inventory()




def draw_room_parts():
    current_row_num = 0
    for current_row in room_parts:
        #this is pre column processing
        temp_str = ""
        current_column_num = 0
        for list_item in current_row:
            if current_column_num == char_column and current_row_num == char_row:
                temp_str = temp_str + "◻"
            elif list_item in(2, 4, 5, 6, 7, 9, -10, -20, -30, -40):
                temp_str = temp_str + " "
            elif list_item == 0:
                temp_str = temp_str + "+"
            elif list_item == 1:
                temp_str = temp_str + "-"
            elif list_item == 3:
                temp_str = temp_str + "|"
            elif list_item == 10:
                temp_str = temp_str + "^"
            elif list_item == 20:
                temp_str = temp_str + "∨"
            elif list_item == 30:
                temp_str = temp_str + "<"
            elif list_item == 40:
                temp_str = temp_str + ">"
            elif list_item == 8:
                temp_str = temp_str + "*"
            else:
                temp_str = temp_str + "?"
            temp_str = temp_str + " "
            current_column_num += 1
        #this is post column processing
        print(temp_str)
        current_row_num += 1



def draw_inventory():
    print("\n" + "use 1u, 2u, 3u ect. to select and use an item." + "\n\n" + "press q to quit the inventory" + "\n")
    current_row_num = 0
    # [TL] This draw function looks only at the "invintory" array for 
    #      deciding what to draw. It turns out that the array elements in
    #      "invintory" are never modified (by "controller_in_inventory"),
    #      so this function always draws the same thing.
    for current_row in invintory:
        #this is pre column processing
        temp_str = ""
        current_column_num = 0
        for list_item in current_row:
            if list_item in(2, 4, 5, 6, 7, 9, -10, -20, -30, -40):
                temp_str = temp_str + " "
            elif list_item == 0:
                temp_str = temp_str + "+"
            elif list_item == 1:
                temp_str = temp_str + "-"
            elif list_item == 3:
                temp_str = temp_str + "|"
            elif list_item == 10:
                temp_str = temp_str + "^"
            elif list_item == 20:
                temp_str = temp_str + "∨"
            elif list_item == 30:
                temp_str = temp_str + "<"
            elif list_item == 40:
                temp_str = temp_str + ">"
            elif list_item == 8:
                temp_str = temp_str + "*"
            elif list_item == slot1_select:
                temp_str += 10
            else:
                temp_str = temp_str + "?"
            temp_str = temp_str + " "
            current_column_num += 1
        #this is post column processing
        print(temp_str)
        current_row_num += 1
    print("\n\n\n")



def controller():
    if controller_type == 0:
        controller_in_rooms()
    if controller_type == 1:
        controller_in_inventory()
#    print(controller_type)
    


def controller_in_rooms():
    global char_column
    global char_row
    global controller_type
    global scene_type
#    global inventory
    
#    inventory = False
    button = input()
    old_loc_row = char_row
    old_loc_col = char_column
    if button == "e":
        controller_type = 1
        scene_type = 1
    if button == "a" and not is_wall(char_row, char_column - 1):
        char_column -= 1
    if button == "d" and not is_wall(char_row, char_column + 1):
        char_column += 1
    if button == "w" and not is_wall(char_row - 1, char_column):
        char_row -= 1
    if button == "s" and not is_wall(char_row + 1, char_column):
        char_row += 1
    if is_door(old_loc_row, old_loc_col) and is_hidden_door(char_row, char_column):
        if button == "a":
            discover_room(find_left_room_corners(char_row, char_column))
        if button == "d":
            discover_room(find_right_room_corners(char_row, char_column))
        if button == "w":
                    discover_room(find_top_room_corners(char_row, char_column))
        if button == "s":
                    discover_room(find_bottem_room_corners(char_row, char_column))




def controller_in_inventory():

#   global inventory
    global controller_type
    global scene_type

#   inventory = True

    button = str(input())
    if button == "q":
        controller_type = 0
        scene_type = 0



    invintory[2][1] = 1
    invintory[2][5] = 1
    invintory[2][9] = 1
    invintory[2][13] = 1
    invintory[6][1] = 1
    invintory[6][5] = 1
    invintory[6][9] = 1
    invintory[6][13] = 1
    invintory[6][18] = 1
    
    if button == "1":
       invintory[2][1] = 10
    if button == "2":
       invintory[2][5] = 10
    if button == "3":
       invintory[2][9] = 10
    if button == "4":
       invintory[2][13] = 10
    if button == "5":
       invintory[6][1] = 10
    if button == "6":
       invintory[6][5] = 10
    if button == "7":
       invintory[6][9] = 10
    if button == "8":
       invintory[6][13] = 10
    if button == "9":
       invintory[6][18] = 10

    if button == "1u":
        move_object(1)
    elif button == "2u":
        move_object(2)
    elif button == "3u":
        move_object(3)
    elif button == "4u":
        move_object(4)
    elif button == "5u":
        move_object(5)
    elif button == "6u":
        move_object(6)
    elif button == "7u":
        move_object(7)
    elif button == "8u":
        move_object(8)
    elif button == "9u":
        ninth_slot_scan()
    


def move_object(selected_item):
    source_row = 1 if selected_item < 5 else 5
    source_column = (((selected_item - 1) * 4) + 1) % 16
    if invintory[source_row][source_column] == 4:
        print("invalid entry: cannot relocate nonexistant item")
        return
    if invintory[5][18] != 4:
        print("invalid entry: cannot replace occupied slot")
        return
    invintory[5][18] = invintory[source_row][source_column]
    invintory[source_row][source_column] = 4
    #   the four different slot collumn numbers that you are trying to land in are [5][1,5,9,13]
    #   second row is 22 but we want it to be 1 I think what we do is mod it by 21



def ninth_slot_scan():
    if invintory[1][1] == 4:
        invintory[1][1] = invintory[5][18]
    elif invintory[1][5] == 4:
        invintory[1][5] = invintory[5][18]
    elif invintory[1][9] == 4:
        invintory[1][9] = invintory[5][18]
    elif invintory[1][13] == 4:
        invintory[1][13] = invintory[5][18]
    elif invintory[5][1] == 4:
        invintory[5][1] = invintory[5][18]
    elif invintory[5][5] == 4:
        invintory[5][5] = invintory[5][18]
    elif invintory[5][9] == 4:
        invintory[5][9] = invintory[5][18]
    elif invintory[5][13] == 4:
        invintory[5][13] = invintory[5][18]
    else:
        print("inventory is full")
        return
    invintory[5][18] = 4
    



def is_hidden_door(row, column):
    door = room_parts[row][column]
    if door in(-10, -20, -30, -40):
        return True
    return False



def is_door(row, column):
    door = room_parts[row][column]
    if door in(10, 20, 30, 40):
        return True
    return False



def end_game():
    if room_parts[char_row][char_column] == 8:
        return True
    return False



def find_left_corner(starting_row, starting_column):
    while True:
        if is_corner(starting_row, starting_column):
            return starting_row, starting_column
        starting_column -= 1
        if not is_in_world(starting_row, starting_column):
            print("Oops! Could not execute find_left_corner")
            return
        


def find_right_corner(starting_row, starting_column):
    while True:
        if is_corner(starting_row, starting_column):
            return starting_row, starting_column
        starting_column += 1
        if not is_in_world(starting_row, starting_column):
            print("Oops! Could not execute find_right_corner")
            return


def find_top_corner(starting_row, starting_column):
    while True:
        if is_corner(starting_row, starting_column):
            return starting_row, starting_column
        starting_row -= 1
        if not is_in_world(starting_row, starting_column):
            print("Oops! Could not execute find_top_corner")
            return


def find_bottem_corner(starting_row, starting_column):
    while True:
        if is_corner(starting_row, starting_column):
            return starting_row, starting_column
        starting_row += 1
        if not is_in_world(starting_row, starting_column):
            print("Oops! Could not execute find_bottem_corner")
            return



#   when finding room, always start clockwise.



#   always return upper corner, than bottem corner.



def find_bottem_room_corners(door_row, door_column):
    rc = find_right_corner(door_row, door_column)
    bc = find_bottem_corner(rc[0] + 1, rc[1])
    lc = find_left_corner(bc[0], bc[1] - 1)
    tc = find_top_corner(lc[0] - 1, lc[1])
    return [tc, bc]



def find_top_room_corners(door_row, door_column):
    lc = find_left_corner(door_row, door_column)
    tc = find_top_corner(lc[0] - 1, lc[1])
    rc = find_right_corner(tc[0], tc[1] + 1)
    bc = find_bottem_corner(rc[0] + 1, rc[1])
    return [tc, bc]



def find_left_room_corners(door_row, door_column):
    bc = find_bottem_corner(door_row, door_column)
    lc = find_left_corner(bc[0], bc[1] - 1)
    tc = find_top_corner(lc[0] - 1, lc[1])
    rc = find_right_corner(tc[0], tc[1] + 1)
    return [tc, bc]



def find_right_room_corners(door_row, door_column):
    tc = find_top_corner(door_row, door_column)
    rc = find_right_corner(tc[0], tc[1] + 1)
    bc = find_bottem_corner(rc[0] + 1, rc[1])
    lc = find_left_corner(bc[0], bc[1] - 1)
    return [tc, bc]



def discover_room(bounds):
    #modifies room_parts
    global room_parts
    row_start = bounds[0][0]
    row_end = bounds[1][0]
    column_start = bounds[0][1]
    column_end = bounds[1][1]
    for row in range(row_start, row_end + 1):
        for column in range(column_start, column_end + 1):
            current_item = room_parts[row][column]
            if current_item == 2:
                room_parts[row][column] = 0
            elif current_item == 5:
                room_parts[row][column] = 1
            elif current_item == 6:
                room_parts[row][column] = 3
            elif current_item == 9:
                room_parts[row][column] = 8
            elif current_item == -10:
                room_parts[row][column] = 10
            elif current_item == -20:
                room_parts[row][column] = 20
            elif current_item == -30:
                room_parts[row][column] = 30
            elif current_item == -40:
                room_parts[row][column] = 40
            elif current_item == 4:
                room_parts[row][column] = 4
            else:
                room_parts[row][column] = 99
            


room_parts =[
#0 1 2 3 4 5 6 7 8 9 ect.
[4,4,4,4,4,2,5,5,5,2,4,4,4,4,4],
[4,4,4,4,4,6,4,4,4,6,4,4,4,4,4],
[4,4,4,4,4,6,4,4,4,6,4,4,4,4,4],
[4,4,4,4,4,6,4,4,4,6,4,4,4,4,4],
[4,4,4,4,4,2,5,-20,5,2,4,4,4,4,4],
[2,5,5,5,2,0,1,10,1,0,2,5,5,5,2],
[6,4,4,4,6,3,4,4,4,3,6,4,4,4,6],
[6,4,4,4,-40,30,4,4,4,40,-30,4,4,9,6],
[6,4,4,4,6,3,4,4,4,3,6,4,4,4,6],
[2,5,5,5,2,0,1,20,1,0,2,5,5,5,2],
[4,4,4,4,4,2,5,-10,5,2,4,4,4,4,4],
[4,4,4,4,4,6,4,4,4,6,4,4,4,4,4],
[4,4,4,4,4,6,4,4,4,6,4,4,4,4,4],
[4,4,4,4,4,6,4,4,4,6,4,4,4,4,4],
[4,4,4,4,4,2,5,5,5,2,4,4,4,4,4]
]



invintory =[

[0,1,0,4,0,1,0,4,0,1,0,4,0,1,0],
[3,slot1,3,4,3,slot2,3,4,3,slot3,3,4,3,slot4,3],
[0,slot1_select,0,4,0,slot2_select,0,4,0,slot3_select,0,4,0,slot4_select,0],
[4],
[0,1,0,4,0,1,0,4,0,1,0,4,0,1,0,4,4,0,1,0],
[3,slot5,3,4,3,slot6,3,4,3,slot7,3,4,3,slot8,3,4,4,3,slot9,3],
[0,slot5_select,0,4,0,slot6_select,0,4,0,slot7_select,0,4,0,slot8_select,0,4,4,0,slot9_select,0],
]


invintory[1][1] = 8
invintory[1][5] = 8
invintory[1][9] = 8
invintory[1][13] = 8
invintory[5][1] = 8
invintory[5][5] = 8

#    TEST inventory 1by1

# [TL] This is probably where your assumption was incorrect. By putting the 
#      variables 'slot1' and 'slot1_select' into the array, I can see that
#      you hoped that the variables would "stay" there and that by changing
#      the global variables, it would update these elements in the array.
#      Unfortunately, it doesn't work like that. This code below only ever runs
#      once, to setup the array values. When it's running, the 'slot1' variable
#      is read (to extract the value it contains, which starts out as 4) and 
#      it's actually the literal value '4' that gets put into the array when it
#      is made, not the variable itself. Make sense? So, from here on out, 
#      whenever you are changing any of these global variables they ARE actually
#      getting updated, BUT the values in this array are staying the same.
#      If this array stays your "source of truth" for the inventory data, then
#      you need to modify the specific values in this array in order for the
#      "draw_inventory" function to see the changes. For example, the inventory
#      controller would need to change 'invintory' as follows to change this data:
#        invintory[1][1] = <new value for slot1>
#      The above line gets the 2nd sub-array out of 'invintory', then references
#      the 2nd array element (where you have the 'slot1' variable being read) and 
#      changes it.
#      "
"""
invintory = [
[0,1,0],
[3,slot1,3],
[0,slot1_select,0]
]

"""

#if inventory is True:
#    print("+ - +   + - +   + - +   + - +\n" +
#          "| " + slot1 + " |")
         


while game:
    draw()
    controller()
#    if inventory is True:
#        slot1_select, slot2_select, slot3_select, slot4_select, slot5_select, slot6_select, slot7_select, slot8_select, slot9_select, controller_type, scene_type, inventory = controller_in_inventory(slot1_select, slot2_select, slot3_select, slot4_select, slot5_select, slot6_select, slot7_select, slot8_select, slot9_select, controller_type, scene_type, inventory)

    game = not end_game()
    if game is False:
        draw()

#discover_room(find_bottem_room_corners(10, 7))
#discover_room(find_top_room_corners(4, 7))
#discover_room(find_left_room_corners(7, 4))
#discover_room(find_right_room_corners(7, 10))

