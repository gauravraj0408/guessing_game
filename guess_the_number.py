print("""\t╔═════════════════════════╗
\t║    No. Guessing Game    ║
\t╚═════════════════════════╝""")
print("  \tNote : 5 Attempts Only")
number = 18
no_of_guess = 1
try:
    while (no_of_guess <= 5):
        num = int(input(" Enter Number : "))
        if num > 20:
            print(" Your Guess is too High\n")
            pass
        elif num > 18:
            print(" Your Guess is High\n")
        elif num < 18 and num >= 15:
            print(" Your Guess is Low\n")
        elif num < 15:
            print(" Your Guess is too Low\n")
        else :
            print("\n Your Guess is Right\n\t\tYou Won")
            print(" No. of Guess Remained: ", 5 - no_of_guess)
            break
        print(" Remaining Guesses : ", 5 - no_of_guess)
        no_of_guess = no_of_guess + 1
except Exception as error:
    print("\n Alphabets , Symbols are not allowed !!!\n\t\tExiting Program")
if no_of_guess > 5:
    print(" Game Over")
