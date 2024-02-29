import datetime
import time
import math
import uuid
import psycopg2

from .utils import extract_date_fn, get_current_date
from .api_services import get_earning_dates, final_1
from ..config.config import connect_to_database



def insert_row(data_dict, conn):
    # Create the qt_stock_screener table
    earning_date = get_earning_dates(data_dict["ticker"])
    if "body" in earning_date:
        try:
            earning_date = earning_date["body"]["earnings"]["earningsChart"]["earningsDate"][0]["fmt"]
            earning_date = datetime.datetime.strptime(
                f"{earning_date} 00:00:00", "%Y-%m-%d  %H:%M:%S")
            is_earnings_within_2w = (True
                                     if earning_date < get_current_date(
                                         timezone="GMT").replace(tzinfo=None) + datetime.timedelta(15, 0)
                                     else False)
        except:
            earning_date = None
            is_earnings_within_2w = False
    else:
        earning_date = None
        is_earnings_within_2w = False

    try:

        with conn.cursor() as cursor:
            uuid_value = str(uuid.uuid4())
            cursor.execute("""
                INSERT INTO public.stock_screener (
                    stock_screener_id, run_date, ticker, market_price, exp_date, upcoming_earnings_date, is_earnings_within_2w,
                    put_l1_strikeprice, put_l1_mid_percent, put_l1_mid_price, put_l1_volume,
                    put_l2_strikeprice, put_l2_mid_percent, put_l2_mid_price, put_l2_volume,
                    put_l3_strikeprice, put_l3_mid_percent, put_l3_mid_price, put_l3_volume,
                    put_l4_strikeprice, put_l4_mid_percent, put_l4_mid_price, put_l4_volume,
                    put_l5_strikeprice, put_l5_mid_percent, put_l5_mid_price, put_l5_volume,
                    call_l1_strikeprice, call_l1_mid_percent, call_l1_mid_price, call_l1_volume,
                    call_l2_strikeprice, call_l2_mid_percent, call_l2_mid_price, call_l2_volume,
                    call_l3_strikeprice, call_l3_mid_percent, call_l3_mid_price, call_l3_volume,
                    call_l4_strikeprice, call_l4_mid_percent, call_l4_mid_price, call_l4_volume,
                    call_l5_strikeprice, call_l5_mid_percent, call_l5_mid_price, call_l5_volume,
                    create_date, update_date
                )
                VALUES (
                    %(uuid_value)s, CURRENT_TIMESTAMP, %(ticker)s, %(market_price)s, %(exp_date)s, %(upcoming_earnings_date)s, %(is_earnings_within_2w)s,
                    %(put_l1_strikeprice)s, %(put_l1_mid_percent)s, %(put_l1_avg_bid_ask)s, %(put_l1_volume)s,
                    %(put_l2_strikeprice)s, %(put_l2_mid_percent)s, %(put_l2_avg_bid_ask)s, %(put_l2_volume)s,
                    %(put_l3_strikeprice)s, %(put_l3_mid_percent)s, %(put_l3_avg_bid_ask)s, %(put_l3_volume)s,
                    %(put_l4_strikeprice)s, %(put_l4_mid_percent)s, %(put_l4_avg_bid_ask)s, %(put_l4_volume)s,
                    %(put_l5_strikeprice)s, %(put_l5_mid_percent)s, %(put_l5_avg_bid_ask)s, %(put_l5_volume)s,
                    %(call_l1_strikeprice)s, %(call_l1_mid_percent)s, %(call_l1_avg_bid_ask)s, %(call_l1_volume)s,
                    %(call_l2_strikeprice)s, %(call_l2_mid_percent)s, %(call_l2_avg_bid_ask)s, %(call_l2_volume)s,
                    %(call_l3_strikeprice)s, %(call_l3_mid_percent)s, %(call_l3_avg_bid_ask)s, %(call_l3_volume)s,
                    %(call_l4_strikeprice)s, %(call_l4_mid_percent)s, %(call_l4_avg_bid_ask)s, %(call_l4_volume)s,
                    %(call_l5_strikeprice)s, %(call_l5_mid_percent)s, %(call_l5_avg_bid_ask)s, %(call_l5_volume)s,
                    now(), now()
                )
            """, {
                'uuid_value': uuid_value,
                'is_earnings_within_2w': is_earnings_within_2w,
                "upcoming_earnings_date": earning_date,
                **data_dict
            })
            query = cursor.query
        conn.commit()

    except Exception as e:
        return {"status": False, "output": f"Error {e}"}

    return {"status": True, "output": "inserted successfully;", "query": query}

def process_symbol(sym):
    final_dict = {
        "status": False,
        "json_output": {},
        "error": ""
    }
    try:
        symbol_details = final_1(symbol=sym)

        if len(symbol_details.keys()) >70:
            pass
        else:
            if len(symbol_details.keys()) == 3:
                final_dict["error"] = f" Api Failed. {sym} {symbol_details}"
            else:
                final_dict["error"] = f"Skipping symbol {sym} due to {symbol_details.get('error')}"

    except Exception as e:
        final_dict["error"] = f"Error processing symbol {sym}: {e}"

    if len(final_dict["error"]) == 0:
        final_dict["status"] = True
        final_dict["json_output"] = symbol_details
    else:
        final_dict["status"] = False

    return final_dict


def insert_dataframe_row(conn, json_obj):
    row = json_obj
    row2 = {key: None if isinstance(value, float) and math.isnan(
        value) else value for key, value in row.items()}
    output = insert_row(data_dict=row2, conn=conn)
    return output


def process_symbols_and_insert(conn, symbols_list):
    failed_to_process = []
    failed_to_insert = []
    insert_sym_dict = []
    error_output = []
    for i, sym in enumerate(symbols_list):
        print(i, end=": ")
        output = process_symbol(sym)
        if output["status"] != True or len(output["json_output"].keys()) != 76:
            time.sleep(6)
            output = process_symbol(sym)
            if output["status"] != True or len(output["json_output"].keys()) != 76:
                time.sleep(6)
                output = process_symbol(sym)
                
        time.sleep(6)
        if output["status"] == True and len(output["json_output"].keys()) == 76:
            o2 = insert_dataframe_row(conn, output.get("json_output"))
            # insert_sym_dict.append(output.get("json_output"))
            if o2.get("status") != True:
                failed_to_insert.append(sym)
                output["error"] = f"failed to insert - {o2}"
                print(f" Insert err- {o2}")
                
        else:
            failed_to_process.append(sym)
            output["error"] += f"failed to proceed - {len(output['json_output'].keys())}"
        if "error" in output:
            if len(output["error"])!=0:
                # print(f"error in {sym} {output["error"]}")
                error_output.append(output["error"])

    return failed_to_process, failed_to_insert, insert_sym_dict, error_output




def get_tickers_name():


    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("SELECT ticker FROM stock_details")
    rows = cur.fetchall()
    tickers_list = [row[0] for row in rows]
    conn.close()

    return tickers_list
