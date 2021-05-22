import requests
from flask import Flask,request,render_template,redirect
from twilio.rest import Client
account_sid="AC0ff7ddfb5928083b446d7e2ff9e76f95"
auth_token="8374095d7b647dfe42b346eef8f1b503"
client=Client(account_sid,auth_token)

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
        if ss=="" or ds=="":
            return render_template('home.html',msg='Select Source and Destination')
        if ss==ds:
            return render_template('home.html',msg="You cant provide Same state for both Source and Destination")
        destination_state_population=d[ds]["meta"]["population"]
        destination_state_confirmed_cases=d[ds]["total"]["confirmed"]
        print(destination_state_confirmed_cases/destination_state_population)
        user={'name':firstname+' '+lastname,'email':email,'mobile':mobile,'aadhar':aadhar,'date':date,
        'source':ss,'destination':ds}
        if((destination_state_confirmed_cases/destination_state_population)*100<=8):
            client.messages.create(to="whatsapp:+919908315470",from_="whatsapp:+14155238886",body="hello your status is confirmed")
            return render_template("status.html",user=user,status="Confirmed")
        else:
            client.messages.create(to="whatsapp:+919908315470",from_="whatsapp:+14155238886",body="Sorry, your status is not confirmed")
            status="not confirmed,because destination state has more covid effected people we care for your health"
            return render_template("status.html",user=user,status=status)
print("application about to run")
app.run()
