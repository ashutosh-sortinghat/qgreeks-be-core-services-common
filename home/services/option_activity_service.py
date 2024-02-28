import requests
import json
from ..config.config import DBConfig
def get_option_activity(start_date = "2024-02-10", end_date="2024-02-25"):
    url = DBConfig(start_date=start_date, end_date=end_date).option_activity_api
    payload = {}
    headers = {
        'accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return json.loads(response.text)
