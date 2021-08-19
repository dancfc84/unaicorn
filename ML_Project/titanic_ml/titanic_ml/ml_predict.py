

def prediction_model(pclass, sex, age, sibsp, parch, fare, embarked, title):
    import pickle
    x = [[pclass, sex, age, sibsp, parch, fare, embarked, title]] #This HAS to be in the same order as the dataframe, what the mjodel has been trained on
    randomForest = pickle.load(open('titanic_model.sav', 'rb'))
    prediction = randomForest.predict(x)
    return prediction
