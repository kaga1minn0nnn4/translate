import nltk
import deepl

def word_analysis(sentence):
    token = nltk.word_tokenize(sentence)
    parts = nltk.pos_tag(token)
    return [part[0] for part in parts if part[1] in ('NNP','NNPS','PRP','PRP$','WP','WP$')]

def ja2en(ja):
    translator = deepl.Translator("8860ea8a-bed6-a3a0-06ff-977d247797eb:fx")
    return str(translator.translate_text(ja, target_lang="EN-US"))
