from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from .models import Link

# Create your views here.
class LinkCreate(CreateView):
	model = Link
	fields = ["url"]

	def form_valid(self, form):
		prev = Link.objects.filter(url=form.instance.url)
		if prev:
			return redirect("link_show", pk=prev[0].pk)
		return super(LinkCreate, self).form_valid(form)

class LinkShow(DetailView):
	model = Link