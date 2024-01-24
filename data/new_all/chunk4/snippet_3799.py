# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67832031/typeerror-int-argument-must-be-a-string-a-bytes-like-object-or-a-number-not
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def ANN(optimizer = "adam", neurons = 32, batch_size = 32, epochs = 50, activation = "relu", patience =5, loss = 'mse'):
  _l_(611368)


  model = _c_(611322, _n_(611321, "Sequential", lambda: Sequential))
  _l_(611323)
  _c_(611331, _a_(611325, _n_(611324, "model", lambda: model), "add"), _c_(611330, _n_(611326, "Dense", lambda: Dense), _n_(611327, "neurons", lambda: neurons), input_dim=_n_(611328, "look_back", lambda: look_back), activation= _n_(611329, "activation", lambda: activation)))
  _l_(611332)
  _c_(611339, _a_(611334, _n_(611333, "model", lambda: model), "add"), _c_(611338, _n_(611335, "Dense", lambda: Dense), _n_(611336, "neurons", lambda: neurons), activation= _n_(611337, "activation", lambda: activation)))
  _l_(611340)
  _c_(611345, _a_(611342, _n_(611341, "model", lambda: model), "add"), _c_(611344, _n_(611343, "Dense", lambda: Dense), 1))
  _l_(611346)
  _c_(611351, _a_(611348, _n_(611347, "model", lambda: model), "compile"), optimizer = _n_(611349, "optimizer", lambda: optimizer), loss = _n_(611350, "loss", lambda: loss))
  _l_(611352)
  early_stopping = _c_(611355, _n_(611353, "EarlyStopping", lambda: EarlyStopping), monitor = "loss", patience = _n_(611354, "patience", lambda: patience))
  _l_(611356)
  history = _c_(611364, _a_(611358, _n_(611357, "model", lambda: model), "fit"), _n_(611359, "x_train", lambda: x_train), _n_(611360, "y_train", lambda: y_train), batch_size = _n_(611361, "batch_size", lambda: batch_size), epochs = _n_(611362, "epochs", lambda: epochs), callbacks = [_n_(611363, "early_stopping", lambda: early_stopping)], verbose = 0)
  _l_(611365)
  aux = _n_(611366, "model", lambda: model)
  _l_(611367)
  return aux

boundaries = [(0,2), (0,2), (0,2), (0,2), (10,100), (20,50), (3,20)]
_l_(611369)
def performance(x_train, y_train, x_test, y_test, optimizer = None, activation = None, loss = None, batch_size = None, neurons = None, epochs = None, patience=None):
  _l_(611435)


  model = _c_(611378, _n_(611370, "ANN", lambda: ANN), optimizer=_n_(611371, "optimizer", lambda: optimizer), activation= _n_(611372, "activation", lambda: activation), loss=_n_(611373, "loss", lambda: loss), batch_size=_n_(611374, "batch_size", lambda: batch_size), neurons= _n_(611375, "neurons", lambda: neurons), epochs = _n_(611376, "epochs", lambda: epochs), patience=_n_(611377, "patience", lambda: patience))
  _l_(611379)

  trainScore = _c_(611384, _a_(611381, _n_(611380, "model", lambda: model), "evaluate"), _n_(611382, "x_train", lambda: x_train), _n_(611383, "y_train", lambda: y_train), verbose=0)
  _l_(611385)
  _c_(611392, _n_(611386, "print", lambda: print), 'Train Score: %.2f MSE (%.2f RMSE)' % (_n_(611387, "trainScore", lambda: trainScore), _c_(611391, _a_(611389, _n_(611388, "math", lambda: math), "sqrt"), _n_(611390, "trainScore", lambda: trainScore))))
  _l_(611393)
  testScore = _c_(611398, _a_(611395, _n_(611394, "model", lambda: model), "evaluate"), _n_(611396, "x_test", lambda: x_test), _n_(611397, "y_test", lambda: y_test), verbose=0)
  _l_(611399)
  _c_(611406, _n_(611400, "print", lambda: print), 'Test Score: %.2f MSE (%.2f RMSE)' % (_n_(611401, "testScore", lambda: testScore), _c_(611405, _a_(611403, _n_(611402, "math", lambda: math), "sqrt"), _n_(611404, "testScore", lambda: testScore))))
  _l_(611407)
  trainPredict = _c_(611411, _a_(611409, _n_(611408, "model", lambda: model), "predict"), _n_(611410, "x_train", lambda: x_train))
  _l_(611412)
  testPredict = _c_(611416, _a_(611414, _n_(611413, "model", lambda: model), "predict"), _n_(611415, "x_test", lambda: x_test))
  _l_(611417)
  #calculate mean absolute percent error
  trainMAPE = _c_(611421, _n_(611418, "mean_absolute_error", lambda: mean_absolute_error), _n_(611419, "y_train", lambda: y_train), _n_(611420, "trainPredict", lambda: trainPredict))
  _l_(611422)
  testMAPE = _c_(611426, _n_(611423, "mean_absolute_error", lambda: mean_absolute_error), _n_(611424, "y_test", lambda: y_test), _n_(611425, "testPredict", lambda: testPredict))
  _l_(611427)
  aux = _c_(611430, _n_(611428, "print", lambda: print), 'testMAPE: %.2f MAPE' % _n_(611429, "trainMAPE", lambda: trainMAPE)), _c_(611433, _n_(611431, "print", lambda: print), 'testMAPE: %.2f MAPE' % _n_(611432, "testMAPE", lambda: testMAPE))
  _l_(611434)
    
  return aux
writer = _c_(611438, _a_(611437, _n_(611436, "pd", lambda: pd), "ExcelWriter"), '/content/Scores.xlsx')
_l_(611439)
for sheetNum in _c_(611441, _n_(611440, "range", lambda: range), 1,5):
  _l_(611517)

  dataframe = _c_(611447, _a_(611443, _n_(611442, "pd", lambda: pd), "read_excel"), 'Fri.xlsx',sheet_name='Sheet'+_c_(611446, _n_(611444, "str", lambda: str), _n_(611445, "sheetNum", lambda: sheetNum)))
  _l_(611448)
  
  # load the dataset
  dataset = _a_(611450, _n_(611449, "dataframe", lambda: dataframe), "values")
  _l_(611451)
  dataset = _c_(611454, _a_(611453, _n_(611452, "dataset", lambda: dataset), "astype"), 'float32')
  _l_(611455)
  
  
  train_size = _c_(611460, _n_(611456, "int", lambda: int), _c_(611459, _n_(611457, "len", lambda: len), _n_(611458, "dataset", lambda: dataset)) * 0.48)
  _l_(611461)
  test_size = _c_(611464, _n_(611462, "len", lambda: len), _n_(611463, "dataset", lambda: dataset)) - _n_(611465, "train_size", lambda: train_size)
  _l_(611466)
  train, test = _n_(611467, "dataset", lambda: dataset)[0:_n_(611468, "train_size", lambda: train_size), :], _n_(611469, "dataset", lambda: dataset)[_n_(611470, "train_size", lambda: train_size):_c_(611473, _n_(611471, "len", lambda: len), _n_(611472, "dataset", lambda: dataset)), :]
  _l_(611474)
  
  # reshape into X=t and Y=t+1
  look_back = 10
  _l_(611475)
  x_train, y_train = _c_(611479, _n_(611476, "create_dataset", lambda: create_dataset), _n_(611477, "train", lambda: train), _n_(611478, "look_back", lambda: look_back))
  _l_(611480)
  x_test, y_test = _c_(611484, _n_(611481, "create_dataset", lambda: create_dataset), _n_(611482, "test", lambda: test), _n_(611483, "look_back", lambda: look_back))
  _l_(611485)
  
  
  
  # normalize the dataset
  scaler = _c_(611487, _n_(611486, "MinMaxScaler", lambda: MinMaxScaler), feature_range=(0, 1))
  _l_(611488)
  x_train = _c_(611492, _a_(611490, _n_(611489, "scaler", lambda: scaler), "fit_transform"), _n_(611491, "x_train", lambda: x_train))
  _l_(611493)
  x_test = _c_(611497, _a_(611495, _n_(611494, "scaler", lambda: scaler), "fit_transform"), _n_(611496, "x_test", lambda: x_test))
  _l_(611498)
  abc_obj = _c_(611507, _n_(611499, "abc", lambda: abc), _c_(611505, _n_(611500, "performance", lambda: performance), _n_(611501, "x_train", lambda: x_train), _n_(611502, "y_train", lambda: y_train), _n_(611503, "x_test", lambda: x_test), _n_(611504, "y_test", lambda: y_test)), _n_(611506, "boundaries", lambda: boundaries))
  _l_(611508)
  _c_(611511, _a_(611510, _n_(611509, "abc_obj", lambda: abc_obj), "fit"))
  _l_(611512)

  #Get solution obtained after fit() execution:
  solution = _c_(611515, _a_(611514, _n_(611513, "abc_obj", lambda: abc_obj), "get_solution"))
  _l_(611516)