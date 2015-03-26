#!/usr/bin/env python
# encoding: utf-8

from django.shortcuts import render_to_response
from django.utils.translation import ugettext as _ 
from language.settings import LANGUAGES
from django.core.context_processors import csrf
from bidiutils.context_processors import bidi

def home(request):
    context = {
        'almas': _(u"My Name is almas"),
        'LANGUAGES':LANGUAGES,
    }
    context.update(bidi(request))
    context.update(csrf(request))
    return render_to_response('index.html', context)
