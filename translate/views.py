from django.shortcuts import render
from .models import Sentence
from .controller import word_analysis, ja2en

# Create your views here.

def translate(request):
    params = {}
    if request.POST.get("Japanese", None):
        sentence = Sentence()

        sentence.ja_str = request.POST["Japanese"]
        sentence.en_str = ja2en(sentence.ja_str)
        sentence.en_count = len(str(sentence.en_str).split(" "))
        sentence.analysis_words = ", ".join(word_analysis(sentence.en_str))

        params["sentence"] = sentence

    return render(request, "translate/translate.html", params)
