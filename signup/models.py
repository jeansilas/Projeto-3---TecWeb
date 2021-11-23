from django.db import models
from django.conf import settings

# Create your models here.


class Account(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    date = models.DateField(auto_now=True)

    def __str__ (self):
        return f"{self.id}. {self.name}         {self.date}"
