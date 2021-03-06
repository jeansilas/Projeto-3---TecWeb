from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignUP.index, name="SignUP"),
    path('account/<int:account_id>', views.SignUP.api_account,name="Accounts"),
    path('account/',views.SignUP.api_account,name="Accounts"),
    path('account',views.SignUP.api_account,name="Accounts"),
    path("create",views.create,name="User-Account"),
    path('accounts',views.SignUP.api_accounts,name="Accounts"),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('account/<str:account_name>/notes',views.SignUP.api_account_notes_get),
    path('account/<str:account_name>/note',views.SignUP.api_account_note_post),
    path('account/<str:account_name>/tags',views.SignUP.api_account_tags_get),

]