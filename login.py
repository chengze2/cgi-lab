#!/usr/bin/env python3
import cgi
import cgitb
import os
import json
from templates import login_page, secret_page, after_login_incorrect
from secret import username, password
cgitb.enable()

print("Content-Type: text/html")

# print(login_page())
#printing out username and password
# form = cgi.FieldStorage()
# print("USERNAME:")
# print(form.getvalue("username"))
# print("PASSWORD:")
# print(form.getvalue("password"))

#loging in
# form = cgi.FieldStorage()
# p_user = form.getvalue("username")
# p_password = form.getvalue("password")

# if p_user == username and p_password == password:
#     print(secret_page(p_user, p_password))

# else:
#     print(login_page())

#SET COOKIES ========
form = cgi.FieldStorage()
p_user = form.getvalue("username")
p_password = form.getvalue("password")

#COOKIE VARIABLES
c_username = ""
c_password = ""

#PARSING THROUGH COOKIES
try:
    cookie_string = os.environ.get("HTTP_COOKIE")
    cookie_pairs = cookie_string.split(";") #gives ["key=val", "key=val"]
    for pair in cookie_pairs:
        key, val = pair.split("=")
        if "username" in key:
            c_username = val
        elif "password" in key:
            c_password = val
except:
    pass

#CHECK IF COOKIES ARE SET
if c_username and c_password:
    print("\n\n")
    print(secret_page(c_username,c_password))

elif os.environ.get("REQUEST_METHOD", "GET") == "POST": #IF POST CHECK IF LOGIN CORRECT
    if p_user == username and p_password == password:
        #set username cookie
        print("Set-Cookie: username={};".format(p_user))
        #set password cookie
        print("Set-Cookie: password={};".format(p_password))
        print(secret_page(p_user, p_password))

    else:
        #incorrect login
        print(after_login_incorrect())
else:
    #GO TO START LOGIN
    print(login_page())
    pass

#print(os.environ)
