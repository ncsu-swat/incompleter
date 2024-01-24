# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55409448/tkinter-attribute-error-object-has-no-attribute-i-dont-understand-why-it-can
##Importing modules-------------------------------------------------------
#------------------------------------------------------------------------
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(559258)

except ImportError:
    pass
try:
    from tkinter import messagebox
    _l_(559260)

except ImportError:
    pass


#Setting up GUI ---------------------------------------------------------
#------------------------------------------------------------------------
#MainWindow
class FireofStromwarld(_a_(559262, _n_(559261, "tk", lambda: tk), "Tk")):
    _l_(559421)

    def __init__(self, *args, **kwargs):
        _l_(559391)

        _c_(559269, _a_(559265, _a_(559264, _n_(559263, "tk", lambda: tk), "Tk"), "__init__"), _n_(559266, "self", lambda: self), *_n_(559267, "args", lambda: args), **_n_(559268, "kwargs", lambda: kwargs))
        _l_(559270)

        _c_(559273, _a_(559272, _n_(559271, "self", lambda: self), "title"), "The Fire of Stromwarld")
        _l_(559274)
        _c_(559277, _a_(559276, _n_(559275, "self", lambda: self), "config"), bg = 'grey')
        _l_(559278)

        #Centering Window
        WindowWidth = 900
        _l_(559279)
        WindowHeight = 600
        _l_(559280)
        ScreenWidth = _c_(559283, _a_(559282, _n_(559281, "self", lambda: self), "winfo_screenwidth"))
        _l_(559284)
        ScreenHeight = _c_(559287, _a_(559286, _n_(559285, "self", lambda: self), "winfo_screenheight"))
        _l_(559288)
        xCoordinate = _c_(559292, _n_(559289, "int", lambda: int), (_n_(559290, "ScreenWidth", lambda: ScreenWidth) / 2) - (_n_(559291, "WindowWidth", lambda: WindowWidth) / 2))
        _l_(559293)
        yCoordinate = _c_(559297, _n_(559294, "int", lambda: int), (_n_(559295, "ScreenHeight", lambda: ScreenHeight) / 2) - (_n_(559296, "WindowHeight", lambda: WindowHeight) / 2))
        _l_(559298)

        _c_(559307, _a_(559300, _n_(559299, "self", lambda: self), "geometry"), _c_(559306, _a_(559301, '{}x{}+{}+{}', "format"), _n_(559302, "WindowWidth", lambda: WindowWidth), _n_(559303, "WindowHeight", lambda: WindowHeight), _n_(559304, "xCoordinate", lambda: xCoordinate), _n_(559305, "yCoordinate", lambda: yCoordinate)))
        _l_(559308)
        _c_(559311, _a_(559310, _n_(559309, "self", lambda: self), "resizable"), width = False, height = False)
        _l_(559312)

        #Setting up container to hold all frames
        frmContainer = _c_(559316, _a_(559314, _n_(559313, "tk", lambda: tk), "Frame"), _n_(559315, "self", lambda: self))
        _l_(559317)
        _c_(559320, _a_(559319, _n_(559318, "frmContainer", lambda: frmContainer), "config"), width = 750,
                            height = 450,
                            bg = 'grey')
        _l_(559321)
        _c_(559324, _a_(559323, _n_(559322, "frmContainer", lambda: frmContainer), "grid_propagate"), 0)
        _l_(559325)

        _c_(559328, _a_(559327, _n_(559326, "frmContainer", lambda: frmContainer), "grid"), row = 0, column = 0, padx = 75, pady = 75)
        _l_(559329)

        #Listing avaliable frames
        _n_(559330, "self", lambda: self).frames = ['MainMenu', 'GameMenu']
        _l_(559331)
        _a_(559333, _n_(559332, "self", lambda: self), "frames")[0] = _c_(559337, _n_(559334, "MainMenu", lambda: MainMenu), parent = _n_(559335, "frmContainer", lambda: frmContainer), controller = _n_(559336, "self", lambda: self))
        _l_(559338)
        _a_(559340, _n_(559339, "self", lambda: self), "frames")[1] = _c_(559344, _n_(559341, "GameMenu", lambda: GameMenu), parent = _n_(559342, "frmContainer", lambda: frmContainer), controller = _n_(559343, "self", lambda: self))
        _l_(559345)

        _c_(559349, _a_(559348, _a_(559347, _n_(559346, "self", lambda: self), "frames")[0], "grid"), row = 0, column = 0, sticky = 'nsew')
        _l_(559350)
        _c_(559354, _a_(559353, _a_(559352, _n_(559351, "self", lambda: self), "frames")[1], "grid"), row = 0, column = 0, sticky = 'nsew')
        _l_(559355)

        _c_(559358, _a_(559357, _n_(559356, "self", lambda: self), "ShowFrame"), 0)
        _l_(559359)

        #Menubar(The Problem Part)
        _n_(559360, "self", lambda: self).menuBar = _c_(559364, _a_(559362, _n_(559361, "tk", lambda: tk), "Menu"), _n_(559363, "self", lambda: self))
        _l_(559365)
        _n_(559366, "self", lambda: self).GameMenu = _c_(559371, _a_(559368, _n_(559367, "tk", lambda: tk), "Menu"), _a_(559370, _n_(559369, "self", lambda: self), "menuBar"), tearoff = 0)
        _l_(559372)
        _c_(559378, _a_(559375, _a_(559374, _n_(559373, "self", lambda: self), "GameMenu"), "add_command"), label = 'Exit',
                                  font = ('arial', 9),
                                  command = _a_(559377, _n_(559376, "self", lambda: self), "quit"))
        _l_(559379)

        _c_(559385, _a_(559382, _a_(559381, _n_(559380, "self", lambda: self), "menuBar"), "add_cascade"), label = 'Game',
                                 menu = _a_(559384, _n_(559383, "self", lambda: self), "GameMenu"))
        _l_(559386)

        _c_(559389, _a_(559388, _n_(559387, "self", lambda: self), "RemoveFunc"))
        _l_(559390)

    def ShowFrame(self, pagename):
        _l_(559400)

        frame = _a_(559393, _n_(559392, "self", lambda: self), "frames")[_n_(559394, "pagename", lambda: pagename)]
        _l_(559395)
        _c_(559398, _a_(559397, _n_(559396, "frame", lambda: frame), "tkraise"))
        _l_(559399)

    def CreateMenu(self):
        _l_(559409)

        NewMenu = _a_(559402, _n_(559401, "self", lambda: self), "menuBar")
        _l_(559403)
        _c_(559407, _a_(559405, _n_(559404, "self", lambda: self), "configure"), menu = _n_(559406, "NewMenu", lambda: NewMenu))
        _l_(559408)

    def RemoveFunc(self):
        _l_(559420)

        emptyMenu = _c_(559413, _a_(559411, _n_(559410, "tk", lambda: tk), "Menu"), _n_(559412, "self", lambda: self))
        _l_(559414)
        _c_(559418, _a_(559416, _n_(559415, "self", lambda: self), "configure"), menu = _n_(559417, "emptyMenu", lambda: emptyMenu))
        _l_(559419)


#MainMenu
class MainMenu(_a_(559423, _n_(559422, "tk", lambda: tk), "Frame")):
    _l_(559471)

    def __init__(self, parent, controller):
        _l_(559470)

        _c_(559429, _a_(559426, _a_(559425, _n_(559424, "tk", lambda: tk), "Frame"), "__init__"), _n_(559427, "self", lambda: self), _n_(559428, "parent", lambda: parent))
        _l_(559430)

        _n_(559431, "self", lambda: self).controller = _n_(559432, "controller", lambda: controller)
        _l_(559433)

        _c_(559436, _a_(559435, _n_(559434, "self", lambda: self), "config"), bg = 'grey')
        _l_(559437)

        #Objects on Main Menu
        lblTitle = _c_(559441, _a_(559439, _n_(559438, "tk", lambda: tk), "Label"), _n_(559440, "self", lambda: self),
                            text = "The Fire of Stromwarld",
                            font = ('Arial', 28, 'bold'),
                            fg = 'brown',
                            bg = 'grey',
                            justify = 'center')
        _l_(559442)

        btnStart = _c_(559449, _a_(559444, _n_(559443, "tk", lambda: tk), "Button"), _n_(559445, "self", lambda: self),
                             text = "Start Game",
                             font = ('Arial',16),
                             bg = 'grey',
                             relief = 'flat',
                             command = lambda: _c_(559448, _a_(559447, _n_(559446, "controller", lambda: controller), "ShowFrame"), 1))
        _l_(559450)

        btnExit = _c_(559456, _a_(559452, _n_(559451, "tk", lambda: tk), "Button"), _n_(559453, "self", lambda: self),
                            text = "Exit",
                            font = ('Arial',16),
                            bg = 'grey',
                            relief = 'flat',
                            width = 9,
                            command = _a_(559455, _n_(559454, "self", lambda: self), "quit"))
        _l_(559457)

        #Positioning of Main Window Objects
        _c_(559460, _a_(559459, _n_(559458, "lblTitle", lambda: lblTitle), "grid"), row = 0, column = 0, padx = 178, pady = 75)
        _l_(559461)
        _c_(559464, _a_(559463, _n_(559462, "btnStart", lambda: btnStart), "grid"), row = 1, column = 0, pady = (50,20))
        _l_(559465)
        _c_(559468, _a_(559467, _n_(559466, "btnExit", lambda: btnExit), "grid"), row = 2, column = 0)
        _l_(559469)


#GameMenu
class GameMenu(_a_(559473, _n_(559472, "tk", lambda: tk), "Frame")):
    _l_(559824)

    def __init__(self, parent, controller):
        _l_(559823)

        _c_(559479, _a_(559476, _a_(559475, _n_(559474, "tk", lambda: tk), "Frame"), "__init__"), _n_(559477, "self", lambda: self), _n_(559478, "parent", lambda: parent))
        _l_(559480)

        _n_(559481, "self", lambda: self).controller = _n_(559482, "controller", lambda: controller)
        _l_(559483)

        _c_(559486, _a_(559485, _n_(559484, "self", lambda: self), "config"), bg = 'grey')
        _l_(559487)

        #Creating Menu Base
        _c_(559490, _a_(559489, _n_(559488, "controller", lambda: controller), "CreateMenu"))
        _l_(559491)

        #Objects on Game Menu
        #Player and Monster Stat boxes
        frmPlayerStats = _c_(559495, _a_(559493, _n_(559492, "tk", lambda: tk), "Frame"), _n_(559494, "self", lambda: self),
                                  width = 180,
                                  height = 150,
                                  borderwidth = 2,
                                  relief = 'ridge')
        _l_(559496)
        _c_(559499, _a_(559498, _n_(559497, "frmPlayerStats", lambda: frmPlayerStats), "grid_propagate"), 0)
        _l_(559500)

        frmMonStats = _c_(559504, _a_(559502, _n_(559501, "tk", lambda: tk), "Frame"), _n_(559503, "self", lambda: self),
                            width = 180,
                            height = 80,
                            borderwidth = 2,
                            relief = 'groove')
        _l_(559505)
        _c_(559508, _a_(559507, _n_(559506, "frmMonStats", lambda: frmMonStats), "grid_propagate"), 0)
        _l_(559509)

        #Player Stats
        lblPlayerName = _c_(559513, _a_(559511, _n_(559510, "tk", lambda: tk), "Label"), _n_(559512, "frmPlayerStats", lambda: frmPlayerStats),
                                 text = "Player:",
                                 font = ('arial', 13))
        _l_(559514)

        lblPlayerLevel = _c_(559518, _a_(559516, _n_(559515, "tk", lambda: tk), "Label"), _n_(559517, "frmPlayerStats", lambda: frmPlayerStats),
                                  text = "Lvl: 1",
                                  font = ('arial', 10))
        _l_(559519)

        lblPlayerHPTitle = _c_(559523, _a_(559521, _n_(559520, "tk", lambda: tk), "Label"), _n_(559522, "frmPlayerStats", lambda: frmPlayerStats),
                                    text = "HP: ",
                                    font = ('arial', 10))
        _l_(559524)

        lblPlayerHPStats = _c_(559528, _a_(559526, _n_(559525, "tk", lambda: tk), "Label"), _n_(559527, "frmPlayerStats", lambda: frmPlayerStats),
                                    text = "10 / 10",
                                    font = ('arial', 10),
                                    fg = 'green')
        _l_(559529)

        lblPlayerMPTitle = _c_(559533, _a_(559531, _n_(559530, "tk", lambda: tk), "Label"), _n_(559532, "frmPlayerStats", lambda: frmPlayerStats),
                                    text = "MP: ",
                                    font = ('arial', 10))
        _l_(559534)

        lblPlayerMPStats = _c_(559538, _a_(559536, _n_(559535, "tk", lambda: tk), "Label"), _n_(559537, "frmPlayerStats", lambda: frmPlayerStats),
                                    text = "5 / 5",
                                    font = ('arial', 10),
                                    fg = 'blue')
        _l_(559539)

        lblPlayerBaseAttkTitle = _c_(559543, _a_(559541, _n_(559540, "tk", lambda: tk), "Label"), _n_(559542, "frmPlayerStats", lambda: frmPlayerStats),
                                          text = "Attack: ",
                                          font = ('arial', 10))
        _l_(559544)

        lblPlayerBaseAttkStats = _c_(559548, _a_(559546, _n_(559545, "tk", lambda: tk), "Label"), _n_(559547, "frmPlayerStats", lambda: frmPlayerStats),
                                          text = "5",
                                          font = ('arial', 10),
                                          fg = 'red')
        _l_(559549)

        lblPlayerWeapTitle = _c_(559553, _a_(559551, _n_(559550, "tk", lambda: tk), "Label"), _n_(559552, "frmPlayerStats", lambda: frmPlayerStats),
                                      text = "Weapon: ",
                                      font = ('arial', 10))
        _l_(559554)

        lblPlayerWeapStats = _c_(559558, _a_(559556, _n_(559555, "tk", lambda: tk), "Label"), _n_(559557, "frmPlayerStats", lambda: frmPlayerStats),
                                      text = "None | +2",
                                      font = ('arial', 10))
        _l_(559559)

        lblPlayerArmTitle = _c_(559563, _a_(559561, _n_(559560, "tk", lambda: tk), "Label"), _n_(559562, "frmPlayerStats", lambda: frmPlayerStats),
                                     text = "Armour: ",
                                     font = ('arial', 10))
        _l_(559564)

        lblPlayerArmStats = _c_(559568, _a_(559566, _n_(559565, "tk", lambda: tk), "Label"), _n_(559567, "frmPlayerStats", lambda: frmPlayerStats),
                                     text = "5",
                                     font = ('arial', 10))
        _l_(559569)

        #Monster Stats
        lblMonName = _c_(559573, _a_(559571, _n_(559570, "tk", lambda: tk), "Label"), _n_(559572, "frmMonStats", lambda: frmMonStats),
                              text = "Monster:",
                              font = ('arial', 11))
        _l_(559574)

        lblMonHPTitle = _c_(559578, _a_(559576, _n_(559575, "tk", lambda: tk), "Label"), _n_(559577, "frmMonStats", lambda: frmMonStats),
                                 text = "HP: ",
                                 font = ('arial', 9))
        _l_(559579)

        lblMonHPStats = _c_(559583, _a_(559581, _n_(559580, "tk", lambda: tk), "Label"), _n_(559582, "frmMonStats", lambda: frmMonStats),
                                 text = "10 / 10",
                                 font = ('arial', 9),
                                 fg = 'green')
        _l_(559584)

        lblMonMPTitle = _c_(559588, _a_(559586, _n_(559585, "tk", lambda: tk), "Label"), _n_(559587, "frmMonStats", lambda: frmMonStats),
                                 text = "MP: ",
                                 font = ('arial', 9))
        _l_(559589)

        lblMonMPStats = _c_(559593, _a_(559591, _n_(559590, "tk", lambda: tk), "Label"), _n_(559592, "frmMonStats", lambda: frmMonStats),
                                 text = "5 / 5",
                                 font = ('arial', 9),
                                 fg = 'blue')
        _l_(559594)

        #Main Objects
        #Text display
        txtMain = _c_(559598, _a_(559596, _n_(559595, "tk", lambda: tk), "Text"), _n_(559597, "self", lambda: self),
                          width = 78,
                          height = 22,
                          borderwidth = 1,
                          relief = 'solid',
                          wrap = 'word',
                          cursor = 'left_ptr')
        _l_(559599)
        _c_(559602, _a_(559601, _n_(559600, "txtMain", lambda: txtMain), "grid_propagate"), 0)
        _l_(559603)

        scrlTxtMain = _c_(559607, _a_(559605, _n_(559604, "tk", lambda: tk), "Scrollbar"), _n_(559606, "self", lambda: self))
        _l_(559608)
        _c_(559613, _a_(559610, _n_(559609, "txtMain", lambda: txtMain), "configure"), yscrollcommand = _a_(559612, _n_(559611, "scrlTxtMain", lambda: scrlTxtMain), "set"))
        _l_(559614)
        _c_(559619, _a_(559616, _n_(559615, "scrlTxtMain", lambda: scrlTxtMain), "configure"), command = _a_(559618, _n_(559617, "txtMain", lambda: txtMain), "yview"))
        _l_(559620)

        #User input
        lblentUserInput = _c_(559624, _a_(559622, _n_(559621, "tk", lambda: tk), "Label"), _n_(559623, "self", lambda: self),
                                   text = '>>>',
                                   font = ('arial', 9),
                                   bg = 'white')
        _l_(559625)

        entUserInput = _c_(559629, _a_(559627, _n_(559626, "tk", lambda: tk), "Entry"), _n_(559628, "self", lambda: self),
                                font = ('arial', 9),
                                relief = 'sunken',
                                justify = 'left',
                                width = 69,
                                borderwidth = 2)
        _l_(559630)

        btnUserInput = _c_(559634, _a_(559632, _n_(559631, "tk", lambda: tk), "Button"), _n_(559633, "self", lambda: self),
                                 text = "Enter",
                                 font = ('arial', 7),
                                 relief = 'groove',
                                 width = 7)
        _l_(559635)

        #Action Buttons
        btnAction1 = _c_(559639, _a_(559637, _n_(559636, "tk", lambda: tk), "Button"), _n_(559638, "self", lambda: self),
                               text = "Attack",
                               font = ('arial', 10),
                               relief = 'raised',
                               cursor = 'X_cursor',
                               width = 10,
                               height = 2)
        _l_(559640)
        _c_(559643, _a_(559642, _n_(559641, "btnAction1", lambda: btnAction1), "grid_propagate"), 0)
        _l_(559644)

        btnAction2 = _c_(559648, _a_(559646, _n_(559645, "tk", lambda: tk), "Button"), _n_(559647, "self", lambda: self),
                               text = "Special",
                               font = ('arial', 10),
                               relief = 'raised',
                               cursor = 'cross_reverse',
                               width = 10,
                               height = 2,)
        _l_(559649)
        _c_(559652, _a_(559651, _n_(559650, "btnAction2", lambda: btnAction2), "grid_propagate"), 0)
        _l_(559653)

        btnAction3 = _c_(559657, _a_(559655, _n_(559654, "tk", lambda: tk), "Button"), _n_(559656, "self", lambda: self),
                               text = "Heal",
                               font = ('arial', 10),
                               relief = 'raised',
                               cursor = 'heart',
                               width = 10,
                               height = 2)
        _l_(559658)
        _c_(559661, _a_(559660, _n_(559659, "btnAction3", lambda: btnAction3), "grid_propagate"), 0)
        _l_(559662)

        btnAction4 = _c_(559666, _a_(559664, _n_(559663, "tk", lambda: tk), "Button"), _n_(559665, "self", lambda: self),
                               text = "Run",
                               font = ('arial', 10),
                               relief = 'raised',
                               cursor = 'right_side',
                               width = 10,
                               height = 2)
        _l_(559667)
        _c_(559670, _a_(559669, _n_(559668, "btnAction4", lambda: btnAction4), "grid_propagate"), 0)
        _l_(559671)

        #Inventory
        lblInventoryTitle = _c_(559675, _a_(559673, _n_(559672, "tk", lambda: tk), "Label"), _n_(559674, "self", lambda: self),
                                     text = 'Inventory:' + ' ' * 27,
                                     font = ('arial',11, 'italic'),
                                     bg = 'white')
        _l_(559676)

        lstbInventory = _c_(559680, _a_(559678, _n_(559677, "tk", lambda: tk), "Listbox"), _n_(559679, "self", lambda: self),
                                   font = ('arial', 9),
                                   width = 23,
                                   height = 11,
                                   cursor = 'hand2')
        _l_(559681)

        scrllstbInventory = _c_(559685, _a_(559683, _n_(559682, "tk", lambda: tk), "Scrollbar"), _n_(559684, "self", lambda: self))
        _l_(559686)
        _c_(559691, _a_(559688, _n_(559687, "lstbInventory", lambda: lstbInventory), "configure"), yscrollcommand = _a_(559690, _n_(559689, "scrllstbInventory", lambda: scrllstbInventory), "set"))
        _l_(559692)
        _c_(559697, _a_(559694, _n_(559693, "scrllstbInventory", lambda: scrllstbInventory), "configure"), command = _a_(559696, _n_(559695, "lstbInventory", lambda: lstbInventory), "yview"))
        _l_(559698)

        #Positioning of Game Objects
        #Main object placements
        _c_(559701, _a_(559700, _n_(559699, "txtMain", lambda: txtMain), "grid"), row = 0, column = 0, rowspan = 30, columnspan = 10)
        _l_(559702)
        _c_(559705, _a_(559704, _n_(559703, "scrlTxtMain", lambda: scrlTxtMain), "grid"), row = 0, column = 10, rowspan = 30, padx = (0, 1), sticky = 'nsw')
        _l_(559706)

        #Entry line placement
        _c_(559709, _a_(559708, _n_(559707, "lblentUserInput", lambda: lblentUserInput), "grid"), row = 31, column = 0, columnspan = 2)
        _l_(559710)
        _c_(559713, _a_(559712, _n_(559711, "entUserInput", lambda: entUserInput), "grid"), row = 31, column = 2, columnspan = 6, sticky = 'w')
        _l_(559714)
        _c_(559717, _a_(559716, _n_(559715, "btnUserInput", lambda: btnUserInput), "grid"), row = 31, column = 7, columnspan = 4, sticky = 'w')
        _l_(559718)

        #Action buttons placements
        _c_(559721, _a_(559720, _n_(559719, "btnAction1", lambda: btnAction1), "grid"), row = 32, column = 3, padx = 15, pady = 20)
        _l_(559722)
        _c_(559725, _a_(559724, _n_(559723, "btnAction2", lambda: btnAction2), "grid"), row = 32, column = 4, padx = 15, pady = 20)
        _l_(559726)
        _c_(559729, _a_(559728, _n_(559727, "btnAction3", lambda: btnAction3), "grid"), row = 32, column = 5, padx = 15, pady = 20)
        _l_(559730)
        _c_(559733, _a_(559732, _n_(559731, "btnAction4", lambda: btnAction4), "grid"), row = 32, column = 6, padx = 15, pady = 20)
        _l_(559734)

        #Stats objects placenments
        _c_(559737, _a_(559736, _n_(559735, "frmPlayerStats", lambda: frmPlayerStats), "grid"), row = 0, column = 11, columnspan = 2, padx = 3)
        _l_(559738)
        _c_(559741, _a_(559740, _n_(559739, "lblPlayerName", lambda: lblPlayerName), "grid"), row = 0, column = 0, sticky = 'w')
        _l_(559742)
        _c_(559745, _a_(559744, _n_(559743, "lblPlayerLevel", lambda: lblPlayerLevel), "grid"), row = 0, column = 1, sticky = 'w')
        _l_(559746)
        _c_(559749, _a_(559748, _n_(559747, "lblPlayerHPTitle", lambda: lblPlayerHPTitle), "grid"), row = 1, column = 0, sticky = 'w')
        _l_(559750)
        _c_(559753, _a_(559752, _n_(559751, "lblPlayerHPStats", lambda: lblPlayerHPStats), "grid"), row = 1, column = 1, sticky = 'w')
        _l_(559754)
        _c_(559757, _a_(559756, _n_(559755, "lblPlayerMPTitle", lambda: lblPlayerMPTitle), "grid"), row = 2, column = 0, sticky = 'w')
        _l_(559758)
        _c_(559761, _a_(559760, _n_(559759, "lblPlayerMPStats", lambda: lblPlayerMPStats), "grid"), row = 2, column = 1, sticky = 'w')
        _l_(559762)
        _c_(559765, _a_(559764, _n_(559763, "lblPlayerBaseAttkTitle", lambda: lblPlayerBaseAttkTitle), "grid"), row = 3, column = 0, sticky = 'w')
        _l_(559766)
        _c_(559769, _a_(559768, _n_(559767, "lblPlayerBaseAttkStats", lambda: lblPlayerBaseAttkStats), "grid"), row = 3, column = 1, sticky = 'w')
        _l_(559770)
        _c_(559773, _a_(559772, _n_(559771, "lblPlayerWeapTitle", lambda: lblPlayerWeapTitle), "grid"), row = 4, column = 0, sticky = 'w')
        _l_(559774)
        _c_(559777, _a_(559776, _n_(559775, "lblPlayerWeapStats", lambda: lblPlayerWeapStats), "grid"), row = 4, column = 1, sticky = 'w')
        _l_(559778)
        _c_(559781, _a_(559780, _n_(559779, "lblPlayerArmTitle", lambda: lblPlayerArmTitle), "grid"), row = 5, column = 0, sticky = 'w')
        _l_(559782)
        _c_(559785, _a_(559784, _n_(559783, "lblPlayerArmStats", lambda: lblPlayerArmStats), "grid"), row = 5, column = 1, sticky = 'w')
        _l_(559786)

        _c_(559789, _a_(559788, _n_(559787, "frmMonStats", lambda: frmMonStats), "grid"), row = 1, column = 11, columnspan = 2, padx = 3, pady = 4)
        _l_(559790)
        _c_(559793, _a_(559792, _n_(559791, "lblMonName", lambda: lblMonName), "grid"), row = 0, column = 0, sticky = 'w')
        _l_(559794)
        _c_(559797, _a_(559796, _n_(559795, "lblMonHPTitle", lambda: lblMonHPTitle), "grid"), row = 1, column = 0, sticky = 'w')
        _l_(559798)
        _c_(559801, _a_(559800, _n_(559799, "lblMonHPStats", lambda: lblMonHPStats), "grid"), row = 1, column = 1, sticky = 'w')
        _l_(559802)
        _c_(559805, _a_(559804, _n_(559803, "lblMonMPTitle", lambda: lblMonMPTitle), "grid"), row = 2, column = 0, sticky = 'w')
        _l_(559806)
        _c_(559809, _a_(559808, _n_(559807, "lblMonMPStats", lambda: lblMonMPStats), "grid"), row = 2, column = 1, sticky = 'w')
        _l_(559810)

        #Inventory object placements
        _c_(559813, _a_(559812, _n_(559811, "lblInventoryTitle", lambda: lblInventoryTitle), "grid"), row = 2, column = 11, columnspan = 2, padx = 3, pady = (4,0), sticky = 'w')
        _l_(559814)
        _c_(559817, _a_(559816, _n_(559815, "lstbInventory", lambda: lstbInventory), "grid"), row = 3, column = 11, rowspan = 32, padx = (3,0), sticky = 'w')
        _l_(559818)
        _c_(559821, _a_(559820, _n_(559819, "scrllstbInventory", lambda: scrllstbInventory), "grid"), row = 3, column = 12, rowspan = 32, sticky = 'nsw')
        _l_(559822)


#Runnning Program -------------------------------------------------------
#------------------------------------------------------------------------
game = _c_(559826, _n_(559825, "FireofStromwarld", lambda: FireofStromwarld))
_l_(559827)
_c_(559830, _a_(559829, _n_(559828, "game", lambda: game), "mainloop"))
_l_(559831)