from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.user_detail, name='detail'),
    path('edit/', views.user_edit, name='edit'),
]
