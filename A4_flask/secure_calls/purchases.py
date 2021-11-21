from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from psycopg2 import sql
import json

from tools.logging import logger

def handle_request():
    logger.debug("Get Purchases Handle Request")

    un = request.args.get('username')
    
    cur = g.db.cursor()
    cur.execute(sql.SQL("SELECT (title, author, price) FROM cart WHERE customer = %s;"),(un,))
    buylist = cur.fetchall()
    cur.close()
    
    message = '{"buylist":['
    for b in buylist:
       
        if count < len(buylist) :
            message += '{"title":"'+str(b[0]) + '","author":"' + str(b[1]) + '","price":"' + str(b[2]) +'"},'
            count=count+1
        else:
            message += '{"title":"'+str(b[0]) + '","author":"' + str(b[1]) + '","price":"' + str(b[2]) +'"}'
    message += "]}"


    print(message)
    return json_response( token = create_token( g.jwt_data) , data = json.loads(message))
