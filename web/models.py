from django.db import models
from versatileimagefield.fields import VersatileImageField
from ckeditor.fields import RichTextField



# Create your models here.

class Contact(models.Model):

    name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=128)
    project_details = models.TextField()

    def __str__(self):
        return str(self.name)


class Blog(models.Model):
    CATEGORY_CHOICES = (('agency', 'Agency'),('digital', 'Digital'), ('creative', 'Creative'), )

    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.CharField(max_length=128, choices= CATEGORY_CHOICES, default="creative")
    featured_image = VersatileImageField()
    description = models.TextField(max_length=400)
    image_one = VersatileImageField()
    image_two = VersatileImageField()
    points = RichTextField(blank=True, null=True)


    def __str__(self):
        return str(self.title)

