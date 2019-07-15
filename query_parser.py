#! /usr/bin/python
# -*- coding:utf-8 -*-

# Module import
import regex as re
from stop_word import stop_word_fr


# function to delete punctuation
def reg(query):
    query = query.lower()
    query = re.sub(r"\p{P}+", r"", query)
    return(query)
# function to delete stop_word


def sup_stop_word(query):
    query = query.split()
    k = set(query).difference(stop_word_fr)
    return(k)

# function for parsing a user text


def text_parse(query):
    query = reg(query)
    k = sup_stop_word(query)
    k = list(k)
    query = re.sub(r"\p{P}+", r" ", ','.join(k))
    return(query)
# function for parsing adress


def text_parse_wiki(query):
    # variable initiate
    adress_2 = ''
    coma = ","
    cpt = 0
    # count coma number
    if coma in query:
        for letter in query:
            if letter == coma:
                cpt = cpt + 1
            if cpt == 2:
                # convert query in liste
                adress_2 = query.split(",")
                del adress_2[2]
                # convert query in string
                adress_2 = re.sub(r"\p{P}+", r"", ','.join(adress_2))
                # drop a number
                adress_2 = re.sub(r"\d", r"", adress_2)
            elif cpt == 1:
                adress_2 = query.split(",")
                adress_2 = re.sub(r"\p{P}+", r"", ','.join(adress_2))
    else:
        adress_2 = query
    return(adress_2)
