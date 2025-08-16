import os
from app.main import app  # Import your FastAPI app

# Required for Gunicorn (WSGI server)
from fastapi.middleware.wsgi import WSGIMiddleware

# Convert FastAPI (ASGI) to WSGI
wsgi_app = WSGIMiddleware(app)

# Gunicorn looks for a variable named "application"
application = wsgi_app