from django.shortcuts import render


def index(request):
    context = {}
    return render(request, "index.html", context=context)


def login_view(request):
    context = {}
    return render(request, "signin.html", context=context)