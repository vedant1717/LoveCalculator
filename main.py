import random as rd
should_continue=True

while should_continue:
    male_name=input("Enter your name:\n")
    female_name=input("Enter your partner's name:\n")
    percent=rd.randint(0,100)
    print(f"Love between {male_name} & {female_name} is {percent}%.")
    user_inp=input("Do you want to check any other result? Y or N?\n").lower()
    if user_inp=='n':
        print("Thanks for using the love calculator.")
        should_continue=False