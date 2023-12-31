from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Plan, Transaction
from .forms import TransactionForm, PlanForm, EditTransactionForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# pylint: disable=no-member


class PlanList(generic.ListView):
    """View for listing plans."""

    model = Plan
    queryset = Plan.objects
    template_name = 'index.html'
    paginate_by = 22

    """ Handles POST requests for deleting the plans."""
    def post(self, request, *args, **kwargs):

        if 'delete_plans' in request.POST:
            plans_ids = request.POST.getlist('plans_ids')

            if plans_ids:
                Plan.objects.filter(id__in=plans_ids).delete()

            messages.success(request, 'Plan(s) deleted successfully! ')
            return redirect('home')

    """Returns the queryset for listing plans."""
    def get_queryset(self):
        return Plan.objects.all()


class PlanDetail(View):
    """View for displaying plan details."""

    template_name = 'plan_details.html'

    """ Handles GET requests for displaying plan details, transactions, and
    transaction form. Renders the plan details template with relevant context.
    """
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

    """ Handles the POST requests for ading a new transaction to the plan.
    If form is valid, add a new transaction. To the plan and redirects To
    plan_details.
    """
    def post(self, request, slug, *args, **kwargs):
        queryset = Plan.objects.all()
        plan = get_object_or_404(queryset, slug=slug)
        plan.remaining = plan.budget - plan.total_spent
        transactions = Transaction.objects.filter(plan=plan)

        form = TransactionForm(request.POST)

        if form.is_valid():
            transaction = form.save(commit=False)

            if transaction.amount > plan.remaining:
                form.add_error(
                    'amount', 'Transaction amount exceeds the plan budget.')
                return render(
                    request,
                    self.template_name,
                    {
                        'plan': plan,
                        'transactions': transactions,
                        'form': form
                    }
                )

            transaction.plan = plan
            transaction.save()
            messages.success(request, 'Transaction added successfully!')
            return redirect('plan_detail', slug=slug)

        # Check if delete button is clicked, if it is,delete marked transaction
        if 'delete_transactions' in request.POST:
            transaction_ids = request.POST.getlist('transaction_ids')

            if transaction_ids:
                Transaction.objects.filter(id__in=transaction_ids).delete()
            messages.success(request, 'Transaction(s) deleted succesfully!')
            return redirect('plan_detail', slug=slug)

        context = {
            'plan': plan,
            'transactions': transactions,
            'form': form,
        }

        return render(request, self.template_name, context)


class AddPlan(LoginRequiredMixin, View):
    """View for adding a new plan."""

    template_name = 'add_plan.html'

    """ Renders the form for adding a new plan """
    def get(self, request, *args, **kwargs):
        form = PlanForm()
        return render(request, self.template_name, {'form': form})

    """ Handles the submission of the form. If the form is valid,
    creates a new plan associated with the current user and redirects to the
    page of the created plan.
    """
    def post(self, request, *args, **kwargs):

        form = PlanForm(request.POST)

        if form.is_valid():
            plan = form.save(commit=False)
            plan.user = request.user

            if not plan.slug:
                plan.slug = plan.name.lower().replace(" ", "-")

            plan.save()
            messages.success(request, 'Plan added successfully')
            return redirect('plan_detail', slug=plan.slug)
        else:
            return render(request, self.template_name, {'form': form})


class EditTransaction(LoginRequiredMixin, View):
    """View for editing transaction."""

    template_name = 'edit_transaction.html'

    """ Retrieves the transaction and associated plan for editing.
    Renders the form for editing the transaction.
    """
    def get(self, request, slug, transaction_id, *args, **kwargs):
        transaction = get_object_or_404(Transaction, id=transaction_id)
        form = EditTransactionForm(instance=transaction)
        plan = transaction.plan
        plan.remaining = plan.budget - plan.total_spent

        context = {
            'form': form,
            'transaction': transaction,
            'plan': plan,
        }

        return render(request, self.template_name, context)

    """ Creates a form instance with the submitted data and the transaction.
    If the form if valid, saves the changes and redirects to plan_detail.
    If the amount is bigger than the remaining money in the plan, displays
    an error message.
    """
    def post(self, request, slug, transaction_id, *args, **kwargs):
        transaction = get_object_or_404(Transaction, id=transaction_id)
        form = EditTransactionForm(request.POST, instance=transaction)
        plan = transaction.plan
        plan_remaining_money = plan.budget - plan.total_spent

        if form.is_valid():
            new_amount = form.cleaned_data['amount']

            if new_amount > plan_remaining_money:
                form.add_error(
                    'amount', 'Transaction amount exceeds the plan budget.')
                context = {
                    'form': form,
                    'slug': slug,
                    'transaction': transaction,
                    'plan': plan,
                }
                return render(request, self.template_name, context)

            form.save()
            messages.success(request, 'Transaction edited successfully!')
            return redirect('plan_detail', slug=slug)

        context = {
            'form': form,
            'slug': slug,
            'transaction_id': transaction_id,
        }

        return render(request, self.template_name, context)
