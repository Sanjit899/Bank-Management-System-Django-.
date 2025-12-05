Bank Management System – Django Project

A fully functional Bank Management System built using Django, featuring secure authentication, user account management, and core banking operations such as Deposit, Withdraw, Transfer, and Transaction History.
This project simulates a basic digital banking platform suitable for learning backend development, database handling, and Django framework concepts.

🚀 Features
🔐 Authentication

User Registration

Login / Logout

Secure password handling using Django Auth

🏦 Banking Operations

Deposit money

Withdraw money

Transfer amount between accounts

Auto-generated unique account number for each user

Real-time account balance updates.

📄 Transaction Management

Records every deposit, withdrawal, and transfer

Shows clear debit/credit history

Tracks sender, receiver, amount, and timestamp

🎨 Frontend

Clean and simple UI

Bootstrap-based responsive design

Styled forms for Register, Login, Deposit, Withdraw, Transfer.


🗄️ Database

MySQL database integration

Models for Account and Transactions

Relational links between users and accounts.


🛠️ Tech Stack

Backend: Django (Python)

Database: MySQL

Frontend: HTML, CSS, Bootstrap

Tools: VS Code, Git, GitHub.


📂 Project Structure

bank_project/
│── bank_project/
│── core/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── static/
│   └── templates/
│── staticfiles/
│── templates/
│── requirements.txt
│── README.md


Install  dependencies :- 
# choose a folder for your project and cd into it
cd C:\Users\YourUser\projects
mkdir bank-django
cd bank-django

# create and activate venv (Windows PowerShell)
python -m venv venv
# activate in PowerShell
venv\Scripts\Activate.ps1

# or in cmd.exe:
# venv\Scripts\activate.bat

Install Django and the MySQL driver
python -m pip install --upgrade pip
pip install Django
pip install mysqlclient

Create a MySQL database and user (using your root password)

Open your MySQL client (from terminal) and run:

# connect as root (it will prompt for password)
mysql -u root -p
# enter: root

# inside MySQL prompt:
CREATE DATABASE bankdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
# optionally create a dedicated user  instead of using root:
CREATE USER 'bankuser'@'localhost' IDENTIFIED BY 'some_secure_password';
GRANT ALL PRIVILEGES ON bankdb.* TO 'bankuser'@'localhost';
FLUSH PRIVILEGES;
EXIT;

Run migrations and start the dev server
# make sure your project root is where manage.py is
python manage.py makemigrations
python manage.py migrate

# create admin user
python manage.py createsuperuser
# follow prompts (username, email, password)

# run dev server
python manage.py runserver

open http://127.0.0.1:8000.

Set Environment Variables
Create a .env file:
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=bank_db
DB_USER=root
DB_PASS=root
DB_HOST=localhost
DB_PORT=3306

Apply Migrations :- python manage.py migrate.

Run Server :- python manage.py runserver

Now open:
👉 http://127.0.0.1:8000.


🎯 Purpose of This Project

This project is built to help beginners understand how banking logic works and how to apply CRUD operations, authentication, database relations, and real-world finance-style transactions using Django.

It improves skills in:

Backend development

Authentication systems

Database modelling

Transaction handling

Full-stack mini-project deployment.

Admin dashboard for managing accounts

Email/SMS notifications for transactions

PDF export of statements

Loan & EMI module

OTP verification

Multi-currency support

API version (Django REST Framework).

🤝 Contributing

Pull requests are welcome!
Feel free to submit suggestions or enhancements.

📜 License

This project is open-source and available under the MIT License.
