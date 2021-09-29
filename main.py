import abc
import re 
import pandas as pd 
  
# custom packages 
from libs.Loader import DataLoader
from libs.Parser import TextParser

# INIT
loader = DataLoader()
parser = TextParser()

# GET DATA 
dataframe = loader.get()

# PARSE DATA 
dataframe = parser.parse(dataframe)

a = input('word : ')
print(dataframe[dataframe.eng==a.upper().strip()])
