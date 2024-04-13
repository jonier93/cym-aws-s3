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
        print("Successfull connection")
        return connection
    except:
        print("Error connecting to the database")
        return None
        
def add_user():
    instruction = "INSERT INTO users VALUES (45268, 'Jonier', 'Porras', '4/2/2000')"
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
    instruction = "SELECT * FROM users WHERE id = " + ident
    connection = connectionSQL()
    cursor = connection.cursor()
    try:
        cursor.execute(instruction)
        result = cursor.fetchall()
        if len(result) != 0:
            return result
        else:
            return None
    except:
        return None

