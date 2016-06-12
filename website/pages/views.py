from django.conf import settings
from django.shortcuts import render_to_response
from .tools import get_page_filler


def home(request):
    filler_list = get_page_filler()

    return render_to_response('pages/page_home.html', locals())
