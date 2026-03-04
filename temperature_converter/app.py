from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result1 = result2 = None
    
    if request.method == "POST":
        temperature = float(request.form["temperature"])
        unit = request.form["unit"]

        if unit == "C":
            result1 = ("Fahrenheit", (temperature * 9/5) + 32)
            result2 = ("Kelvin", temperature + 273.15)

        elif unit == "F":
            result1 = ("Celsius", (temperature - 32) * 5/9)
            result2 = ("Kelvin", (temperature - 32) * 5/9 + 273.15)

        elif unit == "K":
            result1 = ("Celsius", temperature - 273.15)
            result2 = ("Fahrenheit", (temperature - 273.15) * 9/5 + 32)

    return render_template("index.html", r1=result1, r2=result2)

if __name__ == "__main__":
    app.run(debug=True)