from django.contrib import admin
from .models import User

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'username')
    search_fields = ('email','is_admin')
    
admin.site.register(User,CustomUserAdmin)