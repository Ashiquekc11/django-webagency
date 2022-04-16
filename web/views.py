from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
from .models import Author, Contact, Blog, Project, Service, Slider, Testimonial


def index(request):
    sliders = Slider.objects.all()
    projects = Project.objects.all()
    testimonials = Testimonial.objects.all()
    context = {"is_index": True, "sliders": sliders,
               "projects": projects, "testimonials": testimonials}
    return render(request, "web/index.html", context)


def about(request):
    context = {"is_about": True}
    return render(request, "web/about-us.html", context)


def startup(request):
    context = {"is_startup": True}
    return render(request, "web/index-startup.html", context)


def contact(request):
    context = {"is_contact": True}
    return render(request, "web/contact.html", context)


def notfound(request):
    context = {"is_notfound": True}
    return render(request, "web/404.html", context)


def projects(request):
    context = {"is_projects": True}
    return render(request, "web/projects.html", context)


def projectdetails(request):
    context = {"is_projectdetails": True}
    return render(request, "web/project-details.html", context)


def servicestwo(request):
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    context = {"is_servicestwo": True, "services": services, "testimonials": testimonials}
    return render(request, "web/services-2.html", context)


def servicesdetails(request, slug):
    service = Service.objects.get(slug=slug)
    services = Service.objects.all()
    context = {"is_servicesdetails": True, "service":service, "services":services}
    return render(request, "web/services-details.html", context)


def blogwithsidebar(request):
    blogs = Blog.objects.all()
    context = {"is_blogwithsidebar": True, "blogs": blogs,}
    return render(request, "web/blog-with-sidebar.html", context)


def blogsinglewithsidebar(request, pk):
    blog = Blog.objects.get(pk=pk)
    context = {"is_blogsinglewithsidebar": True, "blog": blog}
    return render(request, "web/blog-single-with-sidebar.html", context)
