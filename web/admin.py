from django.contrib import admin
from .models import Author, Contact, Blog, Project, Service, Slider, Testimonial, SocialMedia

# Register your models here.
admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Slider)
admin.site.register(Project)
admin.site.register(Service)
admin.site.register(Testimonial)
admin.site.register(SocialMedia)
