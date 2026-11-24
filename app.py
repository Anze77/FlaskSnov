from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/Ljubezen", methods = ["POST"])
def love_calc():
    print(request.form)
    i1 = request.form["ime1"]
    i2 = request.form["ime2"]
    p = 0
    if i1.strip().lower() == "anže" or i2.strip().lower() == "anže":
        p = random.randint(90,100)
    if i1.strip().lower() == "žiga" or i2.strip().lower() == "žiga":
        p = random.randint(0,10)
    else:
        p = random.randint(0,100)

    if p < 15:
        k = "Pozabi"
    elif p < 50:
        k = "Morda"
    else:
        k = "Poroka!"


    if "x" in i1.lower() or "x" in i2.lower():
        p = random.randint(0,100) * 2
        if p > 100:
            p = 100

    z = i1[:len(i1)//2] + i2[len(i2)//2:]




    if i1.lower() == i2.lower():
        p = 100
        k = "Samoljubje"


    return render_template("index.html", ime1 = i1, ime2 = i2, procent = p, komentar = k, zdruzevanje = z )

app.run(debug=True)