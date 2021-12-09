from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
import bcrypt
import psycopg2
from psycopg2 import sql

from tools.logging import logger

def handle_request():

    logger.debug("Login Handle Request")
    #use data here to auth the user

    pw = request.form['password']
    un = request.form['username']

    cur = g.db.cursor()

    cur.execute(sql.SQL("SELECT * FROM users WHERE username = %s;"),(un,))
    u_cred = cur.fetchone() #store the id associated with the requested username from the db
    
    #check user credentials agains the db
    if u_cred is not None:    #if no such user exists in the db
        logger.debug("Username already exists")
        return json_response( status_= 401, message= "Username already exists", authentication = False)

    else: #if the user exists and the password matches
        salty_pw = bcrypt.hashpw(bytes(pw, "utf-8"), bcrypt.gensalt(10))

        cur.execute(sql.SQL("INSERT INTO users (username, password) VALUES(%s, %s);"),(un,salty_pw.decode("utf-8")))
        cur.close()
        g.db.commit()
        logger.debug("Successful Signup, Welcome " + un)

        return "successful signup"
