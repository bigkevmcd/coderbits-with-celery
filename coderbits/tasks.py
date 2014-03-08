import urllib
import urllib2

from celery.utils.log import get_task_logger
from celery import shared_task

from coderbits.models import Snippet

logger = get_task_logger(__name__)


@shared_task
def highlight_snippet_task(snippet_id):
    snippet = Snippet.objects.get(pk=snippet_id)
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
