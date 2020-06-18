from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    #personalizando o model admin, customizando. Exibe estes campos:
    list_display = ['name','slug','start_date', 'created_at']
    #procura por nome e pelo slug
    search_fields = ['name','slug']
    #o prepulated_fields repete o nome, tirando a acentuação e os espaços
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(Course,CourseAdmin)