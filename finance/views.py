from django.shortcuts import render, HttpResponse

# Create your views here.


def get_finance(request):
    return render(request, "finance/finance_list.html")
