from django.forms import ModelForm

from coderbits.models import Snippet


class SnippetForm(ModelForm):

    class Meta:
        model = Snippet
        exclude = ['highlighted_code']
