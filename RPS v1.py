import random


def main():
    possibleChoices = {
        "1" : "rock",
        "2" : "paper",
        "3" : "scissors"
    }

    computerChoice = random.choice(list(possibleChoices.values()))
    print(computerChoice)

    humanChoice = input("What do you want to play? (rock, paper, scissors)")
    humanChoice.lower()

    if humanChoice == "paper":
        if computerChoice == "paper":
            print("Draw!")
            print("--------------------------------------------")
            print("Computer choice - " + computerChoice.capitalize())
            print("--------------------------------------------")
            print("Human choice - " + humanChoice.capitalize())
        if computerChoice == "scissors":
            print("You lose!")
            print("--------------------------------------------")
            print("Computer choice - " + computerChoice.capitalize())
            print("--------------------------------------------")
            print("Human choice - " + humanChoice.capitalize())
        if computerChoice == "rock":
            print("You win!")
            print("--------------------------------------------")
            print("Computer choice - " + computerChoice.capitalize())
            print("--------------------------------------------")
            print("Human choice - " + humanChoice.capitalize())
    if humanChoice == "scissors":
        if computerChoice == "paper":
            print("You win!")
            print("--------------------------------------------")
            print("Computer choice - " + computerChoice.capitalize())
            print("--------------------------------------------")
            print("Human choice - " + humanChoice.capitalize())
        if computerChoice == "scissors":
            print("Draw!")
            print("--------------------------------------------")
            print("Computer choice - " + computerChoice.capitalize())
            print("--------------------------------------------")
            print("Human choice - " + humanChoice.capitalize())
        if computerChoice == "rock":
            print("You lose!")
            print("--------------------------------------------")
            print("Computer choice - " + computerChoice.capitalize())
            print("--------------------------------------------")
            print("Human choice - " + humanChoice.capitalize())
    if humanChoice == "rock":
        if computerChoice == "paper":
            print("You lose!")
            print("--------------------------------------------")
            print("Computer choice - " + computerChoice.capitalize())
            print("--------------------------------------------")
            print("Human choice - " + humanChoice.capitalize())
        if computerChoice == "scissors":
            print("You win!")
            print("--------------------------------------------")
            print("Computer choice - " + computerChoice.capitalize())
            print("--------------------------------------------")
            print("Human choice - " + humanChoice.capitalize())
        if computerChoice == "rock":
            print("Draw!")
            print("--------------------------------------------")
            print("Computer choice - " + computerChoice.capitalize())
            print("--------------------------------------------")
            print("Human choice - " + humanChoice.capitalize())




if __name__ == '__main__':
    main()