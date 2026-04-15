#The underground mapping tool (UMT)


#diagram for room vars.

#   VISIBLE ATRIBUTES

#   0 = corner, "+"
#   1 = horizontal wall, " -"
#   3 = vertical wall, "|"
#   4 = traversable space, " "

#   INVISIBLE ATRIBUTES

#   2 = corner 
#   5 = horizontal wall
#   6 = verical wall
#   7 = traversable space

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

#   VARIABLES

char_row = 7

char_column = 7


#draw functon assums world has no errors
#somebodys elses resposibily to ensure character is in a legal position

#FUNCTIONS

def is_wall(row, column):
    if row >= len(room_parts):
        return True
    if row < 0:
        return True
    #assums that all rows are the same size
    if column >= len(room_parts[0]):
        return True
    if column < 0:
        return True
    if room_parts[row][column] in(0, 1, 2, 3, 5, 6):
        return True

    return False

    


def draw():
    current_row_num = 0
    for current_row in room_parts:
        #this is pre column processing
        temp_str = ""
        current_column_num = 0
        for list_item in current_row:
            if current_column_num == char_column and current_row_num == char_row:
                temp_str = temp_str + "\b"
            elif list_item == 4:
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
                temp_str = temp_str + "⌄"
            elif list_item == 30:
                temp_str = temp_str + "<"
            elif list_item == 40:
                temp_str = temp_str + ">"
            else:
                temp_str = temp_str + "?"
            temp_str = temp_str + " "
            current_column_num += 1
        #this is post column processing
        print(temp_str)
        current_row_num += 1

def controller():
    global char_column
    global char_row
    button = input()
    if button == "a" and not is_wall(char_row, char_column - 1):
        char_column -= 1
    if button == "d" and not is_wall(char_row, char_column + 1):
        char_column += 1
    if button == "w" and not is_wall(char_row - 1, char_column):
        char_row -= 1
    if button == "s" and not is_wall(char_row + 1, char_column):
        char_row += 1    



room_parts =[
[4,4,4,4,4,0,1,1,1,0,4,4,4,4,4],
[4,4,4,4,4,3,4,4,4,3,4,4,4,4,4],
[4,4,4,4,4,3,4,4,4,3,4,4,4,4,4],
[4,4,4,4,4,3,4,4,4,3,4,4,4,4,4],
[4,4,4,4,4,0,1,20,1,0,4,4,4,4,4],
[0,1,1,1,0,0,1,10,1,0,0,1,1,1,0],
[3,4,4,4,3,3,4,4,4,3,3,4,4,4,3],
[3,4,4,4,40,30,4,4,4,40,30,4,4,4,3],
[3,4,4,4,3,3,4,4,4,3,3,4,4,4,3],
[0,1,1,1,0,0,1,20,1,0,0,1,1,1,0],
[4,4,4,4,4,0,1,10,1,0,4,4,4,4,4],
[4,4,4,4,4,3,4,4,4,3,4,4,4,4,4],
[4,4,4,4,4,3,4,4,4,3,4,4,4,4,4],
[4,4,4,4,4,3,4,4,4,3,4,4,4,4,4],
[4,4,4,4,4,0,1,1,1,0,4,4,4,4,4]
]

draw()
print("\n")