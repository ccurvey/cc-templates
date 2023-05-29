from django.urls import path

from . import views

app_name = 'nineteen'

urlpatterns = [
    path("person/list/", views.PersonListView.as_view(), name="person-list"),
    path("person/detail/<uuid:person_uuid>/", views.PersonDetailView.as_view(), name="person-detail"),
    path("", views.index, name="index"),
]
