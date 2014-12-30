from django.test import TestCase
from .models import Link

# Create your tests here.
class ShortenerText(TestCase):
	def test_shortens(self):
		"""
		Test that urls get shorter.
		"""
		url = "http://www.example.com/"
		l = Link(url=url)
		short_url = Link.shorten(1)
		# checks if short_url length is less than url length.
		self.assertLess(len(short_url), len(url))