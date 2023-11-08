from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# pylint: disable=no-member


class Plan(models.Model):
    """
    Represents a financial plan created by a user.
    """
    name = models.CharField(max_length=20, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name

    """
    total_spent calculated the total spent by summing up all transaction
    amounts
    using the "aggregate" method
    """
    @property
    def total_spent(self):
        """
        Calculates the total amount spent in the plan.
        """
        return (self.transaction_set
                .aggregate(models.Sum('amount'))['amount__sum'] or 0)


class Category(models.Model):
    """
    Represents a category for transactions.
    """
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Transaction(models.Model):
    """
    Represents a financial transaction associated with a plan and category.
    """
    plan = models.ForeignKey(
        Plan, null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return (
            f'{self.plan.user.username} - '
            f'{self.plan.name} - '
            f'{self.category.name} - '
            f'€{self.amount} - '
            f'{self.date.strftime("%Y-%m-%d")} '
        )

    def save_amount(self, *args, **kwargs):
        """
        Update the total spent in the associated plan when saving a new
        transaction.
        """
        self.plan.total_spent += self.amount
        self.plan.save()

        super().save(*args, **kwargs)
