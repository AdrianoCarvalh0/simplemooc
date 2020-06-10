from django.db import models

# Create your models here.

class Course(models.Motel):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    # campo de texto pode estar em branco mas não fica vazio, não nulo
    # blank = True ==> Campo não obrigatório
    description = models.TextField('Descrição', blank=True)
    start_date = models.DateField('Data de criação', null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)