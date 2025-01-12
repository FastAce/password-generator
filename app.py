from flask import Flask, render_template, request
from password_generator import generate_password, check_password_strength

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    password = ""
    if request.method == "POST":
        length = int(request.form.get("length"))
        use_letters = "letters" in request.form
        use_numbers = "numbers" in request.form
        use_symbols = "symbols" in request.form
        password = generate_password(length, use_letters, use_numbers, use_symbols)
    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

