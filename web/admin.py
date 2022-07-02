from django.contrib import admin
from .models import Author, Contact, Blog, Project, Service, Slider, Testimonial, SocialMedia, About, Category

# Register your models here.
from import_export.admin import ImportExportActionModelAdmin



@admin.register(Contact)
class ContactAdmin(ImportExportActionModelAdmin):
    pass


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    pass

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("category","title",)
    list_filter = ("title", "category")
    autocomplete_fields = ("category",)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    pass

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    pass

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    # actions = []
    list_display = ("phone", "email",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)
