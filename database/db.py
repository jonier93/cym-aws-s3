import pymysql

db_host = 'db-app-cymetria.czys8c6kiyal.us-east-1.rds.amazonaws.com'
db_user = 'jonier'
db_passw = '12345678'
db_name = 'db_cym'

def connectionSQL(): 
    try:
        connection = pymysql.connect(
            host = db_host,
            user = db_user,
            password = db_passw,
            database = db_name)
        print("Successfull connection to Database")
        return connection
    except:
        print("Error connecting to the database")
        return None
        
def add_user(ident, name, lastname, birthday):
    instruction = "INSERT INTO users VALUES ("+ident+", '"+name+"', '"+lastname+"', '"+birthday+"')"
    connection = connectionSQL()
    cursor = connection.cursor()
    try:
        cursor.execute(instruction)
        connection.commit()
        print("User added")
    except:
        print("Error when adding the user")
    return True;

def consult_user(ident):
    instruction = "SELECT * FROM users WHERE id=" + ident + ";"
    connection = connectionSQL()
    cursor = connection.cursor()
    try:
        cursor.execute(instruction)
        result_data = cursor.fetchall()
        return result_data
    except:
        print("Error consulting the data")
        return None

