from joblib import load

def encode(object):
    enc = load('../model/dell_slow_dispatch_encoderV1.joblib')
    obj = enc.transform(object)
    return obj
