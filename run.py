# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

print("""
  ___   _   _  _ ___  ___ ___  ___ _  _   _ _____ ___ _  _ 
 | _ ) /_\ | \| |   \| __| _ \/ __| \| | /_\_   _/ __| || |
 | _ \/ _ \| .` | |) | _||   /\__ \ .` |/ _ \| || (__| __ |
 |___/_/ \_\_|\_|___/|___|_|_\|___/_|\_/_/ \_\_| \___|_||_|
                                                           
""")

# Small by Glenn Chappell 4/93 -- based on Standard
# Includes ISO Latin-1
# figlet release 2.1 -- 12 Aug 1994
# Permission is hereby given to modify this font, as long as the
# modifier's name is placed on a comment line.

# Modified by Paul Burton <solution@earthlink.net> 12/96 to include new parameter
# supported by FIGlet and FIGWin.  May also be slightly modified for better use
# of new full-width/kern/smush alternatives, but default output is NOT changed.


print("Welcome to Bandersnatch")
print("YOU choose your own adventure")
user_name = input("What is your name?")
print()
print("Welcome " + user_name + " Lets start your adventure shall we? Remember to choose the right path")
print("You have just devleoped an idea for a computer game and need to pitch the idea to Tuckersoft Ltd to help you develop it")
choice1 = input("You\'re at a crossraod, where do you want to go? Type 'left' or 'right'.").lower()

if choice1 == "left":
    input("You\'re are running late, doy ou get a taxi or train to get to Tuckersoft Ltd? Type 'wait' for train or 'taxi' to hail a taxi")
else:
    print("Wrong choice. You just got hit by bus and died. Game Over.")