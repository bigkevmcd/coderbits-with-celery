"""
RailsCasts 271 Snippet management tests.
"""
from django.test import TestCase

from coderbits.forms import SnippetForm
from coderbits.models import Snippet


class SnippetFormTest(TestCase):

    def test_create_snippet(self):
        """
        We can create a Snippet.
        """
        form = SnippetForm(
          {'name': u'My Snippet',
           'language': 'python',
           'plain_code': u'from django.test import TestCase'})

        self.assertTrue(form.is_valid(), "Form is not valid")
        snippet = form.save()

        self.assertEqual(u'My Snippet', snippet.name)
        self.assertEqual(u'python', snippet.language)
        self.assertEqual(u'from django.test import TestCase',
                         snippet.plain_code)
