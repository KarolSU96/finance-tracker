from . import views
from django.urls import path

urlpatterns = [
    path('', views.PlanList.as_view(), name ='home'),
    path('<slug:slug>/', views.PlanDetail.as_view(), name ='plan_detail')
]
