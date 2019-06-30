from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import JuliaForm
import math
import numpy as np
import io
import matplotlib.pyplot as plt
from PIL import Image
from .function import logistic, julia
# Create your views here.

real, image = [0], [0]

def plt2png():
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=200)
    s = buf.getvalue()
    buf.close()
    return s

def index(request):
    params = {
        'title':'Juliasetviewer',
        'message':'z_n+1=z^2+c',
        'ac':'cの実部と虚部を入力してください',
        'form':JuliaForm()
    }
    return render(request, 'julia/index.html', params)

def next(request):
    if (request.method == 'POST'):
        real[0] = request.POST['Real']
        image[0] = request.POST['Image']
    return render(request, 'julia/next.html')

def img_plot(request):
    m, d = float(real[0]), float(image[0])
    x, y = [np.linspace(-2, 2, 500)] * 2
    X, Y = np.meshgrid(x, y)
    plt.pcolor(X, Y, julia(X, Y, m, d))
    plt.gray()
    png = plt2png()
    plt.cla()
    response = HttpResponse(png, content_type='image/png')
    return response