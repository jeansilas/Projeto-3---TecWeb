from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('account/<int:account_id>', views.api_account),
    path('account/',views.api_account),
    path('account',views.api_account),
    path('account/<str:account_name>/notes/',views.api_account_notes_get),
    path('account/<str:account_name>/note/',views.api_account_note_post),
    path('account/<str:account_name>/tags/',views.api_account_tags_get),
    path('accounts',views.api_accounts)

]