from django.shortcuts import render
import requests, json, urllib
from urllib.request import urlopen


def dictionaryView(request):

    dictionaryWord = []
    word = "Look up something!"

    word_type = None
    definition = None
    example = None

    if request.method == "POST":
        # Get the input data from the page
        language = request.POST.get("language")
        lookup_word = request.POST.get("word")
        
        # Customise the API link with the variables
        url = "https://api.dictionaryapi.dev/api/v2/entries/{}/{}".format(language, lookup_word)
        
        response = requests.get(url).json()

        try:
            word = response[0]["word"]

            word_type = response[0]["meanings"][0]["partOfSpeech"].capitalize()

            try:
                definition = response[0]["meanings"][0]["definitions"][0]["definition"]
            except KeyError:
                definition = ""

            try:
                example = response[0]["meanings"][0]["definitions"][0]["example"]
            except KeyError:
                example = ""

        except KeyError:
            print("We could not find the definition of the word you are looking for")

        # dictionaryWord = list(zip(titles, word_types, definitions, examples, synonyms))

    word_caps = word.capitalize()
    context = {
        "word": word_caps,
        "word_type": word_type,
        "definition": definition,
        "example": example,
    }

    return render(request, "dictionary/dictionary.html", context)