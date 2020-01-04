from django.contrib import admin

# Register your models here.

from .models import Post #we must import the class we just created

admin.site.register(Post) #torna nosso modelo visível na página de administração

