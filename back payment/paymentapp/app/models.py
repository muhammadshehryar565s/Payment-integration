from django.db import models

# Create your models here.
class Cardpayment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    bill = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
