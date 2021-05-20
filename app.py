import requests
from flask import Flask,request,render_template,redirect
url="https://api.covid19india.org/v4/data.json"
page=requests.get(url)
d=page.json()
app=Flask(__name__,template_folder="c:/users/phani t/desktop")
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
        user={'name':firstname+' '+lastname,'email':email,'mobile':mobile,'aadhar':aadhar,'date':date,
        'source':ss,'destination':ds}
        if((destination_state_confirmed_cases/destination_state_population)*100<=8):
            return render_template("status.html",user=user,status="Confirmed")
        else:
            status="Not Confirmed (This may be due to more no of Covid Cases)"
            return render_template("status.html",user,status=status)
print("application about to run")
app.run()