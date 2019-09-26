from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.transactions.models import Transaction
from apps.transactions.serializers import TransactionSerializers
#from Products.serializers import ProductsSerializers


class TransactionsList(APIView):
    def get(self, request, format=None):
        queryset = Transaction.objects.all()
        serializer = TransactionSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = TransactionSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)