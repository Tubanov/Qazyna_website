from django.urls import path
from . import views
from .views import LoginUser, logout_user

app_name = 'login'

urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
    path('add/', views.add, name='add'),
    path('logout/', logout_user, name='logout'),
]