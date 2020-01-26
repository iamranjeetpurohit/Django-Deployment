from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('register/$',views.register,name='register'),
    path('special/$',views.special,name='special'),
    path('user_login/$',views.user_login,name='user_login')
]
