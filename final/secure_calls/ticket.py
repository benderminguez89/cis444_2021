import ticketpy
from datetime import date, timedelta
import os

from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from psycopg2 import sql
import json

from tools.logging import logger

def handle_request():
    logger.debug("Get Books Handle Request")

    now = date.today()
    til = timedelta(weeks=52)
    til = now + til
    print("searching for events from:"+str(now)+" until: "+str(til))
    
    key = 'Scjv74PwIErH2jthOFDmmAZPE8f0OWGq'#os.environ.get('TIX_API')


    tm_client = ticketpy.ApiClient(key)

    pages = tm_client.events.find(
        city='San Diego',
        startDateTime= str(now) +'T20:00:00Z',
        end_date_time= str(til) +'T20:00:00Z'
    ).limit(2)

    print("\nUpcoming Events in San Diego:")
    events = '{"events":['
    for p in pages:
        events += '{"title":"'+str(p.name)+'"},'
        print(p.name)
    events += '{"end":"none"}]}'

    return json_response( token = create_token(  g.jwt_data ) , data= json.loads(events, strict=False))
