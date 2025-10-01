# """
# 1️⃣ Unit Testing

# Definition: Test individual components (functions, methods, classes) in isolation.
# Goal: Make sure each unit works correctly.

# Popular Python frameworks:
# unittest → Built-in, standard library
# pytest → Most popular in modern Python projects
# hypothesis → For property-based testing
# """

# # Using pytest
# def add(a, b):
#     return a + b

# def test_add():
#     assert add(2, 3) == 5
#     assert add(-1, 1) == 0

# # Use case: Testing a function in a web API, calculator, or service module.
# # Current trend: pytest is the most widely used in 2025 for Python projects, including Django and FastAPI apps.

# """
# 2️⃣ Integration Testing

# Definition: Test multiple components together to see if they interact correctly.
# Goal: Verify that APIs, databases, and modules work together.

# Popular Python frameworks/libraries:
# pytest (with fixtures and pytest-django or pytest-asyncio)
# requests → To test API endpoints
# httpx → Async HTTP client for FastAPI/async apps
# """

# from fastapi.testclient import TestClient
# from myapp import app  # Your FastAPI app

# client = TestClient(app)

# def test_get_users():
#     response = client.get("/users")
#     assert response.status_code == 200
#     assert "username" in response.json()[0]

# # Use case: Making sure your backend API interacts correctly with database and returns expected data.
# # Trend: Integration testing is mandatory for APIs and microservices, and pytest + TestClient or pytest-django is most popular.


# """
# 3️⃣ End-to-End (E2E) Testing

# Definition: Test the complete flow of the application from the user's perspective.
# Goal: Simulate real user behavior on frontend + backend.

# Popular frameworks:
# Frontend: Selenium, Playwright, Cypress (JS-based, but can integrate with Python)
# Full-stack: Robot Framework (Python-friendly)
# """
# from playwright.sync_api import sync_playwright

# def test_login():
#     with sync_playwright() as p:
#         browser = p.chromium.launch()
#         page = browser.new_page()
#         page.goto("https://myapp.com/login")
#         page.fill("#username", "admin")
#         page.fill("#password", "1234")
#         page.click("#login-button")
#         assert page.url == "https://myapp.com/dashboard"
#         browser.close()

# """
# 4️⃣ Load / Performance Testing

# Definition: Test how your application performs under high traffic or stress.
# Goal: Ensure stability, speed, and resource management.

# Popular frameworks/tools:
# locust → Python-based load testing tool
# JMeter → Enterprise-grade, Java-based
# k6 → Modern JS/HTTP load testing tool
# """

# from locust import HttpUser, task, between

# class WebsiteUser(HttpUser):
#     wait_time = between(1, 5)

#     @task
#     def load_home(self):
#         self.client.get("/")

#     @task
#     def load_users(self):
#         self.client.get("/users")


# """

# | Type                | Goal                           | Popular Framework/Library | Real-Life Use Case              |
# | ------------------- | ------------------------------ | ------------------------- | ------------------------------- |
# | Unit Testing        | Test individual components     | `pytest`, `unittest`      | Functions, methods, classes     |
# | Integration Testing | Test combined components       | `pytest + TestClient`     | API + DB interaction            |
# | E2E Testing         | Test full user workflow        | `Playwright`, `Selenium`  | Login flow, e-commerce checkout |
# | Load Testing        | Test performance & scalability | `Locust`, `JMeter`, `k6`  | Website/API under high traffic  |


# """

# """
# For Python backend projects (Django, FastAPI, Flask): pytest + Playwright + Locust = full stack testing.

# Most used combo in 2025:
# pytest for unit & integration + Playwright for E2E + Locust for load testing
# """