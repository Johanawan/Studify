from django.shortcuts import render

# Create your views here.

def dictionaryView(request):
    return render(request, "dictionary/dictionary.html")