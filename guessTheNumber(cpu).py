import random
x = int(input('choose a number for guessing random number between 1 and yours: '))
def cpu_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high(H), too low(L) or correct(C)?'.lower())
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Whooooaaa! The computer guessed your number, {guess} correctly!')

cpu_guess(x)