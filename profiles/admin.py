from django.contrib import admin
from .models import Profile
# Register your models here.
class AdminProfile(admin.ModelAdmin):
    list_display = ('user','location',)
    list_display_links = ('user','location',) 
     
    list_per_page = 25
admin.site.register(Profile,AdminProfile)
