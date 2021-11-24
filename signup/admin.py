from django.contrib import admin
from .models import Account, Notes, Tag

admin.site.register(Account)
admin.site.register(Tag)
admin.site.register(Notes)

# Register your models here.
