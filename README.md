# 📚 University Library Fine Management System

A modern web-based library fine management application developed using **Python Flask, HTML5, CSS3, and SQLite**.

This project automates overdue book fine calculations, manages student borrowing records, determines account penalty statuses, and generates membership cancellation email previews.

## ✨ Features

- Automated overdue book fine calculation
- Student and borrowed book information management
- Standard overdue rate: $0.50 per day
- Severe overdue rate: $1.50 per additional day after 14 days
- Maximum fine of $25.00 per book
- Automatic account status determination
- Membership cancellation for qualifying overdue fines
- System-generated email notification previews
- SQLite database integration
- Saved student fine records dashboard
- Input validation and error handling
- Responsive white and sky-blue Liquid Glass UI

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Flask | Web application backend |
| HTML5 | Webpage structure |
| CSS3 | Liquid Glass interface |
| SQLite | Local database |
| Git & GitHub | Version control |
| VS Code | Development environment |

## 📊 Fine Calculation Algorithm

**Standard overdue period (1–14 days)**

Fine = Overdue Days × $0.50

**Severe overdue period (more than 14 days)**

Fine = $7.00 + (Overdue Days − 14) × $1.50

**Maximum charge:** $25.00 per book.

### Account Status

- **Good Standing:** $0.00
- **Warning:** $0.01–$10.00
- **Penalty:** $10.01–$25.00
- **Suspended:** Uncapped fine exceeds $25.00

Membership cancellation is triggered when the uncapped fine exceeds $25.00.

## 📁 Project Structure

```text
LibrarySystem/
├── app.py
├── database.py
├── requirements.txt
├── .gitignore
├── README.md
├── templates/
│   ├── index.html
│   ├── result.html
│   └── records.html
└── static/
    └── style.css
```

The SQLite database file is created locally.

## 🚀 Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/university-library-fine-management-system.git
```

**2. Open the project**

```bash
cd university-library-fine-management-system
```

**3. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

**4. Create the SQLite database**

```bash
python database.py
```

**5. Run the Flask server**

```bash
python app.py
```

**6. Open the application**

```text
http://127.0.0.1:5000/
```

## 🖥️ Application Pages

### Homepage
Provides a form for entering student information, borrowed book details, and overdue days.

### Fine Calculation Result
Displays the calculated fine, final capped fine, account status, and membership status.

### Database Dashboard
Displays saved borrower fine calculation records in a searchable-by-browser table view.

### Email Notification Preview
Generates a cancellation notice for suspended accounts. Email delivery is not configured.

## 🧪 Testing

The system can be tested using different overdue periods, including:

- Zero overdue days
- Standard overdue days
- Severe overdue days
- Maximum fine threshold
- Membership cancellation
- Invalid and negative inputs

## ⚠️ Current Limitations

- The system processes one book per calculation.
- Membership statuses are calculated per submitted record rather than across an entire student account.
- Email notifications are generated as previews, not sent automatically.
- User authentication is not implemented.
- The application uses a local SQLite database and Flask development server.

## 🎓 Academic Information

**Module:** IT2107 – Advanced Data Structures and Algorithms  
**Assignment:** Individual Assignment – Task 2  
**Academic Year:** Year 2, Semester 1  
**Institution:** CINEC Campus

## 📌 Project Objective

To demonstrate the practical application of algorithms, conditional statements, error handling, database operations, and web application development in an automated university library fine management system.

---

**Developed for academic and educational purposes.**
