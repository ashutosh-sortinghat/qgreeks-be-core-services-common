import requests
import json

def get_option_activity(account_id="b1b17b57-bfca-4d09-ae37-a0a5529e0221", start_date = "2024-02-10", end_date="2024-02-25"):
    url = f"https://qginternalapis.azurewebsites.net/options-activity/account-id/{account_id}/start-date/{start_date}/end-date/{end_date}/"
    # https://qginternalapis.azurewebsites.net/options-activity/start-date/{start_date}/end-date/{end_date}/
    payload = {}
    headers = {
        'accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return json.loads(response.text)
