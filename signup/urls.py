from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignUP.index, name="SignUP"),
    path('account/<int:account_id>', views.SignUP.api_account,name="Accounts"),
    path('account/',views.SignUP.api_account,name="Accounts"),
    path('account',views.SignUP.api_account,name="Accounts"),
    path('accounts',views.SignUP.api_accounts,name="Accounts")

]