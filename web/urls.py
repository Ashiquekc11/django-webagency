from django.urls import path
from . import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about-us"),
    path("contact/", views.contact, name="contact"),
    path("startup/", views.startup, name="index-startup"),
    path("not-found/", views.notfound, name="404"),
    path("projects/", views.projects, name="projects"),
    path("project-details/", views.projectdetails, name="project-details"),
    path("services-two/", views.servicestwo, name="services-2"),
    path("services-details/<str:pk>/", views.servicesdetails, name="services-details"),
    path("blog-with-sidebar/", views.blogwithsidebar, name="blog-with-sidebar"),
    path("blog-single-with-sidebar/<str:pk>/", views.blogsinglewithsidebar, name="blog-single-with-sidebar"),
]