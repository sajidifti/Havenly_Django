from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class DesignerInfo(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profile_pics', blank=True)
    email = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    status_ = (
        (1, "Active"),
        (2, "Deactivate")
    )
    status = models.IntegerField(choices=status_)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    image = models.ImageField(upload_to='post_images')
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    upload_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-upload_date',]

    def __str__(self):
        return self.description


class React(models.Model):
    post = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='react_user')



class ContactUs(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    message = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Reply(models.Model):
    post_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reply_user')
    message = models.TextField()

    def __str__(self):
        return self.message


class DesignerMessage(models.Model):
    designer_user = models.IntegerField()
    customer_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_user')
    message = models.TextField()
    reply_message = models.TextField()

    def __str__(self):
        return self.message
