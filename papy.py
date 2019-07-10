#! /usr/bin/python
# -*- coding:utf-8 -*-

# Import modules


from flask import Flask, request, render_template, jsonify
from query_parser import *
from map import *
from wiki import *


# Flask app initialisation

app = Flask(__name__)


@app.route('/')
def index_1():
    return render_template('for_m.html')

# Route create
@app.route('/process', methods=['POST'])
def process():
    place_id = 'AFCCGG'
    # process to catch a user text
    query_0 = request.form['query']
    output = "Salut Poussin ton message se resume ainsi ! : \
    je veux connaitre le lieu qui ressort de cette phrase: " + query_0
    # using parse function
    query = text_parse(query_0)
    # initialization for Map Class
    m = Map_G(query)
    # Application of method class coord_map
    if m.coord_map() == {}:
        return jsonify({'output': "Mon poussin tu me fais reflechir \
                        sans succès.Ajoute le pays de ta recherche"})
    else:
        # recuperation of place_Id
        place_id = m.coord_map()["place_Id"]
        # Application of method class coord_adress
        adress = m.coord_adress(place_id)
        # using the second text function
        adress_wiki = text_parse_wiki(adress)
        # instance for Wiki class
        wik = Wiki(adress_wiki)
        adress_1 = "Bien sûr mon poussin ! La voici: " + adress
        # Application of method class wiki_inf()
        if wik.wiki_inf()['url'] == '':
            wiki = "Mon poussin je ne me souviens plus  \
                     de l'histoire de ce lieu"
        else:
            wiki = "Mais t'ai-je déjà raconté l'histoire \
                    de ce quartier qui m'a vu en culottes \
                    courtes ?" + wik.wiki_inf()['text'] + "\n" + \
                    "Si tu veux en savoir plus mon poussin voici \
                    le lien wikipedia: "
        if query_0:
            # sending data
            return jsonify({'output': output,
                            'lat': m.coord_map()["lat"],
                            'lng': m.coord_map()["lng"],
                            'place_id': m.coord_map()["place_Id"],
                            'wiki': wiki, 'adress': adress_1,
                            'url': wik.wiki_inf()['url']})


if __name__ == '__main__':
    app.run(debug=True)
