from django.shortcuts import render, HttpResponse
from django.views import generic
from .models import Plan


class PlanList(generic.ListView):
    model = Plan
    queryset = Plan.objects
    template_name ='home.html'
    paginate_by = 22

    def get_queryset(self):
        return Plan.objects.all()