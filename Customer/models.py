from django.db import models

class Customer(models.Model):
    Name = models.CharField(max_length = 100)
    Age = models.SmallIntegerField()


    def __str__(self) -> str:
        return f'{self.Name} age is {self.Age}'

    class Meta:
        ordering = ['Name']
        verbose_name_plural = 'Customer'