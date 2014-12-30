from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Link(models.Model):
	# Using this field is actually a Charfield but with a URL validator. AWESOME!
	url = models.URLField()

	@staticmethod
	def shorten(link):
		l, _ = Link.objects.get_or_create(url=link.url)
		return str(l.pk)

	@staticmethod
	def expand(slug):
		link_id = int(slug)
		l = Link.objects.get(pk=link_id)
		return l.url

	def get_absolute_url(self):
		return reverse("link_show", kwargs={"pk": self.pk})