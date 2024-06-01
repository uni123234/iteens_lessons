from django.shortcuts import render

def home(request):
    menu = ["home", "about", "posts"]

    data = {
        'menu': menu
    }
    return render(request,'blog/index.html', context=data)

def about(request):
    return render(request, 'blog/about.html')