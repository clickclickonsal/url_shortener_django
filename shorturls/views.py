from django.views.generic.edit import CreateView
from .models import Link

# Create your views here.
class LinkCreate(CreateView):
	model = Link
	fields = ["url"]