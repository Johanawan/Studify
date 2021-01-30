from django.shortcuts import render

# Create your views here.
def youtube(request):
    context = {
        
    }
    return render(request, "youtube/youtube.html", context)