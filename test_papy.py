#! /usr/bin/python
# -*- coding:utf-8 -*-
import regex as re
import requests
import wikipedia
from map import *
from query_parser import *
from stop_word import *
from wiki import *
# unit test for delete punctuation function


def reg(demande):
    demande = demande.lower()
    demande = re.sub(r"\p{P}+", r"", demande)
    return(demande)
# test with pytest


def test_reg():
    assert reg('CONNAIS-TU OPENCLASSROOMS FRANCE') ==
                'connaistu openclassrooms france'


def test_text_parse_wiki():
    assert text_parse_wiki('7 Cité Paradis, 75010 Paris, France')
                            == " Cité Paradis  Paris"

# Test mock of  API Google Maps  using mock
# query sucess map instance for coordinates


m_success = Map_G("Openclassroom France ")


def test_with_request_get_mock_success(monkeypatch):
    result = {'lat': 48.8748465, 'lng': 2.3504873,
              'place_Id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'}

    class MockResponse:
        def json(self):
            return({
                    "html_attributions": [],
                                "results": [
                    {
                        "geometry": {
                            "location": {
                            "lat":  48.8748465,
                            "lng":  2.3504873
                    }
                },
                "place_id": 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'}]})

    def mock_requests_get_sucess_1(url,  params):
        return MockResponse()
    monkeypatch.setattr('requests.get', mock_requests_get_sucess_1)
    assert m_success.coord_map() == result


def test_with_request_get_mock_success_adres(monkeypatch):
    m_success.coord_adress('ChIJIZX8lhRu5kcRGwYk8Ce3Vc8')
    result = "7 Cité Paradis, 75010 Paris, France"

    class MockResponse:
        def json(self):
            return({'html_attributions': [],
                    'result': {"formatted_address":
                    "7 Cité Paradis, 75010 Paris, France"}})

    def mock_requests_get_adress_succes(url,  params):
        return MockResponse()
    monkeypatch.setattr('requests.get', mock_requests_get_adress_succes)
    assert m_success.coord_adress('ChIJIZX8lhRu5kcRGwYk8Ce3Vc8') == result

# query fail initialize for coordinates


def test_with_request_get_mock_fail(monkeypatch):
    m_fail = Map_G("Openclassroom ")
    result = {}

    class MockResponse:
        def json(self):
            return({
                    "html_attributions": [],
                                "results": []})

    def mock_requests_get_fail(url, params):
        return MockResponse()
    monkeypatch.setattr('requests.get', mock_requests_get_fail)
    assert m_fail.coord_map() == result


def test_with_request_get_mock_fail_adres(monkeypatch):
    m_fail_adres = Map_G("Openclassroom  France")
    result = ''

    class MockResponse:
        def json(self):
            return({'html_attributions': [], 'status': 'INVALID_REQUEST'})

    def mock_requests_get_adress_fail(url,  params):
        return MockResponse()
    monkeypatch.setattr('requests.get', mock_requests_get_adress_fail)
    assert m_fail_adres.coord_adress('AFCCGG') == result

# Test mock of  API Wiki Media sucess


def test_with_wikipedia_summary_sucess(monkeypatch):
    wiki = Wiki("Cité Paradis Paris")
    wiki.wiki_inf()
    result = 'La cité Paradis est une voie publique située \
              dans le 10e arrondissement de Paris.'

    def mock_wikipedia_summary(v, sentences):
        return result
    monkeypatch.setattr('wikipedia.summary', mock_wikipedia_summary)
    assert wiki.wiki_inf()['text'] == result
# Test mock of  API Wiki Media failed 1


def test_with_wikipedia_summary_fail_1(monkeypatch):
    wiki = Wiki("NonExistingPageWithStrangeName")
    wiki.wiki_inf()
    result = 'la page n\'existe pas sur wikipedia'

    def mock_wikipedia_summary_fail_1(v, sentences):
        return result
    monkeypatch.setattr('wikipedia.summary', mock_wikipedia_summary_fail_1)
    assert wiki.wiki_inf()['text'] == result

# Test mock of  API Wiki Media failed 2


def test_with_wikipedia_summary_fail_1(monkeypatch):
    wiki = Wiki("Krindja")
    wiki.wiki_inf()
    result = 'la page n\'existe pas sur wikipedia'

    def mock_wikipedia_summary_fail_2(v, sentences):
        return result
    monkeypatch.setattr('wikipedia.summary', mock_wikipedia_summary_fail_2)
    assert wiki.wiki_inf()['text'] == result
