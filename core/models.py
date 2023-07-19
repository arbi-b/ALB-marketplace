from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)   
    content = models.TextField(default='')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.first().id)
    photos = models.ImageField(default="defaultpic.jpg", upload_to='images')
    photos2 = models.ImageField(null=True, blank=True, upload_to='images')
    photos3 = models.ImageField(null=True, blank=True, upload_to='images')
    photos4 = models.ImageField(null=True, blank=True, upload_to='images')
    photos5 = models.ImageField(null=True, blank=True, upload_to='images')
    photos6 = models.ImageField(null=True, blank=True, upload_to='images')
    photos7 = models.ImageField(null=True, blank=True, upload_to='images')
    photos8 = models.ImageField(null=True, blank=True, upload_to='images')
    photos9 = models.ImageField(null=True, blank=True, upload_to='images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='1')
    price= models.DecimalField(max_digits=10, decimal_places=0, default='0')



    
    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk' : self.pk})