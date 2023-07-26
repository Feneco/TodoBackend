from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'pub_date', 'to_date', 'done')

# Register your models here.
admin.site.register(Todo, TodoAdmin)
