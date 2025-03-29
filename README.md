E-Commerce API 🛒
A production-ready RESTful API built with FastAPI for managing products and orders in an e-commerce platform.

🚀 Features
✅ Product Management → Add & list products
✅ Order Processing → Place orders with stock validation
✅ Database → Uses SQLite (easily switchable to PostgreSQL/MySQL)
✅ Modular Architecture → Routes, Models, and Schemas in separate files
✅ Docker Support → Easy deployment using Docker
✅ Tested Codebase → Unit & Integration tests included

🛠 Tech Stack
Backend: FastAPI, SQLAlchemy

Database: SQLite (or PostgreSQL/MySQL)

Containerization: Docker

Testing: Pytest

📦 Setup & Installation
1️⃣ Clone the repository
bash
Copy
Edit
git clone git@github.com:somitmittal/ECommerceApp.git
cd ECommerceApp
2️⃣ Create & Activate a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Run the Application
bash
Copy
Edit
uvicorn main:app --reload
API is now live at → http://127.0.0.1:8000

📌 API Endpoints
Method	Endpoint	Description
GET	/products	Fetch all products
POST	/products	Add a new product
POST	/orders	Place an order
🐳 Run with Docker
bash
Copy
Edit
docker build -t ecommerce-api .
docker run -p 8000:8000 ecommerce-api
✅ Running Tests
bash
Copy
Edit
pytest
