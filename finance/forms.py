from django import forms
from .models import Plan, Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['category','amount','description']

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['name','budget','description',]


class EditTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['category','amount', 'description']

