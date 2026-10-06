# GreatKart – Django E-Commerce Website

GreatKart is a **Django-based E-Commerce Website** developed as an academic project using **Python and Django**. The project demonstrates essential e-commerce functionality such as user authentication, product browsing, shopping cart, checkout, orders, and product management.

> **Note:** This project was developed for academic/learning purposes and is not a commercial live e-commerce platform.

## 🚀 Features

* User Registration & Login
* Email Verification
* User Profile Management
* Product Categories
* Product Search
* Product Details
* Product Gallery
* Shopping Cart
* Add/Remove Products from Cart
* Cart Quantity Management
* Checkout
* Order Placement
* Order History
* Order Details
* Admin Panel
* Product & Category Management
* Responsive UI

## 🛠️ Technologies Used

### Backend

* Python
* Django

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap

### Database

* SQLite

### Other

* Django Authentication
* Gmail SMTP
* Git & GitHub

## 📂 Project Structure

```text
GreatKart/
│
├── accounts/
├── carts/
├── category/
├── orders/
├── store/
├── greatkart/
├── templates/
├── static/
├── media/
├── manage.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/sathvarahitesh/greatkart-django.git
```

### 2. Open the project

```bash
cd greatkart-django
```

### 3. Create a virtual environment

```bash
python -m venv env
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\env\Scripts\Activate.ps1
```

**Windows CMD:**

```cmd
env\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Create an admin user

```bash
python manage.py createsuperuser
```

### 8. Start the development server

```bash
python manage.py runserver
```

Open the website:

```text
http://127.0.0.1:8000/
```

## 🔐 Environment Variables

For production or public deployment, sensitive information such as email credentials and secret keys should be stored using environment variables rather than directly inside `settings.py`.

Do not upload:

* Passwords
* API keys
* Email credentials
* `.env` files
* Virtual environment
* Local database files containing sensitive data

## 📸 Project Screenshots

Screenshots of the application can be added here.

```text
screenshots/
├── home.png
├── products.png
├── product-detail.png
├── cart.png
└── checkout.png
```

## 🎓 Academic Project

**Project:** GreatKart – E-Commerce Website
**Technology:** Python with Django
**Database:** SQLite
**Purpose:** Academic / Learning Project

## 👨‍💻 Developer

**Hitesh Sathvara**

* GitHub: https://github.com/sathvarahitesh

## 📄 License

This project is created for educational and learning purposes.
