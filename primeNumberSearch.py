currNumber = int(input("What number To check If it is a prime number? =====> "))


i = 2
Prime = True
while i < currNumber:
    if currNumber % i == 0:
        print("Divided by " + str(i))
        prime = False
        i = currNumber

    if Prime:
        if currNumber % i != 0:
            print("Checking Number Primage")
            i += 1

if Prime:
    print("Number Not Prime")
else:
    print("Number Prime!")

input("Press Any Key To Quit...")

