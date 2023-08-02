from django.db import models
from django.urls import reverse

# Create your models here.
class ProjectStorage(models.Model):
    titolo = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")
    description = models.CharField(max_length=500)
    lenguage = models.SlugField(db_index=True)
    link = models.CharField(max_length=300, null=True)
    link_github = models.CharField(max_length=300, null=True)
    state = models.CharField(max_length=200, null=True)

    def get_absolute_url(self):
        return reverse("post-detail-page", args=[self.slug])
    
    def __str__(self):
        return self.titolo

class MySkill(models.Model):
    lenguage = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")
    type = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.lenguage
    

class MyUpdateContact(models.Model):
    instagram = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)
    github = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    stmplib_token = models.CharField(max_length=500, null = True)
    image = models.ImageField(upload_to="images", null=True)

    def __str__(self):
        return "My Contact data"
    

