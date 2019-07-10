#! /usr/bin/python
# -*- coding:utf-8 -*-

# Module Import
import regex as re
import wikipedia


class Wiki:
    """This class represent the API Wikipedia Using """
    def __init__(self, adress):
        self.adress = adress

    # Method a wrapper of wikipedia API
    def wiki_inf(self):
        inf = {}
        try:
            # try to load the wikipedia page
            wikipedia.set_lang("fr")
            d = wikipedia.page(self.adress)
            wiki = wikipedia.summary(self.adress, sentences=2)
            inf['text'] = wiki
            inf['url'] = d.url
        # catch a Page exception error
        except wikipedia.exceptions.PageError:
            inf['text'] = "la page n'existe pas sur wikipedia"
            inf['url'] = ''
        except wikipedia.exceptions.DisambiguationError:
            inf['text'] = "la page n'existe pas sur wikipedia"
            inf['url'] = ''
        return(inf)
