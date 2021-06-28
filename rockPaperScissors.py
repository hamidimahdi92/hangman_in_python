import random


def play():
    player = input(f'Pick up one: (r) for Rock, (p) for Paper and (s) for Scissors: \n')
    cpu = random.choice(['r', 'p', 's'])

    if player == cpu:
        return 'It\'s a draw!'

    # r > s, s > p, p > r

    if is_win(player, cpu):
        return 'You won!'

    return 'You fail'


def is_win(player, cpu):
    if (player == 'r' and cpu == 's') or (player == 's' and cpu == 'p') or (player == 'p' and cpu == 'r'):
        return True


print(play())
