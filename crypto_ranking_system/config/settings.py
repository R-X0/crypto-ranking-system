import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
CMC_API_KEY = os.getenv('CMC_API_KEY')
CMC_API_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# Database Configuration
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

# Application Settings
UPDATE_INTERVAL = 3600  # 1 hour