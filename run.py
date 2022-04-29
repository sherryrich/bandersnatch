import colorama
import sys
import time
from colorama import Fore
colorama.init(autoreset=True)


def typewrite(string):
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        # time.sleep(0.1)


print(F"""{Fore.RED}
  ___   _   _  _ ___  ___ ___  ___ _  _   _ _____ ___ _  _ 
 | _ ) /_\ | \| |   \| __| _ \/ __| \| | /_\_   _/ __| || |
 | _ \/ _ \| .` | |) | _||   /\__ \ .` |/ _ \| || (__| __ |
 |___/_/ \_\_|\_|___/|___|_|_\|___/_|\_/_/ \_\_| \___|_||_|
                                                           
""")

# credit https://patorjk.com/software/taag/#p=author&f=Small&t=Bandersnatch


print(F"{Fore.YELLOW}\n\t\tWelcome to Bandersnatch \U0001F47E !\n")
typewrite("You just developed a new computer game 'Bandersnatch'.")
typewrite("You must to get to the office of Tuckersoft Ltd to sell the game.")
print()
typewrite("There are numerous paths. Choose wisely & complete your adventure.")
print()
user_name = input("What is your name?\n").capitalize()
print()
print("Welcome " + user_name + "!. \nRemember to choose the right path to make 'Bandersnatch' a reality.")
print()
play_game = input("Do you wish to play? Y/N\n").capitalize()
if play_game == "Y":
    print("lets start your adventure " + user_name )
else:
    print("Goodbye")
print()

choice1 = input("You\'re traveling to the company and are at a crossraods, which way do\nyou want to go? Type 'left' or 'right'.\n").lower()
print()
if choice1 == "left":
    choice2 = input(F"{Fore.GREEN}Good choice. You\'re now at the train station but the train is running late.\nDo you wait for the train or get a taxi to get to Tuckersoft offices?\nType 'wait' to take the train or type 'taxi' to hail a taxi\n").lower()
    if choice2 == "wait":
        choice3 = input(F"{Fore.GREEN}Good choice. You took the train and made it on time for the meeting. Tuckersoft like the game.\nThere are 3 offers on the table. Which one do you choose?\nType '1' to take offer 1\nType '2' to take offer 2\nType '3' to take offer 3\n").lower()
        if choice3 == "1":
            print(F"{Fore.RED}Bad choice, you got fired and they stole your idea. Game over")
        elif choice3 == "2":
            print(F"{Fore.RED}Bad choice, they take your idea and it fails to get any sales due to poor reviews. Game over")
        elif choice3 == "3":
            print(F"{Fore.GREEN}Good choice. You politely decline their offer and decide to go alone, you win and the game is a huge worldwide sucess. You Win")
        else:
            print(F"{Fore.RED}You failed to take any offer. Game over")
    else:
        print(F"{Fore.RED}Wrong choice. You have missed the meeting.\nTuckersoft Ltd are no longer interested.\nGame Over.")
else:
    print(F"{Fore.RED}Wrong choice. You just got hit by a bus and died. Game Over.")

lead_time = input("The company ask how many weeks will it take you to finish the completed version?")
if lead_time:
	lead_time = int(lead_time)
	if lead_time >= 21:
	    print(F"{Fore.RED}Thats too long, we cant do a deal. Game Over.")
	elif lead_time <= 20:
	    print(F"{Fore.GREEN}Ok you got yourself a deal.")
	else: 
	    print("Please enter number of weeks")