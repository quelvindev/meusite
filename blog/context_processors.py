
from blog.models import MyBlog

def models_processors(request):
    setups = MyBlog.objects.order_by('-id').first
    return {
        'setups':setups
    }