#bishanpreet 102003243
#jasleen 102003238
from os import stat
from mancala_helpers import *
from mancala_minimax import minimax, simple_evaluate

def get_user_action(state):
    actions = list(map(str, valid_actions(state)))
    player, board = state
    prompt = "Player %d, choose an action (%s): " % (player, ",".join(actions))
    while True:
        action = input(prompt)
        if action in actions: return int(action)
        print("Invalid action, try again.")

if __name__ == "__main__":

    max_depth = 1
    state = initial_state()
    while not game_over(state):

        player, board = state
        print(string_of(board))
        if player == 0:
            action = get_user_action(state)
            state = perform_action(action, state)
        else:
            print("--- AI's turn --->")
            #print(string_of(board))
            print(state)
            print(max_depth)

            state, _ = minimax(state, max_depth, simple_evaluate)
            #print(string_of(board))

    player, board = state
    print(string_of(board))
    if is_tied(board):
        print("Game over, it is tied.")
    else:
        winner = winner_of(board)
        print("Game over, player %d wins." % winner)
