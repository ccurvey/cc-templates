from django.shortcuts import render
from .models import Person
from vanilla import ListView


# Create your views here.
def index(request):
    return render(request, "fakeout/index.html")


class PersonListView(ListView):
    model = Person
    template_name = 'fakeout/person_list.html'

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']
