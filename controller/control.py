from flask import render_template, request, jsonify
from database.db import *
from boto3.session import Session
from keys import ACCESS_KEY, SECRET_KEY

def connection_s3():
    session_s3 = Session(ACCESS_KEY, SECRET_KEY)
    s3 = session_s3.resource('s3')
    print("Succesfull Connection to S3")
    return s3
    
def save_file_local(ident, photo):
    extension = photo.filename.split(".")[1]
    photo_name = ident + "." + extension
    photo_path = "/tmp/" + photo_name
    photo.save(photo_path)
    print("Photo Saved")
    return photo_path, photo_name

def upload_file_s3(s3, photo_path, photo_name):
    bucket_name = "bucket-photos-cym"
    photo_path_s3 = "images/" + photo_name
    s3.meta.client.upload_file(photo_path, bucket_name, photo_path_s3)
    print("File Upload")
 
def get_file_s3(s3, ident):
    bucket_name = "bucket-photos-cym"
    bucket_repo = s3.Bucket(bucket_name)
    all_obj = bucket_repo.objects.all()
    path_name_file = []
    for obj in all_obj:
        path_name_file = obj.key
        name_file = (path_name_file.split("/")[1]).split(".")[0]
        if name_file == ident:
            print("file found")
            break
    if len(path_name_file) != 0:
        return path_name_file
    else:
        return None

def func_home(): 
    return render_template("home.html")

def func_register_page():
    return render_template("register.html")
    
def func_consult_page():
    return render_template("consult.html")

def func_register_user(data_user, req_file):
    ident, name, lastname, birthday = data_user["id"], data_user["name"], data_user["lastname"], data_user["birthday"]
    photo = req_file["photo"]
    add_user(ident, name, lastname, birthday)
    s3 = connection_s3()
    photo_path, photo_name = save_file_local(ident, photo)
    upload_file_s3(s3, photo_path, photo_name)
    return "<h1> User was added </h1>"
    
def func_consult_user(req_data):
    ident = req_data["id"]
    result_data = consult_user(ident)
    s3 = connection_s3()
    file_found = get_file_s3(s3, ident)
    print(file_found)
    if len(result_data) != 0:
        resp_data = {
            'status': 'OK',
            'name': result_data[0][1],
            'lastname': result_data[0][2],
            'birthday': result_data[0][3],
            'photo': file_found
        }
    else:
        resp_data = {'status': 'Error'}
    
    return jsonify(resp_data)

