import pytz
import datetime


def extract_date_fn(date_str):
    d2 = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S").date()
    return d2


def get_current_date(timezone="IST"):
    utc_now = datetime.datetime.utcnow()
    gmt = pytz.timezone(timezone)
    gmt_now = utc_now.replace(tzinfo=pytz.utc).astimezone(gmt)
    today_datetime = gmt_now.replace(hour=0, minute=0, second=0, microsecond=0)
    return today_datetime

def filter_properties(list_val, market_price, suffix_properties="call"):
    output_list = {}
    suffix = ""
    list_length = min(len(list_val), 5)
    if suffix_properties == "call":
        list_val = list_val[:5]
    else:
        list_val = list_val[-5:]


def filter_properties(list_val, market_price, suffix_properties="call"):
    output_list = {}
    suffix = ""

    if suffix_properties == "call":
        list_val = list_val[:5]
    else:
        list_val = list_val[-5:]
    list_length = len(list_val)

    for idx in range(1, 6):

        if idx <= list_length:
            val = list_val[idx - 1]
            strike = int(val.get("strike", 0))
            last_trade_date = val.get("last_trade_date", 0)
            bid = val.get("bid", 0)
            ask = val.get("ask", 0)
            volume = val.get("volume", None)
            implied_volatility = val.get("implied_volatility", None)
            in_the_money = val.get("in_the_money", None)

            avg_market_price = round((bid + ask) / 2 * 100, 2)
            mid_percent = round(((bid + ask) / 2) * 100 / market_price, 2)
        else:
            strike = last_trade_date = bid = ask = volume = implied_volatility = in_the_money = 0
            avg_market_price = mid_percent = None

        if suffix_properties != "call":
            idx = 6 - idx
        output_list.update({
            f"{suffix_properties}_l{idx}_strikeprice": strike,
            f"{suffix_properties}_l{idx}_last_trade_date": last_trade_date,
            f"{suffix_properties}_l{idx}_avg_bid_ask": avg_market_price,
            f"{suffix_properties}_l{idx}_mid_percent": mid_percent,
            f"{suffix_properties}_l{idx}_volume": volume,
            f"{suffix_properties}_l{idx}_implied_volatility": implied_volatility,
            f"{suffix_properties}_l{idx}_in_the_money": in_the_money
        })
    return output_list


def convert_date_to_timestamp_with_zone(date, timezone="GMT"):
    target_timezone = pytz.timezone(timezone)
    localized_datetime = target_timezone.localize(date)
    timestamp = int(localized_datetime.timestamp())
    return timestamp


