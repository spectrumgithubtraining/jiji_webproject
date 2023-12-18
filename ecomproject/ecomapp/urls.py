
from django.urls import path
from .views import index,product_view

from . import views

urlpatterns = [
    path('', index, name='index'),
     path('login/', views.login_view, name='login'),
    path('forgotpassword/', views.forgot_password_view, name='forgot_password'),
    path('signup/', views.signup_view, name='signup'),
    path('product/', views.product_view, name='product'), 
]