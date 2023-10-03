import random, os, time

def dice_roll(sides):
  dice_roll = random.randint(1, sides)
  return dice_roll

def six_and_twelve_roll():
  roll_6 = dice_roll(6)
  roll_12 = dice_roll(12)
  dice_total = roll_6 * roll_12
  return dice_total
  

def generate_character():
  counter = 1
  while counter <= 3:
    os.system("clear")
    if counter == 1:
      dice_total = six_and_twelve_roll()
      health = int(dice_total / 2 + 10)
      strength = int(dice_total / 2 + 12)
      legend_1 = input("Name your Legend:\n")
      os.system("clear")
      type_1 = input("Character Type (Human, Elf, Wizard, Orc):\n").capitalize()
      os.system("clear")
      print("LEGEND 1")
      time.sleep(1)
      print()
      print(f"Legend Name: {legend_1}")
      time.sleep(1)
      print(f"Legend Type: {type_1}")
      time.sleep(1)
      print(f"Health: {health}")
      time.sleep(1)
      print(f"Strength: {strength}")
      print()
      print()
      time.sleep(2)
      counter += 1
      add_character = input("Do you wish to create another character? ")
      if add_character == "yes":
        time.sleep(1)
    
        continue
      else:
        break
    elif counter == 2:
      dice_total = six_and_twelve_roll()
      health = int(dice_total / 2 + 10)
      strength = int(dice_total / 2 + 12)
      legend_2 = input("Name your Legend:\n")
      os.system("clear")
      type_2 = input("Character Type (Human, Elf, Wizard, Orc):\n").capitalize()
      os.system("clear")
      print("LEGEND 2")
      time.sleep(1)
      print()
      print(f"Legend Name: {legend_2}")
      time.sleep(1)
      print(f"Legend Type: {type_2}")
      time.sleep(1)
      print(f"Health: {health}")
      time.sleep(1)
      print(f"Strength: {strength}")
      print()
      print()
      time.sleep(2)
      counter += 1
      add_character = input("Do you wish to create another character? ")
      if add_character == "yes":
        print()
        continue
      else:
        break 
    elif counter == 3:
      dice_total = six_and_twelve_roll()
      health = int(dice_total / 2 + 10)
      strength = int(dice_total / 2 + 12)
      legend_3 = input("Name your Legend:\n")
      os.system("clear")
      type_3 = input("Character Type (Human, Elf, Wizard, Orc):\n").capitalize()
      os.system("clear")
      print("LEGEND 3")
      time.sleep(1)
      print()
      print(f"Legend Name: {legend_3}")
      time.sleep(1)
      print(f"Legend Type: {type_3}")
      time.sleep(1)
      print(f"Health: {health}")
      time.sleep(1)
      print(f"Strength: {strength}")
      print()
      print()
      time.sleep(2)
      break
   


#run character generator

print("+++---CHARACTER GENERATOR---+++")
time.sleep(2)
generate_character()
time.sleep(1)
os.system("clear")
print("Good luck on your adventures!")