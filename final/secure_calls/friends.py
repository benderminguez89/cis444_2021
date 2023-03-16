from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from psycopg2 import sql
import json

from tools.logging import logger


def handle_request():
    logger.debug("Friends")

    un = request.args.get('username')
    friend = request.args.get('f_username')
    logger.debug(event)
    logger.debug(request.args.get('username'))

    cur = g.db.cursor()
    cur.execute(sql.SQL("SELECT * FROM  friends WHERE username = %s;"),(un,))
    info = cur.fetchone()
    logger.debug(info)

    '''
    Friend suggestions should be sourced based on common interests/mutual friends/locality
    ---- profile setting around privacy should also be factored in
    ---- if this is a pending request signal they shouldnt be appearing as a potential friend
    ---- have I blocked their request previously?, if so do not add to suggested list
    ---- 
    __________________________________________________________________________________________
    Requests, Approvals, Blocking:    
    - check if a friend by f_name exists in any status
    ----- if not allow request, add to db with pending status
    - else(already exists) 
    - is this a pending request by me
    - subsequent check, is this a pending request by them
    ----- if so, populate buttons to approve, reject or blcok requests
    '''

    if info is None:
        cur.execute(sql.SQL("INSERT INTO friendss (username, f_name, status) VALUES(%s, %s);"),(un, f_name, "requested"))

        cur.close()
        g.db.commit()
        return "Request sent to " +friend


    return "You're already interested in that!"
