from django.shortcuts import render

# Create your views here.
def timer(request):
    context = {

    }

    return render(request, "timer/timer.html", context)