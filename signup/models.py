from django.db import models

# Create your models here.


class Account(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField(max_length=200)
    content = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return f"{self.id}. {self.name}         {self.date}"