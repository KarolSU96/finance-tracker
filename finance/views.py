from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views import generic, View
from .models import Plan, Transaction


class PlanList(generic.ListView):
    model = Plan
    queryset = Plan.objects
    template_name ='home.html'
    paginate_by = 22

    def get_queryset(self):
        return Plan.objects.all()

class PlanDetail(View):
    template_name = 'plan_details.html'
    def get(self, request, slug, *args, ** kwargs):
        queryset = Plan.objects.all()
        plan = get_object_or_404(queryset, slug=slug)
        plan.remaining = plan.budget - plan.total_spent
        transactions = Transaction.objects.filter(plan=plan)

        context= {
            'plan': plan,
            'transactions': transactions,
        }

        return render(request, self.template_name, context)
        
