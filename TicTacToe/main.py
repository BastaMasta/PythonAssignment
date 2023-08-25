from play_user import *

game_map = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


while True:
    # Player 1
    clear()
    print_map(game_map)
    game_map = play_player("❌", game_map)
    if check_won(game_map):
        print("Player 1 Has won the game!")
        print_map(game_map)
        break
    if check_completed(game_map):
        print_map(game_map)
        print("Game finished!\nNobody won!\nITS A DRAW!!!!!")
        break

    # Player 2
    clear()
    print_map(game_map)
    game_map = play_player("⭕", game_map)
    if check_won(game_map):
        print("Player 2 Has won the game!")
        print_map(game_map)
        break
    if check_completed(game_map):
        print_map(game_map)
        print("Game finished!\nNobody won!\nITS A DRAW!!!!!")
        break

print("Thanks for playing my game!")
