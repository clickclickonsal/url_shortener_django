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

	def test_recover_link(self):
		"""
		Tests that shortened and expanded url is the same as original.
		"""
		url = "http://www.example.com/"
		l = Link(url=url)
		short_url = Link.shorten(l)
		l.save()
		# Another user asks for the expansion of short_url
		exp_url = Link.expand(short_url)
		# Checks that expanded url is equal to original url.
		self.assertEqual(url, exp_url)