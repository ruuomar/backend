from django.urls import path, include
from . import views
urlpatterns = [
path('api/v1/Job', views.insertJob),
path('api/v1/getJob', views.getJob),
path('api/v1/updateJob/<JId>/', views.updateJob),
path('api/v1/deleteJob/<AId>/',views.deleteJob),

path('api/v1/insertApplicant' , views.insertApplicant),
path('api/v1/getApplicant', views.getApplicant),
path('api/v1/updateApplicant/<AId>/', views.updateApplicant),
path('api/v1/deleteapplicant/<AId>/',views.deleteapplicant),

path('api/v1/insertAppJob',views.insertAppJob),
path('api/v1/getAppJob',views.getAppJob),
path('api/v1/updateAppJob/<id>/',views.updateAppJob),
path('byid/<id>/', views.getbyid),
path('api/v1/deleteAppJob/<id>/',views.deleteAppJob)

]

