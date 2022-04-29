from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
from .models import Author, Contact, Blog, Project, Service, Slider, Testimonial, Category
from .forms import ContactForm
from django.db.models import Q



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


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


# def contact(request):
#     data = {
#     "name": "Ashique",
#     "email": "ashiquekc@gmail.com",
#     }
#     form = ContactForm(request.POST or None, initial=data)
#     print(request.user)
#     if request.method == "POST":
#         if form.is_valid():
#             form_data = form.save(commit=False)
#             form_data.ip_address = get_client_ip(request)
#             form_data.save()
#     else:
#         pass
#     context = {
#         "is_contact": True,
#         "form":form
#     }
#     return render(request, "web/contact.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully updated",
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
            }
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        context = {
            "is_contact": True,
            "form": form,
        }
    return render(request, "web/contact.html", context)


def notfound(request):
    context = {"is_notfound": True}
    return render(request, "web/404.html", context)


def projects(request):
    projects = Project.objects.all()
    categorys = Category.objects.all()
    # q = Project.objects.values('category').distinct()
    context = {
        "is_projects": True,
        "projects": projects,
        "categorys": categorys,
    }
    return render(request, "web/projects.html", context)


def projectdetails(request, slug):
    projects = Project.objects.all()
    project = Project.objects.get(slug=slug)
    context = {
    "is_projectdetails": True,
    "projects": projects,
    "project": project,
    }
    return render(request, "web/project-details.html", context)


def servicestwo(request):
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    context = {"is_servicestwo": True,
               "services": services, "testimonials": testimonials}
    return render(request, "web/services-2.html", context)


def servicesdetails(request, slug):
    service = Service.objects.get(slug=slug)
    services = Service.objects.all()
    context = {"is_servicesdetails": True,
               "service": service, "services": services}
    return render(request, "web/services-details.html", context)


def blogwithsidebar(request):
    blogs = Blog.objects.all()
    context = {"is_blogwithsidebar": True, "blogs": blogs, }
    return render(request, "web/blog-with-sidebar.html", context)


def blogsinglewithsidebar(request, pk):
    blog = Blog.objects.get(pk=pk)
    context = {"is_blogsinglewithsidebar": True, "blog": blog}
    return render(request, "web/blog-single-with-sidebar.html", context)


def results(request):
    results = None
    query = (request.GET.get('q'))
    if query:
        results = Blog.objects.filter(Q(content__icontains=query) | Q(title__icontains=query))
    context = {
    "is_results": True,
    "query": query,
    "results": results
    }
    return render(request, "web/results.html", context)
