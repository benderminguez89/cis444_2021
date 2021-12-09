from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from psycopg2 import sql
import json

from tools.logging import logger

def handle_request():
    logger.debug("Get Purchases Handle Request")
    
    un = g.jwt_data['sub']
    
    cur = g.db.cursor()
    cur.execute(sql.SQL("SELECT title, author, price FROM cart WHERE customer = %s;"),(un,))
    buylist = cur.fetchall()
    cur.close()

    count = 1
    books = '{"books":['
    for b in buylist:
        if count < len(buylist) :
            books += '{"title":"'+str(b[0]) + '","author":"' + str(b[1]) + '","price":"' + str(b[2]) +'"},'
            count += 1
        else:
            books += '{"title":"'+str(b[0]) + '","author":"' + str(b[1]) + '","price":"' + str(b[2]) +'"}'
    books += "]}"

    logger.debug(books)
    g.jwt_data['books'] = books

    return json_response( token = create_token( g.jwt_data ) , data= json.loads(books))
