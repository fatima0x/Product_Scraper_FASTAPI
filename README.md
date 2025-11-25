Product Scraper API (FastAPI + PostgreSQL + Selenium + BeautifulSoup)

A full-stack data extraction pipeline built using FastAPI, PostgreSQL, Selenium, and BeautifulSoup.
This project scrapes product details from multiple webpages, stores them in a database, and exposes them through API endpoints.

🚀 Tech Stack

Python 3.13

FastAPI – API framework

PostgreSQL – Database

SQLAlchemy – ORM

Requests + BeautifulSoup – Static scraping

Selenium WebDriver – Dynamic scraping

Uvicorn – ASGI server

📌 Features
✔ Static Scraping (BeautifulSoup)

Extracts product title, price, availability, rating & category

Lightweight and fast

✔ Dynamic Scraping (Selenium)

Used when JavaScript-rendered pages fail static scraping

Headless Chrome execution via Selenium Manager

✔ Database Storage

Stores scraped products in PostgreSQL automatically

Integrated using SQLAlchemy models

✔ API Endpoints (FastAPI)

POST /scrape – Scrapes products & stores them in database

GET /products – Fetches all stored products

✔ CSV Export (Optional)

Saves data in /output/products.csv

📁 Project Folder Structure
Product_Scraper_FASTAPI/
│── main.py
│── requirements.txt
│── README.md
│── app/
│ ├── routes.py
│── scraper/
│ ├── static_scraper.py
│ ├── selenium_scraper.py
│ └── **init**.py
│── database.py
│── models.py
│── output/
│ └── products.csv (auto-generated)
│── venv/ (ignored)

🔧 Setup Instructions
1️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate # Mac/Linux
venv\Scripts\activate # Windows

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Start PostgreSQL & create a database

Example:

CREATE DATABASE product_scraper;

Update your DB URL inside database.py.

4️⃣ Run FastAPI server
uvicorn main:app --reload

5️⃣ Open API docs

Navigate to:

👉 http://127.0.0.1:8000/docs

Use:

POST /scrape

GET /products

📌 Sample API Output
{
"message": "Scraping complete!",
"items": [
{
"Title": "A Light in the Attic",
"Price": "£51.77",
"Availability": "In stock",
"Category": "Poetry",
"Rating": "Three",
"Product URL": "https://books.toscrape.com/..."
}
]
}

🎯 Why This Project Is Valuable for Upwork

This project demonstrates:

✔ Web scraping (BeautifulSoup, Selenium)
✔ REST APIs (FastAPI)
✔ Database integration (PostgreSQL)
✔ Clean architecture
✔ Real-world data extraction pipeline

Perfect to show clients your backend + scraping skills.

📌 Future Enhancements (Optional)

Add pagination scraping

Async scraping optimization

Docker containerization

Frontend dashboard with charts

Scrapy integration

🏁 Author

Fatima Suleman
Backend Developer • FastAPI • Python • Data Scraping
