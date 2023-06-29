import copy
def pad(num: int) -> str:
    x = str(num)
    if len(x) > 1:
        return x
    else:
        return "0"+x


def pad_all(nums: list) -> list:
    x = []
    for i in nums:
        x.append(pad(i))
    return x



def initial_state() -> tuple:
    return (0, [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0])


def game_over(state: tuple) -> bool:
    lst = state[1]
    if (lst[0] == lst[1] == lst[2] == lst[3] == lst[4] == lst[5] == 0) or (lst[7] == lst[8] == lst[9] == lst[10] == lst[11] == lst[12] == 0):
        return True
    else:
        return False

def valid_actions(state: tuple) -> list:
    actions = []
    lst = state[1]
    player = state[0]
    if player == 0:
        for i in range(6):
            if lst[i] > 0:
                actions.append(i)
        return actions
    else:
        for i in range(6):
            if lst[i+7] >0: actions.append(i+7)
        return actions



def mancala_of(player: int) -> int:
    if player ==0: return 6
    elif player==1: return 13


def pits_of(player: int) -> list:
   if player ==0:
       return [0,1,2,3,4,5]
   elif player==1:
        return [7,8,9,10,11,12]


def player_who_can_do(move: int) -> int:
    if move in [0,1,2,3,4,5] : return 0
    elif move in [7,8,9,10,11,12]: return 1



def opposite_from(position: int) -> int:
    d_p_1 = {}
    d_p_1[0]=12
    d_p_1[1]=11
    d_p_1[2]=10
    d_p_1[3]=9
    d_p_1[4]=8
    d_p_1[5]=7

    d_p_1[7]=5
    d_p_1[8]=4
    d_p_1[9]=3
    d_p_1[10]=2
    d_p_1[11]=1
    d_p_1[12]=0
    return d_p_1[position]



def play_turn(move: int, board: list) -> tuple:
    player = player_who_can_do(move)
    new_board = copy.deepcopy(board)
    gems = new_board[move]
    new_board[move] = 0

    hasht = {}
    hasht[0] =1
    hasht[1] = 0

    if player ==0:
         x =0
         offset = 1
         gems_counter = gems
         for i in range(gems):
            if i + move + offset == 13: offset += 1
            elif (i+move+offset) - 14 == 13: offset += 1

            if i + move +offset > 13:
                gem_position = (i+move+offset) - 14
            else:
                gem_position = i + move + offset

            new_board[gem_position] += 1
            gems_counter -= 1
            if gems_counter ==0 and gem_position==6: x = 1

            if gems_counter==0 and gem_position in pits_of(0) and new_board[gem_position] == 1 and new_board[opposite_from(gem_position)] > 0:
                gems_from_myside = new_board[gem_position]
                gems_from_opside = new_board[opposite_from(gem_position)]
                new_board[6] = gems_from_myside+gems_from_opside
                new_board[gem_position] = 0
                new_board[opposite_from(gem_position)] = 0

         return (hasht[x],new_board)


    if player ==1:

         x_2 = 1
         offset = 1
         gems_counter2 = gems
         for i in range(gems):
            if i + move + offset == 6: offset += 1
            elif (i+move+offset) - 14 == 6: offset += 1

            if i + move +offset > 13:
                gem_position = (i+move+offset) - 14
            else:
                gem_position = i + move + offset

            new_board[gem_position] += 1
            gems_counter2 -= 1
            if gems_counter2 == 0 and gem_position == 13:  x_2 = 0

            if gems_counter2==0 and gem_position in pits_of(1) and new_board[gem_position] == 1 and new_board[opposite_from(gem_position)] > 0:
                gems_from_myside = new_board[gem_position]
                gems_from_opside = new_board[opposite_from(gem_position)]

                new_board[13] = gems_from_myside+gems_from_opside
                new_board[gem_position] = 0
                new_board[opposite_from(gem_position)] = 0


         return (hasht[x_2],new_board)





def clear_pits(board: list) -> list:

    length = len(board)
    middle_index = length // 2
    first_half = board[:middle_index]
    second_half = board[middle_index:]

    for i in range(6):
        first_half[6] += first_half[i]
        first_half[i]=0
        second_half[6] += second_half[i]
        second_half[i] = 0
    return (first_half+second_half)






def perform_action(action, state):
    player, board = state
    new_player, new_board = play_turn(action, board)
    if 0 in [len(valid_actions((0, new_board))), len(valid_actions((1, new_board)))]:
        new_board = clear_pits(new_board)
    return new_player, new_board


def score_in(state: tuple) -> int:
    lst = state[1]
    return lst[6] - lst[13]


def is_tied(board: list) -> bool:
    if board[mancala_of(0)] - board[mancala_of(1)] == 0: return True
    else: return False


def winner_of(board: list) -> int:
    if board[mancala_of(0)] > board[mancala_of(1)]: return 0
    elif board[mancala_of(0)] < board[mancala_of(1)]: return 1



def string_of(board: list) -> str:
    new_board = pad_all(board)
    return '\n           {} {} {} {} {} {}\n        {}                   {}\n           {} {} {} {} {} {}\n'.format(new_board[12],new_board[11],new_board[10],new_board[9],new_board[8],new_board[7],new_board[13],new_board[6],new_board[0],new_board[1],new_board[2],new_board[3],new_board[4],new_board[5])
