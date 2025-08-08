# 🎓 Student Marks & Attendance Tracker (SMART)

A simple web application built with Django that allows managing student data, recording assessment marks, tracking attendance, and generating reports.

##  Project Overview

This project is designed for school or university instructors to:
- Keep track of students, subjects, and assessments.
- Add and view marks for various tests.
- Record and manage student attendance.
- Generate attendance and grade reports per student or subject.

  ## 🌐 Live Demo
🔗 [live demo](https://smart-ybec.onrender.com)


##  Features

- ✅ CRUD operations for Students, Subjects, Assessments, Marks, and Attendance.
- 📊 Attendance Report View (per subject or student).
- 📈 Mark Report View (per student).
- 🔎 Filtering by subject, date, and student name.
- 📁 Admin dashboard with all data tables.
- 🌐 Simple, clean, mobile-friendly UI.

## 🛠️ Tech Stack

- **Backend**: Django 5.x
- **Database**: SQLite (default, can switch to PostgreSQL or MySQL)
- **Frontend**: HTML, CSS, Bootstrap
- **Admin Interface**: Django Admin


## ⚙️ Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/student-tracker.git
   cd student-tracker
   ```

2. **Create a Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```

4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Run the Development Server

```bash
 python manage.py runserver
```

6. Access the App
    Open your browser and go to `http://127.0.0.1:8000/`

👨‍🏫 Admin Access

To create a superuser:

```bash
python manage.py createsuperuser
```

Then visit /admin to log in and manage records via Django Admin.

