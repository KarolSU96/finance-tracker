from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Plan(models.Model):
    name = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

class Transaction(models.Model):
    plan = models.ForeignKey(Plan, null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering= ['-created_on']

    def __str__(self):
        return f"{self.plan.user.username} - {self.plan.name} - {self.category.name} - €{self.amount} - {self.date.strftime('%Y-%m-%d')} "