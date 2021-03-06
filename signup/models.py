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

class Tag(models.Model):
    tag = models.CharField(max_length=30)
    
    
    def __str__(self):
        return '{0}'.format(self.tag)

class Notes(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=400)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    account =  models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return '{0}, {1}'.format(self.id, self.title)