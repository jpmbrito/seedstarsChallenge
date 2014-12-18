from django.views.generic.edit import CreateView, ListView

# Create your views here.
class SeedStarsUser_Create(CreateView):
    model = SeedStarsUser

class SeedStarsUser_List(ListView):
    model = SeedStarsUser
