from flask import Flask, render_template, request
from flask_json import FlaskJSON, JsonError, json_response, as_json
import jwt
import psycopg2
import datetime
import bcrypt
import db_con
import json

from db_con import get_db_instance, get_db

app = Flask(__name__)
FlaskJSON(app)

USER_PASSWORDS = {"bender": "derminguez"}


global JWT
JWT_SECRET = None

global_db_con = get_db()

with open("secret", "r") as f:
    JWT_SECRET = f.read()

########################## Insert into Cart ###############################
@app.route('/cart', methods=["POST"]) #endpoint
def cart():
    title = request.form["title"]
    cur = global_db_con.cursor()
    cur.execute("INSERT INTO cart (title, author, price) SELECT title, author, price FROM books WHERE title = '" + title + "';")
    cur.close()
    global_db_con.commit()

    print("Added book to cart.")
    return json_response(data={"message": str(title) +" added successfully."}, status=200) 

########################## Buy something ###############################
@app.route('/buy', methods=["GET"]) #endpoint
def buy():
    in_jwt = request.args.get("jwt")

    cur = global_db_con.cursor()
    cur.execute("select * from cart;")
    buylist = cur.fetchall()
    cur.close()

   
    count=1
    message = '{"buylist":['
    for b in buylist:
       
        if count < len(buylist) :
            message += '{"title":"'+str(b[1]) + '","author":"' + str(b[2]) + '","price":"' + str(b[3]) +'"},'
            count=count+1
        else:
            message += '{"title":"'+str(b[1]) + '","author":"' + str(b[2]) + '","price":"' + str(b[3]) +'"}'
    message += "]}"


    print(message)
    return json_response(data=json.loads(message), status=200)

########################## Bookstore ##################################
"""
gets a list of books available for purchase from books table in database, returns json
"""
@app.route('/bkstr', methods=["GET"]) #endpoint
def bkstr():
    in_jwt = request.args.get("jwt")
    
    cur = global_db_con.cursor()
    cur.execute("select * from books;")
    catalogue = cur.fetchall()
    cur.close()

    count=0
    message = '{"books":['
    for b in catalogue:
        if b[0] < len(catalogue) :
            message += '{"title":"'+str(b[1]) + '","author":"' + str(b[2]) + '","price":"' + str(b[3]) +'"},'
        else:
            message += '{"title":"'+str(b[1]) + '","author":"' + str(b[2]) + '","price":"' + str(b[3]) +'"}'
    message += "]}"
    
    return json_response(data=json.loads(message))
    
#######################################################################


########################## Authenticate User ###########################
"""
Based on entered credentials
     1) If the user exists in the database, validate username and password, 
        return jwt containing ecrypted username and password for use during session
     2) If the user does not exist in the database, prompt user 
         "This account does not exist, would you like to create it now?" 
        if yes, add to database, return jwt 
        if no, return to login screen
     3) user exists but passwords dont match, prompt user to try again invalid credentials                 
"""
@app.route('/authU', methods=['POST']) #endpoint
def authU():
    cur = global_db_con.cursor()

    cur.execute("select * from users where username = '" + str(request.form["username"]) + "';")
    u_cred = cur.fetchone() #store the id associated with the requested username from the db
 
    cur.close()

    print(type(request.form["password"]))
    print(u_cred)
    #check user credentials agains the db
    if u_cred[0] is None:    #if no such user exists in the db
        print("No such user")
        return json_response( data={"message": "Invalid User name: " +
                                    str(request.form["username"])}, status =404)

    else:               #if the user exists and the password matches
        if bcrypt.checkpw(bytes(request.form["password"], "utf-8"), bytes(u_cred[2], "utf-8")) == True:
            print("Successful Login, Welcome Back: " + str(request.form["username"]))

            JWT = jwt.encode( {"userID": u_cred[0],"pw":u_cred[2]}, JWT_SECRET, algorithm="HS256")

            return json_response( data={"jwt": JWT})
        else:
            print("Imposter! Thats not the password!!")

            return json_response( data={"message": "Incorrect Password"}, status = 404)

########################### SignUp ##################################
"""
Create a new user profile from input credentials
          1) Determines whether a user already exists in the database:
             a) if the user exists: inform user and redirect to login
             b) if user doesnt already exist create new user in database, return jwt
"""
@app.route('/signup', methods=["POST"])
def signup():
    cur = global_db_con.cursor()

    cur.execute("select id from users where username = '" + str(request.form["username"]) + "';")
    u_id = cur.fetchone()
    

    if u_id !=  None:
        print("That name is already taken, BE MORE ORIGINAL!")
        return json_response(data={"message": + str(request.form["username"]) + " is already exists!"})
    else:
        salty_pw = bcrypt.hashpw(bytes(request.form["password"], "utf-8"), bcrypt.gensalt(10))

        cur.execute("INSERT INTO users (username, password) VALUES ('"
                    + str(request.form["username"]) + "', '" + salty_pw.decode("utf-8") +  "');")
        cur.close()
        global_db_con.commit()

        print("Created user: " + request.form["username"] + ".")
        return json_response(data={"message": str(request.form["username"]) +" created successfully."})


app.run(host='0.0.0.0', port=80)
