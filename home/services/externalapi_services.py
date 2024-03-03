import requests
import time
from .utils import extract_date_fn, get_current_date, \
                    convert_date_to_timestamp_with_zone, filter_properties
import datetime
from qg_app.config import DBConfig

def get_options_expirations(symbol):

    url = DBConfig().options_expirations_api

    querystring = {"symbol": f"{symbol}"}

    headers = {
        "X-RapidAPI-Key": "94c0a913b8mshd15fe7d6bf053e7p177a78jsnfdf4efc4eeca",
        "X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()


def get_option_chain(symbol, date):
    url = DBConfig().option_chain_api
    querystring = {"symbol": f"{symbol}",
                   "expiration": date, "display": "list"}
    headers = {
        "X-RapidAPI-Key": "94c0a913b8mshd15fe7d6bf053e7p177a78jsnfdf4efc4eeca",
        "X-RapidAPI-Host": "mboum-finance.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()


def get_option_price(symbol):

    url = DBConfig().market_price_api

    querystring = {"symbol": f"{symbol}", "format": "json", "outputsize": "30"}

    headers = {
        "X-RapidAPI-Key": "94c0a913b8mshd15fe7d6bf053e7p177a78jsnfdf4efc4eeca",
        "X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return float(response.json().get("price"))


def get_earning_dates(symbol):

    url = DBConfig().earning_date_api
    querystring = {"symbol": symbol}
    headers = {
        "X-RapidAPI-Key": "94c0a913b8mshd15fe7d6bf053e7p177a78jsnfdf4efc4eeca",
        "X-RapidAPI-Host": "mboum-finance.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)

    return response.json()


def final_1(symbol):
    try:
        print("-", end=" ")
        symbol = symbol.strip()
        time.sleep(1)
        exp_date = get_options_expirations(symbol=symbol).get("dates", None)
        if exp_date is None:
            return {"error": f"No data exp_date {get_options_expirations(symbol=symbol)}"}

        exp_date = [datetime.datetime.strptime(f"{d} 00:00:00", "%Y-%m-%d  %H:%M:%S") for d in exp_date]

        if len(exp_date) == 0:
            return {"error": f"No data exp_date {exp_date}"}

        recent_date = get_current_date(timezone="GMT").replace(tzinfo=None)
        second_date = [date
                       for date in exp_date
                       if date >= (recent_date + datetime.timedelta(3, 0))
                       # and date < (recent_date + datetime.timedelta(10, 0))
                       ]
        if len(second_date) == 0:
            return {"error": f"No weekly data missing second_date{exp_date}"}

        timestamp = convert_date_to_timestamp_with_zone(timezone="GMT", date=second_date[0])
        time.sleep(1)
        symbol_m_price = get_option_price(symbol=symbol)
        time.sleep(1)
        second_date = second_date[0]
        option_chain = get_option_chain(symbol=symbol, date=f"{timestamp}")
        calls = option_chain['body'][0]['options'][0]["calls"] if option_chain['body'] else []
        puts = option_chain['body'][0]['options'][0]["puts"] if option_chain['body'] else []
        get_call_above_price_list = [call for call in calls if call["strike"] > symbol_m_price]
        get_put_below_price_list = [put for put in puts if put["strike"] <= symbol_m_price]

        filtered_get_put_below_price_list = filter_properties(get_put_below_price_list, market_price=symbol_m_price, suffix_properties="put")
        filtered_get_call_above_price_list = filter_properties(get_call_above_price_list, market_price=symbol_m_price)
        final_call_put_price_list = dict(filtered_get_put_below_price_list, **filtered_get_call_above_price_list)
        
        extra_col = {"datetime": second_date, "date": second_date.date(), "ticker": symbol, "market_price": symbol_m_price, "is_weekly_data_available": True,
                     "exp_date": second_date}
        final_price_list = dict(final_call_put_price_list, **extra_col)
        if len(final_price_list.keys()) == 76:
            print(symbol, end="  ")
    except Exception as e:
        return {"error": f"error {e}"}
    return final_price_list

