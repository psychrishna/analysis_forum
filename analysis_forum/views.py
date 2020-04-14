from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .forms import FileUploadForm
from django.contrib import messages
import pandas as pd
import json
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


# Create your views here.
def home(request):
    form = FileUploadForm()
    context = {
        'form':form
    }
    return render(request, 'analysis_forum/index.html', context)

def file_upload(request):
    if(request.method == "POST"):
        form = FileUploadForm(request.POST,request.FILES)
        #print(form)
        if form.is_valid():
            #form.save()
            #db = pd.read_csv(settings.MEDIA_ROOT + "\\datasets\\"+str(request.FILES['file_name']))
            db = pd.read_csv(settings.MEDIA_ROOT + "\\datasets\\"+str(request.FILES["file_name"]))
            messages.success(request, "The Dataset has been uploaded!")
            response = HttpResponse(json.dumps(list(db.columns)))
            response.set_cookie("file_name",str(request.FILES['file_name']))
            return response
        else:
            return HttpResponse("")

 
def data_send_categorical(request):
    if(request.method == "POST"):
        print("here")
        print(request.POST)
        x_index = request.POST["x-value"]
        #y_index = request.POST["y-value"]
        dict1 = {}
        db = pd.read_csv(settings.MEDIA_ROOT + "\\datasets\\"+request.COOKIES["file_name"])
        dict1[x_index] = list(set(db[x_index]))
        #dict1["y_0"] = list(db[y_index])
        dict1[x_index + "_frequency"] = []
        #print(dict1["x_0"])
        list1 = list(db[x_index])
        for i in dict1[x_index]:
            dict1[x_index + "_frequency"].append(list1.count(i))
        count = 0
        for i in db.columns:
            if(count == 3):
                break
            dict1[i] = list(set(db[i]))
            list1 = list(db[i])
            dict1[i+"_frequency"] = [list1.count(j) for j in dict1[i]]
            count += 1
        print(dict1)
        return  HttpResponse(json.dumps(json.dumps(dict1)))
    return HttpResponse("")

def data_send_numerical(request):
    if(request.method == "POST"):
        try:
            print(request.POST)
            x_index = request.POST["x-value"]
            y_index = request.POST["y-value"]
            dict1 = {}
            db = pd.read_csv(settings.MEDIA_ROOT + "\\datasets\\"+request.COOKIES["file_name"])
            dict1[x_index] = list(db[x_index])
            dict1[y_index] = list(db[y_index])
            #print(dict1["x_0"])
            # model = build_regression_model()
            # model.fit(db[x_index], db[y_index], epochs = 100)
            
            min_x = min(db[x_index])
            max_x = max(db[x_index])
            
            X_train = np.asarray(dict1[x_index]).reshape(-1,1)
            Y_train = np.asarray(dict1[y_index]).reshape(-1,1)
            
            regr = linear_model.LinearRegression()
            regr.fit(X_train, Y_train)
            params = [regr.coef_,regr.intercept_]

            min_y = float(params[0])*min_x+float(params[1])
            max_y = float(params[0])*max_x+float(params[1])
            

            # count = 1
            # for i in db.columns:
            #     if(count == 3):
            #         break
            #     if(db[i].dtype == db[x_index].dtype):
            #         dict1[i] = list(db[i])
            #         count += 1
            
            dict1["min"] = [min_x, min_y]
            dict1["max"] =  [max_x, max_y]
            response = HttpResponse(json.dumps(dict1))
            response.set_cookie("slope",str(float(params[0])))
            response.set_cookie("intercept",str(float(params[1])))
            return response
        except:
            print("exception")
            response = HttpResponse()
            response.status_code = 404
            response.content = "BAD REQUEST"
            return response
    return HttpResponse("")


def dataset_columns(request):
    db = pd.read_csv(settings.MEDIA_ROOT + "\\datasets\\"+request.COOKIES["file_name"])
    #types = ["int", "float"]
    resp = {"qualitative":[],"quantitative":[]}
    for col in db.columns:
        if db[col].dtype=="object":
            resp["qualitative"].append(col)
        else:
            resp["quantitative"].append(col)


    return  HttpResponse(json.dumps(json.dumps(resp)))

def barplot_script(request):
    return render(request, 'analysis_forum/barchart.html')

def pieplot_script(request):
    return render(request, 'analysis_forum/pie.html')

def polararea_script(request):
    return render(request, 'analysis_forum/polar.html')

def lineplot_script(request):
    return render(request, 'analysis_forum/line.html')

def scatterplot_script(request):
    return render(request, 'analysis_forum/scatter.html')

def histogram_script(request):
    return render(request, 'analysis_forum/histogram.html')

def linear_regression(request):
     return render(request, 'analysis_forum/linear.html')

