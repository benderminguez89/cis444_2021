import ticketpy

from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from psycopg2 import sql
import json

from tools.logging import logger

def handle_request():
    logger.debug("Lets find some tickets")

    cur = g.db.cursor()
    cur.execute(sql.SQL("SELECT genre FROM music;"))
    genres = cur.fetchall()
    cur.close()
    
    # input api key
    consumer_key = ''
    consumer_secret = ''
    tm_client = ticketpy.ApiClient(consumer_key)

    
    pages = tm_client.events.find(
        classification_name= 'Alternative Rock',
        city = 'San Diego',
        startDateTime = '2021-12-16T20:00:00Z',
        end_date_time= '2022-12-16T20:00:00Z'
    ).limit(10)

    events = '{"concerts":['
    for event in pages:
        if event[0] < len(pages):
            events += '{"name:"' +str(event.name) + '", status:"' + str(event.status)
            print(event.name, event.status, event.price_ranges, event.local_start_date, event.local_start_time)
        events += "]}"

    return json_response( token = create_token( g.jwt_data ), data= json.loads(events))
