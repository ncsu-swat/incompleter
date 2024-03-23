#Source: https://stackoverflow.com/questions/44447862/attributeerror-in-python-regarding-classes
import tkinter

DEFAULT_FONT = 'Helvetica, 16'


class UserInterface:
    def __init__(self):
        self._root_window = tkinter.Tk()

        self._canvas = tkinter.Canvas(master=self._root_window,
                                      width=400,
                                      height=400,
                                      background='#2A722E')

        self._canvas.grid(row=0,
                          column=0,
                          padx=30,
                          pady=30,
                          sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S)

        self._ask_user_input()

    def run(self):
        self._root_window.mainloop()

    def _ask_user_input(self):
        user_input = UserInput()
        user_input.show()

        if user_input.ok_is_clicked():
            input_list = user_input.get_input_list()
            return input_list


class UserInput:
    def __init__(self):
        self._user_input = tkinter.Toplevel()

        row_num = tkinter.Label(master=self._user_input,
                                text='Specify a row number 4-16:',
                                font=DEFAULT_FONT)
        row_num.grid(row=0,
                     column=0,
                     padx=10,
                     pady=10,
                     sticky=tkinter.W)

        self._row_num_entry = tkinter.Entry(master=self._user_input,
                                            width=15,
                                            font=DEFAULT_FONT)
        self._row_num_entry.grid(row=0,
                                 column=1,
                                 padx=10,
                                 pady=10,
                                 sticky=tkinter.E)

        col_num = tkinter.Label(master=self._user_input,
                                text='Specify a column number 4-16:',
                                font=DEFAULT_FONT)
        col_num.grid(row=1,
                     column=0,
                     padx=10,
                     pady=10,
                     sticky=tkinter.W)

        self._col_num_entry = tkinter.Entry(master=self._user_input,
                                            width=15,
                                            font=DEFAULT_FONT)
        self._col_num_entry.grid(row=1,
                                 column=1,
                                 padx=10,
                                 pady=10, sticky=tkinter.E)

        first_player = tkinter.Label(master=self._user_input,
                                     text='Specify the first player B/W:',
                                     font=DEFAULT_FONT)
        first_player.grid(row=2,
                          column=0,
                          padx=10,
                          pady=10,
                          sticky=tkinter.W)

        self._first_player_entry = tkinter.Entry(master=self._user_input,
                                                 width=15,
                                                 font=DEFAULT_FONT)
        self._first_player_entry.grid(row=2,
                                      column=1,
                                      padx=10,
                                      pady=10,
                                      sticky=tkinter.W)

        win_condition = tkinter.Label(master=self._user_input,
                                      text='Specify a winning condition, < or >:',
                                      font=DEFAULT_FONT)
        win_condition.grid(row=3,
                           column=0,
                           padx=10,
                           pady=10,
                           sticky=tkinter.W)

        self._win_condition_entry = tkinter.Entry(master=self._user_input,
                                                  width=15,
                                                  font=DEFAULT_FONT)
        self._win_condition_entry.grid(row=3,
                                       column=1,
                                       padx=10,
                                       pady=10,
                                       sticky=tkinter.E)

        ok_button = tkinter.Button(master=self._user_input,
                                   text='OK',
                                   font=DEFAULT_FONT,
                                   command=self._ok_button_clicked)
        ok_button.grid(row=4,
                       columnspan=2,
                       padx=40,
                       pady=40)

        self._ok_clicked = False
        self._input_list = []

    def show(self) -> None:
        self._user_input.grab_set()
        self._user_input.wait_window()

    def ok_is_clicked(self) -> bool:
        return self._ok_clicked

    def _ok_button_clicked(self):
        self._ok_clicked = True

        row_num = self._row_num_entry.get()
        col_num = self._col_num_entry.get()
        starter = self._first_player_entry.get()
        winning = self._win_condition_entry.get()

        self._input_list.extend([row_num, col_num, starter, winning])

        self._user_input.destroy()

    def get_input_list(self) -> list:
        return self._input_list


if __name__ == '__main__':
    game = UserInterface()
    game.run()