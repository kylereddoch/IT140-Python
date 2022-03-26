num_rows = int(input())
num_cols = int(input())

# Note 1: You will need to declare more variables
# Note 2: Place end=' ' at the end of your print statement to separate seats by spaces

letter1 = '1'
letter2 = 'A'

for row in range(num_rows): # sets maximum changes to letter1.
   letter2 = 'A' # makes sure letter2 starts over after the inner loop first finishes.
   for col in range(num_cols): # sets maximum changes to letter2.
      print(letter1 + letter2, end=' ') # Print before incrementing letter2.
      letter2 = chr(ord(letter2) + 1) # converts 'A' to its unicode value, increments it by one, then converts it back to a letter.
   letter1 = chr(ord(letter1) + 1) # only runs after the inner loop is done to increment letter1 for the next loop.

print()
