from typing import Any
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime, timedelta

from .services.symbol_processing import process_symbols_and_insert, get_tickers_name
from .services.option_activity_service import get_option_activity
from .config.config import connect_to_database



@api_view(['GET'])
def insert_symbols(request):

    symbols_250_list = get_tickers_name()
    print(len(symbols_250_list))
    conn = connect_to_database()
    failed_to_process, failed_to_insert, insert_sym_dict, output =  process_symbols_and_insert(
        conn, symbols_250_list)
    print("----------------------", len(output), len(failed_to_insert), len(failed_to_process), output)
    if failed_to_process or failed_to_insert:
        fail_symbol = failed_to_process + failed_to_insert
        failed_to_process, failed_to_insert, insert_sym_dict, output = process_symbols_and_insert(
            conn, fail_symbol)
        print("----------------------", len(output), len(failed_to_insert), len(failed_to_process), output)

    conn.close()
    return Response({"requst": f"inserted successfully{failed_to_process}, {failed_to_insert}, {output}"})
 

@api_view(['GET'])
def get_insight_state(request):
    
    account_id = request.query_params.get('account_id')
    account_id = account_id if account_id else "b1b17b57-bfca-4d09-ae37-a0a5529e0221"
    start_date_str = request.query_params.get('startdate')
    end_date_str = request.query_params.get('enddate')

    start_date = (datetime.strptime(start_date_str, "%Y-%m-%d").date() 
                    if start_date_str else datetime.now().date() - timedelta(days=7))
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date() if end_date_str else datetime.now().date()
    
    
    activity_logs = get_option_activity(start_date, end_date)
    if "status" in activity_logs:
        return Response(activity_logs)
    
    # print(start_date, str(end_date))
    # end_date = end_date - timedelta(days=1)
    filtered_logs_today = [log for log in activity_logs 
                           if log.get("create_date", "")[:10] == str(end_date)
                           and log.get("filled_qty", 0.0) not in ['string', None]
                           and log.get("net_credit", 0.0) not in ['string', None]]
    
    total_contracts_today = sum(float(log.get("filled_qty", 0.0)) for log in filtered_logs_today)
    total_premium_today = sum(float(log.get("net_credit", 0.0)) for log in filtered_logs_today)
    total_contracts_week = sum(float(log.get("filled_qty", 0.0))
                               for log in activity_logs 
                               if log.get("filled_qty", 0.0) not in ['string', None])
    total_premium_week = sum(float(log.get("net_credit", 0.0))
                             for log in activity_logs 
                             if log.get("net_credit", 0.0) not in ['string', None])
    
    return Response({
        "total_contracts_today": total_contracts_today,
        "total_contracts_week": total_contracts_week,
        "total_premium_today": total_premium_today,
        "total_premium_week": total_premium_week
    })

