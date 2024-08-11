from django.urls import path

from texnomart import views
from texnomart import auth

urlpatterns = [
    # product
    path('', views.ProductListApiView.as_view(), name='products'),
    path('product-detail/<slug:slug>', views.ProductDetail.as_view(), name='product_detail'),
    path('product-add/', views.ProductAdd.as_view(), name='product_add'),
    path('product-change/<slug:slug>', views.ProductChange.as_view(), name='product_change'),
    path('product-delete/<slug:slug>', views.ProductDelete.as_view(), name='product_delete'),

    # category
    path('category-list/', views.CategoryListApiView.as_view(), name='categories'),
    path('category-detail/<slug:slug>', views.CategoryDetail.as_view(), name='category_detail'),
    path('category-add/', views.CategoryAdd.as_view(), name='category_add'),
    path('category-change/<slug:slug>', views.CategoryChange.as_view(), name='category_change'),
    path('category-delete/<slug:slug>', views.CategoryDelete.as_view(), name='category_delete'),

    # auth
    path("login/", auth.UserLoginAPIView.as_view(), name="user_login"),
    path("register/", auth.UserRegisterAPIView().as_view(), name="user_register"),
    path("logout/", auth.UserLogoutAPIView.as_view(), name="user_logout")
]