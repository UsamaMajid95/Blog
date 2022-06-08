
from django.db import models
from django.db.models import CASCADE


class Category(models.Model):
    name= models.CharField(max_length=30)

    def __str__(self):
        return self.name

class post(models.Model):
    title=models.CharField(max_length=250)
    body= models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    last_modified=models.DateTimeField(auto_now=True)
    categories=models.ManyToManyField( 'Category' ,related_name='post')

    def __str__(self):
        return self.title


class Comment(models.Model):
    author= models.CharField(max_length=50)
    body= models.TextField()
    created_on =models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(post,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.author