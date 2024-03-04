#Source: https://stackoverflow.com/questions/61591232/typeerror-unorderable-types-str-float
import numpy as np 
import pandas as pd 
import re  
import nltk 
nltk.download('stopwords')  
from nltk.corpus import stopwords 
tweets = pd.read_csv("C:\\Users\\data.csv")
tweets.shape