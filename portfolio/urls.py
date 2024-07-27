from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("projects/<int:id>", views.projects, name="projects"),
    path("category/<str:cat>", views.categories, name="categories"),
]