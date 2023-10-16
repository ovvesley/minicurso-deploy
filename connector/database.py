import psycopg2

def connect_postgressql(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres",
    port="5432"
):
    
    print ("Connecting to PostgreSQL")
    print ("host: " + host)
    print ("database: " + database)
    print ("user: " + user)
    print ("password: " + password)
    print ("port: " + port)

    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=port
    )
    print("Connected to PostgreSQL")
    return conn
