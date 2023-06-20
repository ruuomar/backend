from django.urls import path, include
from . import views
urlpatterns = [
path('api/v1/Job', views.insertJob),
path('data/', views.data_view, name='data'),
]

