from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404
from django.template import loader
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_protect
from django.utils.translation import get_language

from . models import DynPage

DEFAULT_TEMPLATE = 'dynpages/default.html'


def dynpage(request, url):

    if not url.startswith('/'):
        url = '/' + url

    language = get_language()
    language_prefix = '/%s' % language

    if url.startswith(language_prefix):
        url = url[len(language_prefix):]

    try:
        dynpage = get_object_or_404(DynPage, url=url, language=get_language())
    except Http404:
        if not url.endswith('/') and settings.APPEND_SLASH:
            url += '/'
            dynpage = get_object_or_404(DynPage, url=url, language=get_language())
            return HttpResponsePermanentRedirect('%s/' % request.path)
        else:
            raise
    return render_dynpage(request, dynpage)


@csrf_protect
def render_dynpage(request, dynpage):
    """
    Internal interface to the flat page view.
    """
    if dynpage.template_name:
        template = loader.select_template((dynpage.template_name, DEFAULT_TEMPLATE))
    else:
        template = loader.get_template(DEFAULT_TEMPLATE)

    dynpage.content = mark_safe(dynpage.content)

    response = HttpResponse(template.render({'dynpage': dynpage}, request))
    return response
