#Source: https://stackoverflow.com/questions/67832031/typeerror-int-argument-must-be-a-string-a-bytes-like-object-or-a-number-not
def ANN(optimizer = "adam", neurons = 32, batch_size = 32, epochs = 50, activation = "relu", patience =5, loss = 'mse'):

  model = Sequential()
  model.add(Dense(neurons, input_dim=look_back, activation= activation))
  model.add(Dense(neurons, activation= activation))
  model.add(Dense(1))
  model.compile(optimizer = optimizer, loss = loss)
  early_stopping = EarlyStopping(monitor = "loss", patience = patience)
  history = model.fit(x_train, y_train, batch_size = batch_size, epochs = epochs, callbacks = [early_stopping], verbose = 0)
  return model

boundaries = [(0,2), (0,2), (0,2), (0,2), (10,100), (20,50), (3,20)]
def performance(x_train, y_train, x_test, y_test, optimizer = None, activation = None, loss = None, batch_size = None, neurons = None, epochs = None, patience=None):

  model = ANN(optimizer=optimizer, activation= activation, loss=loss, batch_size=batch_size, neurons= neurons, epochs = epochs, patience=patience)

  trainScore = model.evaluate(x_train, y_train, verbose=0)
  print('Train Score: %.2f MSE (%.2f RMSE)' % (trainScore, math.sqrt(trainScore)))
  testScore = model.evaluate(x_test, y_test, verbose=0)
  print('Test Score: %.2f MSE (%.2f RMSE)' % (testScore, math.sqrt(testScore)))
  trainPredict = model.predict(x_train)
  testPredict = model.predict(x_test)
  #calculate mean absolute percent error
  trainMAPE = mean_absolute_error(y_train, trainPredict)
  testMAPE = mean_absolute_error(y_test, testPredict)
    
  return print('testMAPE: %.2f MAPE' % trainMAPE), print('testMAPE: %.2f MAPE' % testMAPE)
writer = pd.ExcelWriter('/content/Scores.xlsx')
for sheetNum in range(1,5):
    dataframe = pd.read_excel('Fri.xlsx',sheet_name='Sheet'+str(sheetNum))
    
    # load the dataset
    dataset = dataframe.values
    dataset = dataset.astype('float32')
    
    
    train_size = int(len(dataset) * 0.48)
    test_size = len(dataset) - train_size
    train, test = dataset[0:train_size, :], dataset[train_size:len(dataset), :]
    
    # reshape into X=t and Y=t+1
    look_back = 10
    x_train, y_train = create_dataset(train, look_back)
    x_test, y_test = create_dataset(test, look_back)
    
  
    
    # normalize the dataset
    scaler = MinMaxScaler(feature_range=(0, 1))
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.fit_transform(x_test)
    abc_obj = abc(performance(x_train, y_train, x_test, y_test), boundaries)
    abc_obj.fit()

    #Get solution obtained after fit() execution:
    solution = abc_obj.get_solution()