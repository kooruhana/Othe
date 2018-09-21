# Yuchen Rong ID:75819508

BLACK = 1
WHITE = 2
NONE = 0


def new_game_board(COLUMNS:int,ROWS:int,top_left:str)->[[int]]:
    """Get the initial board of the game.
    """
    board = []
    for col in range(COLUMNS):
        board.append([])
        for row in range(ROWS):
            board[-1].append(NONE)
    if top_left == 'B':
        board[int(COLUMNS/2-1)][int(ROWS/2-1)] = BLACK
        board[int(COLUMNS/2)][int(ROWS/2)] = BLACK
        board[int(COLUMNS/2)][int(ROWS/2-1)] = WHITE
        board[int(COLUMNS/2-1)][int(ROWS/2)] = WHITE
    elif top_left == 'W':
        board[int(COLUMNS/2-1)][int(ROWS/2-1)] = WHITE
        board[int(COLUMNS/2)][int(ROWS/2)] = WHITE
        board[int(COLUMNS/2)][int(ROWS/2-1)] = BLACK
        board[int(COLUMNS/2-1)][int(ROWS/2)] = BLACK
    return board

def create_game_state_dict(board:[[int]],turn:str)->dict:
    turn_a = ''
    if turn == 'B':
        turn_a = BLACK
    elif turn == 'W':
        turn_a = WHITE
    game = {}
    game['board'] = board
    game['turn'] = turn_a
    game['winner'] = ""
    return game

def get_col()->int:
    """Get the column number
    """
    valid_list = [4,6,8,10,12,14,16]
    while True:
        try:
            col = int(input(""))
            while col not in valid_list:
                print('Invalid column number')
                col = int(input(""))

            return col
        except:
            print('Invalid column number')
            continue
def get_row()->int:
    """Get the row number
    """
    valid_list = [4,6,8,10,12,14,16]
    while True:
        try:
            row = int(input(""))
            while row not in valid_list:
                    print('Invalid row number')
                    row = int(input(""))
            return int(row)
        except:
            print('Invalid row number')
            continue





class GameState():
    def __init__(self,col,row,first_turn,top_left,win_method):
        self._col = col                             # line1
        self._row = row                             # line2

        self._first_turn = first_turn[0]

        self._top_left = top_left[0]

        self._win_mode = win_method

        new_board = new_game_board(self._col,self._row,self._top_left)
        self._new_game_dict = create_game_state_dict(new_board,self._first_turn)

    def _winner(self):
        return self._new_game_dict['winner']

    def _print(self):
            print("Black: {}         White:{}     ".format(self._black_num(),self._white_num()))
            print('\n')
            new_board = zip(*self._new_game_dict['board'])
            n = 0
            for col in new_board:
                while n < self._col:
                    for unit in col:
                        if unit == 0:
                            print('.',end='    ')
                        else:
                            if unit==1:
                                print('B',end='    ')
                            elif unit==2:
                                print('W',end='    ')

                        n+=1
                print('\n')
                n = 0

    def _change_turn(self):
        if self._new_game_dict['turn'] == BLACK:
            self._new_game_dict['turn'] = WHITE
        else:
            self._new_game_dict['turn'] = BLACK

    def _check_grid(self,col,row):
        """Check if it is an empty grid
        """
        if self._new_game_dict['board'][col][row] == NONE:
            return True
        else:
            return False

    def _check_end(self,check_all):
        """Check if the end of the line is valid to make a move
        """
        possible = []
        for list in check_all:
            try:
                if self._new_game_dict['board'][list[0]][list[1]] == NONE:
                    return
                else:
                    possible.append([list[0],list[1]])
            except IndexError:
                return
        if self._new_game_dict['board'][possible[-1][0]][possible[-1][1]] == self._new_game_dict['turn']\
                and self._new_game_dict['board'][possible[0][0]][possible[0][1]] != self._new_game_dict['turn']\
                and check_all[-1][0]>=0\
                and check_all[-1][1]>=0:
            for grid in possible[0:-1]:
                if self._new_game_dict['board'][grid[0]][grid[1]] == BLACK:
                    self._new_game_dict['board'][grid[0]][grid[1]] = WHITE
                elif self._new_game_dict['board'][grid[0]][grid[1]] == WHITE:

                    self._new_game_dict['board'][grid[0]][grid[1]] = BLACK

        else:
            return

    def _check_a_line(self,col,row,coldelta,rowdelta)->bool:
            """Check if making move is valid through single direction
            """
            color = self._new_game_dict['turn']
            check_all = []
            for i in range(1,17):
                try:
                     check_all.append([col+coldelta*i,row+rowdelta*i])
                     if not is_valid_column_number(col+coldelta*i,self._col) \
                            or not is_valid_row_number(row+rowdelta*i,self._row)\
                            or self._new_game_dict['board'][col+coldelta*i][row+rowdelta*i] == NONE\
                            or self._new_game_dict['board'][col+coldelta*i][row+rowdelta*i] == color:
                        break
                except:
                    pass
            self._check_end(check_all)
            try:
                if self._new_game_dict['board'][check_all[-1][0]][check_all[-1][1]] == self._new_game_dict['turn']\
                        and len(check_all)!=1\
                        and check_all[-1][0]>=0\
                        and check_all[-1][1]>=0:
                    self._new_game_dict['board'][col][row] = self._new_game_dict['turn']
                    return True

                else:
                    return False
            except IndexError:
                return False

    def _check_a_move(self,col,row)->bool:
          """Check the availability of making a move in all eight directions
          """
          all = [self._check_a_line(col,row,-1,-1),
                 self._check_a_line(col,row,0,-1),
                 self._check_a_line(col,row,1,-1),
                 self._check_a_line(col,row,1,0),
                 self._check_a_line(col,row,1,1),
                 self._check_a_line(col,row,0,1),
                 self._check_a_line(col,row,-1,1),
                 self._check_a_line(col,row,-1,0)
                 ]
          if True in all:
              return True
          else:
              return False


    def _white_num(self)->int:
        count = 0
        for c in self._new_game_dict['board']:
            for element in c:
                if element == 2:
                    count+=1
        return count

    def _black_num(self)->int:
        count = 0
        for c in self._new_game_dict['board']:
            for element in c:
                if element == 1:
                    count+=1
        return count

    def _check_board_full(self):
        """Check if the board is full
        """
        full = True
        for c in self._new_game_dict['board']:
            for element in c:
                if element == 0:
                    full = False
        return full

    #WINNER

    def _winner_type(self):
        if self._win_mode == '>':
            if self._white_num()>self._black_num():
                self._new_game_dict['winner'] = 'White'
            elif self._black_num()>self._white_num():
                self._new_game_dict['winner'] = 'Black'
            else:
                self._new_game_dict['winner'] = 'Draw'
        elif self._win_mode == '<':
            if self._white_num()<self._black_num():
                self._new_game_dict['winner'] = 'White'
            elif self._black_num()<self._white_num():
                self._new_game_dict['winner'] = 'Black'
            else:
                self._new_game_dict['winner'] = 'Draw'

    def _get_winner(self):
        self._winner_type()
        return self._new_game_dict['winner']







def is_valid_column_number(input_col:int,board_col:int)->bool:
    return 0 <= input_col < board_col

def is_valid_row_number(input_row:int,board_row:int)->bool:
    return 0 <= input_row < board_row