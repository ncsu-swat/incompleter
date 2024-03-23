#Source: https://stackoverflow.com/questions/21764770/typeerror-got-multiple-values-for-argument
BOX_LENGTH = 100
turtle.speed(0)
fill = 0
for i in range(8):
    fill += 1
    if fill % 2 == 0:
        Horizontol_drawbox(BOX_LENGTH, fillBox = False)
    else:
        Horizontol_drawbox(BOX_LENGTH, fillBox = True)

    for i in range(8):
        fill += 1
        if fill % 2 == 0:
            Vertical_drawbox(BOX_LENGTH,fillBox = False)
        else:
            Vertical_drawbox(BOX_LENGTH,fillBox = True)