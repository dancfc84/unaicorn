
from django.shortcuts import render
from . import ml_predict

def index (request): #Create a function for each webpage
    return render (request, 'index.html')

def result (request): #Create a function for each webpage

    pclass = int(request.GET['pclass']) # All the variables needed for our prediction
    sex = int(request.GET['sex'])
    age = int(request.GET['age']) # Age is the variable, gets it from the index.html form
    sibsp = int(request.GET['sibsp'])
    parch = int(request.GET['parch'])
    fare = int(request.GET['fare'])
    embarked = int(request.GET['embarked'])
    title = int(request.GET['title'])
    prediction = ml_predict.prediction_model(pclass, sex, age, sibsp, parch, fare, embarked, title)
    return render (request, 'result.html', {'prediction':prediction}) # Returns the value to result page from index and calls it prediction
