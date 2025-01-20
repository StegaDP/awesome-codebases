weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

import random; weaponRoll = random.randint(1, len(weapons))
heroStrength = weapons[weaponRoll-1]

if weaponRoll <= 2: print("You rolled a weak weapon, friend")
elif weaponRoll <= 4: print("Your weapon is meh")
else: print("Nice weapon, friend!")

if weaponRoll != 1: print("Thank goodness you didn't roll the Fist")
