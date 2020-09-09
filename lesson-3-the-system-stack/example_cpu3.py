import sys

# Operation Codes (OP Codes)

PRINT_HELLO_WORLD   = 1     #0b00000001
HALT                = 2     #0b00000010
PRINT_NUM           = 3     #0b00000011
SAVE_REG            = 4
PRINT_REG           = 5
ADD                 = 6     # ADD takes 2 registers, adds their values and stores the result in the first register given



memory = [0] * 256


registers = [0] * 8

running = True

pc = 0    # pc stands for Program Counter

# Get file name from command line arguments
if len(sys.argv) != 2:
    print("Usage: example_cpu.py filename")
    sys.exit(1)


def load_memory(filename):
    # Open a file and load into memory
    address = 0

    try: 
        with open(filename) as program_file:
            for line in program_file:
                # Split the current line on the # symbol
                split_line = line.split('#')
                # print(split_line)

                code_value = split_line[0].strip() # removes whitespace and /n character

                # Make sure that the value before the # symbol is not empty
                if code_value == '':
                    continue

                num = int(code_value)
                memory[address] = num
                address += 1
                
    except FileNotFoundError:
        print(f'{sys.argv[1]} File not found')
        sys.exit(2)


load_memory(sys.argv[1])

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

    elif instruction == SAVE_REG:
        # Save some value to some register
        # First number after instruction will be the value to store
        # Second number after instruction will be register
        num = memory[pc + 1]
        reg_location = memory[pc + 2]
        registers[reg_location] = num
        pc += 3

    elif instruction == PRINT_REG:
        reg_location = memory[pc + 1]
        print(registers[reg_location])
        pc += 2
    
    elif instruction == ADD:
        # ADD takes 2 registers, adds their values and stores the result in the first register given
        # Get register 1
        # Get register 2
        # Add the values of both registers together
        # Store in register 1
        reg_1 = memory[pc + 1]
        reg_2 = memory[pc + 2]
        registers[reg_1] += registers[reg_2]
        pc += 3

    elif instruction == HALT:
        # print hello world
        print("The program has reached a HALT function and is now ending. Thanks for playing.")
        running = False

    else:
        print(f'Unknown instruction: {instruction}. The program will now force exit.')
        running = False
        sys.exit(1)