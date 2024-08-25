from django.db import models

# Create your models here.
# bfhl_app/models.py

class ProcessedData(models.Model):
    user_id = models.CharField(max_length=20)
    numbers = models.CharField(max_length=100)
    alphabets = models.CharField(max_length=100)
    lowest_lowercase_alphabet = models.CharField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
