import os
from loguru import logger


SPACE_X_API_BASE_URL = "https://api.spacexdata.com"
SPACE_X_API_LAUNCHES_URL = "v5/launches/"
TIMEOUT = 5  # seconds


# DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost:5432/{DB_NAME}"
DATABASE_URL = os.getenv("DATABASE_URL")
