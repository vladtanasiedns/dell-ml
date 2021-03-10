from tensorflow.keras.models import load_model

def predict(object):
    model = load_model('../model/dell_slow_dispatchV1')
    pred = model.predict(object)
    return pred