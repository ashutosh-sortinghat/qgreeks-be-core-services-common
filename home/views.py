from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin, ListModelMixin
from typing import Any
from rest_framework import permissions, viewsets, generics, mixins
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_204_NO_CONTENT
from rest_framework.decorators import api_view
from datetime import datetime, timedelta
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
from rest_framework.decorators import action

from .services.stockscreener_services import process_symbols_and_insert, get_tickers_name
from .services.qtoptiondatastats_services import get_option_activity
from .config.config import connect_to_database
from home.serializers import StockDetailsSerializer, StockScreenerSerializer
from .models import StockDetails, StockScreener
from home.services.chatbotapi_services import Conversation


conversation_instance = Conversation()

@api_view(['POST'])
def insert_symbols(request):

    symbols_list = get_tickers_name()
    print(len(symbols_list))
    conn = connect_to_database()
    failed_to_process, failed_to_insert, \
    insert_sym_dict, output =  process_symbols_and_insert(conn, symbols_list)
    print("\n ----------------------", len(output), len(failed_to_insert), len(failed_to_process), output)
    conn.close()

    return Response({"requst": f"inserted successfully{failed_to_process}, {failed_to_insert}, {output}"})
 

@api_view(['GET'])
def get_insight_state(request, account_id):
    
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
    
    total_contracts_today = round(sum(float(log.get("filled_qty", 0.0)) for log in filtered_logs_today), 2)
    total_premium_today = round(sum(float(log.get("net_credit", 0.0)) for log in filtered_logs_today), 2)
    total_contracts_week = round(
                                sum(float(log.get("filled_qty", 0.0))
                                        for log in activity_logs 
                                        if log.get("filled_qty", 0.0) not in ['string', None])
                                , 2)
    total_premium_week = round(
                                sum(float(log.get("net_credit", 0.0))
                                    for log in activity_logs 
                                    if log.get("net_credit", 0.0) not in ['string', None])
                                , 2)
    
    return Response({
        "total_contracts_today": total_contracts_today,
        "total_contracts_week": total_contracts_week,
        "total_premium_today": total_premium_today,
        "total_premium_week": total_premium_week
    })


@api_view(['POST'])
def generate_response(request):
    try:
        question = request.query_params.get('question')
        if question ==None:
            print("question not found")
            question = "Hii"
        answer = conversation_instance.send_message(question)
        return Response({"Question": question, "Answer": answer})
    except Exception as e:
        return Response(status=HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)})


 
class StockDetailsViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = StockDetails.objects.all()
    serializer_class = StockDetailsSerializer
    
    @action(detail=True, methods=['get'], url_path="(?P<tickerName>[^/.]+)/search/ticker")
    def search(self, request, pk=None, tickerName=None):
        try:
            # print("---------------------ran", pk, tickerName)
            tickerNameList = [ticker.strip() for ticker in tickerName.split(",")]
            details = StockDetails.objects.all().filter(ticker__in=tickerNameList)

            st_serializer = StockDetailsSerializer(details,  many=True,context={'request': request})
            if len(st_serializer.data)==0:
                return Response({'message': 'stock might not exists !! Error'})
            return Response(st_serializer.data)
        
        except Exception as e:
            print(e)
            return Response({
                'message': 'stock might not exists !! Error'
            })


class StockScreenerViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = StockScreener.objects.all()
    serializer_class = StockScreenerSerializer
    

    # @action(detail=True, methods=['get'], url_path="(?P<tickerName>[^/.]+)/search/ticker")
    # def search(self, request, pk=None, tickerName=None):
    #     try:
    #         # print("---------------------ran", pk, tickerName)
    #         tickerNameList = [ticker.strip()
    #                           for ticker in tickerName.split(",")]
    #         details = StockScreener.objects.all().filter(ticker__in=tickerNameList)
    #         st_serializer = StockScreenerSerializer(
    #             details,  many=True, context={'request': request})
    #         if len(st_serializer.data) == 0:
    #             return Response({'message': 'stock might not exists !! Error'})
    #         return Response(st_serializer.data)

    #     except Exception as e:
    #         print(e)
    #         return Response({
    #             'message': 'stock might not exists !! Error'
    #         })



# class StockList(generics.ListCreateAPIView):
#     queryset = StockScreener.objects.all()
#     serializer_class = StockScreenerSerializer
#     # permission_classes = [IsAdminUser]
#     lookup_field = 'pk' 
#     def list(self, request):
#         # Note the use of `get_queryset()` instead of `self.queryset`
#         queryset = self.get_queryset()
#         serializer = StockScreenerSerializer(queryset, context=serializer_context, many=True)
#         return Response(serializer.data)
    
#     # @action
#     # def create(self, request):
#     #     print("----------------------got")
#     #     return Response("not")


# class MyModelUpdateView(GenericAPIView, UpdateModelMixin, ListModelMixin):
#     queryset = StockScreener.objects.all()
#     serializer_class = StockScreenerSerializer
#     lookup_field = 'pk'

#     def list(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def perform_update(self, serializer):
#         # Add additional logic before updating the object
#         instance = serializer.save()
#         return Response("none")

#     # def get_extra_actions(self):
#     #     return {}