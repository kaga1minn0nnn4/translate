from django.shortcuts import render
import deepl
from .models import Sentence

# Create your views here.

def translate(request):
    if request.method == "POST":
        sentence = Sentence()

        sentence.ja_str = request.POST["Japanese"]
        translator = deepl.Translator("8860ea8a-bed6-a3a0-06ff-977d247797eb:fx")
        sentence.en_str = translator.translate_text(sentence.ja_str, target_lang="EN-US")
        sentence.en_count = len(str(sentence.en_str).split(" "))

        return render(request, "translate/translate.html", {"sentence": sentence})
    else:
        return render(request, "translate/translate.html", {})
