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

class PersonDetailView(DetailView):
    model = Person
    template_name = 'fakeout/person_detail.html'
    lookup_field = "uuid"
    lookup_url_kwarg = 'person_uuid'

    def get_object(self):
        return Person.objects.get(uuid=self.kwargs['person_uuid'])



