from flask import Flask, render_template, redirect, request
import pymongo
from bson import ObjectId


client = pymongo.MongoClient("mongodb+srv://devika:1234@cluster0.jl6vuvp.mongodb.net/?retryWrites=true&w=majority")
db = client.perci


app=Flask(__name__)

@app.route("/")
def  home():
    data = list(db.issue.find())
    # print(data[0]["booking_past"][1]["doctor"])
    return render_template("home.html", data_list=data[0])

@app.route("/form/")
def  form():
    return render_template("form.html")

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


if __name__ == "__main__":
    app.run(port=5000,debug=True)


