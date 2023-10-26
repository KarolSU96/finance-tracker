from django.contrib import admin
from .models import Plan, Transaction, Category


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'budget', 'slug', 'created_on')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('created_on',)
    search_fields = ['name']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('plan', 'category', 'amount', 'created_on')
    list_filter = ('created_on',)
    search_fields = ['description', 'category']


admin.site.register(Category)
