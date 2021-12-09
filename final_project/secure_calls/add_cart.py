
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from psycopg2 import sql
import json

from tools.logging import logger


def handle_request():
    logger.debug("Add to Cart Handle Request")

    un = request.args.get('username')
    title = request.args.get('title')
    logger.debug(title)
    logger.debug(request.args.get('username'))
    
    cur = g.db.cursor()
    cur.execute(sql.SQL("SELECT * FROM books WHERE title = %s;"),(title,))
    info = cur.fetchone()
    logger.debug(info)
    book = str(info[1]) 
    author = str(info[2])
    price = float(info[3].translate({ord('$'):None}))

    cur.execute(sql.SQL("INSERT INTO cart (title, author, price, customer) VALUES(%s, %s, %s, %s);"),(book,author,price,un))
    
    cur.close()
    g.db.commit()
    
    
    return "we added a book to cart"
