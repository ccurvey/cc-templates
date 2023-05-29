from django.shortcuts import render
from .models import Person
from vanilla import ListView, DetailView


# Create your views here.
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
        try:
            import wingdbstub
        except ImportError:
            pass

        return [
            (field.verbose_name, field.value_to_string(self))
            for field in self.__class__._meta.fields
        ]


class PersonDetailView(DetailView):
    model = PersonProxy
    template_name = 'fakeout/person_detail.html'
    lookup_field = "uuid"
    lookup_url_kwarg = 'person_uuid'
