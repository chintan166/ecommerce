from django.contrib import admin
from .models import Accounts

class AccountsAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','username','email','phone_number')

admin.site.register(Accounts,AccountsAdmin)