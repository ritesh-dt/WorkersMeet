from django import template

from googletrans import Translator

register = template.Library()

code_to_lang = {
    "0": "en",
    "1": "hi",
    "2": "mr"
}

@register.simple_tag
def trans(text, dest=None):
    if dest is None or dest == "en":
        return text
    if dest not in code_to_lang.items():
        dest = dest.split("/")[1]
    if dest == "0":
        return text

    translator = Translator()
    textDict = translator.translate(text, dest=code_to_lang[dest])
    return textDict.__dict__()["text"]