from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from psycopg2 import sql
import json

from tools.logging import logger

def handle_request():
    logger.debug("Get Books Handle Request")
    in_jwt = request.args.get("jwt")
    
    cur = g.db.cursor()
    cur.execute(sql.SQL("SELECT * FROM books;"))
    catalogue = cur.fetchall()
    cur.close()

    booklist = '{"books":['
    for b in catalogue:
        if b[0] < len(catalogue) :
            booklist += '{"title":"'+str(b[1]) + '","author":"' + str(b[2]) + '","price":"' + str(b[3]) +'"},'
        else:
            booklist += '{"title":"'+str(b[1]) + '","author":"' + str(b[2]) + '","price":"' + str(b[3]) +'"}'
    booklist += "]}"
    
    return json_response( token = create_token(  g.jwt_data ) , data= json.loads(booklist))

