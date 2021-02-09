import random
def welcome():
    name = input("Please enter your name: ").title()
    print("Welcome" ,name,"this is a number guessing game")
welcome()
isplaying = "true"
def game():
    print("Please Guess a number (between 1 and 10): ")
    chances = 0
    global points
    points = 0
    number = random.randint(1, 10)
    while chances != 5:
        guess = int(input())
        chances += 1
        print("chances = ", chances)
        if guess == number:
            points += 1
            if points < 1:
                print("Congratulations, YOU WON!!!, and it only took you" ,chances, "tries, you now have" ,points, "points")
                text = input("Would you like to play again??, (Y or N)").lower()
                if text == "n":
                    chances = 0
                    print("Alright, thank you for playing, goodbye")
                    isplaying = "false"
                    break
                elif text == "y":
                    chances = 0
                    isplaying = "false"
                    break
            elif points > 1:
                print("Congratulations, YOU WON!!!, and it only took you" ,chances, "tries, you now have" ,points, "point")
                txt = input("Would you like to play again??, (Y or N)").lower()
                if txt == "n":
                    chances = 0
                    print("Alright, thank you for playing, goodbye")
                    isplaying = "false"
                    break
                elif txt == "y":
                    chances = 0
                    isplaying = "false"
                    break
        elif guess != number:
            if guess < number:
                print("Your guess was too low, please guess a number higher than {}".format(guess))
            elif guess > number:
                print("Your guess was too high, please guess a number lower than {}".format(guess))
    while chances == 5:
        print("Sorry, you have used all of your available attempts, the number we were looking for was {}".format(number))
        option = input("Would you like to try again?? Y or N").lower()
        if option == "n":
            chances = 0
            print("Alright, thank you for playing, goodbye")
            isplaying = "false"
            break
        elif option == "y":
              chances = 0
              isplaying = "false"
              break
if isplaying == "true":
    game()
game()
