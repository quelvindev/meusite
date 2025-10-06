from django.contrib import admin
from blog.models import MyBlog

@admin.register(MyBlog)
class MenuBlogAdmin(admin.ModelAdmin):
    list_display = 'title','description'

    def has_add_permission(self, request):
        return not MyBlog.objects.exists()
    
 