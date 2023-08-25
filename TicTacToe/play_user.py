from os import system, name


def clear():
    # Clear Terminal/Console Screen for every iteration
    if name == 'nt':
        _ = system('cls')  # For windows
    else:
        _ = system('clear')  # For Linux ond OSX


def play_player(character, game_map):
    """Play the given player's turn"""
    pl = {"❌": 1, "⭕": 2}
    pinp = input("Player {} Please enter your move (in the format A2, B1): ".format(pl[character]))
    row = ord(pinp[0].upper()) - 65
    column = int(pinp[1]) - 1
    try:
        if game_map[column][row] == " ":
            game_map[column][row] = character
            return game_map
        else:
            print("You cannot mark there!")
            return play_player(character, game_map)

    except IndexError:
        print("Please enter valid address!")
        return play_player(character, game_map)


def print_map(game_map):
    """Draw the game map"""
    print("     A | B | C  ")
    for e, i in enumerate(game_map):
        print("----------------")
        print("{}||  {} | {} | {}  ".format(e + 1, i[0], i[1], i[2]))


def check_won(game_map):
    """Check if anyone has won the game"""
    win_seq = ["❌", "⭕"]
    for i in win_seq:
        for j in range(0, 3):
            if game_map[j][0] == game_map[j][1] == game_map[j][2] == i:
                return True
            elif game_map[0][j] == game_map[1][j] == game_map[2][j] == i:
                return True
        if game_map[0][0] == game_map[1][1] == game_map[2][2] == i:
            return True
        elif game_map[0][2] == game_map[1][1] == game_map[2][0] == i:
            return True
        else:
            return False


def check_completed(game_map):
    """Check if the game map is exhausted (completely filled)"""
    for i in range(0, 3):
        for j in range(0, 3):
            if game_map[i][j] == " ":
                return False
    return True
