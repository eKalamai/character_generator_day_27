#Import libraries
import random, os, time


#Create separate subroutines

#character name and character type
def character():
  #os.system("clear")
  legend_name = input("Name your Legend: ")
  os.system("clear")
  legend_type = input("What type is your legend?(Human, Elf, Wizard, Orc): ")
  os.system("clear")
  print("===LEGEND STATS===")
  print()
  time.sleep(1)
  print(f"Legend Name: {legend_name}")
  time.sleep(1)
  print(f"Legend Type: {legend_type}")
  time.sleep(1)
  print(f"Health: {health} ")
  time.sleep(1)
  print(f"Strength: {strength}")
  
#dice roll
def dice_roll(sides):
  dice_roll = random.randint(1, sides)
  return dice_roll

#health
def health():
  roll_6 = dice_roll(6)
  roll_12 = dice_roll(12)
  health = int(roll_6 * roll_12 / 2 + random.randint(1,15))
  return health


#strength
def strength():
  roll_6 = dice_roll(6)
  roll_12 = dice_roll(12)
  strength = int(roll_6 * roll_12 / 2 + random.randint(1,15))
  return strength


#specify variables
health = health()
strength = strength()
create = "yes"
counter = 1
#create while loop with option to create multiple characters
def create_loop():
while create == "yes":
    character()
    create = input("Do you wish to create another legend?: ")
      if create == "yes":
        counter += 1
        time.sleep(1)
        continue
      else:
        break
#begin program

print("Welcome to the Character Generator")
os.system("clear")
while counter < 4:
  if counter == 1:
    character()
    create_loop()
  if counter == 2:
    character()
    create_loop()
  if counter == 3:
    character()
    create_loop()
print("Best of luck on your quest for glory!")