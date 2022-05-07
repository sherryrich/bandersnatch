import colorama
import sys
import time
import random
from password import password_list
from art import logo_art, win_art, deal_art, game_over_art, stages
from colorama import Fore
colorama.init(autoreset=True)


def typewrite(string):
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)


print(f"{Fore.RED}{logo_art}")

print(F"{Fore.YELLOW}\n\t\tWelcome to Bandersnatch \U0001F47E !\n")
typewrite("You just developed a new computer game 'Bandersnatch'.\n")
typewrite("You must to get to the office of Tuckersoft Ltd to sell the game.")
print()
typewrite("There are numerous paths. Choose wisely & complete your adventure.")
print()
play_game = input("Do you wish to play? Y/N\n").capitalize()
if play_game == "Y":
    typewrite("Ok lets start your adventure")
else:
    print("Goodbye")
    print(f"{Fore.RED}{game_over_art}")
print()
user_name = input("What is your name?\n").capitalize()
print()
typewrite("Welcome " + user_name + "!.\n")
typewrite("Remember, choose the right path to make 'Bandersnatch' a reality.")
print()

typewrite("You\'re traveling to the company and are at a crossraods\n")
typewrite("Which way do you want to go?\n")
choice1 = input("Type 'left' or 'right'\n").lower()
print()
if choice1 == "left":
    print(F"{Fore.GREEN}Good choice " + user_name + "")
    typewrite("You\'re at the train station but the train is running late.\n")
    typewrite("Do you wait for a train or get a taxi to Tuckersoft offices?\n")
    choice2 = input("Type 'wait' for train or 'taxi' take a taxi\n").lower()
    if choice2 == "wait":
        print(F"{Fore.GREEN}Good choice " + user_name + "")
        choice3 = input("You took the train and made it on time for the meeting. Tuckersoft like the game.\nThere are 3 offers on the table. Which one do you choose?\nType '1' to take offer 1\nType '2' to take offer 2\nType '3' to take offer 3\n").lower()
        if choice3 == "1":
            print(F"{Fore.RED}Bad choice, you didnt get hired")
            print("Tuckersoft they stole your idea. Game over")
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
	    print(F"{Fore.GREEN}Congratulations, you got yourself a deal.")
	    print(f"{Fore.GREEN}{deal_art}")
	else: 
	    print("Please enter number of weeks")

game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(password_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("Guess the password to complete the game. Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the password. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")
            print(f"{Fore.RED}{game_over_art}")
    
    if not "_" in display:
        game_is_finished = True
        print(f"{Fore.GREEN}{win_art}")
        typewrite("Thank you for playing Bandersnatch.")

    print(stages[lives])