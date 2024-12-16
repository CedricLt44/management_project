from django.contrib import admin

from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_by', 'created_at') 
    search_fields = ('name', 'created_at','created_by')  
    list_filter = ('name', 'created_at','created_by')  

admin.site.register(Project, ProjectAdmin)