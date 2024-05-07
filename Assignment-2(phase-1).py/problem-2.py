def player_1(chocolates):
    if chocolates <= 0:
        return -1
    elif chocolates == 1:
        return 1
    else:
        return player_2(chocolates - 1)


def player_2(chocolates):
    if chocolates <= 0:
        return 1
    elif chocolates == 1:
        return -1
    elif chocolates % 2 == 0:
        return player_1(chocolates - 2)
    else:
        return player_1(chocolates - 1)


def start_game(n):
    winner = player_1(n)
    if winner == 1:
        print("Player 1 Wins")
    else:
        print("Player 2 Wins")


start_game(10)