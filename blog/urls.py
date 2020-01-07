from django.urls import path
from . import views

urlpatterns = [ #nosso primeiro padrão de urls
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]