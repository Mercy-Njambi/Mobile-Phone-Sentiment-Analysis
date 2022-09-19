from flask import Flask, render_template, request

import marks as m

app = Flask(__name__)

@app.route("/", methods = ["GET",'POST'])
def marks():
    if request.method == "POST":
        hrs = request.form["hrs"]
        mark_pred = m.marks_prediction(hrs)
        mk = mark_pred

    return render_template("index.html", my_marks = mk)



if __name__ == '__main__':
    app.run(debug=True)    