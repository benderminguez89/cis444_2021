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
    
    password_from_user_form = request.form['password']
    logger.debug(request.form['firstname'])
    user = {
            "sub" : request.form['firstname'] #sub is used by pyJwt as the owner of the token
            }

    cur = g.db.cursor()

    cur.execute(sql.SQL("SELECT * FROM users WHERE username = %s;"),(request.form['firstname'],))
    u_cred = cur.fetchone() #store the id associated with the requested username from the db
    cur.close()

    #check user credentials agains the db
    if u_cred[0] is None:    #if no such user exists in the db
        logger.debug("No such user")
        return json_response( status_= 401, message= "No such user ", authentication = False)

    else: #if the user exists and the password matches
        if bcrypt.checkpw(bytes(password_from_user_form, "utf-8"), bytes(u_cred[2], "utf-8")) == True:
            print("Successful Login, Welcome Back: " + str(request.form['firstname']))
 
            return json_response( token= create_token(user), authenticated = True)
        else:
            print("Imposter! Thats not the password!!")

            return json_response(status_ = 401, data={"message": "Incorrect Password"}, authenticated = False)
    
    
    if not user:
        return json_response(status_=401, message = 'Invalid credentials', authenticated =  False )

    return json_response( token = create_token(user) , authenticated = False)

