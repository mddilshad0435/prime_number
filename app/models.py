from django.db import models
from django.conf import settings
# Create your models here.


class PrimeNumber(models.Model):
    ALGORITHM = (
        ('Normal','Normal'),
        ('Optimised','Optimised'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    range = models.CharField(max_length=150)
    time_elapsed = models.FloatField(null=True,blank=True)
    algorithm = models.CharField(max_length=50,choices=ALGORITHM,default="Normal")
    prime_numbers = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

