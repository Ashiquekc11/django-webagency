from django.db import models
from versatileimagefield.fields import VersatileImageField
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=128)
    project_details = models.TextField()

    def __str__(self):
        return str(self.name)


class Blog(models.Model):
    CATEGORY_CHOICES = (('agency', 'Agency'), ('digital',
                        'Digital'), ('creative', 'Creative'), )

    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.CharField(
        max_length=128, choices=CATEGORY_CHOICES, default="creative")
    featured_image = VersatileImageField()
    description = models.TextField()
    content = models.TextField()
    author = models.ForeignKey("Author", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)


class Author(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)
    photo = VersatileImageField()
    about = models.TextField()

    def __str__(self):
        return str(self.name)


class Slider(models.Model):
    title = models.CharField(max_length=128)
    sub_title = models.CharField(max_length=128)
    slider_img = VersatileImageField()
    btn_link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return str(self.title)


class Project(models.Model):
    CATEGORY_CHOICES = (('advertising', 'Advertising'),
                        ('branding', 'Branding'), ('creative', 'Creative'), )

    title = models.CharField(max_length=128)
    category = models.CharField(
        max_length=128, choices=CATEGORY_CHOICES, default="creative")
    image = VersatileImageField()

    def __str__(self):
        return str(self.title)


class Testimonial(models.Model):
    name = models.CharField(max_length=30)
    profile_photo = VersatileImageField()
    feedback = models.TextField()
    designation = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)


class Service(models.Model):

    title = models.CharField(max_length=128)
    icon = models.FileField()
    description = models.TextField()
    content = models.TextField()
    

    def __str__(self):
        return str(self.title)
