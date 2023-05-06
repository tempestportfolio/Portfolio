import random

print('This is a number guessing game. \nQuestions can be answered with "yes" or "no"')
playing = input('Type "start" to begin:\n')
if playing.upper() != "START":
    quit()
else:
    print("Okay! Let's begin!")

while True:
    random_number = (random.randint(1, 100))
    
    number_of_guesses = 0

    while True:

        while True:
            number_of_guesses += 1
            guess = input("Enter a number: \n")
            if guess.isdigit():
                guess = int(guess)

                if guess <= 0:
                    print("Please enter a number greater than 0.")
                    continue
                if guess > 100:
                    print("Please enter a number less than or equal to 100.")
                    continue
            else:
                print("Please enter a number.")
                quit()

            if guess == random_number:
                print("Correct!")
                break
            elif guess > random_number:
                print("You guessed too high!")
            else:
                print("You guessed too low!")

            if number_of_guesses >= 20:
                break

        if number_of_guesses == 20:
            print("You have guessed", number_of_guesses, "times.")
            give_up = input("Would you like to give up? \n")
            if give_up.upper() == "NO":
                continue
            elif give_up.upper() == "YES":
                print("The answer is", random_number)
                break

        if number_of_guesses == 40:
            print("You have guessed", number_of_guesses, "times.")
            give_up = input("Would you like to give up? \n")
            if give_up.upper() == "NO":
                continue
            elif give_up.upper() == "YES":
                print("The answer is", random_number)
                break

        if number_of_guesses == 50:
            print("You have guessed", number_of_guesses, "times.") 
            print("The answer is", random_number)
            break
    
        if guess == random_number:
            break

        else:
            continue

    if guess == random_number:
        print("You got the number correct in", number_of_guesses, "guesses!")
        
    restart = input("Do you want to try again? \n")
    if restart.upper() == "NO":
        print("Okay! Thanks for playing!")
        quit()
    elif restart.upper() == "YES":
        print("Okay! Let's try again!")
        continue