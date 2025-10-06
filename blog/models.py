from django.db import models

class MyBlog(models.Model):

    class Meta:
        verbose_name= 'Meu Blog'
        verbose_name_plural = 'Configurações'


    title = models.CharField(max_length=65,default="",blank=False, null=False)
    description = models.CharField(max_length=255,default="",blank=False, null=False)
    show_header = models.BooleanField(default=True)
    show_search = models.BooleanField(default=True)
    show_menu = models.BooleanField(default=True)
    show_description = models.BooleanField(default=True)
    show_pagination = models.BooleanField(default=True)
    show_footer = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def __str__(self):
        return self.title