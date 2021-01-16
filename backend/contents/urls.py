from django.urls import path
from . import views

app_name = 'contents'

urlpatterns = [
    path('', views.content_list_create),
    path('<int:content_pk>/', views.content_update_delete),
    path('detail/<int:content_pk>/', views.content_detail),
]
