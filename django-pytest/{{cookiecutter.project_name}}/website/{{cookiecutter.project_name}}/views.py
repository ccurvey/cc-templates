from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from vanilla import ListView, DetailView, CreateView

from .models import Person


def index(request):
    return render(request, "fakeout/index.html")


class PersonListView(ListView):
    model = Person
    template_name = 'fakeout/person_list.html'

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']


class PersonProxy(Person):
    class Meta:
        proxy = True

    def get_fields(self):
        return [
            (field.verbose_name, field.value_to_string(self))
            for field in self.__class__._meta.fields
        ]

    def __str__(self):
        return self.first_name


# doing as much as I can through configuration
class PersonDetailView(DetailView):
    model = PersonProxy
    template_name = 'fakeout/person_detail.html'
    lookup_field = "uuid"
    lookup_url_kwarg = 'person_uuid'


class PersonCreateView(CreateView):
    model = PersonProxy
    fields = [
        'first_name',
        'last_name',
        'email',
        'company',
        'address',
        'city',
        'state',
        'postal_code',
    ]

    template_name = 'fakeout/person_create.html'
    success_url = reverse_lazy("nineteen:person-list")

    def form_valid(self, *args, **kwargs):
        ret = super().form_valid(*args, **kwargs)

        messages.success(self.request, f"{self.object} has been created")

        return ret
