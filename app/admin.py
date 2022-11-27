from django.contrib import admin
from .models import PrimeNumber
# Register your models here.
class PrimeNumberAdmin(admin.ModelAdmin):
    list_display = ('user','range','time_elapsed','algorithm','prime_numbers','created_at')


admin.site.register(PrimeNumber,PrimeNumberAdmin)