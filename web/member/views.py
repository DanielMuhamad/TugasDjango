from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponse
from django.views.generic import View


class TestView(View):

    def get(self, request):
        return HttpResponse('GET request!')

class TestTplView(View):

    def get(self, request):
        template = 'member/index.html'
        data = {
            'text': 'saya adalah daniel',
            'ar': [1,2,3,4,5],
            'logika': True
        }
        return render(request, template, data)