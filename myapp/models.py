from django.db import models
from django.views.generic.edit import UpdateView
from django.urls import reverse
# Create your models here.

class UserModel(models.Model):
    username = models.CharField(max_length=30, )
    password = models.CharField(max_length=30)
    tel = models.CharField(max_length=10)
    givename = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    email = models.EmailField(default='')
    

    # def get_absolute_url(self):
    #     return reverse('profile', kwargs={'pk': self.pk})

    def __str__(self):
        return self.username

class BlogModel(models.Model):
    text = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return  self.text


class CommentModel(models.Model):
    comment = models.CharField(max_length=300)
    blog_id = models.ForeignKey(BlogModel, on_delete=models.CASCADE)  # , related_name='comments')

    def __str__(self):
        return self.comment