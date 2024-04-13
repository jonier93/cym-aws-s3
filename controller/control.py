from flask import render_template, request, jsonify
from database.db import *
from boto3.session import Session
from keys import ACCESS_KEY, SECRET_KEY

def connection_s3():
    session = Session(ACCESS_KEY, SECRET_KEY)
    s3 = session.resource('s3')
    return s3
    

def upload_file_s3(s3, photo_name, photo_path_local):
    bucket_name = 'test-s3-jonier'
    file_new = 'images/' + photo_name 
    s3.meta.client.upload_file(photo_path_local, bucket_name,  file_new)
    print("File uploaded")

def get_files_s3(s3, ident):
    bucket_name = 'test-s3-jonier'
    bucket = s3.Bucket(bucket_name)
    file_found = []
    for obj in bucket.objects.all():
        file_name = obj.key
        file_name_clear = file_name.split("/")[-1].split(".")[0]
        if file_name_clear == ident:
            file_found = file_name
            break;
                
    client = s3.meta.client
    if len(file_found) != 0:
        photo_name = file_found.rsplit("/", 1)[-1]
        client.download_file(bucket_name, file_found, photo_name)
        return file_found
    else:
        return None
    

def func_home(): 
    add_user()
    return render_template("home.html")

def func_register_page():
    return render_template("register.html")
    
def func_consult_page():
    return render_template("consult.html")

def func_register_user(req_data, req_photo):
    data_user = req_data
    photo_user = req_photo
    ident, name, lastname, birthday, photo = data_user["id"], data_user["name"], data_user["lastname"], data_user["birthday"], photo_user["photo"]
    file_extension = photo.filename.split('.')[-1]
    photo_name = ident + "." + file_extension
    photo_path_local = "/tmp/" + photo_name
    photo.save(photo_path_local)
    s3 = connection_s3()
    upload_file_s3(s3, photo_name, photo_path_local)
    return "<h1> User was added </h1>"
    
def func_consult_user(req_data):
    ident = req_data["id"]
    result = consult_user(ident)
    s3 = connection_s3()
    file_found = get_files_s3(s3, ident)
    print(file_found)
    if result != None:
        if file_found != None:
            photo = file_found
        else:
            photo = 'error'
        data = {
            'message': 'OK',
            'name': result[0][1],
            'lastname': result[0][2],
            'birthday': result[0][3],
            'photo': photo
        }
    else:
        data = {"message": "error"}
    
    return jsonify(data) 

