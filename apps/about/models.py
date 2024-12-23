from django.db import models

class Abot1(models.Model):
    image = models.ImageField(upload_to='images/about')
    description = models.TextField()

    def __str__(self):
        return self.description[:50]

class About(models.Model):
    title = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.title
    
class Guide(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/about')
    job_name = models.CharField(max_length=50)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.full_name

class Post(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()

    def __str__(self):
        return self.title
