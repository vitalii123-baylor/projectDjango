# 📚 Learning Log: Your Personal Knowledge Tracker

A powerful web application built with **Django** to help you track your learning progress, topics, and daily insights. 

🚀 **Key Features:**
- 🔐 **Secure User Accounts**: Register, log in, and manage your private learning logs.
- 📂 **Topic Management**: Create, view, and organize your study topics and detailed entries.
- 📊 **Advanced Analytics Dashboard**: 
    - Real-time learning activity chart built with **Chart.js**.
    - Performance metrics (Total entries, words written, active topics).
    - Top topics breakdown using Django ORM Aggregation.
- ✨ **Enhanced User Experience**:
    - **Interactive Toasts**: Success/error notifications for better feedback.
    - **Motivational Quote of the Day**: Randomized quotes shown once per session to keep you inspired.
    - **Responsive Design**: Modern UI with Bootstrap 4 and FontAwesome.

🛠️ **Tech Stack:**
- **Backend**: Python 3.14+, Django 6.0.3
- **Frontend**: Bootstrap 4, JavaScript (ES6+), Chart.js
- **Database**: SQLite (Development)

---

## ⚙️ Quick Start

### 1. Installation
Clone the repository to your local machine:
```bash
git clone https://github.com/vitalii123-baylor/projectDjango.git
cd projectDjango
```

### 2. Setup Virtual Environment
Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations & Start Server
```bash
python manage.py migrate
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

---

## 💡 Project Logic (For Review)
- **Dashboard Logic**: Implemented using `django.db.models` (Count, Sum) and `TruncDate` for advanced data grouping.
- **Middleware**: Custom security and UI components for seamless session management.
- **Frontend**: Dynamic UI updates with jQuery and Bootstrap toasts.

Developed by [vitalii123-baylor](https://github.com/vitalii123-baylor)
📖 *Keep growing your mind.*
