from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from coderbits.forms import SnippetForm
from coderbits.models import Snippet
from coderbits.tasks import highlight_snippet_task


def new(request):
    """
    Create a new Snippet.
    """
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save()
            highlight_snippet_task.delay(snippet.id)
            return HttpResponseRedirect(
                reverse('snippet_show', kwargs={'snippet_id': snippet.id}))
    else:
        form = SnippetForm() # An unbound form

    return render(request, 'create.html', {
        'form': form,
    })


def show(request, snippet_id):
    """
    Render a snippet.
    """
    snippet = get_object_or_404(Snippet, pk=int(snippet_id))
    return render(request, 'show.html', {'snippet': snippet})
