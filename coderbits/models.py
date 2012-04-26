from django.db import models

LANGUAGE_CHOICES = [
    (u"ruby", u"Ruby"),
    (u"python", u"Python"),
    (u"javascript", u"JavaScript"),
    (u"css", u"CSS")
]


class Snippet(models.Model):

    name = models.CharField(max_length=255)
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)

    plain_code = models.TextField()
    highlighted_code = models.TextField(blank=True)

    def __unicode__(self):
        return self.name
