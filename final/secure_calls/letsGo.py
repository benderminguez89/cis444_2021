
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from psycopg2 import sql
import json

from tools.logging import logger


def handle_request():
    logger.debug("Add to Cart Handle Request")

    un = request.args.get('username') 

    logger.debug(un)
    
    cur = g.db.cursor()
    cur.execute(sql.SQL("SELECT event FROM interests WHERE username = %s;"),(un,))
    info = cur.fetchall()
    logger.debug(info)

    if info is None:
        return "Pick some events you're interested in!"


    letsgo = '{"events":['

    for i in info:
        cur.execute(sql.SQL("SELECT event, username FROM interests WHERE event = %s AND username != %s;"),(i,un))
        events = cur.fetchall()

        logger.debug(events)
        

        count = 0
        for e in events:
            if(count < len(events)):
                letsgo += '{"event":"'+str(e[0])+'","friend":"'+str(e[1])+'"},'
                count += 1
            else:
               letsgo += '"friend":"'+str(e[1])+'"}'
               count +=1
    letsgo += '{"end":"None"}]}'

    print(letsgo)
               
    return json_response(token = create_token( g.jwt_data ), data= json.loads(letsgo, strict = False))
