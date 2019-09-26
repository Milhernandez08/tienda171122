from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.sales.models import Sale
from apps.sales.serializers import SaleSerializers
#from Sales.serializers import ProductsSerializers

class SalesList(APIView):
    def get(self, request, format=None):
        queryset = Sale.objects.all()
        serializer = SaleSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = SaleSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class SalesDetail(APIView):
    def get_object(self, id):
        try:
            return Sale.objects.get(pk=id)
        except Sale.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = SaleSerializers(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        Sale.objects.get(pk=id)
        return Response("Success")
    
    def put(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = SaleSerializers(example, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)