#! /usr/bin/python
# -*- coding:utf-8 -*-
import requests
from flask import Flask,request,render_template,jsonify
import parser
import regex as re
import wikipedia
from query_parser import test_parse
from key import Key
app = Flask(__name__)

@app.route('/')
def index_1():
	return render_template('formulaire.html')


	

@app.route('/process',methods= ['POST'])

def process():
	
	demande = request.form['demande']
	# lastName = request.form['lastName']
	output = "Salut Poussin ton message se resume ainsi ! : je veux connaitre le lieu qui ressort de cette phrase: " + demande
	# 	query = request.form['demande']
	query = test_parse(demande)
		
	search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
	details_url = "https://maps.googleapis.com/maps/api/place/details/json"
	search_payload = {"key":Key, "query":query}
	search_req = requests.get(search_url, params = search_payload)
	search_json = search_req.json()
	
	place_id = search_json["results"][0]["place_id"]
	lat = search_json["results"][0]["geometry"]["location"]["lat"]
	lng = search_json["results"][0]["geometry"]["location"]["lng"]
	details_payload= {"key":Key, "placeid":place_id}
	details_resp = requests.get(details_url, params = details_payload)
	details_json = details_resp.json()
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

# @app.route('/process_1',methods= ['GET'])
# def index():
# 	query = request.form['demande']
# 	query = test_parse(query)		
# 	search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
# 	details_url = "https://maps.googleapis.com/maps/api/place/details/json"
# 	search_payload = {"key":"AIzaSyDccQ-E6Xu1DGKn4ntp6-1oTdWnjrxzdWM", "query":query}
# 	search_req = requests.get(search_url, params = search_payload)
# 	search_json = search_req.json()
	
# 	place_id = search_json["results"][0]["place_id"]
# 	lat = search_json["results"][0]["geometry"]["location"]["lat"]
# 	lng = search_json["results"][0]["geometry"]["location"]["lng"]
	
# 	return render_template('formulaire.html', placeId = place_id, lat = lat, lng = lng)

# 	elif firstName == '' and lastName == '':
# 		return jsonify({'error' : 'Missing data!'})
# @app.route('/process',methods= ['GET'])
# def retreive():
# 	return render_template('formulaire.html', placeId = place_id, lat = lat, lng = lng)

# @app.route('/sendRequest/',methods= ['GET'])

# def result(query):	

# 	query = request.form['demande']
# 	query = test_parse(query)		
# 	search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
# 	details_url = "https://maps.googleapis.com/maps/api/place/details/json"
# 	search_payload = {"key":"AIzaSyDccQ-E6Xu1DGKn4ntp6-1oTdWnjrxzdWM", "query":query}
# 	search_req = requests.get(search_url, params = search_payload)
# 	search_json = search_req.json()
	
# 	place_id = search_json["results"][0]["place_id"]
# 	lat = search_json["results"][0]["geometry"]["location"]["lat"]
# 	lng = search_json["results"][0]["geometry"]["location"]["lng"]
# 	details_payload = {"key":"AIzaSyDccQ-E6Xu1DGKn4ntp6-1oTdWnjrxzdWM","placeid":place_id}
# 	details_resp = requests.get(details_url, params = details_payload)
# 	details_json = details_resp.json()
# 	url = details_json["result"]["url"]
# 	return jsonify({'result':url})
if __name__ == '__main__':
	app.run(debug=True)

  