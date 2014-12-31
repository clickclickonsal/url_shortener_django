from django.db import models
from django.core.urlresolvers import reverse
from .basechanger import decimal2base_n, base_n2decimal
from hashids import Hashids
hashids = Hashids()
# Create your models here.
class Link(models.Model):
	# Using this field is actually a Charfield but with a URL validator. AWESOME!
	url = models.URLField()

	def get_absolute_url(self):
		return reverse("home")

	# Encodes Url to a short url
	@staticmethod
	def shorten(link):
		l, _ = Link.objects.get_or_create(url=link.url)
		# using library to encrypt id
		return str(hashids.encrypt(l.pk))

	# Decodes short url to original url
	@staticmethod
	def expand(slug):
		# Decrypting slug and getting '(12,)'
		dirty_str = str(hashids.decrypt(slug))
		# stripping out '(,)'
		clean_id = dirty_str.strip("(,)")
		# now converting '12' into 12
		link_id = int(clean_id)
		l = Link.objects.get(pk=link_id)
		return l.url

	def short_url(self):
		return reverse("redirect_short_url",
                   kwargs={"short_url": Link.shorten(self)})