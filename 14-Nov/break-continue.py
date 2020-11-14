# Using break and continue

# break: used to terminate/exit the loop
# continue: used to end an iteration and move onto the next iteration

# Find something in an array

needle = "apple"
haystack = ["banana", "orange", "watermelon", "apple", "melon"]

for h in haystack:
  if needle == h:
    print(h)
    break
