from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'enrollment_number')
    search_fields = ['name', 'enrollment_number']

admin.site.register(Student, StudentAdmin)
