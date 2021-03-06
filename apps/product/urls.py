from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('gallery/', views.gallery, name='gallery'),
    path('photo/<int:pk>/', views.viewPhoto, name='photo'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product, name='product'),
    path('<slug:category_slug>/', views.category, name='category')
]