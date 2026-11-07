
from flask import Flask, render_template, request
from email.message import EmailMessage
from database import create_database, save_record, get_records

app = Flask(__name__)

# Create database when application starts
create_database()


# Calculate library overdue fine
def calculate_fine(days):

    if days <= 14:
        raw_fine = days * 0.50
    else:
        raw_fine = (14 * 0.50) + (days - 14) * 1.50

    # Maximum fine for one book
    final_fine = min(raw_fine, 25.00)

    # Determine account status
    if raw_fine > 25:
        status = "Suspended"
        membership = "Cancelled"

    elif final_fine == 0:
        status = "Good Standing"
        membership = "Active"

    elif final_fine <= 10:
        status = "Warning"
        membership = "Active"

    else:
        status = "Penalty"
        membership = "Active"

    return raw_fine, final_fine, status, membership


# Create cancellation email preview
def generate_email(name, email, book, days):

    message = EmailMessage()

    message["From"] = "library@example.com"
    message["To"] = email
    message["Subject"] = "Library Membership Cancellation"

    message.set_content(
        f"Dear {name},\n\n"
        f"Your borrowed book '{book}' is "
        f"{days} days overdue.\n\n"
        "Your membership has been cancelled because "
        "the calculated fine exceeded $25.00.\n\n"
        "The final fine is capped at $25.00.\n\n"
        "Please contact the university library.\n\n"
        "University Library Administration"
    )

    return message.get_content()


# Homepage
@app.route("/")
def home():
    return render_template("home.html")


# Calculate fine
@app.route("/calculate", methods=["POST"])
def calculate():

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    book = request.form.get("book", "").strip()
    days_input = request.form.get("days", "").strip()

    # Error handling
    if not name or not email or not book:
        return "Error: Please fill in all fields.", 400

    if "@" not in email or "." not in email.split("@")[-1]:
        return "Error: Invalid email address.", 400

    try:
        days = int(days_input)

        if days < 0 or days > 100000:
            return "Error: Enter valid overdue days.", 400

    except ValueError:
        return "Error: Overdue days must be a number.", 400

    # Calculate results
    raw, fine, status, membership = calculate_fine(days)

    # Save into SQLite database
    record_id = save_record(
        name, email, book, days,
        raw, fine, status, membership
    )

    # Generate email when membership is cancelled
    email_text = None

    if membership == "Cancelled":
        email_text = generate_email(
            name, email, book, days
        )

    return render_template(
        "Results.html",
        record_id=record_id,
        name=name,
        email=email,
        book=book,
        days=days,
        raw=raw,
        fine=fine,
        status=status,
        membership=membership,
        email_text=email_text
    )


# Database dashboard
@app.route("/records")
def records():

    all_records = get_records()

    return render_template(
        "record.html",
        records=all_records
    )


if __name__ == "__main__":
    app.run(debug=True)
