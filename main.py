#Import libraries
import random, time, os

#Create separate subroutines

#dice roll
def dice_roll(sides):
  dice_roll = random.randint(1, sides)
  return dice_roll

#character health
def health():
  health_stat = int((dice_roll(6) * dice_roll(12)) / 2 + random.randint(1,15))
  return health_stat

#character strength
def strength():
  strength_stat = int((dice_roll(6) * dice_roll(12)) / 2 + random.randint(1,15))
  return strength_stat

#character name and character type
def character():
  legend_name = input("Name your Legend:\n ")
  time.sleep(.5)
  os.system("clear")
  legend_type = input("What type is your legend?(Human, Elf, Wizard, Orc):\n ")
  time.sleep(.5)
  os.system("clear")
  print("===LEGEND STATS===")
  print()
  time.sleep(.5)
  health_stat = health()
  strength_stat = strength()
  print(f"Legend Name: {legend_name}")
  print()
  time.sleep(.5)
  print(f"Legend Type: {legend_type}")
  print()
  time.sleep(.5)
  print(f"Health: {health()} ")
  print()
  time.sleep(.5)
  print(f"Strength: {strength_stat}")
  print()
  time.sleep(.5)

#option to create up to 3 different characters
def create_loop():
  counter = 1
  while counter <= 3:   
    if counter == 1:
      character()
      create = input("Do you wish to create another legend?: ")
      if create == "yes":
        counter += 1
        time.sleep(1)
        os.system("clear")
        continue
      else:
        break
    elif counter == 2:
      character()
      create = input("Do you wish to create another legend?: ")
      if create == "yes":
        counter += 1
        time.sleep(1)
        os.system("clear")
        continue
      else:
        break
    elif counter == 3:
      character()
      time.sleep(2)
      counter += 1
      
#character generator program
print("Welcome to the Character Generator")
time.sleep(2)
os.system("clear")
create_loop()
time.sleep(.5)
os.system("clear")
print("!!!Best of luck on your quest for glory!!!")