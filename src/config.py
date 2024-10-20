# config.py
import os

ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
TIMEOUT = 30  # seconds
DEFAULT_LANGUAGE = "PT"
API_KEY = '7d221a31dede2449c72d66850e5374d2'
DATABASE_URL = "postgresql://user:password@localhost/mydatabase"

UNITS = 'metric'

class Config:
    DEBUG = False
    TESTING = False
    API_KEY = "your_openweathermap_api_key"
    WEATHER_API_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    API_KEY = ""

class ProductionConfig(Config):
    API_KEY = ""
