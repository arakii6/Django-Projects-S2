from django.db import models
from Customer.models import *

class Purchase(models.Model):
    Amount = models.DecimalField(max_digits=5, decimal_places=2)
    FK = models.ForeignKey(Customer, related_name = 'CP', on_delete=models.CASCADE, verbose_name='Customer')


    def __str__(self) -> str:
        return f'{self.FK.Name} spend {self.Amount}'
    

    class Meta:
        ordering = ['Amount']
        verbose_name_plural = 'Purchase'