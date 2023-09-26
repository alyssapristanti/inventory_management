# Create your models here.
from django.contrib.auth.models import User
from django.db import models

CATEGORY_CHOICES = [
    ('Office Supplies', 'Office Supplies'),
    ('Electronics', 'Electronics'),
    ('Furniture', 'Furniture'),
]


class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default='Category 1')
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
