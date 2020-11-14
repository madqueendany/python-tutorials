# Using for in a collection

# given this array, find whole numbers
# collection = [2, 2.5, 5.8, 4, 8.1, 6]

# output = []

# for c in collection:

#   remainder = c % 1
#   if remainder > 0:
#     continue
#   else:
#     output.append(c)

# print("whole numbers are ", output)

# Using for in a range of numbers

# start = 7
# end = 10
# for n in range(start, end):
#   print(n)


# Infinite loop 
# condition = True
# while condition:
#     print("hello!")

# Using while to loop over a collection
collection = [2, 2.5, 5.8, 4, 8.1, 6]
output = []

counter = 0
while(counter < len(collection)):
  c = collection[counter]

  remainder = c % 1
  if remainder == 0:
    output.append(c)

  counter += 1 # counter = counter + 1

# print("whole numbers are ", output)
