import requests as req
import os

from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from psycopg2 import sql

import json

from tools.logging import logger

def handle_request():
    logger.debug("AMC API Handle Request")

    key = '3C81C7F5-992D-4CCE-84B5-AA312D85739B'#os.environ.get('AMC_API')

    now_playing = 'https://api.amctheatres.com/v2/movies/views/now-playing'
    coming_soon = 'https://api.amctheatres.com/v2/movies/views/coming-soon'
    local = 'https://api.amctheatres.com/v2/theatres?state=california&city=sandiego'
    headers={'X-AMC-Vendor-Key': key}

    response = req.get(now_playing, headers)
    c_response = req.get(coming_soon, headers)

    txt_response = response.text
    c_txt_response = c_response.text
    
    data = json.loads(txt_response)
    d = data['_embedded']['movies']

    movies = '{"now_playing":['
    print("\nNOW PLAYING:")
    for a in d:
        movie = a.get("sortableName")
        print(movie)
        movies += '{"title":"'+str(movie)+'"},'
    
    movies += '{"end":"none"}]}'

    
    c_data = json.loads(c_txt_response)
    c_d = c_data["_embedded"]["movies"]

    coming_soon = '{"coming_soon":['
    print("\nCOMING SOON:")
    for b in c_d:
        c_movie = b.get("sortableName")
        print(c_movie)
        coming_soon += '{"title":"'+str(c_movie)+'"},'
    
    coming_soon += '{"end":"none"}]}'
    
    print(movies, coming_soon)
    return json_response(token = create_token( g.jwt_data ), data= json.loads(movies, strict = False), data2= json.loads(coming_soon, strict = False))
    
