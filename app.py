from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Akash@123",
    database="bsdm"
)

cursor = db.cursor()

@app.route("/")
def signup_page():
    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def signup():
    g_id = request.form["g_id"]
    g_name = request.form["g_name"]
    g_age = request.form["g_age"]
    g_sex = request.form["g_sex"]
    ph_no = request.form["ph_no"]
    g_mail = request.form["g_mail"]

    try:
        sql = """
            INSERT INTO Gabin (g_id, g_name, g_age, g_sex, ph_no, g_mail)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (g_id, g_name, g_age, g_sex, ph_no, g_mail)
        cursor.execute(sql, values)
        db.commit()
        return "Signup successful!"

    except mysql.connector.Error as err:
        return f"Error: {err}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
