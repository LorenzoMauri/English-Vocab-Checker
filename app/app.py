import abc
import re 
import pandas as pd 
  
# custom packages 
from libs.Loader import DataLoader
from libs.Parser import TextParser



from flask import Flask, render_template, request

app = Flask(__name__)
loader = DataLoader()
parser = TextParser()
dataframe = loader.get()
dataframe = parser.parse(dataframe)
sample_size = 20 



@app.route("/", methods = ['GET'])
def getVocab():
    global sample
    sample = dataframe.sample(sample_size)
    return render_template('index.html', 
                            sample =sample,
                            sample_size = sample_size)

@app.route("/check", methods = ['POST'])
def check():
    #word = request.form['fname']
    result = sample.eng

    return render_template('test.html', sample = sample, result=result)



if __name__ == '__main__':
    app.run(debug=True)