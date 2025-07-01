# 💸 FinanceFlow – Personal Expense Tracker Web App

**FinanceFlow** is a full-stack Django web application designed to help users efficiently **track expenses**, **set smart budgets**, and **achieve savings goals**. Built with a focus on usability, finance insight, and modern UI features.

---

## 🚀 Features

- ✅ **User Authentication** (Login / Signup)
- 📆 **Track Expenses** (Daily, Weekly, Monthly, Yearly views)
- 📊 **Budget Management** with category limits & alerts
- 📉 **Visual Spending Insights** (progress bars, dashboards)
- 🎯 **Savings Goals** (e.g., "Buy a Laptop - ₹60,000 by Dec")
- 🔔 Alerts when you're nearing or exceeding budgets
- 📂 Categorized spending with dashboard summaries
- 🧾 Add, view, and manage your expenses easily

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap 5
- **Database:** SQLite (can be switched to PostgreSQL/MySQL)
- **Charts & UI:** Chart.js (for visual insights)
- **Authentication:** Django’s built-in auth system


## 📦 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/FinanceFlow.git
   cd FinanceFlow
Create virtual environment




python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
Install dependencies



pip install -r requirements.txt
Apply migrations


python manage.py makemigrations
python manage.py migrate
Create a superuser


python manage.py createsuperuser
Run the server


python manage.py runserver
Open in browser: http://127.0.0.1:8000

🧩 Directory Structure

financeflow/
├── users/             # User auth and custom models
├── expenses/          # Expense management
├── budgets/           # Budget and salary logic
├── savings/           # Savings goal tracking
├── templates/         # All HTML templates
├── static/            # CSS, JS, assets
├── manage.py
├── requirements.txt
✨ Future Enhancements
📱 Mobile responsive UI

📅 Recurring expense tracking

📧 Monthly expense reports via email

🧠 AI insights to suggest category limits

💬 Multi-language support

🙌 Contributing
Pull requests are welcome! If you’d like to improve something, open an issue or fork the repo and submit a PR.

📜 License
This project is open-source and available under the MIT License.

📣 Author
Developed by Rohith Prudhvi.
📫 Connect on LinkedIn
