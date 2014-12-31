from django.db import models
from django.core.urlresolvers import reverse
from .basechanger import decimal2base_n, base_n2decimal
# Create your models here.
class Link(models.Model):
	# Using this field is actually a Charfield but with a URL validator. AWESOME!
	url = models.URLField()

	def get_absolute_url(self):
		return reverse("link_show", kwargs={"pk": self.pk})

	# Encodes Url to a short url
	@staticmethod
	def shorten(link):
		l, _ = Link.objects.get_or_create(url=link.url)
		return str(decimal2base_n(l.pk))

	# Decodes short url to original url
	@staticmethod
	def expand(slug):
		link_id = int(base_n2decimal(slug))
		l = Link.objects.get(pk=link_id)
		return l.url

	def short_url(self):
		return reverse("redirect_short_url",
                   kwargs={"short_url": Link.shorten(self)})