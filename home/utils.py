from rest_framework import viewsets
from .models import StockDetails
from .serializers import ProductSerializer
from rest_framework.generics import RetrieveAPIView, ListAPIView
from django.http import HttpResponse
from rest_framework import status

import pandas as pd

# class GetMethod(viewsets.ModelViewSet):
#     pass
#     queryset = Account.objects.all()
#     serializer_class = ProductSerializer

#     # def list(self, request, *args, **kwargs):
#     #     data = list(Account.objects.all().values())
#     #     return Response(data)

#     # def retrieve(self, request, *args, **kwargs):
#     #     data = list(Account.objects.filter(id=kwargs['pk']).values())
#     #     return Response(data)

#     # def create(self, request, *args, **kwargs):
#     #     product_serializer_data = ProductSerializer(data=request.data)
#     #     if product_serializer_data.is_valid():
#     #         product_serializer_data.save()
#     #         status_code = status.HTTP_201_CREATED
#     #         return Response({"message": "Product Added Sucessfully", "status": status_code})
#     #     else:
#     #         status_code = status.HTTP_400_BAD_REQUEST
#     #         return Response({"message": "please fill the datails", "status": status_code})

#     # def destroy(self, request, *args, **kwargs):
#     #     product_data = Account.objects.filter(id=kwargs['pk'])
#     #     if product_data:
#     #         product_data.delete()
#     #         status_code = status.HTTP_201_CREATED
#     #         return Response({"message": "Product delete Sucessfully", "status": status_code})
#     #     else:
#     #         status_code = status.HTTP_400_BAD_REQUEST
#     #         return Response({"message": "Product data not found", "status": status_code})

#     # def update(self, request, *args, **kwargs):
#     #     product_details = Account.objects.get(id=kwargs['pk'])
#     #     product_serializer_data = ProductSerializer(
#     #         product_details, data=request.data, partial=True)
#     #     if product_serializer_data.is_valid():
#     #         product_serializer_data.save()
#     #         status_code = status.HTTP_201_CREATED
#     #         return Response({"message": "Product Update Sucessfully", "status": status_code})
#     #     else:
#     #         status_code = status.HTTP_400_BAD_REQUEST
#     #         return Response({"message": "Product data Not found", "status": status_code})
