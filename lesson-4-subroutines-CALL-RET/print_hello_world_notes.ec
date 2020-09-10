# THE FILE CALLED print_hello_world.ec holds the program withouth any blank space.
# START OF OUR PROGRAM FILE
# STORE IN A REGISTER THE LOCATION OF OUR COROUTINE

4   # SAVE_REG
22  # LOCATION OF THE COROUTINE
0

9   # CALL
0   # Register zero
9   # CALL
0   # Register zero
9   # CALL
0   # Register zero
2   # HALT





# Print_hello_world_twice Coroutine
1       # Print Hello World
1       # Print Hello World
10      # RETURN BACK TO WHERE I WAS CALLED FROM


# CALL needs to push pc + 2 to the stack
# Return Operation (RET) just needs to pop from stack and set PC to that value.





# NOT PART OF PROGRAM FILE
def print_hello_world_once():
    print("Hello World")

def print_hello_world_twice():
    print("Hello World")
    print("Hello World")

def print_hello_world_thrice():
    print("Hello World")
    print("Hello World")
    print("Hello World")
