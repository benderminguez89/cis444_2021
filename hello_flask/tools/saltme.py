<<<<<<< HEAD
import bycrypt

password_to_salt = "hello"
salted = bcrypt.hashpw( bytes(password_to_salt, 'utf-8' ), bcrypt.gensalt(10))

print(salted)
=======
import bcrypt

password_to_salt = "hello"
salted = bcrypt.hashpw( bytes(password_to_salt,  'utf-8' ) , bcrypt.gensalt(10))

print(salted)

>>>>>>> b55fc97eba173b0a0cc1a00ccfeb959617673510
