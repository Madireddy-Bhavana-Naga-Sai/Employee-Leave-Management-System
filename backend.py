from flask import Flask, request, render_template

app = Flask(__name__)

# Database (you should use a real database in a production system)
employees = {}
leave_balances = {}

# Add Employee Page
@app.route("/add_employee.html")
def add_employee_page():
    return render_template("add_employee.html")

# Handle Employee Form Submission
@app.route("/add_employee", methods=["POST"])
def add_employee():
    emp_id = request.form["emp_id"]
    employee_name = request.form["employee_name"]
    gender = request.form["gender"]

    # Add the employee to your database
    employees[emp_id] = {"name": employee_name, "gender": gender}
    leave_balances[emp_id] = 0  # Initialize leave balance to 0

    return render_template("add_success.html")

# Apply Leave Page
@app.route("/apply_leave.html")
def apply_leave_page():
    return render_template("apply_leave.html")

# Handle Leave Application Form Submission
@app.route("/apply_leave", methods=["POST"])
def apply_leave():
    emp_id = request.form["emp_id"]
    leave_type = request.form["leave-type"]
    start_date = request.form["start_date"]
    end_date = request.form["end_date"]
    days = int(request.form["days"])
    reason = request.form["reason"]

    # Update leave balance
    leave_balances[emp_id] -= days

    return render_template("leave_confirmation.html")

# Leave Balance Page
@app.route("/leave_balance.html")
def leave_balance_page():
    return render_template("leave_balance.html")

# Check Leave Balance
@app.route("/check_balance", methods=["POST"])
def check_balance():
    emp_id = request.form["emp_id"]
    leave_balance = leave_balances.get(emp_id, 0)

    return f"Leave Balance: {leave_balance} days"

# Main Page
@app.route("/")
def main_page():
    return render_template("main_code.html")

if __name__ == "__main__":
    app.run(debug=True)