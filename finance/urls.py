from . import views
from django.urls import path

urlpatterns = [
    path('', views.PlanList.as_view(), name ='home'),
    path('add_plan/', views.AddPlan.as_view(), name='add_plan'),
    path('<slug:slug>/', views.PlanDetail.as_view(), name ='plan_detail'),
    path('<slug:slug>/edit_transaction/<int:transaction_id>/', views.EditTransaction.as_view(), name='edit_transaction'),
]
