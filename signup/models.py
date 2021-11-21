from django.db import models

# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=30)
    
    
    def __str__(self):
        return '{0}'.format(self.tag)
    
class Account(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField(max_length=200)
    content = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return f"{self.id}. {self.name} {self.date}"
class Notes(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=400)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    account =  models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return '{0}, {1}'.format(self.id, self.title)
    

    