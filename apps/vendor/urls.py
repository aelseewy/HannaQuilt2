from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('become_vendor/', views.become_vendor, name="become_vendor"),
    path('vendor_admin/', views.vendor_admin, name="vendor_admin"),
    path('add-product/', views.add_product, name='add_product'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='vendor/login.html'), name='login'),
    path('myinquiries/', views.myinquiries, name="myinquiries"),
    path('inquiry', views.inquiry1, name="inquiry1"),
    path('send_reply/', views.send_reply, name="send_reply")
]
