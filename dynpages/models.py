from django.db import models
from django.urls import get_script_prefix
from django.utils.encoding import iri_to_uri
from django.conf import settings


class DynPage(models.Model):

    # Settings
    url = models.CharField('URL', max_length=100, db_index=True)
    title = models.CharField('title', max_length=200)
    language = models.CharField('language',
                                max_length=6,
                                default=settings.LANGUAGE_CODE,
                                choices=settings.LANGUAGES,
                                help_text="PS: Page will invalidate when language is removed"
                                )

    # Meta tags
    description = models.TextField('description', max_length=200)
    keywords = models.CharField('keywords', max_length=200)

    # Content
    content = models.TextField('content')

    # Advanced settings
    template_name = models.CharField(
        'template name',
        max_length=70,
        blank=True,
        help_text="Example: 'dynpages/contact_page.html'. If this isn't provided, "
                  "the system will use 'dynpages/default.html'.",
    )

    class Meta:
        verbose_name = "Dynamic page"
        verbose_name_plural = "Dynamic pages"
        ordering = ('url',)

    def __str__(self):
        return "%s -- %s" % (self.url, self.title)

    def get_absolute_url(self):
        return iri_to_uri(get_script_prefix().rstrip('/') + ('/' + self.language + self.url))
