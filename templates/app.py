from flask import Flask, request, render_template
from password_generator import generate_password, check_password_strength

app = Flask(__name__)

# Home page with the form
@app.route("/")
def home():
    return render_template("index.html")

# Route to generate the password
@app.route("/generate", methods=["POST"])
def generate():
    # Retrieve parameters from the form
    length = int(request.form.get("length", 12))
    use_letters = "letters" in request.form
    use_numbers = "numbers" in request.form
    use_symbols = "symbols" in request.form

    # Generate the password and evaluate its strength
    password = generate_password(length, use_letters, use_numbers, use_symbols)
    strength = check_password_strength(password)

    # Return an HTML page with the results
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <title>Password Generator</title>
    </head>
    <body class="bg-light">
        <div class="container mt-5">
            <h1 class="text-center text-primary">Your Generated Password</h1>
            <p class="text-center"><strong>Password:</strong> {password}</p>
            <p class="text-center"><strong>Strength:</strong> <span class="badge bg-info text-dark">{strength}</span></p>
            <div class="text-center">
                <a href="/" class="btn btn-secondary">Generate Another</a>
            </div>
        </div>
    </body>
    </html>
    """

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Use a free port (e.g., 5001)

