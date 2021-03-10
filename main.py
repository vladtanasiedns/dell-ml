from flask import Flask
from utils import encode, predict
import pandas as pd

app = Flask(__name__)

data = pd.read_csv('DELL EMEA TEST DATASET.csv')
df = pd.DataFrame(data)

@app.route("/")
def test():
    print(encode)
    print(predict)
    return "works"

if __name__ == '__main__':
    app.run(debug=True)