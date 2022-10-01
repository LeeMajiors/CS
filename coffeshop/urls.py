from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login_view, name="login"),
    path('register', views.register_view, name="register"),
    path('logout', views.logout_view, name='logout'),
    path('test_register',views.test_register, name='test_register'),
    path('order', views.order, name='order'),
]