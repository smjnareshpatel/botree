from django.contrib import admin

# Register your models here.
from .models import Customer,Cleaner


admin.site.register(Customer)

admin.site.register(Cleaner)
