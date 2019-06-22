#! /usr/bin/python
# -*- coding:utf-8 -*-

# Import modules

import requests
from flask import Flask,request,render_template,jsonify
import parser
import regex as re
import wikipedia
from query_parser import test_parse
from key import Key

# Flask app initialisation

app = Flask(__name__)

@app.route('/')
def index_1():
	return render_template('formulaire.html')	

# Route create

@app.route('/process',methods= ['POST'])

def process():
	# process to catch a user text
	demande = request.form['demande']
	
	output = "Salut Poussin ton message se resume ainsi ! : je veux connaitre le lieu qui ressort de cette phrase: " + demande
	# using parse function
	query = test_parse(demande)
	# using API Google Maps for search	
	search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
	details_url = "https://maps.googleapis.com/maps/api/place/details/json"
	search_payload = {"key":Key, "query":query}
	search_req = requests.get(search_url, params = search_payload)
	search_json = search_req.json()
	# place_id of place research
	place_id = search_json["results"][0]["place_id"]
	# lat of place research
	lat = search_json["results"][0]["geometry"]["location"]["lat"]
	# lont of place research
	lng = search_json["results"][0]["geometry"]["location"]["lng"]
	details_payload= {"key":Key, "placeid":place_id}
	details_resp = requests.get(details_url, params = details_payload)
	details_json = details_resp.json()
	# adress of place research
	adress = details_json["result"]["formatted_address"]
	adress_1 = "Bien sûr mon poussin ! La voici: " + adress
	adress = adress.split(",")
	del adress[1]
	adress =  re.sub(r"\p{P}+", r" ", ','.join(adress))
	
	wikipedia.set_lang("fr")
	wiki = wikipedia.summary(adress, sentences=2)
	d = wikipedia.page(adress)
	url = d.url
	
	wiki = "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ?"+wiki+ "\n"+ "Si tu veux en savoir plus mon poussin voici le lien wikipedia: "
	if demande:
		return jsonify({'output':output, 'lat':lat, 'lng':lng, 'place_id':place_id,'wiki':wiki, 'adress':adress_1,
			           'url': url})


if __name__ == '__main__':
	app.run(debug=True)

  