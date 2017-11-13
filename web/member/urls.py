from django.conf.urls import url
from django.views.generic import View
from member.views import TestView, TestTplView


urlpatterns = [
    url(r'^test/$', TestView.as_view(), name='test'),
    url(r'^tpl/$', TestTplView.as_view(), name='tpl'),
]