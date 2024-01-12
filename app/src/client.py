from typing import List, Dict

import requests
import json

from config import SPACE_X_API_BASE_URL, SPACE_X_API_LAUNCHES_URL, TIMEOUT, logger


class SpaceXClient:
    base_url = SPACE_X_API_BASE_URL
    launches_url = '/'.join((SPACE_X_API_BASE_URL, SPACE_X_API_LAUNCHES_URL))
    
    def get_launches(self, *args, **kwargs) -> List[Dict]:
        """Calls the SpaceX API to get all launches.

        Returns:
            dict: A dictionary containing all launches from the SpaceX API.
        """
        try:
            logger.info(f'Calling {self.launches_url}')
            response = requests.get(self.launches_url, timeout=TIMEOUT)
            data = response.json()
            logger.info(f'Got {len(data)} launches')
        except Exception as e:
            logger.error(f'Error getting launches: {e}')
            raise e
        
        return data
    
    