from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from .models import Link

# Create your views here.
class LinkCreate(CreateView):
	model = Link
	fields = ["url"]

class LinkShow(DetailView):
	model = Link