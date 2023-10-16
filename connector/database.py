import psycopg2

def connect_postgressql(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres",
    port="5432"
):
    
    print ("Connecting to PostgreSQL")
    print ("host: " + str(host))
    print ("database: " + str(database))
    print ("user: " + str(user))
    print ("password: " + len(str(password)) * "*")
    print ("port: " + str(port))

    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=port
    )
    print("Connected to PostgreSQL")
    return conn
