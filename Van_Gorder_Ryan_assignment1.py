#Problem 1
#define the function
def calculate_boost_distance(speed, time):
    #return the boost distance
    return (speed * time)

#Problem 2
#define the function
def generate_silly_name():
    #ask for name input
    input_name = (input("Enter your name: "))
    #ask for integer input
    input_int = int(input("Enter a non-negative whole number: ")) 
    #return silly name
    return input_name * input_int

#Problem 3
#define the function
def generate_first_track():
    #first line
    for val in range(6, 22, 3):
        print(val, end = " ")
    print() 
    #second line
    for val in range(4, 5):
        print(val, end = " ")
    print() 
    #third line
    for val in range(7, 22, 7):
        print(val, end = " ")
    print()
    #fourth line
    for val in range(49, 12, -9):
        print(val, end = " ")
    print()

#Problem 4
def remove_from_pool(powerups):
  if not powerups:
    print("No power-ups in the pool.")
    return
  # User input for powerup to remove in lowercase for case-insensitive comparison
  item_to_remove = input("Enter an item to remove: ").lower()
  # Iterate through the list and remove the matching item
  for var, powerup in enumerate(powerups):
    if powerup.lower() == item_to_remove:
      del powerups[var]
      break  # Exit the loop after the first matching item is removed
  else:
    print(f"{item_to_remove} not found in the pool.")
  # Print the remaining power-ups
  if powerups:
    print("\n".join(powerups))

#Problem 5
def select_powerup(index, powerups):
  if not powerups:
    print("No power-ups in pool.")
    return

  # Get user input for item to remove (outside the loop)
  item_to_remove = input("Enter an item to remove: ").lower()

  for val, powerup in enumerate(powerups):
    if powerup.lower() == item_to_remove:
      del powerups[val]
      break  # Exit the loop after the first matching item is removed

  else:
    print(f"{item_to_remove} not found in pool")

  # Print remaining power-ups (properly indented)
  if powerups:
    print("\n".join(powerups))