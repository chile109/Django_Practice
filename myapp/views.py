from django.shortcuts import render
from datetime import datetime


def hello_world(request):
    return render(
        request,
        "hello_world.html",
        {
            "current_time": str(datetime.now()),
        },
    )
