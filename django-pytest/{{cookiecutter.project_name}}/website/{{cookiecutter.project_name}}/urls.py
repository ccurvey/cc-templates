from django.urls import path

from . import views

app_name = '{{cookiecutter.project_name}}'

urlpatterns = [
    path("person/list", views.PersonListView.as_view(), name="person-list"),
    path("", views.index, name="index"),
]
