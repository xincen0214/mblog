from django.shortcuts import render
from mysite.models import Post
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())