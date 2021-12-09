from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from psycopg2 import sql
import json

from tools.logging import logger

def handle_request():
    logger.debug("Friend Requests Handle Request")
        
    cur = g.db.cursor()
    cur.execute(sql.SQL("SELECT * FROM friends WHERE status = pending;"))
    requests = cur.fetchall()
    cur.close()
    
    #checks for new friend requests
    if requests is not NONE:    
        friend_reqs = '{"friends":['
        for b in requests:
            if b[0] < len(requests) :
                friend_reqs += '{"username":"'+str(b[2]) + '","id":"' + str(b[3]) +'"},'
            else:
                friend_reqs += '{"username":"'+str(b[2]) + '","id":"' + str(b[3]) +'"}'
                friend_reqs += "]}"
        return json_response( token = create_token(  g.jwt_data ) , data= json.loads(friend_reqs))

    #if no new friend requests            
    logger.debug("No new friend requests")

    
