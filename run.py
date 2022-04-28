# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import colorama
from colorama import Fore
colorama.init(autoreset=True)
import sys
import time

def typewrite(string):
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.04)


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


print(F"{Fore.YELLOW}\n\tWelcome to Bandersnatch !\n")
typewrite("You are programmer who has just developed a new computer game 'Bandersnatch'\nyou must to get to the office of Tuckersoft Ltd to sell the game.")
typewrite("There are numerous possible paths so please choose wisely to complete your\nown adventure.")
print()
user_name = input("What is your name?\n").capitalize()
print()
print("Welcome " + user_name + "!. \nlets start your adventure shall we?\nRemember to choose the right path to make 'Bandersnatch' a reality.")
print()
choice1 = input("You\'re traveling to the company and are at a crossraods, which way do\nyou want to go? Type 'left' or 'right'.\n").lower()
print()
if choice1 == "left":
    choice2 = input("Good choice. You\'re now at the train station but the train is running late, do you wait for the train or get a taxi to get to Tuckersoft Ltd offices? Type 'wait' to take the train or type 'taxi' to hail a taxi\n").lower()
    if choice2 == "wait":
        choice3 = input("Good choice. You took the train and made it on time for the meeting. Tuckersoft like the game and there are 3 offers on the table. Which one do you choose? Type '1' to take offer 1, Type '2' to take offer 2, Type '3' to take offer 3\n").lower()
        if choice3 == "1":
            print("Bad choice, you got fired and they stole your idea. Game over")
        elif choice3 == "2":
            print("Bad choice, they take your idea and it fails to get any sales due to poor reviews. Game over")
        elif choice3 == "3":
            print("Good choice. You politely decline their offer and decide to go alone, you win and the game is a huge worldwide sucess. You Win")
        else:
            print("You failed to take any offer. Game over")
    else:
        print("Wrong choice. You have missed the meeting. Tuckersoft Ltd are no longer interested. Game Over.")
else:
    print("Wrong choice. You just got hit by a bus and died. Game Over.")