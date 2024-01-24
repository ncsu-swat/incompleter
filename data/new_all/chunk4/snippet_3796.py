# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67832031/typeerror-int-argument-must-be-a-string-a-bytes-like-object-or-a-number-not
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def ANN(optimizer = "adam", neurons = 32, batch_size = 32, epochs = 50, activation = "relu", patience =5, loss = 'mse'):
  _l_(586521)


  model = _c_(586475, _n_(586474, "Sequential", lambda: Sequential))
  _l_(586476)
  _c_(586484, _a_(586478, _n_(586477, "model", lambda: model), "add"), _c_(586483, _n_(586479, "Dense", lambda: Dense), _n_(586480, "neurons", lambda: neurons), input_dim=_n_(586481, "look_back", lambda: look_back), activation= _n_(586482, "activation", lambda: activation)))
  _l_(586485)
  _c_(586492, _a_(586487, _n_(586486, "model", lambda: model), "add"), _c_(586491, _n_(586488, "Dense", lambda: Dense), _n_(586489, "neurons", lambda: neurons), activation= _n_(586490, "activation", lambda: activation)))
  _l_(586493)
  _c_(586498, _a_(586495, _n_(586494, "model", lambda: model), "add"), _c_(586497, _n_(586496, "Dense", lambda: Dense), 1))
  _l_(586499)
  _c_(586504, _a_(586501, _n_(586500, "model", lambda: model), "compile"), optimizer = _n_(586502, "optimizer", lambda: optimizer), loss = _n_(586503, "loss", lambda: loss))
  _l_(586505)
  early_stopping = _c_(586508, _n_(586506, "EarlyStopping", lambda: EarlyStopping), monitor = "loss", patience = _n_(586507, "patience", lambda: patience))
  _l_(586509)
  history = _c_(586517, _a_(586511, _n_(586510, "model", lambda: model), "fit"), _n_(586512, "x_train", lambda: x_train), _n_(586513, "y_train", lambda: y_train), batch_size = _n_(586514, "batch_size", lambda: batch_size), epochs = _n_(586515, "epochs", lambda: epochs), callbacks = [_n_(586516, "early_stopping", lambda: early_stopping)], verbose = 0)
  _l_(586518)
  aux = _n_(586519, "model", lambda: model)
  _l_(586520)
  return aux

boundaries = [(0,2), (0,2), (0,2), (0,2), (10,100), (20,50), (3,20)]
_l_(586522)
def performance(x_train, y_train, x_test, y_test, optimizer = None, activation = None, loss = None, batch_size = None, neurons = None, epochs = None, patience=None):
  _l_(586588)


  model = _c_(586531, _n_(586523, "ANN", lambda: ANN), optimizer=_n_(586524, "optimizer", lambda: optimizer), activation= _n_(586525, "activation", lambda: activation), loss=_n_(586526, "loss", lambda: loss), batch_size=_n_(586527, "batch_size", lambda: batch_size), neurons= _n_(586528, "neurons", lambda: neurons), epochs = _n_(586529, "epochs", lambda: epochs), patience=_n_(586530, "patience", lambda: patience))
  _l_(586532)

  trainScore = _c_(586537, _a_(586534, _n_(586533, "model", lambda: model), "evaluate"), _n_(586535, "x_train", lambda: x_train), _n_(586536, "y_train", lambda: y_train), verbose=0)
  _l_(586538)
  _c_(586545, _n_(586539, "print", lambda: print), 'Train Score: %.2f MSE (%.2f RMSE)' % (_n_(586540, "trainScore", lambda: trainScore), _c_(586544, _a_(586542, _n_(586541, "math", lambda: math), "sqrt"), _n_(586543, "trainScore", lambda: trainScore))))
  _l_(586546)
  testScore = _c_(586551, _a_(586548, _n_(586547, "model", lambda: model), "evaluate"), _n_(586549, "x_test", lambda: x_test), _n_(586550, "y_test", lambda: y_test), verbose=0)
  _l_(586552)
  _c_(586559, _n_(586553, "print", lambda: print), 'Test Score: %.2f MSE (%.2f RMSE)' % (_n_(586554, "testScore", lambda: testScore), _c_(586558, _a_(586556, _n_(586555, "math", lambda: math), "sqrt"), _n_(586557, "testScore", lambda: testScore))))
  _l_(586560)
  trainPredict = _c_(586564, _a_(586562, _n_(586561, "model", lambda: model), "predict"), _n_(586563, "x_train", lambda: x_train))
  _l_(586565)
  testPredict = _c_(586569, _a_(586567, _n_(586566, "model", lambda: model), "predict"), _n_(586568, "x_test", lambda: x_test))
  _l_(586570)
  #calculate mean absolute percent error
  trainMAPE = _c_(586574, _n_(586571, "mean_absolute_error", lambda: mean_absolute_error), _n_(586572, "y_train", lambda: y_train), _n_(586573, "trainPredict", lambda: trainPredict))
  _l_(586575)
  testMAPE = _c_(586579, _n_(586576, "mean_absolute_error", lambda: mean_absolute_error), _n_(586577, "y_test", lambda: y_test), _n_(586578, "testPredict", lambda: testPredict))
  _l_(586580)
  aux = _c_(586583, _n_(586581, "print", lambda: print), 'testMAPE: %.2f MAPE' % _n_(586582, "trainMAPE", lambda: trainMAPE)), _c_(586586, _n_(586584, "print", lambda: print), 'testMAPE: %.2f MAPE' % _n_(586585, "testMAPE", lambda: testMAPE))
  _l_(586587)
    
  return aux
writer = _c_(586591, _a_(586590, _n_(586589, "pd", lambda: pd), "ExcelWriter"), '/content/Scores.xlsx')
_l_(586592)
for sheetNum in _c_(586594, _n_(586593, "range", lambda: range), 1,5):
  _l_(586670)

  dataframe = _c_(586600, _a_(586596, _n_(586595, "pd", lambda: pd), "read_excel"), 'Fri.xlsx',sheet_name='Sheet'+_c_(586599, _n_(586597, "str", lambda: str), _n_(586598, "sheetNum", lambda: sheetNum)))
  _l_(586601)
  
  # load the dataset
  dataset = _a_(586603, _n_(586602, "dataframe", lambda: dataframe), "values")
  _l_(586604)
  dataset = _c_(586607, _a_(586606, _n_(586605, "dataset", lambda: dataset), "astype"), 'float32')
  _l_(586608)
  
  
  train_size = _c_(586613, _n_(586609, "int", lambda: int), _c_(586612, _n_(586610, "len", lambda: len), _n_(586611, "dataset", lambda: dataset)) * 0.48)
  _l_(586614)
  test_size = _c_(586617, _n_(586615, "len", lambda: len), _n_(586616, "dataset", lambda: dataset)) - _n_(586618, "train_size", lambda: train_size)
  _l_(586619)
  train, test = _n_(586620, "dataset", lambda: dataset)[0:_n_(586621, "train_size", lambda: train_size), :], _n_(586622, "dataset", lambda: dataset)[_n_(586623, "train_size", lambda: train_size):_c_(586626, _n_(586624, "len", lambda: len), _n_(586625, "dataset", lambda: dataset)), :]
  _l_(586627)
  
  # reshape into X=t and Y=t+1
  look_back = 10
  _l_(586628)
  x_train, y_train = _c_(586632, _n_(586629, "create_dataset", lambda: create_dataset), _n_(586630, "train", lambda: train), _n_(586631, "look_back", lambda: look_back))
  _l_(586633)
  x_test, y_test = _c_(586637, _n_(586634, "create_dataset", lambda: create_dataset), _n_(586635, "test", lambda: test), _n_(586636, "look_back", lambda: look_back))
  _l_(586638)
  
  
  
  # normalize the dataset
  scaler = _c_(586640, _n_(586639, "MinMaxScaler", lambda: MinMaxScaler), feature_range=(0, 1))
  _l_(586641)
  x_train = _c_(586645, _a_(586643, _n_(586642, "scaler", lambda: scaler), "fit_transform"), _n_(586644, "x_train", lambda: x_train))
  _l_(586646)
  x_test = _c_(586650, _a_(586648, _n_(586647, "scaler", lambda: scaler), "fit_transform"), _n_(586649, "x_test", lambda: x_test))
  _l_(586651)
  abc_obj = _c_(586660, _n_(586652, "abc", lambda: abc), _c_(586658, _n_(586653, "performance", lambda: performance), _n_(586654, "x_train", lambda: x_train), _n_(586655, "y_train", lambda: y_train), _n_(586656, "x_test", lambda: x_test), _n_(586657, "y_test", lambda: y_test)), _n_(586659, "boundaries", lambda: boundaries))
  _l_(586661)
  _c_(586664, _a_(586663, _n_(586662, "abc_obj", lambda: abc_obj), "fit"))
  _l_(586665)

  #Get solution obtained after fit() execution:
  solution = _c_(586668, _a_(586667, _n_(586666, "abc_obj", lambda: abc_obj), "get_solution"))
  _l_(586669)