# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64863278/what-is-the-solution-to-this-type-error-list-indices-must-be-integers-or-slices
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def run2(score,run):
  _l_(382291)

  global appleX,appleY,snakeCoords
  _l_(382002)
  startX=_c_(382006, _a_(382004, _n_(382003, "random", lambda: random), "randint"), 20,_n_(382005, "cellWidth", lambda: cellWidth))
  _l_(382007)
  startY=_c_(382011, _a_(382009, _n_(382008, "random", lambda: random), "randint"), 20,_n_(382010, "cellHeight", lambda: cellHeight))
  _l_(382012)
  apple=_c_(382014, _n_(382013, "randomlocation", lambda: randomlocation))
  _l_(382015)
  appleX=_n_(382016, "apple", lambda: apple)['x']*_n_(382017, "cell_s", lambda: cell_s)
  _l_(382018)
  appleY=_n_(382019, "apple", lambda: apple)['y']*_n_(382020, "cell_s", lambda: cell_s)
  _l_(382021)
  snakeCoords=[{"x":_n_(382022, "startX", lambda: startX),"y":_n_(382023, "startY", lambda: startY)},
               {"x":_n_(382024, "startX", lambda: startX)-1,"y":_n_(382025, "startY", lambda: startY)},
               {"x":_n_(382026, "startX", lambda: startX)-2,"y":_n_(382027, "startY", lambda: startY)}]
  _l_(382028)
  direction=_n_(382029, "RIGHT", lambda: RIGHT)
  _l_(382030)
  assert _n_(382031, "win_w", lambda: win_w) % _n_(382032, "cell_s", lambda: cell_s)==0
  _l_(382033)
  assert _n_(382034, "win_h", lambda: win_h) % _n_(382035, "cell_s", lambda: cell_s)==0
  _l_(382036)
  
  
  while _n_(382037, "run", lambda: run):
    _l_(382290)

    
    if _n_(382038, "snakeCoords", lambda: snakeCoords)[_n_(382039, "head", lambda: head)]['x']==19 or _n_(382040, "snakeCoords", lambda: snakeCoords)[_n_(382041, "head", lambda: head)]['y']==19:
      _l_(382059)

      _c_(382044, _n_(382042, "gameover", lambda: gameover), _n_(382043, "window", lambda: window))
      _l_(382045)
      _c_(382049, _a_(382048, _a_(382047, _n_(382046, "pygame", lambda: pygame), "time"), "wait"), 500)
      _l_(382050)
      run=False
      _l_(382051)
      _c_(382053, _n_(382052, "terminate", lambda: terminate))
      _l_(382054)
      _c_(382057, _a_(382056, _n_(382055, "sys", lambda: sys), "exit"))
      _l_(382058)
    if _n_(382060, "snakeCoords", lambda: snakeCoords)[_n_(382061, "head", lambda: head)]['x']==_n_(382062, "win_w", lambda: win_w)-20 or _n_(382063, "snakeCoords", lambda: snakeCoords)[_n_(382064, "head", lambda: head)]['y']==_n_(382065, "win_h", lambda: win_h)-20:
      _l_(382083)

      _c_(382068, _n_(382066, "gameover", lambda: gameover), _n_(382067, "window", lambda: window))
      _l_(382069)
      _c_(382073, _a_(382072, _a_(382071, _n_(382070, "pygame", lambda: pygame), "time"), "wait"), 500)
      _l_(382074)
      run=False                 
      _l_(382075)                 
      _c_(382077, _n_(382076, "terminate", lambda: terminate))
      _l_(382078)
      _c_(382081, _a_(382080, _n_(382079, "sys", lambda: sys), "exit"))
      _l_(382082)
   
    for body in _n_(382084, "snakeCoords", lambda: snakeCoords)[1:]:
      _l_(382108)

      if _n_(382085, "snakeCoords", lambda: snakeCoords)[_n_(382086, "head", lambda: head)]['x']==_n_(382087, "body", lambda: body)['x'] and _n_(382088, "snakeCoords", lambda: snakeCoords)[_n_(382089, "head", lambda: head)]['y']==_n_(382090, "body", lambda: body)['y']:
        _l_(382107)

        _c_(382093, _n_(382091, "gameover", lambda: gameover), _n_(382092, "window", lambda: window))
        _l_(382094)
        _c_(382098, _a_(382097, _a_(382096, _n_(382095, "pygame", lambda: pygame), "time"), "wait"), 500)
        _l_(382099)
        _c_(382101, _n_(382100, "terminate", lambda: terminate))
        _l_(382102)
        _c_(382105, _a_(382104, _n_(382103, "sys", lambda: sys), "exit"))
        _l_(382106)
 
    if _n_(382109, "direction", lambda: direction)==_n_(382110, "UP", lambda: UP):
      _l_(382116)

      move={'x':_n_(382111, "snakeCoords", lambda: snakeCoords)[_n_(382112, "head", lambda: head)]['x']-1,'y':_n_(382113, "snakeCoords", lambda: snakeCoords)[_n_(382114, "head", lambda: head)]['y']}
      _l_(382115)
    if _n_(382117, "direction", lambda: direction)==_n_(382118, "DOWN", lambda: DOWN):
      _l_(382124)

      move={'x':_n_(382119, "snakeCoords", lambda: snakeCoords)[_n_(382120, "head", lambda: head)]['x']+1,'y':_n_(382121, "snakeCoords", lambda: snakeCoords)[_n_(382122, "head", lambda: head)]['y']}
      _l_(382123)
    if _n_(382125, "direction", lambda: direction)==_n_(382126, "RIGHT", lambda: RIGHT):
      _l_(382132)

      move={'x':_n_(382127, "snakeCoords", lambda: snakeCoords)[_n_(382128, "head", lambda: head)]['x'],'y':_n_(382129, "snakeCoords", lambda: snakeCoords)[_n_(382130, "head", lambda: head)]['y']+1}
      _l_(382131)
    if _n_(382133, "direction", lambda: direction)==_n_(382134, "LEFT", lambda: LEFT):
      _l_(382140)

      move={'x':_n_(382135, "snakeCoords", lambda: snakeCoords)[_n_(382136, "head", lambda: head)]['x'],'y':_n_(382137, "snakeCoords", lambda: snakeCoords)[_n_(382138, "head", lambda: head)]['y']-1}
      _l_(382139)
    _c_(382144, _a_(382142, _n_(382141, "snakeCoords", lambda: snakeCoords), "insert"), 0,_n_(382143, "move", lambda: move))
    _l_(382145)
    
    
   
    if _n_(382146, "apple", lambda: apple)['x']==_n_(382147, "snakeCoords", lambda: snakeCoords)[_n_(382148, "head", lambda: head)]['x'] and _n_(382149, "apple", lambda: apple)['y']==_n_(382150, "snakeCoords", lambda: snakeCoords)[_n_(382151, "head", lambda: head)]['y']:
      _l_(382210)

      apple=_c_(382153, _n_(382152, "randomlocation", lambda: randomlocation))
      _l_(382154)
      _c_(382158, _a_(382156, _n_(382155, "drawgame", lambda: drawgame), "drawapple"), _n_(382157, "red", lambda: red))
      _l_(382159)
      score+=1
      _l_(382160)
      if _n_(382161, "appleX", lambda: appleX)==_n_(382162, "snakeCoords", lambda: snakeCoords)[_n_(382163, "head", lambda: head)]['x'] and _n_(382164, "direction", lambda: direction)==_n_(382165, "RIGHT", lambda: RIGHT):
        _l_(382171)

        newhead=[{'x':_n_(382166, "startX", lambda: startX)-3,'y':_n_(382167, "startY", lambda: startY)}]
        _l_(382168)
        snakeCoords+=_n_(382169, "newhead", lambda: newhead)
        _l_(382170)
      if _n_(382172, "appleX", lambda: appleX)==_n_(382173, "snakeCoords", lambda: snakeCoords)[_n_(382174, "head", lambda: head)]['x'] and _n_(382175, "direction", lambda: direction)==_n_(382176, "LEFT", lambda: LEFT):
        _l_(382182)

        newhead=[{'x':_n_(382177, "startX", lambda: startX)+3,'y':_n_(382178, "startY", lambda: startY)}]
        _l_(382179)
        snakeCoords+=_n_(382180, "newhead", lambda: newhead)
        _l_(382181)
      if _n_(382183, "appleY", lambda: appleY)==_n_(382184, "snakeCoords", lambda: snakeCoords)[_n_(382185, "head", lambda: head)]['y'] and _n_(382186, "direction", lambda: direction)==_n_(382187, "UP", lambda: UP):
        _l_(382193)

        newhead=[{'x':_n_(382188, "startX", lambda: startX),'y':_n_(382189, "startY", lambda: startY)+3}]
        _l_(382190)
        snakeCoords+=_n_(382191, "newhead", lambda: newhead)
        _l_(382192)
      if _n_(382194, "appleY", lambda: appleY)==_n_(382195, "snakeCoords", lambda: snakeCoords)[_n_(382196, "head", lambda: head)]['y'] and _n_(382197, "direction", lambda: direction)==_n_(382198, "DOWN", lambda: DOWN):
        _l_(382204)

        newhead=[{'x':_n_(382199, "startX", lambda: startX),'y':_n_(382200, "startY", lambda: startY)-3}]
        _l_(382201)
        snakeCoords+=_n_(382202, "newhead", lambda: newhead)
        _l_(382203)
      _c_(382208, _a_(382207, _a_(382206, _n_(382205, "pygame", lambda: pygame), "display"), "update"))
      _l_(382209)

    if _n_(382211, "score", lambda: score)==10:
      _l_(382221)

      _c_(382214, _n_(382212, "gameover", lambda: gameover), _n_(382213, "window", lambda: window))
      _l_(382215)
      _c_(382219, _a_(382218, _a_(382217, _n_(382216, "pygame", lambda: pygame), "time"), "wait"), 500)
      _l_(382220)
   
    for event in _c_(382225, _a_(382224, _a_(382223, _n_(382222, "pygame", lambda: pygame), "event"), "get")):
      _l_(382289)

      if _a_(382227, _n_(382226, "event", lambda: event), "type")==_a_(382229, _n_(382228, "pygame", lambda: pygame), "QUIT"):
        _l_(382238)

        run=False
        _l_(382230)
        _c_(382232, _n_(382231, "terminate", lambda: terminate))
        _l_(382233)
        _c_(382236, _a_(382235, _n_(382234, "sys", lambda: sys), "exit"))
        _l_(382237)
      
      if _a_(382240, _n_(382239, "event", lambda: event), "type")==_n_(382241, "KEYDOWN", lambda: KEYDOWN):
        _l_(382288)

        if _a_(382243, _n_(382242, "event", lambda: event), "key")==_n_(382244, "K_RIGHT", lambda: K_RIGHT) and _n_(382245, "direction", lambda: direction)!=_n_(382246, "LEFT", lambda: LEFT):
          _l_(382287)

          direction=_n_(382247, "RIGHT", lambda: RIGHT)
          _l_(382248)
        elif _a_(382250, _n_(382249, "event", lambda: event), "key")==_n_(382251, "K_LEFT", lambda: K_LEFT)  and _n_(382252, "direction", lambda: direction)!=_n_(382253, "RIGHT", lambda: RIGHT):
          _l_(382286)

          direction=_n_(382254, "LEFT", lambda: LEFT)
          _l_(382255)
        elif _a_(382257, _n_(382256, "event", lambda: event), "key")==_n_(382258, "K_UP", lambda: K_UP) and _n_(382259, "direction", lambda: direction)!=_n_(382260, "DOWN", lambda: DOWN):
          _l_(382285)

          direction=_n_(382261, "UP", lambda: UP)
          _l_(382262)
        elif _a_(382264, _n_(382263, "event", lambda: event), "key")==_n_(382265, "K_DOWN", lambda: K_DOWN)  and _n_(382266, "direction", lambda: direction)!=_n_(382267, "UP", lambda: UP):
          _l_(382284)

          direction=_n_(382268, "DOWN", lambda: DOWN)
          _l_(382269)
        elif _a_(382271, _n_(382270, "event", lambda: event), "key")==_n_(382272, "K_ESCAPE", lambda: K_ESCAPE) :
          _l_(382283)

          _c_(382274, _n_(382273, "terminate", lambda: terminate))
          _l_(382275)
          _c_(382278, _a_(382277, _n_(382276, "sys", lambda: sys), "exit"))
          _l_(382279)
        else:
           _c_(382281, _n_(382280, "print", lambda: print), "Invalid Key Pressed")
           _l_(382282)
           
if _n_(382292, "__name__", lambda: __name__)=="__main__":
  _l_(382297)

  _c_(382295, _n_(382293, "main", lambda: main), _n_(382294, "run", lambda: run))
  _l_(382296)