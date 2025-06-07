from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

from .models import Product
from .serializers import ProductSerializer

class ProductPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 100

class ProductFilter(filters.FilterSet):
    # simple text filters
    name = filters.CharFilter(lookup_expr='icontains')
    seller = filters.CharFilter(lookup_expr='icontains')
    tags = filters.CharFilter(lookup_expr='icontains')
    type = filters.CharFilter(lookup_expr='icontains')
    
    # price range filters
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    
    # exact match filters
    category = filters.ChoiceFilter(choices=[('clothing', 'Clothing'), ('rsvp', 'RSVP')])
    color = filters.CharFilter(lookup_expr='iexact')
    size = filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Product
        fields = ['name', 'seller', 'tags', 'type', 'category', 'color', 'size']

class ListProductView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = ProductPagination
    
    search_fields = ['name', 'description', 'tags', 'seller', 'type']
    
    ordering_fields = ['name', 'price', 'created_at', 'seller']
    ordering = ['-created_at']

class RetrieveProductView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer