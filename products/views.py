from django.shortcuts import render
from .models import Category, Product
from .serializer import CategorySerializer, ProductSerializer
from  rest_framework import generics, permissions, viewsets, filters


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

   