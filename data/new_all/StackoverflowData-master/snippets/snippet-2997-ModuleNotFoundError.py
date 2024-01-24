#Source: https://stackoverflow.com/questions/55409448/tkinter-attribute-error-object-has-no-attribute-i-dont-understand-why-it-can
##Importing modules-------------------------------------------------------
#------------------------------------------------------------------------
import tkinter as tk
from tkinter import messagebox


#Setting up GUI ---------------------------------------------------------
#------------------------------------------------------------------------
#MainWindow
class FireofStromwarld(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("The Fire of Stromwarld")
        self.config(bg = 'grey')

        #Centering Window
        WindowWidth = 900
        WindowHeight = 600
        ScreenWidth = self.winfo_screenwidth()
        ScreenHeight = self.winfo_screenheight()
        xCoordinate = int((ScreenWidth / 2) - (WindowWidth / 2))
        yCoordinate = int((ScreenHeight / 2) - (WindowHeight / 2))

        self.geometry('{}x{}+{}+{}'.format(WindowWidth, WindowHeight, xCoordinate, yCoordinate))
        self.resizable(width = False, height = False)

        #Setting up container to hold all frames
        frmContainer = tk.Frame(self)
        frmContainer.config(width = 750,
                            height = 450,
                            bg = 'grey')
        frmContainer.grid_propagate(0)

        frmContainer.grid(row = 0, column = 0, padx = 75, pady = 75)

        #Listing avaliable frames
        self.frames = ['MainMenu', 'GameMenu']
        self.frames[0] = MainMenu(parent = frmContainer, controller = self)
        self.frames[1] = GameMenu(parent = frmContainer, controller = self)

        self.frames[0].grid(row = 0, column = 0, sticky = 'nsew')
        self.frames[1].grid(row = 0, column = 0, sticky = 'nsew')

        self.ShowFrame(0)

        #Menubar(The Problem Part)
        self.menuBar = tk.Menu(self)
        self.GameMenu = tk.Menu(self.menuBar, tearoff = 0)
        self.GameMenu.add_command(label = 'Exit',
                                  font = ('arial', 9),
                                  command = self.quit)

        self.menuBar.add_cascade(label = 'Game',
                                 menu = self.GameMenu)

        self.RemoveFunc()

    def ShowFrame(self, pagename):
        frame = self.frames[pagename]
        frame.tkraise()

    def CreateMenu(self):
        NewMenu = self.menuBar
        self.configure(menu = NewMenu)

    def RemoveFunc(self):
        emptyMenu = tk.Menu(self)
        self.configure(menu = emptyMenu)


#MainMenu
class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.config(bg = 'grey')

        #Objects on Main Menu
        lblTitle = tk.Label(self,
                            text = "The Fire of Stromwarld",
                            font = ('Arial', 28, 'bold'),
                            fg = 'brown',
                            bg = 'grey',
                            justify = 'center')

        btnStart = tk.Button(self,
                             text = "Start Game",
                             font = ('Arial',16),
                             bg = 'grey',
                             relief = 'flat',
                             command = lambda: controller.ShowFrame(1))

        btnExit = tk.Button(self,
                            text = "Exit",
                            font = ('Arial',16),
                            bg = 'grey',
                            relief = 'flat',
                            width = 9,
                            command = self.quit)

        #Positioning of Main Window Objects
        lblTitle.grid(row = 0, column = 0, padx = 178, pady = 75)
        btnStart.grid(row = 1, column = 0, pady = (50,20))
        btnExit.grid(row = 2, column = 0)


#GameMenu
class GameMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.config(bg = 'grey')

        #Creating Menu Base
        controller.CreateMenu()

        #Objects on Game Menu
        #Player and Monster Stat boxes
        frmPlayerStats = tk.Frame(self,
                                  width = 180,
                                  height = 150,
                                  borderwidth = 2,
                                  relief = 'ridge')
        frmPlayerStats.grid_propagate(0)

        frmMonStats = tk.Frame(self,
                            width = 180,
                            height = 80,
                            borderwidth = 2,
                            relief = 'groove')
        frmMonStats.grid_propagate(0)

        #Player Stats
        lblPlayerName = tk.Label(frmPlayerStats,
                                 text = "Player:",
                                 font = ('arial', 13))

        lblPlayerLevel = tk.Label(frmPlayerStats,
                                  text = "Lvl: 1",
                                  font = ('arial', 10))

        lblPlayerHPTitle = tk.Label(frmPlayerStats,
                                    text = "HP: ",
                                    font = ('arial', 10))

        lblPlayerHPStats = tk.Label(frmPlayerStats,
                                    text = "10 / 10",
                                    font = ('arial', 10),
                                    fg = 'green')

        lblPlayerMPTitle = tk.Label(frmPlayerStats,
                                    text = "MP: ",
                                    font = ('arial', 10))

        lblPlayerMPStats = tk.Label(frmPlayerStats,
                                    text = "5 / 5",
                                    font = ('arial', 10),
                                    fg = 'blue')

        lblPlayerBaseAttkTitle = tk.Label(frmPlayerStats,
                                          text = "Attack: ",
                                          font = ('arial', 10))

        lblPlayerBaseAttkStats = tk.Label(frmPlayerStats,
                                          text = "5",
                                          font = ('arial', 10),
                                          fg = 'red')

        lblPlayerWeapTitle = tk.Label(frmPlayerStats,
                                      text = "Weapon: ",
                                      font = ('arial', 10))

        lblPlayerWeapStats = tk.Label(frmPlayerStats,
                                      text = "None | +2",
                                      font = ('arial', 10))

        lblPlayerArmTitle = tk.Label(frmPlayerStats,
                                     text = "Armour: ",
                                     font = ('arial', 10))

        lblPlayerArmStats = tk.Label(frmPlayerStats,
                                     text = "5",
                                     font = ('arial', 10))

        #Monster Stats
        lblMonName = tk.Label(frmMonStats,
                              text = "Monster:",
                              font = ('arial', 11))

        lblMonHPTitle = tk.Label(frmMonStats,
                                 text = "HP: ",
                                 font = ('arial', 9))

        lblMonHPStats = tk.Label(frmMonStats,
                                 text = "10 / 10",
                                 font = ('arial', 9),
                                 fg = 'green')

        lblMonMPTitle = tk.Label(frmMonStats,
                                 text = "MP: ",
                                 font = ('arial', 9))

        lblMonMPStats = tk.Label(frmMonStats,
                                 text = "5 / 5",
                                 font = ('arial', 9),
                                 fg = 'blue')

        #Main Objects
        #Text display
        txtMain = tk.Text(self,
                          width = 78,
                          height = 22,
                          borderwidth = 1,
                          relief = 'solid',
                          wrap = 'word',
                          cursor = 'left_ptr')
        txtMain.grid_propagate(0)

        scrlTxtMain = tk.Scrollbar(self)
        txtMain.configure(yscrollcommand = scrlTxtMain.set)
        scrlTxtMain.configure(command = txtMain.yview)

        #User input
        lblentUserInput = tk.Label(self,
                                   text = '>>>',
                                   font = ('arial', 9),
                                   bg = 'white')

        entUserInput = tk.Entry(self,
                                font = ('arial', 9),
                                relief = 'sunken',
                                justify = 'left',
                                width = 69,
                                borderwidth = 2)

        btnUserInput = tk.Button(self,
                                 text = "Enter",
                                 font = ('arial', 7),
                                 relief = 'groove',
                                 width = 7)

        #Action Buttons
        btnAction1 = tk.Button(self,
                               text = "Attack",
                               font = ('arial', 10),
                               relief = 'raised',
                               cursor = 'X_cursor',
                               width = 10,
                               height = 2)
        btnAction1.grid_propagate(0)

        btnAction2 = tk.Button(self,
                               text = "Special",
                               font = ('arial', 10),
                               relief = 'raised',
                               cursor = 'cross_reverse',
                               width = 10,
                               height = 2,)
        btnAction2.grid_propagate(0)

        btnAction3 = tk.Button(self,
                               text = "Heal",
                               font = ('arial', 10),
                               relief = 'raised',
                               cursor = 'heart',
                               width = 10,
                               height = 2)
        btnAction3.grid_propagate(0)

        btnAction4 = tk.Button(self,
                               text = "Run",
                               font = ('arial', 10),
                               relief = 'raised',
                               cursor = 'right_side',
                               width = 10,
                               height = 2)
        btnAction4.grid_propagate(0)

        #Inventory
        lblInventoryTitle = tk.Label(self,
                                     text = 'Inventory:' + ' ' * 27,
                                     font = ('arial',11, 'italic'),
                                     bg = 'white')

        lstbInventory = tk.Listbox(self,
                                   font = ('arial', 9),
                                   width = 23,
                                   height = 11,
                                   cursor = 'hand2')

        scrllstbInventory = tk.Scrollbar(self)
        lstbInventory.configure(yscrollcommand = scrllstbInventory.set)
        scrllstbInventory.configure(command = lstbInventory.yview)

        #Positioning of Game Objects
        #Main object placements
        txtMain.grid(row = 0, column = 0, rowspan = 30, columnspan = 10)
        scrlTxtMain.grid(row = 0, column = 10, rowspan = 30, padx = (0, 1), sticky = 'nsw')

        #Entry line placement
        lblentUserInput.grid(row = 31, column = 0, columnspan = 2)
        entUserInput.grid(row = 31, column = 2, columnspan = 6, sticky = 'w')
        btnUserInput.grid(row = 31, column = 7, columnspan = 4, sticky = 'w')

        #Action buttons placements
        btnAction1.grid(row = 32, column = 3, padx = 15, pady = 20)
        btnAction2.grid(row = 32, column = 4, padx = 15, pady = 20)
        btnAction3.grid(row = 32, column = 5, padx = 15, pady = 20)
        btnAction4.grid(row = 32, column = 6, padx = 15, pady = 20)

        #Stats objects placenments
        frmPlayerStats.grid(row = 0, column = 11, columnspan = 2, padx = 3)
        lblPlayerName.grid(row = 0, column = 0, sticky = 'w')
        lblPlayerLevel.grid(row = 0, column = 1, sticky = 'w')
        lblPlayerHPTitle.grid(row = 1, column = 0, sticky = 'w')
        lblPlayerHPStats.grid(row = 1, column = 1, sticky = 'w')
        lblPlayerMPTitle.grid(row = 2, column = 0, sticky = 'w')
        lblPlayerMPStats.grid(row = 2, column = 1, sticky = 'w')
        lblPlayerBaseAttkTitle.grid(row = 3, column = 0, sticky = 'w')
        lblPlayerBaseAttkStats.grid(row = 3, column = 1, sticky = 'w')
        lblPlayerWeapTitle.grid(row = 4, column = 0, sticky = 'w')
        lblPlayerWeapStats.grid(row = 4, column = 1, sticky = 'w')
        lblPlayerArmTitle.grid(row = 5, column = 0, sticky = 'w')
        lblPlayerArmStats.grid(row = 5, column = 1, sticky = 'w')

        frmMonStats.grid(row = 1, column = 11, columnspan = 2, padx = 3, pady = 4)
        lblMonName.grid(row = 0, column = 0, sticky = 'w')
        lblMonHPTitle.grid(row = 1, column = 0, sticky = 'w')
        lblMonHPStats.grid(row = 1, column = 1, sticky = 'w')
        lblMonMPTitle.grid(row = 2, column = 0, sticky = 'w')
        lblMonMPStats.grid(row = 2, column = 1, sticky = 'w')

        #Inventory object placements
        lblInventoryTitle.grid(row = 2, column = 11, columnspan = 2, padx = 3, pady = (4,0), sticky = 'w')
        lstbInventory.grid(row = 3, column = 11, rowspan = 32, padx = (3,0), sticky = 'w')
        scrllstbInventory.grid(row = 3, column = 12, rowspan = 32, sticky = 'nsw')


#Runnning Program -------------------------------------------------------
#------------------------------------------------------------------------
game = FireofStromwarld()
game.mainloop()