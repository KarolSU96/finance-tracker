from django import forms
from .models import Plan, Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['category','amount','description']