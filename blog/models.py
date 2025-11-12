from django.db import models
from utils.validate_png import validade_icon
from utils.images import resize_image

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
    favicon = models.ImageField(upload_to='dist/img/%Y/%m', 
                                blank=True, 
                                null=True,
                                default='',
                                validators=[validade_icon])
    

    def save(self,*args, **kwargs):
        current_favicon = str(self.favicon.name)
        super().save(*args, **kwargs)
        favicon_chaged = False

        if self.favicon:
            favicon_chaged = current_favicon!= self.favicon.name
        if favicon_chaged:
            resize_image(self.favicon,32)
            


    def __str__(self):
        return self.title