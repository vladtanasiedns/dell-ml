from flask import Flask, request
import ml
import pandas as pd
import numpy as np
import json
from utils import allowed_file

app = Flask(__name__)

# data = pd.read_csv('DELL EMEA TEST DATASET.csv')
# df = pd.DataFrame(data)
# df["slow_dispatch"] = np.where(df["velocity"].astype('int64') >= 30, 1, 0)
# df = df.dropna()
# df = df.drop(["slow_dispatch", "velocity"], axis=1)

# @app.route("/")
# def test():
#     data = encode.encode(df)
#     preds = predict.predict(data)
#     preds = np.array(preds)
#     preds_flat = preds.flatten()
#     x = [str(x) for x in preds_flat]
#     return json.dumps(x)

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return {"message": "no file selected"}
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return {"message": "no file selected"}
        if file and allowed_file(file.filename):
            df = pd.read_csv(file)
            df["slow_dispatch"] = np.where(df["velocity"].astype('int64') >= 30, 1, 0)
            df = df.dropna()
            df = df.drop(["slow_dispatch", "velocity"], axis=1)
            data = ml.encode(df)
            preds = ml.predict(data)
            preds = np.array(preds)
            preds_flat = preds.flatten()
            x = [str(x) for x in preds_flat]
            return json.dumps(x)

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)