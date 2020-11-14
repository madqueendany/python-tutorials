# # if , else

# 1. Simple conditional statements
## Using ==, !=
# isAlive = True
# isDead = False

# if isDead:
#   print('I am alive!')
# else:
#   print('I am dead.')

# isSleeping = input("Brother John, are you sleeping? (y/n): ") # y/n
# if isSleeping != "y":
#   print("Bro John is awake!")
# else:
#   print("Bro John is sleeping")

# if not isSleeping:
#   print("Bro John is awake!")
# else:
#   print("Bro John is sleeping")

# 2. Using conditional operators
## < > <= >=
# myAge = 30
# if myAge > 40:
#   print('I am older than 40.')
# else:
#   print('I am younger than 40.')

# 3. Using data type equality

## Using strings
# name = "Kevin"

# user_name = input("Enter your name: ")

# if name == user_name:
#   print("hello", name)
# else:
#   print("You're not Kevin")


## Using integers/floats
# a_score = int(input("Enter Aldrich score: "))
# k_score = int(input("Enter Kevin score: "))

# if a_score > k_score:
#   print("Aldrich wins.")
# else:
#   print("Kevin wins.")

# if, elif, else
# job = input("Which class are you? ")
# if job == "Soldier":
#   print("Go to barracks")

# elif job == "Mage":
#   print("Go to wizard academy")

# elif job == "Archer":
#   print("Go to archery range")

# else:
#   print("Nowhere to go.")

# monster_health = 100
# monster_attack_score = 20
# player_health = 100
# player_attack_score = 10

# print("Adventurer sees a monster. What should he do?")
# print("1. Attack")
# print("2. Flee")
# action = int(input("Enter action: "))

# if action == 1:
#   print("Adventurer attacks")
#   monster_health -= player_attack_score
#   player_health -= monster_attack_score
#   print("You attack the monster. It is now left with", monster_health, "HP")
#   print("Monster attacks you. You are left with", player_health, "HP")
# elif action == 2:
#   print("Adventurer escapes")
