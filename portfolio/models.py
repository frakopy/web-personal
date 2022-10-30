from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=160, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripcion')
    image = models.ImageField(verbose_name='Imagen', upload_to='projects')
    url = models.URLField(blank=True, null=True)
    # auto_now_add will be executed once, that is just when a register is created the first time
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    # auto_now will be executed every time a record is modified
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edicion')

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-created']

    def __str__(self):
        return self.title
