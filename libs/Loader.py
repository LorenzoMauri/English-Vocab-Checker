import abc
import pandas as pd 
  
class Loader(abc.ABC):
  @abc.abstractmethod
  def get(self):
    pass

class DataLoader(Loader):
  def get(self, pathname = 'src/vocabs.txt', sep = '\n'):
    return pd.read_csv(pathname, header = None, sep = sep)


