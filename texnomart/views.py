from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from texnomart.models import Product, Category
from texnomart.serializers import ProductSerializer, CategoryModelSerializer


# product
class ProductListApiView(ListAPIView):
    permission_classes = (AllowAny,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = ProductSerializer

    @method_decorator(cache_page(15))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def get_queryset(self):
        return Product.objects.select_related('category').prefetch_related('comments', 'product_images', 'product_attributes')


class ProductDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    model = Product
    serializer_class = ProductSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset


class ProductAdd(generics.CreateAPIView):
    permission_classes = [AllowAny]
    model = Product
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset


class ProductChange(generics.UpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset


class ProductDelete(generics.DestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset


# category
class CategoryListApiView(ListAPIView):
    permission_classes = (AllowAny,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = CategoryModelSerializer

    def get_queryset(self):
        return Category.objects.all()


class CategoryDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    model = Category
    serializer_class = CategoryModelSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset


class CategoryAdd(generics.CreateAPIView):
    permission_classes = [AllowAny]
    model = Category
    serializer_class = CategoryModelSerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset


class CategoryChange(generics.UpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CategoryModelSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset


class CategoryDelete(generics.DestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = CategoryModelSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset