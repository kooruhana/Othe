# Yuchen Rong ID:75819508

import othello

def interface_console():
    print('FULL')
    col = othello.get_col()
    row = othello.get_row()
    game = othello.GameState(col,row)
    game._print()
    while game._check_board_full() == False:
        try:
            while True:
                user_input = user_move_input()
                col_num = int(user_input[0])-1
                row = int(user_input[1])-1
                if game._check_a_move(col_num,row) == True:
                        game._change_turn()
                        break
                else:
                        print('INVALID')
                        break
            print('\n')
            game._print()
            print('\n')
        except IndexError and ValueError:
            print('INVALID')
    print("Game Over")
    print('The winner is {}'.format(game._get_winner()))



def user_move_input()->list:
    """Get user's input and split it
    """
    user_input = input()
    try:
        input_list = user_input.split()
        return input_list
    except:
        print('Invalid')

if __name__ == '__main__':
    interface_console()
