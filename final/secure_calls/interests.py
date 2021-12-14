
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from psycopg2 import sql
import json

from tools.logging import logger


def handle_request():
    logger.debug("Add to Cart Handle Request")

    un = request.args.get('username')
    event = request.args.get('title')
    logger.debug(event)
    logger.debug(request.args.get('username'))
    
    cur = g.db.cursor()
    cur.execute(sql.SQL("SELECT * FROM interests WHERE event = %s AND username = %s;"),(event,un))
    info = cur.fetchone()
    logger.debug(info)

    if info is None:
        cur.execute(sql.SQL("INSERT INTO interests (event, username) VALUES(%s, %s);"),(event,un))

        cur.close()    
        g.db.commit()
        return "Added "+event+ " to your interests"

    
    return "You're already interested in that!"
