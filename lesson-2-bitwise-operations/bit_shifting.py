############################ Bit Shifting ############################
#   Shift to the Right ( >> )     and      Shift to the left ( << )

#       a >> 1  means shift a to the right 1 bit
#       b >> 3  means shift b to the left 3 bits


#       0b1110 >> 1 = 0111

print(bin(0b1110 >> 1))
print(bin(0b1110 >> 3))

# Shifting can be used to make functions that multiply and divide.

#       0b1110 >> 1 = 0111   is the same as 14 / 2 = 7
#       0b1110 >> 2 = 0011   is the same as 14 / 4 = 3.5
#       0b1110 >> 3 = 0001   is the same as 14 / 4 = 1


#       0b1110 << 1 =  is the same as 14 * 2 = 
#       0b1110 << 2 =  is the same as 14 * 4 = 
#       0b1110 << 3 =  is the same as 14 * 4 =


print(bin(0b1110 >> 1))
