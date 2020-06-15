from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    fields = ('name','slug','description','start_date')

# Register your models here.
admin.site.register(Course,CourseAdmin)