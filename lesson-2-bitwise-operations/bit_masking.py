############################ Bit Masking ############################
#                               10000010

#                10               00                   0010
#                ^                ^                    ^
#            Number                                 Instruction
#            of 
#            operands
#            (up to 3)


# How to pull out the value that is contained in the first two bits:

instruction = 0b10000010

first_two_bits = instruction >> 6
print(f'First two bits: {bin(first_two_bits)}')


# How to get the fifth and sixth bits (should be 0b11)
instruction_2 = 0b10011010

first_through_sixth = instruction_2 >> 3
# To get the last 2 bits then use AND where the binary in the second half of the AND has all zeros except for the bits that you want to extract.
fifth_and_sixth = first_through_sixth & 0b00000011

print(f'Fifth and Sixth bits. Shift First: {bin(fifth_and_sixth)}')

#*** This process can be reversed as well ***#
instruction_3 = 0b10011010

mask = instruction_3 & 0b00011000

shifted = mask >> 3

print(f'Fifth and Sixth bits. Mask First: {bin(shifted)}')
