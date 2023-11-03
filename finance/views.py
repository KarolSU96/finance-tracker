from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views import generic, View
from .models import Plan, Transaction
from .forms import TransactionForm


class PlanList(generic.ListView):
    model = Plan
    queryset = Plan.objects
    template_name ='home.html'
    paginate_by = 22

    def get_queryset(self):
        return Plan.objects.all()

class PlanDetail(View):
    template_name = 'plan_details.html'
    
    # Handles GET requests for displaying plan details, transactions, and
    # transaction form. Renders the plan details template with relevant context.
    def get(self, request, slug, *args, ** kwargs):
        queryset = Plan.objects.all()
        plan = get_object_or_404(queryset, slug=slug)
        plan.remaining = plan.budget - plan.total_spent
        transactions = Transaction.objects.filter(plan=plan)
        form = TransactionForm()

        context = {
            'plan': plan,
            'transactions': transactions,
            'form': form,
        }

        return render(request, self.template_name, context)
    
    # Handles the POST requests for ading a new transaction to the plan. 
    # If form is valid, add a new transaction. To the plan and redirects To
    # plan_details.
    def post(self, request, slug, *args, **kwargs):
            queryset = Plan.objects.all()
            plan = get_object_or_404(queryset, slug=slug)
            plan.remaining = plan.budget - plan.total_spent
            transactions = Transaction.objects.filter(plan=plan)

            form = TransactionForm(request.POST)

            if form.is_valid():
                transaction = form.save(commit=False)
                transaction.plan = plan
                transaction.save()
                return redirect('plan_detail', slug=slug)

            # Check if delete button is clicked, if it is, delete marked transactions
            if 'delete_transactions' in request.POST:
                transaction_ids = request.POST.getlist('transaction_ids')

                if transaction_ids:
                    Transaction.objects.filter(id__in=transaction_ids).delete()

                return redirect('plan_detail', slug=slug)

            context = {
                'plan': plan,
                'transactions': transactions,
                'form': form,
            }

            return render(request, self.template_name, context)

class Register(View):
    template_name = 'register.html'