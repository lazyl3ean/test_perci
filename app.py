
from flask import Flask, render_template, redirect, request
import pymongo
from bson import ObjectId
from flask_mail import Mail, Message


client = pymongo.MongoClient("mongodb+srv://devika:1234@cluster0.jl6vuvp.mongodb.net/?retryWrites=true&w=majority")
db = client.perci


app=Flask(__name__)
app.config["MAIL_SERVER"]="smtp.gmail.com"
app.config["MAIL_PORT"]=465
app.config["MAIL_USERNAME"]="lazychu24@gmail.com"
app.config["MAIL_PASSWORD"]="rdodgisldlfyaqlx"
app.config["MAIL_USE_TLS"]=False
app.config["MAIL_USE_SSL"]=True

mail=Mail(app)

@app.route("/")
def  home():
    data = list(db.issue.find())
    # print(data[0]["booking_past"][1]["doctor"])
    return render_template("home.html", data_list=data[0])



@app.route("/newbookingsform/")
def  newbookingsform():
    return render_template("newbookingsform.html")


# take data from our booking form
@app.route("/updatebooking/", methods=["POST"])
def  updatebooking():
    data = {"issue":request.form["issue"],
        "doctor":request.form["doctor"],
        "date":request.form["date"]
    }

    db.issue.update_one(
        {"_id":ObjectId("62908d89bd4d5ddf11be908a")},
        # bookings is an arry in mongoDB
        {"$push":{"bookings":data}}
    )
    return redirect("/")

@app.route("/form/")
def  form():
    data = list(db.prescription.find())

    return render_template("form.html",data_list=data)

@app.route("/email/<id>/<email>/",methods=["POST"])
def email(id,email):
    data = db.prescription.find_one( {"_id":ObjectId(id)})
    msg =Message("Please deliver medicine",sender="lazychu24@gmail.com",recipients=[email])
    msg.html=render_template("emailbody.html",data_list =data)

    mail.send(msg)

    return redirect("/")
    


if __name__ == "__main__":
    app.run(port=5000,debug=True)


