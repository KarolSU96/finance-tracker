from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Plan(models.Model):
    name = models.CharField(max_length=20, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=20, unique=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name

    # total_spent calculated the total spent by summing up all transaction amounts
    # using the "aggregate" method
    @property
    def total_spent(self):
        return self.transaction_set.aggregate(models.Sum('amount'))['amount__sum'] or 0


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Transaction(models.Model):
    plan = models.ForeignKey(
        Plan, null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.plan.user.username} - {self.plan.name} - {self.category.name} - €{self.amount} - {self.date.strftime('%Y-%m-%d')} "
    
    # Update total_spent in Plan model when saving a new transaction
    def save_amount(self, *args, **kwargs):
        self.plan.total_spent += self.amount
        self.plan.save()

        super().save(*args,**kwargs)