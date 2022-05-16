import random

possibleChoices = {
    "1": "rock",
    "2": "paper",
    "3": "scissors"
}


# Choice Making
def makeComputerChoice():
    computerChoice = random.choice(list(possibleChoices.values()))
    return computerChoice


def makeHumanChoice():
    humanChoice = input("rock, paper or scissors?")
    return humanChoice


# Choice Checks
def paperCheck():
    if humanChoice == "paper":
        draw()
    if humanChoice == "rock":
        lost()
    if humanChoice == "scissors":
        win()


def rockCheck():
    if humanChoice == "paper":
        win()
    if humanChoice == "rock":
        draw()
    if humanChoice == "scissors":
        lost()


def scissorsCheck():
    if humanChoice == "paper":
        lost()
    if humanChoice == "rock":
        win()
    if humanChoice == "scissors":
        draw()


# Endings
def draw():
    print("/----------------------------------------------------\\")
    print("|                                                    |")
    print("| Draw!                                              |")
    print("|                                                    |")
    print("\----------------------------------------------------/")


def win():
    print("/----------------------------------------------------\\")
    print("|                                                    |")
    print("| You Win!                                           |")
    print("|                                                    |")
    print("\----------------------------------------------------/")


def lost():
    print("/----------------------------------------------------\\")
    print("|                                                    |")
    print("| You Lose!                                          |")
    print("|                                                    |")
    print("\----------------------------------------------------/")


def main():
    if pcChoice == "paper":
        paperCheck()

    if pcChoice == "rock":
        rockCheck()

    if pcChoice == "scissors":
        scissorsCheck()


pcChoice = makeComputerChoice()
print(pcChoice)
humanChoice = makeHumanChoice()

if __name__ == '__main__':
    main()
