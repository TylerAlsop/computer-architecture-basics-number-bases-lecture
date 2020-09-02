import sys

# Operation Codes (OP Codes)

PRINT_HELLO_WORLD = 1       #0b00000001
HALT = 2                    #0b00000010
PRINT_NUM = 3               #0b00000011

 # Later we will add more instructions
 # RUN
 # Etc.


# Print "Hello World"
# Print 5
# Return

memory = [
    PRINT_HELLO_WORLD,
    PRINT_NUM,
    5,
    HALT,
]
# Same as:
# print("hello world")
# print("hello world")
# print("hello world")


running = True

pc = 0    # pc stands for Program Counter

while running:
    # Read line by line from memory
    instruction = memory[pc]
    
    if instruction == PRINT_HELLO_WORLD:
        # print hello world
        print("Hello World")
        # move pc up 1
        pc += 1

    elif instruction == PRINT_NUM:
        num = memory[pc + 1]
        print(num)
        pc += 2

    elif instruction == HALT:
        # print hello world
        print("The program has reached a HALT function and is now ending. Thanks for playing.")
        running = False

    else:
        print(f'Unknown instruction: {instruction}. The program will now exit / crash.')
        running = False
        sys.exit(1)