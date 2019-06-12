#! /usr/bin/python
# -*- coding:utf-8 -*-
import regex as re
import requests
import wikipedia
# test in the regex 
def reg(demande):
	demande = demande.lower()
	demande = re.sub(r"\p{P}+", r"", demande)
	return(demande)

def test_reg():
    assert reg('CONNAIS-TU OPENCLASSROOMS FRANCE') == 'connaistu openclassrooms france'

def sup_stop_word(demande):

	demande = demande.split()
	stop_word_fr = ["connais","grandpy","salut","estce","connaistu","a","abord","absolument","afin","ah","ai","aie","ailleurs","ainsi","ait","allaient","allo","allons","allô","alors","anterieur","anterieure","anterieures","apres","après","as","assez","attendu","au","aucun","aucune","aujourd","aujourd'hui","aupres","auquel","aura","auraient","aurait","auront","aussi","autre","autrefois","autrement","autres","autrui","aux","auxquelles","auxquels","avaient","avais","avait","avant","avec","avoir","avons","ayant","b","bah","bas","basee","bat","beau","beaucoup","bien","bigre","boum","bravo","brrr","c","car","ce","ceci","cela","celle","celle-ci","celle-là","celles","celles-ci","celles-là","celui","celui-ci","celui-là","cent","cependant","certain","certaine","certaines","certains","certes","ces","cet","cette","ceux","ceux-ci","ceux-là","chacun","chacune","chaque","cher","chers","chez","chiche","chut","chère","chères","ci","cinq","cinquantaine","cinquante","cinquantième","cinquième","clac","clic","combien","comme","comment","comparable","comparables","compris","concernant","contre","couic","crac","d","da","dans","de","debout","dedans","dehors","deja","delà","depuis","dernier","derniere","derriere","derrière","des","desormais","desquelles","desquels","dessous","dessus","deux","deuxième","deuxièmement","devant","devers","devra","different","differentes","differents","différent","différente","différentes","différents","dire","directe","directement","dit","dite","dits","divers","diverse","diverses","dix","dix-huit","dix-neuf","dix-sept","dixième","doit","doivent","donc","dont","douze","douzième","dring","du","duquel","durant","dès","désormais","e","effet","egale","egalement","egales","eh","elle","elle-même","elles","elles-mêmes","en","encore","enfin","entre","envers","environ","es","est","et","etant","etc","etre","eu","euh","eux","eux-mêmes","exactement","excepté","extenso","exterieur","f","fais","faisaient","faisant","fait","façon","feront","fi","flac","floc","font","g","gens","h","ha","hein","hem","hep","hi","ho","holà","hop","hormis","hors","hou","houp","hue","hui","huit","huitième","hum","hurrah","hé","hélas","i","il","ils","importe","j","je","jusqu","jusque","juste","k","l","la","laisser","laquelle","las","le","lequel","les","lesquelles","lesquels","leur","leurs","longtemps","lors","lorsque","lui","lui-meme","lui-même","là","lès","m","ma","maint","maintenant","mais","malgre","malgré","maximale","me","meme","memes","merci","mes","mien","mienne","miennes","miens","mille","mince","minimale","moi","moi-meme","moi-même","moindres","moins","mon","moyennant","multiple","multiples","même","mêmes","n","na","naturel","naturelle","naturelles","ne","neanmoins","necessaire","necessairement","neuf","neuvième","ni","nombreuses","nombreux","non","nos","notamment","notre","nous","nous-mêmes","nouveau","nul","néanmoins","nôtre","nôtres","o","oh","ohé","ollé","olé","on","ont","onze","onzième","ore","ou","ouf","ouias","oust","ouste","outre","ouvert","ouverte","ouverts","o|","où","p","paf","pan","par","parce","parfois","parle","parlent","parler","parmi","parseme","partant","particulier","particulière","particulièrement","pas","passé","pendant","pense","permet","personne","peu","peut","peuvent","peux","pff","pfft","pfut","pif","pire","plein","plouf","plus","plusieurs","plutôt","possessif","possessifs","possible","possibles","pouah","pour","pourquoi","pourrais","pourrait","pouvait","prealable","precisement","premier","première","premièrement","pres","probable","probante","procedant","proche","près","psitt","pu","puis","puisque","pur","pure","q","qu","quand","quant","quant-à-soi","quanta","quarante","quatorze","quatre","quatre-vingt","quatrième","quatrièmement","que","quel","quelconque","quelle","quelles","quelqu'un","quelque","quelques","quels","qui","quiconque","quinze","quoi","quoique","r","rare","rarement","rares","relative","relativement","remarquable","rend","rendre","restant","reste","restent","restrictif","retour","revoici","revoilà","rien","s","sa","sacrebleu","sait","sans","sapristi","sauf","se","sein","seize","selon","semblable","semblaient","semble","semblent","sent","sept","septième","sera","seraient","serait","seront","ses","seul","seule","seulement","si","sien","sienne","siennes","siens","sinon","six","sixième","soi","soi-même","soit","soixante","son","sont","sous","souvent","specifique","specifiques","speculatif","stop","strictement","subtiles","suffisant","suffisante","suffit","suis","suit","suivant","suivante","suivantes","suivants","suivre","superpose","sur","surtout","t","ta","tac","tant","tardive","te","tel","telle","tellement","telles","tels","tenant","tend","tenir","tente","tes","tic","tien","tienne","tiennes","tiens","toc","toi","toi-même","ton","touchant","toujours","tous","tout","toute","toutefois","toutes","treize","trente","tres","trois","troisième","troisièmement","trop","très","tsoin","tsouin","tu","té","u","un","une","unes","uniformement","unique","uniques","uns","v","va","vais","vas","vers","via","vif","vifs","vingt","vivat","vive","vives","vlan","voici","voilà","vont","vos","votre","vous","vous-mêmes","vu","vé","vôtre","vôtres","w","x","y","z","zut","à","â","ça","ès","étaient","étais","était","étant","été","être","ô"]
	k=(set(demande).difference(stop_word_fr))
	k= list(k) 
	return(k)
def test_sup_stop_word():
    assert sup_stop_word('connaistu openclassrooms france') == ['openclassrooms', 'france']

#first test mock in API Google Maps
def first_test_map(query):
	l = {}
	search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
	
	search_payload = {"key":"AIzaSyDccQ-E6Xu1DGKn4ntp6-1oTdWnjrxzdWM", "query":query}
	search_req = requests.get(search_url, params = search_payload)
	search_json = search_req.json()
	
	place_id = search_json["results"][0]["place_id"]
	lat = search_json["results"][0]["geometry"]["location"]["lat"]
	lng = search_json["results"][0]["geometry"]["location"]["lng"]
	l['lat'] = lat
	l['lng'] = lng
	l['place_Id'] = place_id
	return(l)

def test_with_request_get_mock(monkeypatch):
	result = {'lat': 48.8748465, 'lng': 2.3504873, 'place_Id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'}

	class MockResponse:
		def json(self):
			return({
   					"html_attributions" : [],
   								"results" : [
      				{
         				"geometry" : {
            				"location" : {
               				"lat" :  48.8748465,
               				"lng" :  2.3504873
            		}
         		},
         		
         		
         		"place_id" : 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'}]})

         		
            	
	def mock_requests_get(url,  params):
		return MockResponse()
	monkeypatch.setattr('requests.get', mock_requests_get)
	assert first_test_map("openclassrooms France") == result
def wiki(v):
	wikipedia.set_lang("fr")
	g=wikipedia.summary(v, sentences=1)
	return(g)

def test_with_wikipedia_summary(monkeypatch):
	result = "OpenClassrooms est une école en ligne qui propose à ses membres des cours certifiants et des parcours débouchant sur un métier d'avenir, réalisés en interne, par des écoles, des universités, ou encore par des entreprises partenaires comme Microsoft ou IBM. Jusqu'en 2018, n'importe quel membre du site pouvait être auteur, via un outil nommé 'Course Lab'."

	def mock_wikipedia_summary(v, sentences):
		return("OpenClassrooms est une école en ligne qui propose à ses membres des cours certifiants et des parcours débouchant sur un métier d'avenir, réalisés en interne, par des écoles, des universités, ou encore par des entreprises partenaires comme Microsoft ou IBM. Jusqu'en 2018, n'importe quel membre du site pouvait être auteur, via un outil nommé 'Course Lab'.")
	
	monkeypatch.setattr('wikipedia.summary', mock_wikipedia_summary)
	assert wiki("openclassrooms France") == result