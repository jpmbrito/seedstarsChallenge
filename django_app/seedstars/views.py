from django.views.generic import CreateView, ListView, View
from django.shortcuts import render
from django.core.urlresolvers import reverse

from seedstars.models import *

# Create your views here.
class IndexView(View):
    template_name = 'seedstars/index.html'
    def get(self, request):
        return render(request, self.template_name, {})

class SeedStarsUser_Create(CreateView):
    model = SeedStarsUser
    fields = ['name', 'email']
    template_name = 'seedstars/add.html'

    def get_success_url(self):
        return reverse('ss_list')

class SeedStarsUser_List(ListView):
    model = SeedStarsUser
    template_name = 'seedstars/list.html'
