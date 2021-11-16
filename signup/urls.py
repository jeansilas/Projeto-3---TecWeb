from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('account/<int:account_id>', views.api_account),
    path('account/',views.api_account),
    path('account/change/<int:account_id',views.api_account_plus)

]