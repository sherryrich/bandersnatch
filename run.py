import colorama
import sys
import time
import random
from password import password_list
from art import logo_art, win_art, deal_art, game_over_art, stages
from colorama import Fore
colorama.init(autoreset=True)


continue_game = True


def restart():
    # ask user to restart game
    print(F"{Fore.YELLOW}Would you like to play again?\n")
    restart = input("Type 'Y' or 'N'\n").lower()
    if restart == "y":
        continue_game = True
    elif restart == "n":
        print(F"{Fore.RED}Thank you for playing. Goodbye")
        print(f"{Fore.RED}{game_over_art}")
        quit()


def typewrite(string):
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)


while continue_game:
    # intro to game
    print(f"{Fore.YELLOW}{logo_art}")
    print(F"{Fore.RED}\n\t\tWelcome to Bandersnatch \U0001F47E !\n")
    typewrite("You just developed a new computer game 'Bandersnatch'.\n")
    typewrite("You must to get to the HQ of Tuckersoft Ltd to sell the game.")
    print()
    typewrite("Numerous paths so choose wisely to complete your adventure")
    print()
    # ask user do they want to play
    play_game = input("Do you wish to play? Y/N\n").capitalize()
    if play_game == "Y":
        typewrite("Ok lets start your adventure")
    else:
        print(F"{Fore.RED}Thank you for playing. Goodbye")
        print(f"{Fore.RED}{game_over_art}")
        restart()
    print()
    # ask user for name
    user_name = input("What is your name?\n").capitalize()
    print()
    print(F"{Fore.YELLOW}Welcome " + user_name + "!\n")
    typewrite("Remember, choose the right path to make 'Bandersnatch' reality")
    print()
    typewrite("You\'re traveling to Tuckersoft HQ and are at a crossroads.\n")
    typewrite("Which way do you want to go?\n")
    choice1 = input("Type 'left' or 'right'\n").lower()
    print()
    if choice1 == "left":
        print(F"{Fore.GREEN}Good choice " + user_name + "")
        typewrite("You\'re at the train station but the train is late.\n")
        typewrite("Do you wait for a train or get a taxi to Tuckersoft HQ?\n")
        choice2 = input("Type 'train' for train or 'taxi' for taxi\n").lower()
        if choice2 == "train":
            print(F"{Fore.GREEN}Great choice " + user_name + "")
            typewrite("You took the train and made it to the meeting.\n")
            typewrite("Tuckersoft like the game. 3 offers are on the table.\n")
            print("Type '1' to take offer 1")
            print("Type '2' to take offer 2")
            print("Type '3' to take offer 3")
            choice3 = input("Which one do you choose?\n").lower()
            if choice3 == "1":
                print(F"{Fore.RED}Bad choice " + user_name + "!")
                print(F"{Fore.RED}Tuckersoft steal your idea.")
                print(F"{Fore.RED}Sell the game directly themselves.\n")
                print(f"{Fore.RED}{game_over_art}")
                restart()
            elif choice3 == "2":
                print(F"{Fore.YELLOW}OK, Tuckersoft are still interested\n")
                typewrite("Tuckersoft ask how many weeks will it take you\n")
                typewrite("to finish the completed version?\n")
                lead_time = input("Type a number between 1-40\n")
                # if user selects >= 21 they fail
                if lead_time:
                    lead_time = int(lead_time)
                    if lead_time >= 21:
                        print(F"{Fore.RED}Wrong choice " + user_name + "!")
                        print(f"{Fore.RED}Thats too long, Tuckersoft refuse.")
                        print(f"{Fore.RED}No deal this time.")
                        print(f"{Fore.RED}{game_over_art}")
                        restart()
                    # if they answer <= 20 they get to password game
                    if lead_time <= 20:
                        print(f"{Fore.YELLOW}Congratulations, you got a deal.")
                        print(f"{Fore.YELLOW}Next time try another offer?")
                        print(f"{Fore.YELLOW}{deal_art}")
                        restart()
            elif choice3 == "3":
                print(F"{Fore.GREEN}Fantastic choice " + user_name + "")
                print(F"{Fore.GREEN}You decline offer 3 and decide to")
                print(F"{Fore.GREEN}create and sell the game yourself")
                print(F"{Fore.GREEN}Bandersnatch is a huge hit worldwide.\n")
                game_is_finished = False
                lives = len(stages) - 1
                # choose random word in password_list as assign to variable
                chosen_word = random.choice(password_list)
                word_length = len(chosen_word)
                # empty list
                display = []
                # loop and display "_" for each letter
                for _ in range(word_length):
                    display += "_"
                while not game_is_finished:
                    print(F"{Fore.CYAN}BONUS GAME\n")
                    print(F"{Fore.CYAN}Guess the secret password?\n")
                    # ask user to guess a letter and assign answer to var
                    # make guess lowercase
                    guess = input("Guess a letter: \n").lower()
                    if guess in display:
                        print(f"You've already guessed {guess}")
                    for position in range(word_length):
                        letter = chosen_word[position]
                        # if guessed letter is in chosen word display
                        if letter == guess:
                            display[position] = letter
                    print(f"{' '.join(display)}")
                    # if guess not in word reduce lives by 1
                    # if lives go to 0 then game over
                    if guess not in chosen_word:
                        print(f"{Fore.RED}{guess}, incorrect. Lose a life.")
                        lives -= 1
                        if lives == 0:
                            game_is_finished = True
                            print("You lose.")
                            print(f"{Fore.RED}{game_over_art}")
                            restart()
                    # display has no more blanks they have won
                    if "_" not in display:
                        game_is_finished = True
                        print(f"{Fore.GREEN}Congratulations")
                        print(f"{Fore.GREEN}{win_art}")
                        typewrite("Thank you for playing Bandersnatch.\n")
                        restart()
                        quit()
                    print(stages[lives])
            else:
                print(F"{Fore.RED}You failed to take any valid offer.")
                print(f"{Fore.RED}{game_over_art}")
                restart()
        else:
            print(F"{Fore.RED}Wrong choice " + user_name + "!")
            print(F"{Fore.RED}You have missed the meeting.\n")
            print(F"{Fore.RED}Tuckersoft Ltd are no longer interested.\n")
            print(f"{Fore.RED}{game_over_art}")
            restart()
    else:
        print(F"{Fore.RED}Wrong path " + user_name + "!")
        print(F"{Fore.RED}You just got hit by a bus and died.")
        print(f"{Fore.RED}{game_over_art}")
        restart()
