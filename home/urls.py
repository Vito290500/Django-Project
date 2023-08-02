from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home-page"),
    path("my_project", views.MyProjectView.as_view(), name="my-projects"),
    path("about", views.AboutView.as_view(), name="about_me"),
    path("contact", views.ContactView.as_view(), name="contact_me"),
    path('download/', views.download_file, name='download_file'),
]