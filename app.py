# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FrUwAN4BXZyvsMWXXGg1WVyfZFxSnpew
"""

try:
  from google.colab.output import eval_js
  print(eval_js("google.colab.kernel.proxyPort(5000)"))
except:pass

import requests
from flask import Flask,request,render_template,redirect
url="https://api.covid19india.org/v4/data.json"
page=requests.get(url)
d=page.json()
app=Flask(__name__,template_folder="/content")
@app.route("/home",methods=["GET","POST"])
def home():
    if(request.method=="GET"):
        print("hi")
        return render_template("home.html")
    else:
        firstname=request.form["firstname"]
        lastname=request.form["lastname"]
        email=request.form["email"]
        aadhar=request.form["aadhar"]
        mobile=request.form['mobile']
        date=request.form['date']
        ss=request.form["source"]
        ds=request.form["dest"]
        destination_state_population=d[ds]["meta"]["population"]
        destination_state_confirmed_cases=d[ds]["total"]["confirmed"]
        print(destination_state_confirmed_cases/destination_state_population)
        if((destination_state_confirmed_cases/destination_state_population)*100<=8):
            return render_template("status.html",firstname=firstname,lastname=lastname,status="confirmed",email=email)
        else:
            status="not confirmed,because destination state has more covid effected people we care for your health"
            return render_template("status.html",firstname=firstname,lastname=lastname,status=status,email=email)
app.run()
