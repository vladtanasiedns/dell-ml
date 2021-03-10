from tensorflow.keras.models import load_model

def predict(data):
    model = load_model('model/dell_slow_dispatchV1')
    pred = model.predict(data)
    return pred

from joblib import load

def encode(data):
    enc = load('model/dell_slow_dispatch_encoderV1.joblib')
    return enc.transform(data)