


#           The underground mapping tool (UMT)

import random

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

from math import floor


char_row = 7

char_column = 7

game = True

scene_type = 1

controller_type = 1

#   GLOBAL VARIABLES FOR INVENTORY

inventory = True

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
    print("\n\n" + "use 1u, 2u, 3u ect. to select and use an item." + "\n\n" + 
          "press q to quit the inventory" + "\n\n"
         )
    print("+ - +  + - +  + - +  + - +\n" + "| " + 
          (" " if i.slots[0] == None else i.slots[0].symbol) + " |" + "  " + "| " + 
          (" " if i.slots[1] == None else i.slots[1].symbol) + " |" + "  " + "| " + 
          (" " if i.slots[2] == None else i.slots[2].symbol) + " |" + "  " + "| " + 
          (" " if i.slots[3] == None else i.slots[3].symbol) + " |" + "\n" + "+ " + 
          ("^" if i.selected_slot == 0 else "-") + " +" + "  " + "+ " + 
          ("^" if i.selected_slot == 1 else "-") + " +" + "  " + "+ " + 
          ("^" if i.selected_slot == 2 else "-") + " +" + "  " + "+ " + 
          ("^" if i.selected_slot == 3 else "-") + " +\n\n" +
          "+ - +  + - +  + - +  + - +    + - +\n" + "| " + 
          (" " if i.slots[4] == None else i.slots[4].symbol) + " |" + "  " + "| " + 
          (" " if i.slots[5] == None else i.slots[5].symbol) + " |" + "  " + "| " + 
          (" " if i.slots[6] == None else i.slots[6].symbol) + " |" + "  " + "| " + 
          (" " if i.slots[7] == None else i.slots[7].symbol) + " |" + "    " + "| " + 
          (" " if i.ninth_slot == None else i.ninth_slot.symbol) + " |\n" +"+ " + 
          ("^" if i.selected_slot == 4 else "-") + " +" + "  " + "+ " + 
          ("^" if i.selected_slot == 5 else "-") + " +" + "  " + "+ " + 
          ("^" if i.selected_slot == 6 else "-") + " +" + "  " + "+ " + 
          ("^" if i.selected_slot == 7 else "-") + " +" + "    " + "+ " + 
          ("^" if i.selected_slot == 8 else "-") + " +"
         )
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

    if button == "1u":
        i.move_object(0)
    elif button == "2u":
        i.move_object(1)
    elif button == "3u":
        i.move_object(2)
    elif button == "4u":
        i.move_object(3)
    elif button == "5u":
        i.move_object(4)
    elif button == "6u":
        i.move_object(5)
    elif button == "7u":
        i.move_object(6)
    elif button == "8u":
        i.move_object(7)

    elif button == "9u":
        i.ninth_slot_scan()

    if button == "1":
        i.selected_slot = 0
    elif button == "2":
        i.selected_slot = 1
    elif button == "3":
        i.selected_slot = 2
    elif button == "4":
        i.selected_slot = 3
    elif button == "5":
        i.selected_slot = 4
    elif button == "6":
        i.selected_slot = 5
    elif button == "7":
        i.selected_slot = 6
    elif button == "8":
        i.selected_slot = 7
    elif button == "9":
        i.selected_slot = 8



class World:
    def __init__ (self, current_floor):
        self.floors = [current_floor]
        self.current_floor = current_floor
    def draw (self, world_height, world_width):
        self.current_floor.draw(world_height, world_width)



class Floor:
    def __init__ (self, current_room):
        self.rooms = [current_room]
        self.current_room = current_room
        self.previous_room = None
        self.starting_room = current_room
    def draw (self, floor_height, floor_width):
        for floor_row in range(floor_height + 1):
            symbol = ""
            for floor_column in range(floor_width + 1):
                for room in self.rooms:
                    if room.is_point_in_room(floor_row, floor_column):
                        symbol += room.get_room_symbol(floor_row, floor_column)
                    else:
                        symbol += "  "
            print(symbol)



class Room:
    def __init__ (self, character, n_wall, e_wall, s_wall, w_wall, floor_offset):
        self.is_visible = True
        self.character = character
        self.n_wall = n_wall
        self.e_wall = e_wall
        self.s_wall = s_wall
        self.w_wall = w_wall
        self.room_items = None
        self.master_map = []
        self.floor_offset = floor_offset
        self.recalculate_master_map()
    def recalculate_master_map (self):
        for row in range(self.w_wall.size - 1):
            temp_row = []
            for column in range(self.n_wall.size - 1):
                temp_row.append("  ")
            self.master_map.append(temp_row) 
        temp_row = []
        for index in range(self.n_wall.size):
            temp_row.append(self.n_wall.get_wall_symbol(index) + " ")
        self.master_map.insert(0, temp_row)
        for index in range (self.e_wall.size):
            self.master_map[index].append(self.e_wall.get_wall_symbol(index) + " ")
        temp_row = []
        for index in range (self.s_wall.size):
            temp_row.insert(0, self.s_wall.get_wall_symbol(index) + " ")
        self.master_map.append(temp_row)
        for index in range (self.w_wall.size):
            find_correct_column = (len(self.master_map) - 1 - index)
            self.master_map[find_correct_column].insert(0, self.w_wall.get_wall_symbol(index) + " ")
        self.master_map[1][1] = "□ "
    def is_point_in_room (self, floor_x, floor_y):
        if (floor_x - self.floor_offset.x) < 0 and (floor_y - self.floor_offset.y) < 0:
            return False
        if (floor_x - self.floor_offset.x) <= self.e_wall.size and \
        (floor_y - self.floor_offset.y) <= self.n_wall.size:
            return True
        return False
    def get_room_symbol (self, floor_x, floor_y):
        return self.master_map[(floor_x - self.floor_offset.x)][floor_y - self.floor_offset.y]



class Room_Item:
    def __init__ (self, x, y):
        self.item_x_pos = x
        self.item_y_pos = y



#   Note to self:
#       ensure door positions are not 0



class Wall:
    def __init__ (self, wall_size, direction):
        self.direction = direction # 0 = North, 1 = East, 2 = South, 3 = West
        self.doors = []
        self.size = wall_size
        self.door_positions = []
    def add_door (self, door, door_pos):
        if door_pos >= self.size:
            print("assertion error: door position out of bounds")
            return
        self.doors.append(door)
        self.door_positions.append(door_pos)    
    def get_wall_symbol (self, wall_position):
        self.wall_position = wall_position
        if wall_position == 0:
            return "+"
        for door_index in self.door_positions:
            if door_index == wall_position:
                if self.direction == 0:    
                    return "^"
                elif self.direction == 1:
                    return ">"
                elif self.direction == 2:
                    return "∨"
                else:
                    return "<"
#   at this point we know we have a wall because the program failed all of the door checks
        if self.direction == 0 or self.direction == 2:
            return "-"
        return "|"



class Door:
    def __init__ (self, room):
        self.type = "normal"
        self.next_room = room
        self.is_locked = False
        self.lock_type = "normal"



class Coordinate:
    def __init__ (self, x, y):
        self.x = x
        self.y = y



class Inventory:
    def __init__(self):
        self.slots = [inventory_item(map, "A crinckled up piece of paper with scrawled markings " \
                      "appearing to be in the shape of rooms you have explored", "□"),
                      None,None,None,None,None,None,None]
        self.ninth_slot = None
        self.selected_slot = 0
    def move_object(self, selected_item):
        if self.ninth_slot == None:
            i.ninth_slot = self.slots[selected_item]
            self.slots[selected_item] = None
        elif self.ninth_slot != None:
            slot_nine = self.ninth_slot
            self.ninth_slot = self.slots[selected_item]
            self.slots[selected_item] = slot_nine
    def ninth_slot_scan(self):
        for index in range(8):
            if self.slots[index] == None:
                self.slots[index] = self.ninth_slot
                self.ninth_slot = None
                return
        else:
            print("inventory is full")



class inventory_item:
    def __init__ (self, name, description, symbol):
        self.name = name
        self.description = description
        self.symbol = symbol

rand_length_side = random.choice([2, 4, 9])

rand_length_floor = random.choice([2, 4, 9])

rand_length_side = 4

rand_length_floor = 4

"""
print(rand_length_floor)

print(rand_length_side)
"""

i = Inventory()

character = Coordinate(3,3)

coordinate = Coordinate(4,4)

n_w = Wall(rand_length_floor, 0)

e_w = Wall(rand_length_side, 1)

s_w = Wall(rand_length_floor, 2)

w_w = Wall(rand_length_side, 3)

n_w.add_door(Door(None), 2)

e_w.add_door(Door(None), 2)

s_w.add_door(Door(None), 2)

w_w.add_door(Door(None), 2)

r = Room(character, n_w, e_w, s_w, w_w, coordinate)

f = Floor(r)


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


"""
while game:
    draw()
    controller()
    game = not end_game()
    if game is False:
        draw()
"""

world = World(f)

world.draw(10, 10)