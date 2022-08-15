from django.shortcuts import render


# Create your views here.

def index(request):
    template_name = 'login/index.html'
    context = {}
    return render(request, template_name, context)


def reset(request):
    template_name = 'login/reset.html'
    context = {}
    return render(request, template_name, context)
