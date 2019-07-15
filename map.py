#! /usr/bin/python
# -*- coding:utf-8 -*-

# Module and class import
import requests
from key import Key


class Map_G:
    """This class represent the coordinates of lat long and adress"""
    def __init__(self, query):
        self.query = query
        self.adress = 0
    # Method to take a lont and lat of the query

    def coord_map(self):
        coord = {}
        # Using google map place API
        search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        # parameters of API
        search_payload = {"key": Key, "query": self.query}
        search_req = requests.get(search_url, params=search_payload)
        search_json = search_req.json()
        # take of lat and lont of map
        if search_json['results'] == []:
            coord = {}
        else:
            place_id = search_json["results"][0]["place_id"]
            lat = search_json["results"][0]["geometry"]["location"]["lat"]
            lng = search_json["results"][0]["geometry"]["location"]["lng"]
            coord['lat'] = lat
            coord['lng'] = lng
            coord['place_Id'] = place_id
        return(coord)

    # Method to take adress of the query
    def coord_adress(self, place_id):
        # Using google map place details  API
        details_url = "https://maps.googleapis.com/maps/api/place/details/json"
        details_payload = {"key": Key, "placeid": place_id}
        details_resp = requests.get(details_url, params=details_payload)
        details_json = details_resp.json()
        if details_json == {'html_attributions': [],
                            'status': 'INVALID_REQUEST'}:
            self.adress = ''
        else:
            # adress of place research
            self.adress = details_json["result"]["formatted_address"]
