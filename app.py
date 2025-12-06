from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from deep_translator import GoogleTranslator
from config import get_db
import mysql.connector

app = Flask(__name__)
CORS(app)

# ------------------ HOME PAGE ------------------
@app.route("/")
def home():
    return render_template("index.html")


# ------------------ TRANSLATE ------------------
@app.route("/translate", methods=["POST"])
def translate_text():
    data = request.json
    msg = data.get("message", "")
    translated = GoogleTranslator(source='auto', target='en').translate(msg)
    return jsonify({"translated": translated})


# ------------------ SIGNUP ------------------
@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    name = data["name"]
    email = data["email"]
    password = data["password"]

    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
        (name, email, password)
    )
    conn.commit()

    return jsonify({"status": "success"})


# ------------------ LOGIN ------------------
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data["email"]
    password = data["password"]

    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM users WHERE email=%s AND password=%s",
        (email, password)
    )
    user = cursor.fetchone()

    if user:
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "fail"})


# ------------------ COURSES API ------------------
@app.route("/courses", methods=["GET"])
def get_courses():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM courses")
    rows = cursor.fetchall()
    return jsonify(rows)


# ------------------ RUN ------------------
if __name__ == "__main__":
    app.run(debug=True)
