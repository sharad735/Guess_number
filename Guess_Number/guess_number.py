import random
# def guess(x):
#     random_number = random.randint(1,x)
#     guess = 0
#     while guess != random_number:

#         guess = int(input(f"Guess a number between 1 and {x} : "))
#         if guess > random_number:

#             print("sorry!guess again.Too high")
#         elif guess < random_number:

#             print("sorry!guess again.Too low")


#     print(f"Congrats!you guessed it right!the number {random_number}")
def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:

            guess = random.randint(low,high)
        else:
            guess = low
        feedback = (f"Is {guess} too high (h),too low (l),correct(c)")
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"Computer guessed your number {guess} correctly")  

# guess(12)
computer_guess(12)