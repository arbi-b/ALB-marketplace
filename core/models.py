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
    photos = models.ImageField(null=True, blank=True, upload_to='images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='1')


    
    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk' : self.pk})
    

# class Car(models.Model):
#     post = models.OneToOneField(Post, on_delete=models.CASCADE, primary_key=True)
#     model = models.CharField(max_length=50)
#     year = models.IntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
    
#     def __str__(self):
#         return self.model
    

# class Job(models.Model):
#     post = models.OneToOneField(Post, on_delete=models.CASCADE, primary_key=True)
#     title = models.CharField(max_length=100)
#     location = models.CharField(max_length=100)
#     salary = models.DecimalField(max_digits=10, decimal_places=2)
    
#     def __str__(self):
#         return self.title
    

# class Property(models.Model):
#     post = models.OneToOneField(Post, on_delete=models.CASCADE, primary_key=True)
#     address = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
    
#     def __str__(self):
#         return self.address    
