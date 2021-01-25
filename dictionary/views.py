from django.shortcuts import render
import requests, json, urllib
from urllib.request import urlopen


def dictionaryView(request):

    dictionaryWord = []
    word = "Look up something!"

    if request.method == "POST":
        # Get the input data from the page
        language = request.POST.get("language")
        lookup_word = request.POST.get("word")
        
        # Customise the API link with the variables
        url = "https://api.dictionaryapi.dev/api/v2/entries/{}/{}".format(language, lookup_word)
        
        response = requests.get(url).json()
        
        word_types = []
        definitions = []
        examples = []
        synonyms = []
        dictionaryWord = []

        try:
            word = response[0]["word"]
            for i in range(len(response[0]["meanings"])):
                word_type = response[0]["meanings"][i]["partOfSpeech"]
                word_types.append(word_type)

                try:
                    definition = response[0]["meanings"][i]["definitions"][0]["definition"]
                    definitions.append(definition)
                except KeyError:
                    definition = ""
                    definitions.append(definition)

                try:
                    example = response[0]["meanings"][i]["definitions"][0]["example"]
                    examples.append(example)
                except KeyError:
                    example = ""
                    examples.append(example)
                try:
                    synonym = response[0]["meanings"][i]["definitions"][0]["synonyms"]
                    synonyms.append(synonym)
                except KeyError:
                    synonym = ""
                    synonyms.append(synonym)
        except KeyError:
            print("We could not find the definition of the word you are looking for")

        dictionaryWord = list(zip(word_types, definitions, examples, synonyms))
    
    word_caps = word.capitalize()
    context = {
        "word": word_caps,
        "dictionary_word": dictionaryWord,
    }

    return render(request, "dictionary/dictionary.html", context)