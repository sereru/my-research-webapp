from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from .forms import BoxForm
# Create your views here.

def index(request):

    params = {
        'title': 'box次元',
        'form': BoxForm(),
        'Img': 'アップロードしてください'
    }

    if (request.method == 'POST'):
        params['Img'] = request.POST['Img']
    return render(request, 'boxdimension/index.html', params)