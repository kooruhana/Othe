#Yuchen Rong ID:75819508
import othello,tkinter,math

DEFAULT_FONT = ('Helvetica', 14)


class GameInfo():
    def __init__(self):
        self.rootwindow = tkinter.Tk()
        self.rootwindow.title('Othello Game Options')

        # COLUMN
        self._column_num = tkinter.Spinbox(master=self.rootwindow,values = (4,6,8,10,12,14,16))

        self._column_num.grid(row = 1, column = 1, padx = 0, pady = 0,
            sticky = tkinter.E)

        column_label = tkinter.Label(
            master=self.rootwindow,text='Column number:',font=DEFAULT_FONT
        )

        column_label.grid(row = 1, column = 0, padx = 0, pady = 0,
            sticky = tkinter.W)
        # ROW
        self._row_num = tkinter.Spinbox(self.rootwindow,values = (4,6,8,10,12,14,16))

        self._row_num.grid(row = 2, column = 1, padx = 0, pady = 0,
            sticky = tkinter.E)

        row_label = tkinter.Label(
            master = self.rootwindow,text = 'Row number:',font=DEFAULT_FONT
        )

        row_label.grid(row = 2, column = 0, padx = 0, pady = 0,
            sticky = tkinter.W)
        # START WITH COLOR

        self._start_color = tkinter.Spinbox(self.rootwindow,values = ('Black','White'))

        self._start_color.grid(row=3,column=1,padx=0,pady=0,sticky=tkinter.E
        )

        start_color_label = tkinter.Label(
            master=self.rootwindow,text = "Start color:",font = DEFAULT_FONT
        )

        start_color_label.grid(row = 3, column = 0, padx = 0, pady = 0,
            sticky = tkinter.W)
        # TOP LEFT

        self._top_left = tkinter.Spinbox(self.rootwindow,values = ('Black','White'))

        self._top_left.grid(row=4,column=1,padx=0,pady=0,sticky=tkinter.E
        )

        top_left_label = tkinter.Label(
            master=self.rootwindow,text = "Top left:",font = DEFAULT_FONT
        )

        top_left_label.grid(row = 4, column = 0, padx = 0, pady = 0,
            sticky = tkinter.W)

        # Win method

        self._win_method = tkinter.Spinbox(self.rootwindow,values = ('>','<'))

        self._win_method.grid(row=5,column=1,padx=0,pady=0,sticky=tkinter.E
        )

        win_method_label = tkinter.Label(
            master=self.rootwindow,text = "Win method:",font = DEFAULT_FONT
        )

        win_method_label.grid(row = 5, column = 0, padx = 0, pady = 0,
            sticky = tkinter.W)

        generate_button = tkinter.Button(
            master = self.rootwindow, text = "Start", font = DEFAULT_FONT,
            command = self.read_info
        )

        generate_button.grid(
            row = 0, column = 0, padx = 0, pady = 0,
            sticky = tkinter.W
        )

        version_label = tkinter.Label(
            master=self.rootwindow,text = 'Version:Full',font = DEFAULT_FONT
        )

        version_label.grid(
            row = 0, column = 1, padx = 0, pady = 0,
            sticky = tkinter.E
        )
    def start(self):
        self.rootwindow.mainloop()

    def read_info(self):
        """Get all the choices of users
        """
        self._col = self._column_num.get()

        self._row = self._row_num.get()

        self._begin_color = self._start_color.get()

        self._top_left_color = self._top_left.get()

        self._users_win_method = self._win_method.get()

        self.rootwindow.destroy()
class GUI():
    def __init__(self):
        self.read_info()
        self.rootwindow = tkinter.Tk()
        self.rootwindow.title('Othello')
        self._canvas = tkinter.Canvas(
            master = self.rootwindow, width = 500, height = 500,
            background = "#0C6136"
        )
        self._black_score = tkinter.IntVar()
        self._white_score = tkinter.IntVar()
        self._turn = tkinter.StringVar()
        self._winner = tkinter.StringVar()

        self._canvas.bind('<Configure>', self._on_canvas_resize)
        self._canvas.bind('<Button-1>',self._on_button_click)

        self._canvas.grid(
            row = 1, column = 0, padx = 0, pady = 0,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self.rootwindow.rowconfigure(0, weight = 1)
        self.rootwindow.columnconfigure(0, weight = 1)
        self._canvas.update()
        self.draw_board()

    def _on_button_click(self,event:tkinter.Event):
        x = event.x
        y = event.y

        cor_x = roundown(x,self._col_interval)
        cor_y = roundown(y,self._row_interval)

        if self._new_game._new_game_dict['board'][cor_x][cor_y]!=0:
            return
        else:
            if self._new_game._check_a_move(cor_x,cor_y) == True:
                self._new_game._change_turn()
            else:
                pass
        self._canvas.update()
        self.draw_board()

    def draw_info_board(self):
        """Draw the information board which shows the number of black and white grids and current turn and the winner
           if there is one
        """
        #Get current turn
        if self._new_game._new_game_dict['turn'] == 1:
            _current_turn='Black'
            _current_color = '#414A4C'
        else:
            _current_turn='White'
            _current_color='#F5F5F5'

        _white_score = self._new_game._white_num()
        _black_score = self._new_game._black_num()


        self._white_score.set(_white_score)
        self._black_score.set(_black_score)

        self._game_info_board = tkinter.Frame(master=self.rootwindow)

        self._game_info_board.grid(
            row=0,column=0,padx=0,pady=0
        )

        #Black score

        self._black_label = tkinter.Label(
            master=self._game_info_board,text = 'Black:',font = DEFAULT_FONT,bg='#414A4C'
        )
        self._black_label.grid(
            row = 0,column=0,sticky=tkinter.W
        )
        self._black_var = tkinter.Label(
            master=self._game_info_board,textvariable=self._black_score,font=DEFAULT_FONT,
            bg='#414A4C'
        )
        self._black_var.grid(
            row=0,column=1,sticky=tkinter.W
        )

        #White score
        self._white_label = tkinter.Label(
            master=self._game_info_board,text = 'White:',font = DEFAULT_FONT,bg='#F5F5F5'
        )
        self._white_label.grid(
            row = 0,column=4,sticky = tkinter.E
        )
        self._white_var = tkinter.Label(
            master=self._game_info_board,textvariable=self._white_score,font=DEFAULT_FONT,
            bg='#F5F5F5'
        )
        self._white_var.grid(
            row=0,column=5,sticky =tkinter.E
        )

        #Current turn

        self._turn_label = tkinter.Label(
            master=self._game_info_board,text = 'Turn:',font = DEFAULT_FONT,bg=_current_color
        )
        self._turn_label.grid(
            row = 0,column=2
        )
        self._turn_var = tkinter.Label(
            master=self._game_info_board,text=_current_turn,font=DEFAULT_FONT,
            bg=_current_color
        )
        self._turn_var.grid(
            row=0,column=3
        )

        #Winner
        _winner = ''
        if self._new_game._check_board_full()==True:
            _winner = self._new_game._get_winner()

        self._winner_board = tkinter.Frame(master=self.rootwindow)
        self._winner_board.grid(
            row = 2,column = 0
        )

        self._winner_label = tkinter.Label(
            master=self._winner_board,text = 'Winner:',font = DEFAULT_FONT
        )
        self._winner_label.grid(
            row = 0,column=0
        )
        self._winner_var = tkinter.Label(
            master=self._winner_board,text=_winner,font=DEFAULT_FONT,
        )
        self._winner_var.grid(
            row=0,column=1
        )
        print(_winner)

    def draw_board(self):
        """Draw the whole board includes black and white grids
        """
        window_width = self._canvas.winfo_width()
        window_height = self._canvas.winfo_height()
        self._col_interval = window_width/self._col
        self._row_interval = window_height/self._row
        x0 = 0
        y0 = 0
        while x0 < window_width:
            self._canvas.create_line(x0,y0,x0,window_height)
            x0 += self._col_interval
        x0 = 0
        y0 = 0
        while y0 < window_height:
            self._canvas.create_line(x0,y0,window_width,y0)
            y0 += self._row_interval

        for col in range(self._col):
            for row in range(self._row):
                if self._new_game._new_game_dict['board'][col][row]==1:
                    self._canvas.create_oval((col)*self._col_interval,(row)*self._row_interval,(col+1)*self._col_interval,(row+1)*self._row_interval,fill = '#1A1110')
                elif self._new_game._new_game_dict['board'][col][row]==2:
                    self._canvas.create_oval((col)*self._col_interval,(row)*self._row_interval,(col+1)*self._col_interval,(row+1)*self._row_interval,fill = '#FEFEFA')
        self.draw_info_board()

    def start(self):
        self.rootwindow.mainloop()

    def _on_canvas_resize(self,event: tkinter.Event):
        self._canvas.delete(tkinter.ALL)
        self.draw_board()

    def read_info(self):
        """Get the information from the option window
        """
        self._information = GameInfo()
        self._information.start()
        self._col = int(self._information._col)

        self._row = int(self._information._row)

        self._top_left = self._information._top_left_color

        self._start_color  = self._information._begin_color

        self._win_method = self._information._users_win_method

        self._new_game = othello.GameState(self._col,self._row,self._start_color,self._top_left,self._win_method)

def roundup(x,interval):
    """Get the integer used for bottom right coordinates
    """
    return int(math.ceil(x / interval))

def roundown(x,interval):
    """Get the integer used for top left coordinates
    """
    return int(math.floor(x / interval))

if __name__ == '__main__':
    GUI().start()

