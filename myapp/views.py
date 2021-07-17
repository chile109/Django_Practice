from django.shortcuts import render
from django.http.request import HttpRequest
from datetime import datetime
from .models import Post
import jokekappa

def hello_world(request):
    return render(
        request,
        "hello_world.html",
        {
            "current_time": str(datetime.now()),
        },
    )

def home(request: HttpRequest):
    jokes = [jokekappa.get_joke()["content"] for i in range(10)]
        
    return render(request, 'home.html', {
        'joke': jokes,
    })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})
