import requests
import json

def get_option_activity(start_date = "2024-02-10", end_date="2024-02-25"):
    url = f"https://qginternalapis.azurewebsites.net/options-activity/start-date/{start_date}/end-date/{end_date}/"
    payload = {}
    headers = {
        'accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return json.loads(response.text)
