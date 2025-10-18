from django.db import models

class MeuSite(models.Model):

        class Meta:
                verbose_name= 'Meu Site'
                verbose_name_plural = 'Configurações'


        title = models.CharField(max_length=65,default="",blank=False, null=False)
        favicon = models.ImageField(upload_to='dist/media/img/%Y/%m',
                                        blank=True,
                                        null=True,
                                        default= '',
                                        )

        def __str__(self):
                return self.title

        def __str__(self):
                return self.title
