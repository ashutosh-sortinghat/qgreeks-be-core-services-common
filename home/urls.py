from . import views #ListBooks, list_accounts
from django.urls import path, include
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('qg/insert/tickers/', views.insert_symbols, name='insert tickers'),
    path('insights/stats/', views.get_insight_state, name='stats')

    ]
