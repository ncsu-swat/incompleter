#Source: https://stackoverflow.com/questions/57117240/super-attributeerror-when-trying-to-access-ids
import time
import random
import kivy
from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.button import Button

from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

class Cell(Button):
    def __init__(self, text, loc, board, **kwargs):
        super(Cell, self).__init__(**kwargs)
        self.size = (25,25)
        self.board = board
        self.loc = loc
        self.text = text
        self.val = 0
        self.bind(on_touch_up = self.onPress)
        self.visible = False
        self.app = App.get_running_app()

    def onPress(self, instance, touch):
        if self.collide_point(*touch.pos):
            if self.visible == False:
                self.visible = True
                if touch.button == 'right':
                    if self.text == '!':
                        self.text = '?'
                    else:
                        self.text = '!'
                elif touch.button == 'left':
                    self.text = self.val
                    if self.val == 'X':
                        None
                    elif self.val == '0':
                        self.revealNeighbors(self.loc[0],self.loc[1])
                    else:
                        None

    def revealNeighbors(self,y,x):
        for i in range(-1,2):
            for j in range(-1,2):
                if (0 <= (self.loc[0] + i) < self.board[0]) and (0 <= (self.loc[1] + j) < self.board[1]):
                    print(self)
                    if self.app.root.ids.myboard.cells[i][j].visible != True:
                        self.app.ids.myboard.cells[i][j].visible = True
                        self.app.ids.myboard.cells[i][j].text = self.app.ids.myboard.cells[i][j].val
                        if self.app.ids.myboard.cells[i][j].val == '0':
                            self.app.root.ids.myboard.cells[i][j].revealNeighbors(self.app.ids.myboard.cells[i][j],i,j)


        None


class GameBoard(GridLayout):
    def __init__(self, **kwargs):
        id: myboard
        name: "Board"
        super(GameBoard, self).__init__(**kwargs)

        self.row_force_default = True
        self.row_default_height = 30
        self.col_force_default = True
        self.col_default_width = 30

        self.cols = 30
        self.rows = 16
        Window.size = (self.cols * self.col_default_width, self.rows * self.row_default_height)
        self.cells = list()
        mines = 0
        minelst = list()

        self.score = 0

        for i in range(self.rows):
            temp = list()
            for j in range(self.cols):
                newCell = Cell(text = '0',loc = [i,j], board = [self.rows,self.cols])
                temp.append(newCell)
                self.add_widget(temp[-1])
            self.cells.append(temp)

        for k in range(mines):
            randX = random.randint(0,self.cols - 1)
            randY = random.randint(0,self.rows - 1)
            while self.cells[randY][randX].text == 'X':
                randX = random.randint(0,self.cols - 1)
                randY = random.randint(0,self.rows - 1)
            self.cells[randY][randX].text = 'X'
            temp = list()
            temp.append(randY)
            temp.append(randX)
            minelst.append(temp)
        minelst.sort()

        for mine in minelst:
            if mine[0] == 0: # first row
                if mine[1] == 0: # top-left corner
                    if self.cells[0][1].text != 'X':
                        self.cells[0][1].text = str(int(self.cells[0][1].text) + 1)
                    if self.cells[1][0].text != 'X':
                        self.cells[1][0].text = str(int(self.cells[1][0].text) + 1)
                    if self.cells[1][1].text != 'X':
                        self.cells[1][1].text = str(int(self.cells[1][1].text) + 1)
                elif mine[1] == (self.cols -1): # top-right corner
                    if self.cells[0][self.cols -2].text != 'X':
                        self.cells[0][self.cols -2].text = str(int(self.cells[0][self.cols -2].text) + 1)
                    if self.cells[1][self.cols -1].text != 'X':
                        self.cells[1][self.cols -1].text = str(int(self.cells[1][self.cols -1].text) + 1)
                    if self.cells[1][self.cols -2].text != 'X':
                        self.cells[1][self.cols -2].text = str(int(self.cells[1][self.cols -2].text) + 1)
                else:
                    if self.cells[0][mine[1]-1].text != 'X':
                        self.cells[0][mine[1]-1].text = str(int(self.cells[0][mine[1]-1].text) + 1)
                    if self.cells[0][mine[1]+1].text != 'X':
                        self.cells[0][mine[1]+1].text = str(int(self.cells[0][mine[1]+1].text) + 1)
                    for i in range(3):
                        if self.cells[1][(mine[1]-1)+i].text != 'X':
                            self.cells[1][(mine[1]-1)+i].text = str(int(self.cells[1][(mine[1]-1)+i].text) + 1)
            elif mine[0] == (self.rows -1): # bottom row
                if mine[1] == 0: # bottom-left corner
                    if self.cells[self.rows -1][1].text != 'X':
                        self.cells[self.rows -1][1].text = str(int(self.cells[self.rows -1][1].text) + 1)
                    if self.cells[self.rows -2][0].text != 'X':
                        self.cells[self.rows -2][0].text = str(int(self.cells[self.rows -2][0].text) + 1)
                    if self.cells[self.rows -2][1].text != 'X':
                        self.cells[self.rows -2][1].text = str(int(self.cells[self.rows -2][1].text) + 1)
                elif mine[1] == (self.cols -1): # bottom-right corner
                    if self.cells[self.rows -1][self.cols -2].text != 'X':
                        self.cells[self.rows -1][self.cols -2].text = str(int(self.cells[self.rows -1][self.cols -2].text) + 1)
                    if self.cells[self.rows -2][self.cols -1].text != 'X':
                        self.cells[self.rows -2][self.cols -1].text = str(int(self.cells[self.rows -2][self.cols -1].text) + 1)
                    if self.cells[self.rows -2][self.cols -2].text != 'X':
                        self.cells[self.rows -2][self.cols -2].text = str(int(self.cells[self.rows -2][self.cols -2].text) + 1)
                else:
                    if self.cells[self.rows -1][mine[1]-1].text != 'X':
                        self.cells[self.rows -1][mine[1]-1].text = str(int(self.cells[self.rows -1][mine[1]-1].text) + 1)
                    if self.cells[self.rows -1][mine[1]+1].text != 'X':
                        self.cells[self.rows -1][mine[1]+1].text = str(int(self.cells[self.rows -1][mine[1]+1].text) + 1)
                    for i in range(3):
                        if self.cells[self.rows -2][(mine[1]-1)+i].text != 'X':
                            self.cells[self.rows -2][(mine[1]-1)+i].text = str(int(self.cells[self.rows -2][(mine[1]-1)+i].text) + 1)
            elif mine[1] == 0: # left column w/o corners
                if self.cells[mine[0]-1][0].text != 'X':
                    self.cells[mine[0]-1][0].text = str(int(self.cells[mine[0]-1][0].text) + 1)
                if self.cells[mine[0]+1][0].text != 'X':
                    self.cells[mine[0]+1][0].text = str(int(self.cells[mine[0]+1][0].text) + 1)
                for i in range(3):
                    if self.cells[(mine[0]-1)+i][1].text != 'X':
                        self.cells[(mine[0]-1)+i][1].text = str(int(self.cells[(mine[0]-1)+i][1].text)+1)
            elif mine[1] == (self.cols -1): # right column w/o corners
                if self.cells[mine[0]-1][self.cols -1].text != 'X':
                    self.cells[mine[0]-1][self.cols -1].text = str(int(self.cells[mine[0]-1][self.cols -1].text) + 1)
                if self.cells[mine[0]+1][self.cols -1].text != 'X':
                    self.cells[mine[0]+1][self.cols -1].text = str(int(self.cells[mine[0]+1][self.cols -1].text) + 1)
                for i in range(3):
                    if self.cells[(mine[0]-1)+i][self.cols -2].text != 'X':
                        self.cells[(mine[0]-1)+i][self.cols -2].text = str(int(self.cells[(mine[0]-1)+i][self.cols -2].text)+1)
            else: # interior mines
                for i in range(3):
                    if self.cells[mine[0]-1][(mine[1]-1)+i].text != 'X':
                        self.cells[mine[0]-1][(mine[1]-1)+i].text = str(int(self.cells[mine[0]-1][(mine[1]-1)+i].text)+1)
                    if self.cells[mine[0]+1][(mine[1]-1)+i].text != 'X':
                        self.cells[mine[0]+1][(mine[1]-1)+i].text = str(int(self.cells[mine[0]+1][(mine[1]-1)+i].text)+1)
                if self.cells[mine[0]][mine[1]-1].text != 'X':
                    self.cells[mine[0]][mine[1]-1].text = str(int(self.cells[mine[0]][mine[1]-1].text)+1)
                if self.cells[mine[0]][mine[1]+1].text != 'X':
                    self.cells[mine[0]][mine[1]+1].text = str(int(self.cells[mine[0]][mine[1]+1].text)+1)

        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].val = self.cells[i][j].text
                self.cells[i][j].text = '?'

class MineSweeper(App):
    def build(self):
        self.root = GameBoard()
        return self.root

mineSweeper = MineSweeper()

mineSweeper.run()