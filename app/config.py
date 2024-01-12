import os
from loguru import logger


SPACE_X_API_BASE_URL = 'https://api.spacexdata.com'
SPACE_X_API_LAUNCHES_URL = 'v5/launches/'
TIMEOUT = 5  # seconds

# DB_USER = os.getenv('POSTGRES_USER')
# DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
# DB_NAME = os.getenv('POSTGRES_DB')
DB_USER = 'user'
DB_PASSWORD = 'password'
DB_NAME = 'space_x'

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost:5432/{DB_NAME}"
