# THE FILE CALLED print_num_fnc.ec holds the program withouth any blank space.

# STORE ALL FUNCTION LOCATIONS IN REGISTERS
4       # STORE PRINT_1 into register 0
__ # LOCATION OF PRINT 1
0
4       # STORE PRINT_2 into register 1
__ # LOCATION OF PRINT 2
1
4       # STORE PRINT_3 into register 2
__ # LOCATION OF PRINT 3
2
9 # CALL PRINT_ONE
0
2 # END OF OUR PROGRAM


# print_three coroutine
3       # print_num
3       # the number to print
# CALL PRINT_TWO
10


# print_two coroutine
3       # print_num
2       # the number to print
# CALL PRINT_TWO
10


# print_one coroutine
3       # print_num
1       # the number to print
# CALL PRINT_TWO
10






def print_three():
    print(3)

def print_two():
    print(2)

def print_one():
    print(1)