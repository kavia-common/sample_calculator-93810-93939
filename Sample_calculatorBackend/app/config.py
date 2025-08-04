import os

class Config:
    """Configuration class for Flask application."""
    # PUBLIC_INTERFACE
    SQLALCHEMY_DATABASE_URI = os.environ.get("POSTGRES_URL", "postgresql://user:pass@localhost:5432/sample_calculator_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "sample_calculator_secret")
    ENVIRONMENT = os.environ.get("ENVIRONMENT", "development")
