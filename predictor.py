import pickle

model=pickle.load(open("model.pkl","rb"))

def predict(pregnancies ,glucose,bp,skinthickness,insulin, bmi, dpf, age):
    features=list([pregnancies,glucose,bp,skinthickness,insulin,bmi,dpf,age])
    pos= "Positive"
    neg= "negative"
    predict=model.predict([features])
    probab=model.predict_proba([features])
    #res = "{:.2f}".format(probab)
    probab = str(probab)
    if(predict==1):
        return (pos) # + " and probability value is" + res
    else:
        return (neg) # + " and probability value is" + res)
