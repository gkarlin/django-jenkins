	# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('',
     url(r'^test_click/$', 'django.views.generic.TemplateView',
         {'template': 'test_app/wm_test_click.html'}, name='wm_test_click')
)
