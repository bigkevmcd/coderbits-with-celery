import urllib, urllib2

from celery.task import Task
from celery.registry import tasks

from coderbits.models import Snippet


class HighlightSnippetTask(Task):
    def run(self, snippet_id):
        snippet = Snippet.objects.get(pk=snippet_id)
        logger = self.get_logger()
        logger.info("Processing snippet %d" % snippet_id)
        if snippet:
            data = urllib.urlencode({'lang': snippet.language,
                                     'code': snippet.plain_code})
            request = urllib2.Request('http://pygments.appspot.com/', data)
            response = urllib2.urlopen(request)
            snippet.highlighted_code = response.read()
            snippet.save()
            logger.info("Completed processing snippet %d" % snippet_id)
        else:
            logger.error("Snippet not found")

tasks.register(HighlightSnippetTask)
