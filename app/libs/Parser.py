import abc
import re
import pandas as pd 

class Parser(abc.ABC):
  @abc.abstractmethod
  def parse(self):
    pass

class TextParser(Parser):
  def parse(self, dataframe):
    dataframe =  dataframe.iloc[:,0]
    dataframe = dataframe.apply(lambda x : re.sub('[\\\\n]+', '', x))
    dataframe = dataframe.str.split('&', 1, expand=True)
    dataframe = dataframe.rename(columns={0:'eng', 1:'ita'})
    dataframe['eng'] = dataframe.eng.apply(lambda x : x.strip())
    dataframe['ita'] = dataframe.ita.apply(lambda x : x.strip())
    return dataframe