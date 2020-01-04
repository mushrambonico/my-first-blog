from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #modelo para outro link
    title = models.CharField(max_length=200) #modelo para texto com limite fixo
    text = models.TextField() #modelo para texto sem limite
    created_date = models.DateTimeField(default=timezone.now) #modelo para data e hora mesma coisa que \/
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title