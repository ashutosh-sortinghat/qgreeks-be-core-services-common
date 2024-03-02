from . import views #ListBooks, list_accounts
from django.urls import path, include
from rest_framework import routers
from home.serializers import StockDetailsSerializer


router = routers.DefaultRouter()
router.register(r'StockDetails', views.StockDetailsViewSet)
# router.register(r'stockScreener', views.StockScreenerViewSet)
screener_viewset_fn = views.StockScreenerViewSet.as_view({
                                            'get': 'list' 
                                            # 'post': 'create',
                                            # 'get': 'retrieve',
                                            # 'put': 'update',
                                            # 'patch': 'partial_update' 
                                            })

urlpatterns = [
    path('', include(router.urls)),
    path('qg/insert/tickers/', views.insert_symbols, name='insert_tickers'),
    path('insights/stats/', views.get_insight_state, name='stats'),
    path('StockScreener/', screener_viewset_fn, name="StockScreener")
    ]
