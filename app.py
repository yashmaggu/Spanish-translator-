# Reexport the FastAPI app for Render compatibility
from main import app

# This file is created to make the application compatible with Render's default gunicorn setup
# which tries to import 'app' from a module named 'app'
