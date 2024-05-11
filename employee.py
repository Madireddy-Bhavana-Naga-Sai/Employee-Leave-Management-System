# app.py
from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database setup
conn = sqlite3.connect("leave_management.db")
cursor = conn.cursor()

# Create a table for employee leave requests
cursor.execute('''CREATE TABLE IF NOT EXISTS leave_requests (
    id INTEGER PRIMARY KEY,
    employee_name TEXT,
    start_date DATE,
    end_date DATE,
    status TEXT
)''')
conn.commit()

@app.route("/")
def index():
    # Display a list of leave requests
    cursor.execute("SELECT * FROM leave_requests")
    leave_requests = cursor.fetchall()
    return render_template("index.html", leave_requests=leave_requests)

@app.route("/request_leave", methods=["GET", "POST"])
def request_leave():
    if request.method == "POST":
        employee_name = request.form["employee_name"]
        start_date = request.form["start_date"]
        end_date = request.form["end_date"]
        status = "Pending"  # You can set the initial status as per your requirements

        cursor.execute("INSERT INTO leave_requests (employee_name, start_date, end_date, status) VALUES (?, ?, ?, ?)",
                       (employee_name, start_date, end_date, status))
        conn.commit()

        return redirect(url_for("index"))

    return render_template("request_leave.html")

if __name__ == "__main__":
    app.run(debug=True)
