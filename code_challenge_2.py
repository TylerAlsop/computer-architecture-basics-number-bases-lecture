# Given a hashmap where the keys are integers, print out all of the values of the hashmap in reverse order, ordered by the keys.
# For example, given the following hashmap:
# {
#   14: "vs code",
#   3: "window",
#   9: "alloc",
#   26: "views",
#   4: "bottle",
#   15: "inbox",
#   79: "widescreen",
#   16: "coffee",
#   19: "tissue",
# }
# The expected output is:
# widescreen
# views
# tissue
# coffee
# inbox
# vs code
# alloc
# bottle
# window
# since "widescreen" has the largest integer key, "views" has the second largest, etc.
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

# U.
    # Given a hashmap with integers for keys and strings for values.
    # Need to print each value on its own line
    # Must be printed in descending order according to the size of the integer used for the key

# P.
    # Set the hashmap to a variable name.
    # Organized the hashmap in descending order
    # Create a for loop.
        # For each item in the hashmap
            # Print the value

# E.
given_hashmap = {
  14: "vs code",
  3: "window",
  9: "alloc",
  26: "views",
  4: "bottle",
  15: "inbox",
  79: "widescreen",
  16: "coffee",
  19: "tissue",
}

sorted_hashmap = sorted(given_hashmap)

sorted_hashmap.reverse()

# print(sorted_hashmap)

for item in sorted_hashmap:
    print(given_hashmap[item])


# R.
    # Understanding that the sorted() method returns a sorted array of just the keys would have been helpful to know before trying to print(sorted_hashmap[item]) for each item in sorted_hashmap. printing sorted_hashmap helped me to see that the sorted() method didn't return a sorted version of the entire hashmap (keys and values).
