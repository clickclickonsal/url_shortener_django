from django.db import models

# Create your models here.
class Link(models.Model):
	# Using this field is actually a Charfield but with a URL validator. AWESOME!
	url = models.URLField()

	@staticmethod
	def shorten(long_url):
		l, _ = Link.objects.get_or_create(url=link.url)
		return str(l.pk)

	@staticmethod
	def expand(slug):
		link_id = int(slug)
		l = Link.objects.get(pk=link_id)
		return l.url
		