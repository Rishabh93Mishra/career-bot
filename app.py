from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from deep_translator import GoogleTranslator
import mysql.connector
from config import get_db

app = Flask(__name__)
CORS(app)

# ✅ Homepage route (Fixes Not Found error)
@app.route("/")
def home():
    return render_template("index.html")


# 🚀 Translate API
@app.route("/translate", methods=["POST"])
def translate_text():
    data = request.json
    message = data.get("message", "")
    
    translated_text = GoogleTranslator(source='auto', target='en').translate(message)
    return jsonify({"translated": translated_text})


# 🚀 Signup API
@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    name = data["name"]
    email = data["email"]
    password = data["password"]

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", 
                   (name, email, password))
    conn.commit()

    return jsonify({"status": "success"})


# 🚀 Login API
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data["email"]
    password = data["password"]

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
    user = cursor.fetchone()

    if user:
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "fail"})


if __name__ == "__main__":
    app.run(debug=True)
import mysql.connector

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",          # your MySQL username
        password="Rishabh*1", 
        database="career_bot"
    )
