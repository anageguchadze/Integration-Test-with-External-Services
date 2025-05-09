# Integration-Test-with-External-Services

This is a simple Django REST Framework (DRF) project that demonstrates how to use Redis for caching API responses. The application exposes an `/events/` endpoint that returns a list of events and caches the response for 10 minutes using Redis.

---

## 🔧 Features

- Django REST Framework-based API
- Redis integration using `django-redis`
- Automatic view-level response caching via `@cache_page`
- Manual caching using Django's `cache` API
- Integration tests for cache behavior

---

## 🛠️ Setup Instructions

### 1. Clone the repository
git clone https://github.com/anageguchadze/Integration-Test-with-External-Services.git
cd Integration-Test-with-External-Services

2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt
Make sure Redis is installed and running locally (on localhost:6379).

4. Apply migrations
python manage.py migrate

5. Run the development server
python manage.py runserver
API will be available at: http://127.0.0.1:8000/events/

⚙️ Configuration
Redis Cache (in settings.py):
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
Cache TTL
CACHE_TTL = 600  # 10 minutes

✅ Running Tests
Tests are located in myapp/tests.py.

To run the tests:
python manage.py test
These tests:

Make a GET request to the /events/ endpoint

Update an Event instance in the database

Re-check that the cached data remains unchanged unless the cache is cleared

📦 Dependencies
Django

djangorestframework

django-redis

Redis server (external)

📂 Project Structure
myproject/
│
├── myapp/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── tests.py
│   └── urls.py
│
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── manage.py
└── requirements.txt

📜 License
This project is licensed under the MIT License.