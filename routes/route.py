from flask import request
from server import app
from controller.control import *

@app.route('/')
def home(): 
    return func_home()

@app.route('/register_page')
def register_page():
    return func_register_page()
    
@app.route("/consult_page")
def consult_page():
    return func_consult_page()

@app.route("/register_user", methods=["post"])
def register_user():
    return func_register_user(request.form, request.files)

@app.route("/consult_user", methods=["post"])
def consult_user():
    request_data = request.get_json()
    return func_consult_user(request_data)