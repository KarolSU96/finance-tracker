from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views import generic, View
from .models import Plan


class PlanList(generic.ListView):
    model = Plan
    queryset = Plan.objects
    template_name ='home.html'
    paginate_by = 22

    def get_queryset(self):
        return Plan.objects.all()

class PlanDetail(View):

    def get(self, request, slug, *args, ** kwargs):
        queryset = Plan.objects
        plan = get_object_or_404(queryse, slug=slug)
        

