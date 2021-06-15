from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'Ayesha',
        'title': 'First blog try',
        'content': 'Lab honi thi',
        'date_posted': '15 june, 2021'
    },
    {
        'author': 'HAHAHAHA',
        'title': 'Second blog try',
        'content': 'Nae huwi',
        'date_posted': '15 june, 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
