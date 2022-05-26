from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def  home():
    return render_template("home.html")

@app.route("/form/")
def  form():
    return render_template("form.html")

# @app.route("/bookingdetails/")
# def  bookingdetails():
#     return render_template("bookingdetails.html")

if __name__ == "__main__":
    app.run(port=5000,debug=True)


