import joblib
def predict(list):
    temp=list[0]
    hum=list[1]
    mois=list[2]
    data = [temp, hum, mois]

    mdl = joblib.load('model.pkl')
    ypred = mdl.predict(data)
    prediction = ypred[0]
    return prediction
