from django.db import models

# Create your models here.

class CourseManager(models.Manager):

    #o "|" pipe é o "ou"

    def search(self,query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) |
            models.Q(description__icontains=query)
        )


class Course(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    # campo de texto pode estar em branco mas não fica vazio, não nulo
    # blank = True ==> Campo não obrigatório
    description = models.TextField('Descrição', blank=True)
    start_date = models.DateField('Data de criação', null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    #cria um objeto da classe do Manager do Django
    objects = CourseManager()

    def __str__(self):
        return self.name