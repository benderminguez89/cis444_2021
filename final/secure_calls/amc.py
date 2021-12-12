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

    key = os.environ.get('AMC_API')

    now_playing = 'https://api.amctheatres.com/v2/movies/views/now-playing'
    coming_soon = 'https://api.amctheatres.com/v2/movies/views/coming-soon'
    local = 'https://api.amctheatres.com/v2/theatres?state=california&city=sandiego'
    headers={'X-AMC-Vendor-Key': key}
    response = req.get(now_playing, headers)
    c_response = req.get(coming_soon, headers)

    textResponse = response.text

    data = json.loads(textResponse)
    d = data["_embedded"]["movies"]

    movies = '{"now_playing":['
    print("\nNOW PLAYING:")
    for a in d:
        movie = a.get("sortableName")
        print(movie)
        movies += '{"title":"'+str(movie)+'"},'
    
        movies += "]}"

    txtResponse = c_response.text

    c_data = json.loads(txtResponse)
    c_d = c_data["_embedded"]["movies"]

    coming_soon = '{"coming_soon":['
    print("\nCOMING SOON:")
    for b in c_d:
        c_movie = b.get("sortableName")
        print(c_movie)
        coming_soon += '{"title":"'+str(movie)+'"},'
    
    coming_soon += "]}"
    print(movies, coming_soon)
    return json_response(token = create_token( g.jwt_data ), data= json.loads(movies, coming_soon))
    
