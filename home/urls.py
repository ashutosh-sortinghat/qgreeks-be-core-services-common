from . import views #ListBooks, list_accounts
from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'stock_details', views.StockDetailsViewSet)
router.register(r'stock_screener', views.StockScreenerViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('qg/insert/tickers/', views.insert_symbols, name='insert_tickers'),
    path('insights/stats/', views.get_insight_state, name='stats'),
    path('bot/generate-response/', views.generate_response, name="Chatbot")

    ]
# urlpatterns += [
#     path('stock_screener/<stock_screener_id>/', views.StockScreenerViewSet.as_view({
#          'get': 'retrieve',
#          'put': 'update',
#          'patch': 'partial_update',
#          }), name="stock_screener-detail"),
#     path('stock_screener/', views.StockScreenerViewSet.as_view({
#         'get': 'list',
#         'post': 'create',
#     }), name="stock_screener-list"),
#     path('stock_screener/<int:pk>/search/ticker/',
#             views.StockScreenerViewSet.as_view({'get': 'search'}),
#          name='stock_screener-search')
# ]
