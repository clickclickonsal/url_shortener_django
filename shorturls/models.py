from django.db import models

# Create your models here.
class Link(models.Model):
	# Using this field is actually a Charfield but with a URL validator. AWESOME!
	url = models.URLField()

	@staticmethod
	def shorten(long_url):
		return "h"